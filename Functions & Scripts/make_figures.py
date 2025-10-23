#!/usr/bin/env python3
"""
make_figures.py

Combined script to generate all paper figures:
  1. PDF grid thumbnail
  2. Readability box plots (FKI and GFI)
  3. Sankey diagram

Usage
-----
# Generate all figures
python make_figures.py --all

# Generate specific figures
python make_figures.py --thumbnail
python make_figures.py --readability
python make_figures.py --sankey

# With custom parameters
python make_figures.py --thumbnail --pdf-path ./my.pdf --thumbnail-out ./thumb.jpg
"""

import argparse
import os
import re
from collections import defaultdict, deque
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from tqdm import tqdm


# ============================================================================
# SECTION 1: SANKEY DIAGRAM
# ============================================================================

COLOR_MAP = {
    "ratio": "rgba(31,119,180,0.75)",
    "diff":  "rgba(255,127,14,0.75)",
}

ALIASES_NUM = ["numerator", "numer", "from", "source"]
ALIASES_DEN = ["denominator", "denom", "to", "target"]
ALIASES_SIG = ["signal_type", "signal", "type", "kind", "category"]


def _pick(cols, cands):
    cols = [c.lower().strip() for c in cols]
    for c in cands:
        if c in cols: return c
    return None


def load_df(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df.columns = [c.lower().strip() for c in df.columns]
    num = _pick(df.columns, ALIASES_NUM)
    den = _pick(df.columns, ALIASES_DEN)
    sig = _pick(df.columns, ALIASES_SIG)
    if num is None or den is None:
        raise ValueError(f"Couldn't find numerator/denominator columns. Found: {list(df.columns)}")
    if sig is None:
        df["signal_type"] = "unspecified"
        sig = "signal_type"
    df = df.rename(columns={num:"numerator", den:"denominator", sig:"signal_type"})
    df["numerator"] = df["numerator"].astype(str).str.strip().str.upper()
    df["denominator"] = df["denominator"].astype(str).str.strip().str.upper()
    df["signal_type"] = df["signal_type"].astype(str).str.strip().str.lower()
    # Replace ME_DATADATE with ME
    df["numerator"] = df["numerator"].str.replace("ME_DATADATE", "ME")
    df["denominator"] = df["denominator"].str.replace("ME_DATADATE", "ME")
    return df


def layered_order(df: pd.DataFrame):
    # Build directed graph and indegrees
    outs = defaultdict(set)
    indeg = defaultdict(int)
    nodes = set(df["numerator"]).union(set(df["denominator"]))
    for u, v in zip(df["numerator"], df["denominator"]):
        if v not in outs[u]:
            outs[u].add(v)
            indeg[v] += 1
            nodes.add(u); nodes.add(v)
    for n in nodes:
        indeg.setdefault(n, 0)

    # Kahn's algorithm to find layers (stages)
    layer = defaultdict(int)
    q = deque([n for n in nodes if indeg[n] == 0])
    while q:
        u = q.popleft()
        for v in outs[u]:
            layer[v] = max(layer[v], layer[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    # Stable order: by (layer, name)
    ordered = sorted(nodes, key=lambda n: (layer[n], n))
    index = {n:i for i,n in enumerate(ordered)}
    return ordered, index


def build_sankey(df: pd.DataFrame):
    labels, index = layered_order(df)
    g = df.groupby(["numerator", "denominator", "signal_type"]).size().reset_index(name="count")

    src, tgt, val, col = [], [], [], []
    for _, r in g.iterrows():
        src.append(index[r["numerator"]])
        tgt.append(index[r["denominator"]])
        val.append(int(r["count"]))
        col.append(COLOR_MAP.get(r["signal_type"], "rgba(127,127,127,0.6)"))
    return labels, src, tgt, val, col


def plot_sankey(df: pd.DataFrame) -> go.Figure:
    labels, src, tgt, val, col = build_sankey(df)

    node = dict(
        pad=12,            # moderate spacing between nodes
        thickness=25,      # thicker node boxes -> thicker-looking links
        line=dict(color="black", width=0.4),
        label=labels
    )
    link = dict(source=src, target=tgt, value=val, color=col)

    fig = go.Figure(data=[go.Sankey(
        node=node,
        link=link,
        arrangement="snap",   # respect stages but allow Plotly to optimize spacing
        valueformat=".0f"
    )])

    # Small legend
    fig.add_trace(go.Scatter(x=[None], y=[None], mode="markers",
                             marker=dict(size=10, color=COLOR_MAP["ratio"]), name="ratio"))
    fig.add_trace(go.Scatter(x=[None], y=[None], mode="markers",
                             marker=dict(size=10, color=COLOR_MAP["diff"]), name="diff"))

    fig.update_layout(
        margin=dict(l=10, r=10, t=34, b=40),
        title=dict(text="Sankey: Numerator to Denominator", x=0.5, xanchor="center"),
        font=dict(size=12, color="black"),
        height=700,           # taller figure with thick ribbons
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=True,
        legend=dict(
            x=0, y=-0.01, xanchor="left", yanchor="top",
            bgcolor="rgba(255,255,255,0)",
            bordercolor="rgba(0,0,0,0)",
            borderwidth=0,
            font=dict(size=10),
            orientation="h",
            itemsizing="constant"
        )
    )

    # Hide axes (only relevant to the scatter legend)
    fig.update_xaxes(visible=False, showgrid=False, zeroline=False)
    fig.update_yaxes(visible=False, showgrid=False, zeroline=False)
    return fig


def plot_sankey_diagram(csv_path: Path, output_path: Path):
    """Generate Sankey diagram from CSV data."""
    df = load_df(csv_path)
    fig = plot_sankey(df)

    try:
        fig.write_image(str(output_path))
        print(f"✓ Sankey diagram saved to {output_path}")
    except Exception as e:
        html_path = output_path.with_suffix('.html')
        fig.write_html(str(html_path), include_plotlyjs="cdn")
        print(f"⚠ PDF export failed (is 'kaleido' installed?)")
        print(f"  HTML saved as fallback: {html_path}")



# ============================================================================
# SECTION 2: PDF GRID THUMBNAIL
# ============================================================================

def create_grid_pdf_thumbnail(pdf_path, output_path, thumbnail_size=(150, 150), 
                               columns=7, gap=10):
    """Create a grid thumbnail from PDF pages."""
    import fitz  # PyMuPDF
    from PIL import Image
    
    pdf_document = fitz.open(pdf_path)
    thumbnails = []

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        pix = page.get_pixmap(alpha=False)
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

        # Rotate landscape pages to portrait
        if image.width > image.height:
            image = image.transpose(Image.ROTATE_270)

        image.thumbnail(thumbnail_size)
        thumbnails.append(image)

    # Calculate grid dimensions
    rows = (len(thumbnails) + columns - 1) // columns
    grid_width = columns * (thumbnail_size[0] + gap) - gap
    grid_height = rows * (thumbnail_size[1] + gap) - gap

    # Create grid canvas
    grid_image = Image.new("RGB", (grid_width, grid_height), "white")

    # Paste thumbnails
    for idx, thumbnail in enumerate(thumbnails):
        row = idx // columns
        col = idx % columns
        x_offset = col * (thumbnail_size[0] + gap)
        y_offset = row * (thumbnail_size[1] + gap)
        grid_image.paste(thumbnail, (x_offset, y_offset))

    # Save as PDF
    grid_image.save(output_path, "PDF", resolution=100.0)
    print(f"✓ Grid thumbnail saved to {output_path}")


# ============================================================================
# SECTION 3: READABILITY BOX PLOTS
# ============================================================================

# PDF text extraction
def _extract_text_pdfminer(path):
    try:
        from pdfminer.high_level import extract_text
    except Exception:
        from pdfminer_high_level import extract_text
    return extract_text(path)


def _extract_text_pypdf2(path):
    import PyPDF2
    text = []
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            try:
                text.append(page.extract_text() or "")
            except Exception:
                pass
    return "\n".join(text)


def extract_text_from_pdf(path: str) -> str:
    """Extract text from PDF using available library."""
    try:
        return _extract_text_pdfminer(path)
    except Exception:
        try:
            return _extract_text_pypdf2(path)
        except Exception as e:
            raise RuntimeError(
                f"Could not extract text from {path}. "
                "Install `pdfminer.six` or `PyPDF2`."
            ) from e


# Tokenization and syllable counting
_SENT_SPLIT = re.compile(r'(?<!\b[A-Z])[.!?]+(?=\s+|$)')
_WORD_RE = re.compile(r"[A-Za-z']+")


def split_sentences(text: str) -> List[str]:
    """Split text into sentences."""
    text = re.sub(r'\s+', ' ', text.strip())
    if not text:
        return []
    return [s.strip() for s in _SENT_SPLIT.split(text) if s.strip()]


def tokenize_words(text: str) -> List[str]:
    """Extract words from text."""
    return [m.group(0).lower() for m in _WORD_RE.finditer(text)]


def count_syllables_in_word(word: str) -> int:
    """Count syllables in a single word."""
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    
    exceptions = {
        "queue": 2, "people": 2, "science": 2, "business": 2, "every": 2,
        "evening": 3, "women": 2, "woman": 2, "does": 1, "done": 1, "ones": 1
    }
    if w in exceptions:
        return exceptions[w]
    
    groups = re.findall(r"[aeiouy]+", w)
    syllables = len(groups)
    
    if w.endswith("e") and (not w.endswith("le") or len(w) <= 2):
        syllables -= 1
    if w.endswith(("ial", "ian")):
        syllables += 1
    
    return max(1, syllables)


def count_syllables_in_words(words: List[str]) -> int:
    """Count total syllables in word list."""
    return sum(count_syllables_in_word(w) for w in words)


# Readability metrics
def compute_metrics(text: str):
    """Compute Flesch-Kincaid and Gunning-Fog indices."""
    sents = split_sentences(text)
    words = tokenize_words(text)

    sentences = max(1, len(sents))
    total_words = len(words)

    if total_words == 0:
        return {"FKI": 0.0, "GFI": 0.0}

    syllables = count_syllables_in_words(words)
    complex_words = sum(1 for w in words if count_syllables_in_word(w) >= 3)

    w_per_s = total_words / sentences
    syl_per_w = syllables / total_words
    cw_per_w = complex_words / total_words

    FKI = 0.39 * w_per_s + 11.8 * syl_per_w - 15.59
    GFI = 0.4 * (w_per_s + 100.0 * cw_per_w)

    return {"FKI": FKI, "GFI": GFI}


_VERSION_RX = re.compile(r"modified_(v[1-4])_(sdi|prod|cons|free)")


def measure_dir(dirname: str, group: str) -> pd.DataFrame:
    """Measure readability for all PDFs in directory."""
    rows = []
    files = [f for f in os.listdir(dirname) if f.lower().endswith(".pdf")]
    
    for fname in tqdm(files, desc=f"Processing {group} PDFs", unit="file"):
        path = os.path.join(dirname, fname)
        text = extract_text_from_pdf(path)
        m = compute_metrics(text)
        rec = {"filename": fname, "group": group, "ai_version": ""}
        mat = _VERSION_RX.search(fname)
        if mat:
            rec["ai_version"] = mat.group(1)
        rec.update(m)
        rows.append(rec)
    
    return pd.DataFrame(rows)


def plot_readability_distributions(ai_dir: str, published_dir: str, outdir: str):
    """Generate readability box plots comparing AI and published papers."""
    os.makedirs(outdir, exist_ok=True)
    
    # Measure both corpora
    df_ai = measure_dir(ai_dir, "ai")
    df_pub = measure_dir(published_dir, "published")
    df = pd.concat([df_ai, df_pub], ignore_index=True)
    
    # Prepare data
    df["ai_version_clean"] = np.where(
        df["group"].eq("published"),
        "published",
        df["ai_version"].replace({"": "other"})
    )
    sel = df["ai_version_clean"].isin(["published", "v1", "v2", "v3", "v4"]).copy()
    dfg = df.loc[sel]

    # Plot FKI
    order = ["published", "v1", "v2", "v3", "v4"]
    data = [dfg.loc[dfg["ai_version_clean"].eq(g), "FKI"].dropna().values 
            for g in order]
    
    fig = plt.figure(figsize=(6.0, 4.0))
    plt.boxplot(data, labels=["Published", "AI v1 (sdi)", "AI v2 (prod)", 
                               "AI v3 (cons)", "AI v4 (free)"], showmeans=True)
    plt.ylabel("Flesch–Kincaid Index")
    plt.title("Readability (FKI) by Group")
    plt.tight_layout()
    fki_path = os.path.join(outdir, "fig_boxplot_fki_by_group.pdf")
    fig.savefig(fki_path)
    plt.close(fig)
    print(f"✓ FKI boxplot saved to {fki_path}")

    # Plot GFI
    data = [dfg.loc[dfg["ai_version_clean"].eq(g), "GFI"].dropna().values 
            for g in order]
    
    fig = plt.figure(figsize=(6.0, 4.0))
    plt.boxplot(data, labels=["Published", "AI v1 (sdi)", "AI v2 (prod)", 
                               "AI v3 (cons)", "AI v4 (free)"], showmeans=True)
    plt.ylabel("Gunning–Fog Index")
    plt.title("Readability (GFI) by Group")
    plt.tight_layout()
    gfi_path = os.path.join(outdir, "fig_boxplot_gfi_by_group.pdf")
    fig.savefig(gfi_path)
    plt.close(fig)
    print(f"✓ GFI boxplot saved to {gfi_path}")


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Generate all paper figures",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python make_figures.py --all
  python make_figures.py --thumbnail --readability
  python make_figures.py --sankey --csv signals.csv --sankey-out diagram.pdf
        """
    )
    
    # Figure selection
    parser.add_argument("--all", action="store_true", 
                       help="Generate all figures")
    parser.add_argument("--thumbnail", action="store_true",
                       help="Generate PDF grid thumbnail")
    parser.add_argument("--readability", action="store_true",
                       help="Generate readability box plots")
    parser.add_argument("--sankey", action="store_true",
                       help="Generate Sankey diagram")
    
    # Thumbnail parameters
    parser.add_argument("--pdf-path", type=str,
                       default="./tex/pdfs/ACOSEQ_modified_v1_sdi.pdf",
                       help="Path to PDF for thumbnail")
    parser.add_argument("--thumbnail-out", type=str,
                       default="./grid_thumbnail.pdf",
                       help="Output path for thumbnail")
    parser.add_argument("--thumb-size", type=int, nargs=2, default=[200, 220],
                       help="Thumbnail size (width height)")
    parser.add_argument("--columns", type=int, default=5,
                       help="Number of columns in grid")
    parser.add_argument("--gap", type=int, default=0,
                       help="Gap between thumbnails in pixels")
    
    # Readability parameters
    parser.add_argument("--ai-dir", type=str, default="./ai",
                       help="Directory with AI-generated PDFs")
    parser.add_argument("--published-dir", type=str, default="./published",
                       help="Directory with published PDFs")
    parser.add_argument("--readability-out", type=str, default="./readability_out",
                       help="Output directory for readability plots")
    
    # Sankey parameters
    parser.add_argument("--csv", type=Path, default=Path("signals.csv"),
                       help="CSV file for Sankey diagram")
    parser.add_argument("--sankey-out", type=Path, default=Path("sankey.pdf"),
                       help="Output path for Sankey diagram")
    
    args = parser.parse_args()
    
    # Determine which figures to generate
    generate_all = args.all
    generate_thumb = args.thumbnail or generate_all
    generate_read = args.readability or generate_all
    generate_sank = args.sankey or generate_all
    
    if not (generate_thumb or generate_read or generate_sank):
        parser.print_help()
        print("\nError: Please specify at least one figure type to generate.")
        return
    
    print("=" * 70)
    print("GENERATING PAPER FIGURES")
    print("=" * 70)
    
    # Generate Sankey diagram
    if generate_sank:
        print("\n[1/3] Sankey Diagram")
        print("-" * 70)
        try:
            plot_sankey_diagram(
                csv_path=args.csv,
                output_path=args.sankey_out
            )
        except Exception as e:
            print(f"✗ Error generating Sankey diagram: {e}")
    
    # Generate thumbnail
    if generate_thumb:
        print("\n[2/3] PDF Grid Thumbnail")
        print("-" * 70)
        try:
            create_grid_pdf_thumbnail(
                pdf_path=args.pdf_path,
                output_path=args.thumbnail_out,
                thumbnail_size=tuple(args.thumb_size),
                columns=args.columns,
                gap=args.gap
            )
        except Exception as e:
            print(f"✗ Error generating thumbnail: {e}")
    
    # Generate readability plots
    if generate_read:
        print("\n[3/3] Readability Box Plots")
        print("-" * 70)
        try:
            plot_readability_distributions(
                ai_dir=args.ai_dir,
                published_dir=args.published_dir,
                outdir=args.readability_out
            )
        except Exception as e:
            print(f"✗ Error generating readability plots: {e}")
    
    print("\n" + "=" * 70)
    print("COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()