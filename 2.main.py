# =============================
# main.py (refactored with LLM client adapters + dry-run)
# =============================
import argparse
import os
import sys
from typing import List, Tuple, Callable, Optional
import pandas as pd
from models import Signal, LLMPaperGenerator


# (hypothesis_type, file_tag)
DEFAULT_HYPOTHESES: List[Tuple[str, str]] = [
    ("slow_diffusion", "sdi"),        # v1
    ("production_based", "prod"),     # v2
    ("consumption_based", "cons"),    # v3
    ("none", "free"),                 # v4 (no hypothesis guidance)
]


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for paper generation.

    Notes
    -----
    - Do not change defaults that affect LLM prompts or generated content.
    """
    parser = argparse.ArgumentParser(
        description="Generate LLM-written finance papers from LaTeX templates and a signals.csv."
    )
    parser.add_argument(
        "--base-dir",
        default="./tex",
        help=(
            "Base directory containing .tex files and resources "
            "(incl. compustat_variable_dictionary.csv)."
        ),
    )
    parser.add_argument(
        "--signals-csv",
        default="signals.csv",
        help="CSV with columns like varName,numer,denom,signal_type.",
    )
    parser.add_argument(
        "--n-signals",
        type=int,
        default=1,
        help="How many signals from signals.csv to process (top to bottom).",
    )
    parser.add_argument(
        "--n-versions",
        type=int,
        default=1,
        help=(
            "How many versions to generate per signal. By default, uses all in "
            "--hypotheses (incl. the freeform one)."
        ),
    )
    parser.add_argument(
        "--hypotheses",
        nargs="*",
        default=[h for h, _ in DEFAULT_HYPOTHESES],
        choices=[h for h, _ in DEFAULT_HYPOTHESES],
        help="Subset/order of hypothesis lenses to run. Include 'none' for freeform.",
    )
    parser.add_argument(
        "--provider",
        default="anthropic",
        choices=["openai", "anthropic"],
        help="LLM provider.",
    )
    parser.add_argument(
        "--llm-model",
        default="claude-opus-4-1-20250805",
        help=(
            "LLM model name (e.g., 'gpt-4o-mini', 'gpt-3.5-turbo', "
            "'claude-3-haiku-20240307'). If omitted, a provider-specific default is used."
        ),
    )
    parser.add_argument(
        "--temperature", type=float, default=0.7, help="Sampling temperature."
    )
    parser.add_argument(
        "--max-tokens", type=int, default=20000, help="Max tokens for LLM responses."
    )
    parser.add_argument(
        "--timeout-seconds",
        type=float,
        default=600.0,
        help="Client-side timeout (seconds) for LLM calls.",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip processing if a PDF for that version already exists.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "Do not call LLMs or compile PDFs. Still perform LaTeX cleaning and write out modified .tex files with placeholders."
        ),
    )
    parser.add_argument(
        "--names-only",
        action="store_true",
        help="Only generate/print signal names and write signals_with_names.csv, then exit (skip all other LLM and PDF steps).",
    )
    return parser.parse_args()


def _build_signal_name_and_acronym(
    numer: str, denom: str, signal_type: str, compustat_map: dict
) -> Tuple[str, str]:
    """Return deterministic (signal_name, acronym) based on inputs.

    This is used as a fallback when creative naming via LLM is disabled or fails.
    """
    # Human-friendly names (fallback to acronym if not found)
    n_name = compustat_map.get(numer, numer)
    d_name = compustat_map.get(denom, denom)

    if (signal_type or "").lower() == "diff":
        signal_name = f"Change in {n_name} scaled by lagged {d_name}"
        acronym = f"d{numer}/L{denom}"  # ASCII-friendly acronym
    else:
        # default to ratio
        signal_name = f"{n_name} over {d_name}"
        acronym = f"{numer}/{denom}"

    return signal_name, acronym


def load_signals(
    signals_csv_path: str,
    n_signals: int,
    compustat_map: dict,
    name_provider: Optional[Callable[[str, str, str, str, dict, List[str], int], Tuple[str, str]]] = None,
    max_retries: int = 5,
) -> List[Signal]:
    """Load signals and attach (signal_name, acronym).

    If ``name_provider`` is given, use it to produce creative names via LLM;
    otherwise fall back to deterministic names.
    
    Parameters
    ----------
    max_retries : int
        Number of retry attempts when LLM generates duplicate names (default: 5)
    """
    if not os.path.exists(signals_csv_path):
        raise FileNotFoundError(f"Signals CSV not found: {signals_csv_path}")

    df = pd.read_csv(signals_csv_path)

    required_cols = {"varName", "numer", "denom"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(
            f"signals.csv is missing required column(s): {', '.join(sorted(missing))}"
        )

    # 'signal_type' may be either 'signal' or 'signal_type' depending on upstream files
    if "signal_type" not in df.columns:
        if "signal" in df.columns:
            df = df.rename(columns={"signal": "signal_type"})
        else:
            # default to 'ratio' if the column is absent
            df["signal_type"] = "ratio"

    # Trim to requested number of signals
    if n_signals is not None and n_signals > 0:
        df = df.head(n_signals)

    signals: List[Signal] = []
    used_names: List[str] = []  # Track generated names to prevent duplicates
    
    for idx, row in df.iterrows():
        var_name = str(row["varName"])  # filename stem for the LaTeX template
        numer = str(row["numer"])       # COMPUSTAT acronym
        denom = str(row["denom"])       # COMPUSTAT acronym
        s_type = str(row.get("signal_type", "ratio")).lower()

        print(f"\n[{idx+1}/{len(df)}] Processing signal: {var_name}")

        if name_provider:
            try:
                signal_name, acronym = name_provider(
                    var_name, numer, denom, s_type, compustat_map,
                    used_names,  # Pass list of already-used names
                    max_retries  # Pass retry limit
                )
                # Add successfully generated name to tracking list
                if signal_name not in used_names:
                    used_names.append(signal_name)
                else:
                    print(f"[WARN] Duplicate name despite checks: {signal_name}")
            except Exception as e:
                print(
                    f"[WARN] LLM name provider failed for {var_name}: {e}. "
                    "Falling back to deterministic naming."
                )
                signal_name, acronym = _build_signal_name_and_acronym(
                    numer, denom, s_type, compustat_map
                )
        else:
            signal_name, acronym = _build_signal_name_and_acronym(
                numer, denom, s_type, compustat_map
            )

        signals.append(
            Signal(
                var_name=var_name,
                acronym=acronym,
                signal_name=signal_name,
                numer=numer,
                denom=denom,
                signal_type=s_type,
            )
        )
    
    print(f"\n✓ Successfully generated {len(signals)} unique signal names")
    if len(used_names) != len(set(used_names)):
        print(f"⚠ WARNING: {len(used_names) - len(set(used_names))} duplicate(s) detected despite checks")
    
    return signals


def main() -> None:
    args = parse_args()

    # Build (hypothesis_type, file_tag) list honoring the order from args.hypotheses
    hypothesis_tag_map = {h: t for h, t in DEFAULT_HYPOTHESES}
    hypotheses: List[Tuple[str, str]] = [
        (h, hypothesis_tag_map[h]) for h in args.hypotheses
    ]

    # Cut to n_versions if provided
    if args.n_versions is not None:
        hypotheses = hypotheses[: max(0, args.n_versions)]

    # Set provider-specific default model if not provided
    llm_model = args.llm_model
    if llm_model is None:
        llm_model = "gpt-3.5-turbo" if args.provider == "openai" else "claude-3-haiku-20240307"

    generator = LLMPaperGenerator(
        base_dir=args.base_dir,
        model=args.provider,  # 'model' here is the provider name (openai/anthropic)
        llm_model=llm_model,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        request_timeout_seconds=args.timeout_seconds,
        dry_run=args.dry_run,
    )

    # Figure out paths
    signals_csv_path = os.path.join(args.base_dir, args.signals_csv)

    # Load signals and enrich with LLM-proposed names/acronyms
    try:
        signals = load_signals(
            signals_csv_path,
            args.n_signals,
            generator.compustat_var_names,
            name_provider=None if args.dry_run else generator.generate_signal_name_and_acronym,
        )
    except Exception as e:
        print(f"[ERROR] Failed to load signals: {e}")
        sys.exit(1)

    # Optionally write out an enriched CSV for reference
    try:
        out_rows = [
            {
                "varName": s.var_name,
                "numer": s.numer,
                "denom": s.denom,
                "signal_type": s.signal_type,
                "signal_name": s.signal_name,
                "acronym": s.acronym,
            }
            for s in signals
        ]
        pd.DataFrame(out_rows).to_csv(
            os.path.join('./', "signals_with_names.csv"), index=False
        )
    except Exception as e:
        print(f"[WARN] Could not save signals_with_names.csv: {e}")

    # If we're only interested in names, stop here (skip intros/data/conclusion/PDF).
    if getattr(args, "names_only", False):
        print("Wrote signal names to:", os.path.join(args.base_dir, "signals_with_names.csv"))
        print("Names-only mode: skipping all further LLM calls and PDF generation.")
        return



    # Process each signal
    for signal in signals:
        tex_file_path = os.path.join(args.base_dir, f"{signal.var_name}.tex")
        if not os.path.exists(tex_file_path):
            print(f"[WARN] Missing LaTeX file for {signal.var_name}: {tex_file_path}")
            continue

        try:
            with open(tex_file_path, "r", encoding="utf-8") as f:
                latex_text = f.read()
        except Exception as e:
            print(f"[WARN] Could not read {tex_file_path}: {e}")
            continue

        # Clean title page and replace varName with acronym where appropriate
        cleaned_text = generator.clean_latex_title_page(
            latex_text, varName=signal.var_name, signalName=signal.signal_name, acronym=signal.acronym
        )

        # Generate versions according to selected hypothesis lenses (including 'none' for freeform)
        for version_idx, (hypothesis_type, tag) in enumerate(hypotheses, start=1):
            if args.skip_existing:
                print(
                    f"[INFO] Processing {signal.var_name} v{version_idx} ({hypothesis_type}, tag={tag}) if needed..."
                )
            generator.process_version(
                signal=signal,
                version=version_idx,
                cleaned_text=cleaned_text,
                hypothesis_type=hypothesis_type,
                file_tag=tag,
            )

    print("All done.")


if __name__ == "__main__":
    main()
