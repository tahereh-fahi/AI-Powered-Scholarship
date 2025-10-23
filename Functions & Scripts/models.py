

# =============================
# models.py (refactored with adapters + dry-run)
# =============================
import json
import os
import re
import shutil
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple
from abc import ABC, abstractmethod
import openai
import pandas as pd
from anthropic import Anthropic


# -------------------- LLM Client Abstractions --------------------
class LLMClient(ABC):
    def __init__(self, model_name: str, temperature: float, max_tokens: int, timeout: float) -> None:
        self.model_name = model_name
        self.temperature = float(temperature)
        self.max_tokens = int(max_tokens)
        self.timeout = float(timeout)

    @abstractmethod
    def call(self, prompt: str) -> str:  # pragma: no cover
        raise NotImplementedError


class OpenAIClient(LLMClient):
    def __init__(self, api_key: Optional[str], **kwargs) -> None:
        super().__init__(**kwargs)
        if api_key:
            openai.api_key = api_key

    def call(self, prompt: str) -> str:
        resp = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            request_timeout=self.timeout,
        )
        return resp['choices'][0]['message']['content'].strip()


class AnthropicClient(LLMClient):
    def __init__(self, api_key: Optional[str], **kwargs) -> None:
        super().__init__(**kwargs)
        self.client = Anthropic(api_key=api_key, timeout=self.timeout)

    def call(self, prompt: str) -> str:
        # Try streaming first (as before); fall back to non-streaming
        try:
            text_out: List[str] = []
            with self.client.messages.stream(
                model=self.model_name,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[{"role": "user", "content": prompt}],
            ) as stream:
                for event in stream:
                    try:
                        if getattr(event, "type", "") == "content_block_delta":
                            delta = getattr(event, "delta", None)
                            if delta and hasattr(delta, "text") and delta.text:
                                text_out.append(delta.text)
                    except Exception:
                        pass
                final_msg = stream.get_final_message()
                if not text_out and final_msg and getattr(final_msg, "content", None):
                    for block in final_msg.content:
                        if getattr(block, "type", "") == "text" and getattr(block, "text", ""):
                            text_out.append(block.text)
            return "".join(text_out).strip()
        except Exception:
            message = self.client.messages.create(
                model=self.model_name,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[{"role": "user", "content": prompt}],
            )
            parts: List[str] = []
            for block in getattr(message, "content", []) or []:
                if getattr(block, "type", "") == "text":
                    parts.append(getattr(block, "text", ""))
            return "".join(parts).strip()


@dataclass
class Signal:
    """Simple container for an accounting-based return-predictive signal."""

    var_name: str
    acronym: str
    signal_name: str
    numer: str
    denom: str
    signal_type: str


class LLMPaperGenerator:
    """Generate paper sections and PDFs for finance signals using OpenAI/Anthropic.

    Important: Prompts returned by :meth:`generate_prompt` are intentionally left
    unchanged to preserve output semantics.
    """

    def __init__(
        self,
        base_dir: str,
        model: str = "openai",  # provider family name retained for compatibility
        llm_model: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
        max_tokens: int = 1024,
        request_timeout_seconds: float = 600.0,
        dry_run: bool = False,
    ) -> None:
        self.model = model
        self.llm_model = llm_model
        self.temperature = float(temperature)
        self.max_tokens = int(max_tokens)
        self.request_timeout_seconds = float(request_timeout_seconds)
        self.dry_run = bool(dry_run)

        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

        # Create client adapter (unless dry-run)
        if not self.dry_run:
            if self.model == "openai":
                self.client: Optional[LLMClient] = OpenAIClient(
                    api_key=self.openai_api_key,
                    model_name=self.llm_model,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    timeout=self.request_timeout_seconds,
                )
            elif self.model == "anthropic":
                self.client = AnthropicClient(
                    api_key=self.anthropic_api_key,
                    model_name=self.llm_model,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    timeout=self.request_timeout_seconds,
                )
            else:
                raise ValueError(f"Unsupported model/provider: {self.model}")
        else:
            self.client = None

        self.base_dir = os.path.abspath(base_dir)
        self.pdfs_dir = os.path.join(self.base_dir, "pdfs")
        os.makedirs(self.pdfs_dir, exist_ok=True)

        dict_path = os.path.join(self.base_dir, "compustat_variable_dictionary.csv")
        self.compustat_var_names = self.load_compustat_variable_dictionary(dict_path)

    # ---------- Creative naming via the SAME LLM ----------
    def _get_full_var_name(self, acronym: str, compustat_map: dict) -> str:
        return compustat_map.get(acronym, acronym)

    def generate_signal_name_and_acronym(
        self,
        var_name: str,
        numer: str,
        denom: str,
        signal_type: str,
        compustat_map: dict,
        used_names: Optional[List[str]] = None,
        max_retries: int = 3,
    ) -> Tuple[str, str]:
        """Generate a unique signal name and acronym, ensuring no duplicates.
        
        Parameters
        ----------
        used_names : Optional[List[str]]
            List of already-used signal names to avoid
        max_retries : int
            Maximum number of attempts to generate a unique name
        """
        if used_names is None:
            used_names = []
        
        numer_full = self._get_full_var_name(numer, compustat_map)
        denom_full = self._get_full_var_name(denom, compustat_map)
        is_negative = str(var_name).upper().startswith("NEG")

        for attempt in range(max_retries):
            prompt = (
                "You are naming a financial signal for an academic finance paper. "
                "Create a THREE-WORD NAME that conveys specific ECONOMIC INTUITION about what the signal measures.\n\n"
                
                f"Signal type: {signal_type}\n"
            )

            if (signal_type or "").lower() == "ratio":
                prompt += f"Calculation: '{numer_full}' divided by '{denom_full}'\n"
            elif (signal_type or "").lower() == "diff":
                prompt += f"Calculation: Change in '{numer_full}' scaled by '{denom_full}'\n"

            if is_negative:
                prompt += "Note: The signal uses the negative of this value.\n"

            # Add used names to prompt to avoid duplicates
            if used_names:
                prompt += (
                    f"\nIMPORTANT: The following names are ALREADY USED. "
                    f"You must create a DIFFERENT name:\n"
                )
                # Show last 10 names to keep prompt manageable
                recent_names = used_names[-10:] if len(used_names) > 10 else used_names
                for name in recent_names:
                    prompt += f"  - {name}\n"
                if len(used_names) > 10:
                    prompt += f"  (... and {len(used_names) - 10} more)\n"
                prompt += "\n"

            if attempt > 0:
                prompt += f"\n**RETRY #{attempt}** - Your previous attempt was a duplicate. Generate a completely DIFFERENT name.\n\n"

            prompt += (
                "\nEXAMPLES of good three-word names:\n"
                "- 'Cash Flow Volatility'\n"
                "- 'Asset Growth Rate'\n"
                "- 'Operating Profit Margin'\n"
                "- 'Working Capital Efficiency'\n"
                "- 'Earnings Quality Score'\n"
                "- 'Financial Constraint Index'\n\n"
                
                "GUIDELINES:\n"
                "1. Must be EXACTLY THREE WORDS\n"
                "2. Think: What economic story does this ratio/change tell?\n"
                "   - What firm behavior or characteristic leads to high values?\n"
                "   - What does this reveal about management decisions or firm quality?\n"
                "3. Consider the SPECIFIC relationship between numerator and denominator\n"
                "   - Don't just use generic terms like 'liquidity' or 'flexibility'\n"
                "   - Think about what makes THIS combination meaningful\n"
                "4. Use precise finance terminology (e.g., 'margin', 'turnover', 'coverage', 'intensity', 'quality')\n"
                "5. Avoid: 'ratio', 'difference', 'scaled', 'delta', 'factor', 'metric'\n"
                "6. Avoid: Generic adjectives like 'strategic', 'dynamic', 'enhanced'\n"
                "7. Avoid: Negative words - use positive framing even for low-is-good signals\n"
                "   - Use 'efficiency' not 'inefficiency'\n"
                "   - Use 'quality' not 'poor quality'\n"
                "   - Use 'stability' not 'instability'\n"
                "   - Use 'constraint' not 'lack of constraint'\n"
                "8. Make each name DISTINCTIVE - no repeating the same concept across signals\n"
                "9. Acronym: 3–5 uppercase letters derived from the name\n\n"
                
                "Ask yourself: If this signal predicts returns, what economic mechanism explains it?\n"
                "(e.g., profitability? efficiency? growth? risk? mispricing? constraints?)\n\n"
            )

            prompt += (
                "Respond inside <response></response> tags with strict JSON:\n"
                "{\n"
                '  "name": "Three Word Name",\n'
                '  "acronym": "ACRO"\n'
                "}\n"
            )

            try:
                if self.dry_run:
                    # Dry run: return a mock response
                    return f"DRY_RUN_{var_name}", "DRY"
                
                response_text = self.call_llm(prompt)
                parsed = self.parse_llm_response(response_text)
                
                if isinstance(parsed, dict):
                    generated_name = (parsed.get("name") or parsed.get("signal_name") or "").strip()
                    generated_acronym = (parsed.get("acronym") or parsed.get("abbr") or "").strip()
                    
                    # Clean acronym
                    generated_acronym = re.sub(r"[^A-Z]", "", generated_acronym.upper())
                    
                    # Check if name is duplicate and valid
                    if generated_name and generated_acronym and generated_name not in used_names:
                        if len(generated_name) > 120:
                            generated_name = generated_name[:117].rstrip() + "..."
                        print(f"✓ Generated unique name: {generated_name} ({generated_acronym})")
                        return generated_name, generated_acronym
                    else:
                        if not generated_name or not generated_acronym:
                            print(f"✗ Invalid response: missing name or acronym (attempt {attempt+1}/{max_retries})")
                        else:
                            print(f"✗ Duplicate name generated: {generated_name} (attempt {attempt+1}/{max_retries})")
                else:
                    print(f"✗ Failed to parse response (attempt {attempt+1}/{max_retries})")
                    
            except Exception as e:
                print(f"✗ Error generating name (attempt {attempt+1}/{max_retries}): {e}")
        
        # If all retries failed, generate a fallback unique name
        n_name = compustat_map.get(numer, numer)
        d_name = compustat_map.get(denom, denom)
        if (signal_type or "").lower() == "diff":
            fallback_name = f"Change in {n_name} scaled by lagged {d_name}"
            fallback_acronym = f"d{numer}/L{denom}"
        else:
            fallback_name = f"{n_name} over {d_name}"
            fallback_acronym = f"{numer}/{denom}"
        print(f"⚠ Using fallback name after {max_retries} failed attempts: {fallback_name}")
        return fallback_name, fallback_acronym

    # ------------------------------------------------------

    def cleanup_latex_files(self, base_path: str, file_prefix: str) -> None:
        """Remove common LaTeX aux files for a given prefix, if present."""
        for ext in [".aux", ".log", ".out", ".bbl", ".blg"]:
            fp = os.path.join(base_path, f"{file_prefix}{ext}")
            if os.path.exists(fp):
                try:
                    os.remove(fp)
                    print(f"Removed {fp}")
                except Exception as e:
                    print(f"Error removing {fp}: {str(e)}")

    def compile_and_move_pdf(self, tex_file_path: str) -> bool:
        """Compile a LaTeX file twice (bibtex if present) and move PDF to the output dir."""
        if self.dry_run:
            print("[DRY RUN] Skipping LaTeX compilation.")
            return True

        tex_filename = os.path.basename(tex_file_path)
        tex_name = os.path.splitext(tex_filename)[0]
        cwd = os.getcwd()
        os.chdir(self.base_dir)
        try:
            for _ in range(2):
                os.system(f"pdflatex -interaction=nonstopmode {tex_filename}")
            bib_file = f"{tex_name}.bib"
            if os.path.exists(bib_file):
                os.system(f"bibtex {tex_name}")
                for _ in range(2):
                    os.system(f"pdflatex -interaction=nonstopmode {tex_filename}")
            if os.path.exists(f"{tex_name}.pdf"):
                shutil.move(
                    os.path.join(self.base_dir, f"{tex_name}.pdf"),
                    os.path.join(self.pdfs_dir, f"{tex_name}.pdf"),
                )
                print(
                    f"PDF moved to: {os.path.join(self.pdfs_dir, tex_name)}.pdf"
                )
                self.cleanup_latex_files(self.base_dir, tex_name)
                return True
            else:
                print(f"Error: PDF not generated for {tex_name}")
                return False
        except Exception as e:
            print(f"Error during PDF compilation: {str(e)}")
            return False
        finally:
            os.chdir(cwd)

    def process_version(
        self,
        signal: Signal,
        version: int,
        cleaned_text: str,
        hypothesis_type: str = "slow_diffusion",
        file_tag: Optional[str] = None,
    ) -> None:
        suffix = f"v{version}" + (f"_{file_tag}" if file_tag else "")
        tex_file_name = f"{signal.var_name}_modified_{suffix}"
        output_file_path = os.path.join(self.base_dir, f"{tex_file_name}.tex")
        pdf_file_path = os.path.join(self.pdfs_dir, f"{tex_file_name}.pdf")
        bib_file_name = tex_file_name

        if not self.dry_run and os.path.exists(pdf_file_path):
            print(f"PDF already exists for {tex_file_name}. Skipping processing...")
            return

        introduction_sections, bib_entries = self.generate_intro(
            signal.signal_name, cleaned_text, hypothesis_type=hypothesis_type
        )
        data_section = self.generate_data_section(
            signal.signal_name, signal.denom, signal.numer, signal.signal_type, 
            self.compustat_var_names
        )
        abstract_text = self.extract_abstract(cleaned_text)
        conclusion = self.generate_conclusion(signal.signal_name, abstract_text)

        versioned_text = cleaned_text.replace(
            f"\\bibliography{{{signal.var_name}}}", f"\\bibliography{{{bib_file_name}}}"
        )

        self.export_modified_latex(
            original_latex=versioned_text,
            output_file_path=output_file_path,
            introduction_sections=introduction_sections,
            data_section=data_section,
            conclusion=conclusion,
        )

        if bib_entries:
            self.create_bib_entries(
                bib_entries, signal, version=version, bib_filename=bib_file_name
            )
        else:
            print(f"No bib entries to add for version {version}.")

        print(f"Compiling version {version} for {signal.var_name}...")
        self.compile_and_move_pdf(output_file_path)
        print(f"Completed processing version {version} for {signal.var_name}")

    @staticmethod
    def load_compustat_variable_dictionary(dictionary_file_path: str) -> Dict[str, str]:
        compustat_var_names = pd.read_csv(dictionary_file_path)
        return pd.Series(
            compustat_var_names["shortername"].values,
            index=compustat_var_names["acronym"],
        ).to_dict()

    @staticmethod
    def clean_latex_title_page(
        text: str, varName: str, signalName: str, acronym: str
    ) -> str:
        """Standardize the title page and replace occurrences of varName with acronym.

        This preserves figures/graphics commands while updating surrounding text.
        """
        text = re.sub(r"\bThis report\b", "This paper", text)
        text = re.sub(
            r"(\\title\{.*?:\\\\)(.*?)( and the Cross Section of Stock Returns\})",
            rf"\1{signalName}\3",
            text,
            flags=re.DOTALL,
        )
        pattern = r"(the asset pricing implications of )(.*?)(, and its robustness)"
        text = re.sub(pattern, rf"\1{signalName} ({acronym})\3", text)

        text = text.replace("Online Appendix for Assaying Anomalies:\\\\", "")
        text = text.replace(
            " using the protocol proposed by Novy-Marx and Velikov (2023)", ""
        )
        text = text.replace(
            "\\vspace{\\baselineskip}{Robert Novy-Marx}\\and {Mihail Velikov}",
            "I. M. Harking",
        )

        graphics_pattern = r"(\\includegraphics(?:\[[^\]]*\])?\{[^}]*\})"
        segments = re.split(graphics_pattern, text)
        for i in range(len(segments)):
            if not re.match(graphics_pattern, segments[i]):
                segments[i] = segments[i].replace(varName, acronym)
        new_text = "".join(segments)
        new_text = new_text.replace(
            "\\bibliography{newSignalTestBib}", f"\\bibliography{{{varName}}}"
        )
        return new_text

    # -------------------- YOUR PROMPTS (unchanged) --------------------
    def generate_prompt(self, prompt_type, **kwargs):

        def _hypothesis_guidance(htype):
            if htype == "slow_diffusion":
                return {
                    "label": "Slow diffusion of information",
                    "bullets": [
                        "Link the signal to gradual information incorporation and underreaction.",
                        "Cite seminal work on limited attention / gradual diffusion (e.g., news dispersion, investor inattention).",
                        "Predict return continuation concentrated where attention/frictions are stronger (e.g., small, low-analyst coverage).",
                    ]
                }
            if htype == "production_based":
                return {
                    "label": "Rational risk (production-based asset pricing)",
                    "bullets": [
                        "Map the signal to marginal costs, investment frictions, or conditional risk premia in a production economy.",
                        "Discuss how the signal proxies for exposure to shocks to productivity, adjustment costs, or investment.",
                        "Relate cross-sectional pricing to production-based factors."
                    ]
                }
            # default: consumption_based
            return {
                "label": "Rational risk (consumption-based asset pricing)",
                "bullets": [
                    "Tie the signal to exposure to consumption risk or marginal utility (e.g., long-run risks, habit).",
                    "Discuss state dependence (good vs. bad times) and disaster/macro sensitivity.",
                    "Relate to consumption-based factors and intertemporal marginal rate of substitution."
                ]
            }

        if prompt_type == 'introduction':

            h = _hypothesis_guidance(kwargs.get('hypothesis_type', 'slow_diffusion'))

            main_prompt = f"""
            Write an introduction for a finance academic paper discussing the signal '{kwargs['signal_name']}' that predicts stock returns. Please follow these detailed guidelines:

            Hypothesis lens to adopt (be explicit and consistent throughout):
            - Lens: {h['label']}
            - What to emphasize:
                - {h['bullets'][0]}
                - {h['bullets'][1]}
                - {h['bullets'][2]}
                      
            Structure and Style:
            1. Motivation (2 paragraphs, ~200 words total):
            - Open with a broad statement about market efficiency or asset pricing
            - Identify the specific gap or puzzle in the literature
            - Use active voice and declarative statements

            2. Hypothesis Development (3 paragraphs, ~300 words total):
            - Present economic mechanisms linking the signal to returns
            - Draw on established theoretical frameworks
            - Build logical arguments step by step
            - Support each claim with citations to foundational papers in LaTeX format, such as \\cite{{AuthorsYear}}

            3. Results Summary (3 paragraphs, ~300 words total):
            - Lead with the strongest statistical finding
            - Present results in order of importance
            - Use precise statistical language
            - Include economic significance
            - Mirror exactly the terminology used in the results section

            4. Contribution (3 paragraphs, ~300 words total):
            - Position relative to 3-4 most closely related papers
            - Cite papers from the following journals: Journal of Finance, Journal of Financial Economics, Review of Financial Studies, Journal of Accounting Research, Journal of Accounting and Economics
            - Highlight methodological innovations
            - Emphasize novel findings
            - End with broader implications

            Writing Guidelines:
            - Use active voice (e.g., "We find" instead of "It is found")
            - Maintain formal academic tone
            - Include 2-3 citations per paragraph on average in LaTeX format, e.g., \\cite{{AuthorsYear}}
            - Use \\citep{{AuthorsYear}} for parenthetical citations
            - Use present tense for established findings
            - Use past tense for your specific results
            - Avoid speculation beyond the data
            - Make clear distinctions between correlation and causation

            Base the results section strictly on the following data, matching its terminology and precision:
            {kwargs['modified_latex']}

            Please provide the introduction in JSON format inside <response></response> XML tags, with each section as separate keys, and include the BibTeX entries for all citations used:

            ```json
            {{
                "motivation": "Your motivation text here.",
                "hypothesis_development": "Your hypothesis development text here.",
                "results_summary": "Your results summary text here.",
                "contribution": "Your contribution text here.",
                "bib_entries": {{
                    "CitationKey1": "BibTeX entry for CitationKey1",
                    "CitationKey2": "BibTeX entry for CitationKey2",
                    ...
                }}
            }}
            """
            return main_prompt

        elif prompt_type == 'data':
            numer = kwargs.get('numer', '')
            denom = kwargs.get('denom', '')
            numer_full = kwargs.get('numer_full', numer)
            denom_full = kwargs.get('denom_full', denom)
            signal_name = kwargs.get('signal_name', '')
            signal_type = kwargs.get('signal', 'ratio')
            
            if signal_type == 'ratio':
                construction_desc = f"the ratio of {numer_full} ({numer}) to {denom_full} ({denom})"
                formula_desc = f"dividing {numer} by {denom}"
            elif signal_type == 'diff':
                construction_desc = f"the year-over-year change in {numer_full} ({numer}), scaled by lagged {denom_full} ({denom})"
                formula_desc = f"computing ({numer}(t) - {numer}(t-1)) / {denom}(t-1)"
            else:
                construction_desc = f"a combination of {numer_full} and {denom_full}"
                formula_desc = f"combining {numer} and {denom}"
            
            prompt_data = f"""
            Write a Data section for an academic finance paper that describes how we construct the signal "{signal_name}".

            SIGNAL CONSTRUCTION DETAILS:
            - Signal Name: {signal_name}
            - Construction: {construction_desc}
            - Formula: {formula_desc}
            - Numerator: {numer_full} (COMPUSTAT item: {numer})
            - Denominator: {denom_full} (COMPUSTAT item: {denom})

            REQUIRED CONTENT:
            1. **Data Source** (1 short paragraph):
            - State that data comes from COMPUSTAT
            - Mention coverage of publicly traded U.S. companies
            - Note the sample period (can be general, e.g., "our sample spans several decades")

            2. **Variable Definitions** (1 paragraph):
            - Define {numer_full} ({numer}): What does this variable represent? What does it measure?
            - Define {denom_full} ({denom}): What does this variable represent? What does it measure?
            - Be ACCURATE - only state facts about what these COMPUSTAT items actually measure
            - Do NOT make up information about the variables

            3. **Signal Construction** (1 paragraph):
            - Explain the mathematical construction: {formula_desc}
            - Explain the ECONOMIC INTUITION: What does this ratio/change capture?
            - Mention frequency (e.g., "annual observations using fiscal year-end values")
            - Note any data cleaning steps (e.g., "we require non-missing values for both variables")

            WRITING GUIDELINES:
            - Keep it concise: 3 paragraphs, approximately 300-400 words total
            - Use active voice: "We construct the signal..." not "The signal is constructed..."
            - Be precise: Only make claims about variables that are factually correct
            - Use present tense for methodology
            - Include proper COMPUSTAT variable codes in parentheses
            - Match academic style from Journal of Finance or Review of Financial Studies

            AVOID:
            - Making up variable definitions
            - Overly detailed descriptions of COMPUSTAT database structure
            - Speculation about why the signal might work (save for introduction)
            - References to specific time periods unless necessary

            Please provide the data section in JSON format inside <response></response> XML tags:

            ```json
            {{
                "data_section": "Your complete data section text here (3 paragraphs)."
            }}
            ```
            """
            return prompt_data

        elif prompt_type == 'conclusion':
            main_prompt = f"""
            Write a conclusion for a financial research paper analyzing the signal '{kwargs['signal_name']}' in predicting stock returns.
            Summarize the key findings of the analysis, discussing the significance of the signal in terms of predictive power and practical implications.
            Conclude with suggestions for future research and limitations of this study. The conclusion should be based on the following abstract:
            {kwargs.get('abstract_text') or ""}

            Please provide the conclusion in JSON format inside <response></response> XML tags:

            ```json
            {{
                "conclusion": "Your conclusion text here."
            }}
            """
            return main_prompt
    # ----------------------------------------------------------------

    def call_llm(self, prompt: str) -> str:
        """Call the configured LLM provider with the given prompt and return text."""
        if self.dry_run:
            return ""  # Actual generation skipped in dry-run
        if not self.client:
            raise ValueError("LLM client not initialized.")
        return self.client.call(prompt)

    def parse_llm_response(self, response_text: str) -> Optional[Dict[str, Any]]:
        """Best-effort parsing for LLM outputs into JSON-like dictionaries.

        Attempts, in order:
        1) Extract JSON inside <response>...</response> or fenced code blocks.
        2) Extract top-level JSON/array-like structures.
        3) Infer sections as a mapping if JSON not found.
        4) Return minimal wrapper if certain keywords are present.
        """

        def clean_json_string(json_str: str) -> str:
            json_str = re.sub(r'```json\s*|\s*```', '', json_str)
            json_str = json_str.replace('\\"', '"')
            json_str = json_str.replace('\\\\', '\\')
            json_str = re.sub(r'\\([^\\])', r'\\\\\1', json_str)
            json_str = re.sub(r'\\\\([\\{}])', r'\\\1', json_str)
            return json_str.strip()

        def extract_json_content(text: str) -> Optional[Dict[str, Any]]:
            patterns = [
                r'<response>\s*(\{.*?\})\s*</response>',
                r'```(?:json)?\s*(\{.*?\})\s*```',
                r'(\{(?:[^{}]|(?:\{[^{}]*\}))*\})',
                r'(\[(?:[^\[\]]|(?:\[[^\[\]]*\]))*\])',
            ]
            for pattern in patterns:
                matches = re.finditer(pattern, text, re.DOTALL)
                for match in matches:
                    try:
                        json_str = clean_json_string(match.group(1))
                        return json.loads(json_str)
                    except json.JSONDecodeError:
                        continue
            return None

        def extract_sections_as_json(text: str) -> Optional[Dict[str, str]]:
            sections: Dict[str, str] = {}
            section_patterns = [
                r'^([A-Za-z_]+):\s*(.+?)(?=(?:[A-Za-z_]+:|$))',
                r'#{1,6}\s*([A-Za-z_]+)\s*\n(.*?)(?=(?:#{1,6}|$))',
                r'\\section\{([^}]+)\}\s*(.*?)(?=(?:\\section|$))',
            ]
            for pattern in section_patterns:
                matches = re.finditer(pattern, text, re.DOTALL | re.MULTILINE)
                for match in matches:
                    key = match.group(1).strip().lower().replace(' ', '_')
                    value = match.group(2).strip()
                    sections[key] = value
            return sections if sections else None

        try:
            json_content = extract_json_content(response_text)
            if json_content:
                return json_content
            sections = extract_sections_as_json(response_text)
            if sections:
                return sections
            if 'data_section' in response_text.lower() or 'conclusion' in response_text.lower():
                return {"content": response_text.strip()}
            print("Failed to parse response. Response text (truncated):")
            print(response_text[:500] + "..." if len(response_text) > 500 else response_text)
            return None
        except Exception as e:
            print(f"Error parsing LLM response: {str(e)}")
            print("Original response text (truncated):")
            print(response_text[:500] + "..." if len(response_text) > 500 else response_text)
            return None

    @staticmethod
    def fix_invalid_escape_sequences(json_str: str) -> str:
        return re.sub(r'\\(?![\\\"/bfnrtu])', r'\\\\', json_str)

    def generate_intro(
        self, signal_name: str, modified_latex: str, hypothesis_type: str = "slow_diffusion"
    ) -> Tuple[Optional[Dict[str, str]], Optional[Any]]:
        if self.dry_run:
            # Provide deterministic placeholders without calling LLM
            intro = {
                "motivation": f"[DRY RUN] Motivation for {signal_name}.",
                "hypothesis_development": f"[DRY RUN] Hypothesis development under {hypothesis_type} lens.",
                "results_summary": f"[DRY RUN] Results summary referencing LaTeX stats.",
                "contribution": f"[DRY RUN] Contribution relative to canonical literature.",
            }
            return intro, {}

        prompt = self.generate_prompt(
            'introduction',
            signal_name=signal_name,
            modified_latex=modified_latex,
            hypothesis_type=hypothesis_type
        )
        response_text = self.call_llm(prompt)
        json_response = self.parse_llm_response(response_text)
        if json_response:
            introduction_sections = {
                "motivation": json_response.get("motivation", ""),
                "hypothesis_development": json_response.get("hypothesis_development", ""),
                "results_summary": json_response.get("results_summary", ""),
                "contribution": json_response.get("contribution", ""),
            }
            bib_entries = json_response.get("bib_entries", {})
            return introduction_sections, bib_entries
        else:
            print("Failed to generate introduction.")
            return None, None

    def generate_data_section(
        self, signal_name: str, denom: str, numer: str, signal: str, compustat_map: dict
    ) -> Optional[str]:
        if self.dry_run:
            return (
                f"[DRY RUN] Data section for {signal_name}. Construction uses {numer} and {denom} as a {signal}."
            )
        # Get full variable names for better prompting
        numer_full = self._get_full_var_name(numer, compustat_map)
        denom_full = self._get_full_var_name(denom, compustat_map)
        
        prompt = self.generate_prompt(
            'data', 
            signal_name=signal_name, 
            denom=denom, 
            numer=numer, 
            signal=signal,
            numer_full=numer_full,
            denom_full=denom_full
        )
        response_text = self.call_llm(prompt)
        json_response = self.parse_llm_response(response_text)
        if json_response and "data_section" in json_response:
            return json_response["data_section"]
        else:
            print("Failed to generate data section.")
            return None

    def generate_conclusion(self, signal_name: str, abstract_text: Optional[str]) -> Optional[str]:
        if self.dry_run:
            snippet = (abstract_text or "").strip()[:200]
            return f"[DRY RUN] Conclusion for {signal_name}. Based on abstract snippet: {snippet}"
        prompt = self.generate_prompt('conclusion', signal_name=signal_name, abstract_text=abstract_text)
        response_text = self.call_llm(prompt)
        json_response = self.parse_llm_response(response_text)
        if json_response and "conclusion" in json_response:
            return json_response["conclusion"]
        else:
            print("Failed to generate conclusion.")
            return None

    def replace_latex_introduction(
        self, text: str, introduction_sections: Optional[Dict[str, str]]
    ) -> str:
        if not introduction_sections:
            return text
        introduction_text = (
            f"{introduction_sections.get('motivation','')}\n\n"
            f"{introduction_sections.get('hypothesis_development','')}\n\n"
            f"{introduction_sections.get('results_summary','')}\n\n"
            f"{introduction_sections.get('contribution','')}\n\n"
        )
        introduction_text = introduction_text.replace('%', '\\%').replace('$', '\\$')
        introduction_text = introduction_text.replace('\\n\\n', '\n\n')
        introduction_text = re.sub(r'[ ]{2,}', ' ', introduction_text)

        intro_section_escaped = re.escape("\\section{Introduction}")
        next_section_escaped = re.escape("\\section{")
        pattern = f"({intro_section_escaped})(.*?)(?={next_section_escaped})"

        def replacement_func(match: re.Match) -> str:
            return match.group(1) + "\n\n" + introduction_text + "\n\n"

        modified_text = re.sub(pattern, replacement_func, text, flags=re.DOTALL)
        return modified_text

    def replace_latex_data_section(
        self,
        original_text: str,
        insert_text: Optional[str],
        section_title: str = "\\section{Signal diagnostics}",
    ) -> str:
        if not insert_text:
            return original_text
        section_index = original_text.find(section_title)
        if section_index == -1:
            return original_text
        modified_text = (
            original_text[:section_index]
            + "\n\n" + "\\section{Data}\n\n" + insert_text + "\n"
            + original_text[section_index:]
        )
        return modified_text

    def replace_latex_conclusion(self, text: str, new_conclusion: Optional[str]) -> str:
        if not new_conclusion:
            return text
        conclusion_section = f"\\section{{Conclusion}}\n\n{new_conclusion}\n\n"
        conclusion_section = conclusion_section.replace('\\n\\n', '\n\n')
        pattern = r"\\newpage\s*\\clearpage\s*\\begin\{figure\}\[!htbp\]"
        match = re.search(pattern, text)
        if match:
            start, _ = match.span()
            return text[:start] + conclusion_section + text[start:]
        else:
            return text + conclusion_section

    def export_modified_latex(
        self,
        original_latex: str,
        output_file_path: str,
        introduction_sections: Optional[Dict[str, str]] = None,
        data_section: Optional[str] = None,
        conclusion: Optional[str] = None,
    ) -> None:
        modified_latex = original_latex
        modified_latex = self.replace_latex_introduction(modified_latex, introduction_sections)
        modified_latex = self.replace_latex_data_section(modified_latex, data_section)
        modified_latex = self.replace_latex_conclusion(modified_latex, conclusion)

        with open(output_file_path, 'w', encoding="utf-8") as file:
            file.write(modified_latex)
        print(f"Saved modified LaTeX file at {output_file_path}")

    def extract_abstract(self, latex_content: str) -> Optional[str]:
        match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", latex_content, re.DOTALL)
        if match:
            return match.group(1).strip()
        else:
            print("No abstract found in the document.")
            return None

    def extract_citations(self, text: str) -> List[str]:
        citations = re.findall(r'\\cite\{(.*?)\}', text)
        citation_keys: List[str] = []
        for citation in citations:
            keys = [key.strip() for key in citation.split(',')]
            citation_keys.extend(keys)
        return list(set(citation_keys))

    # ---------- Robust handling for bib_entries of many shapes ----------
    def _normalize_bib_entries(self, bib_entries: Any) -> List[str]:
        normalized: List[str] = []
        if bib_entries is None:
            return normalized
        if isinstance(bib_entries, str):
            s = bib_entries.strip()
            if s:
                normalized.append(s)
            return normalized
        if isinstance(bib_entries, dict):
            for _, val in bib_entries.items():
                if isinstance(val, str) and val.strip():
                    normalized.append(val.strip())
                elif isinstance(val, dict):
                    entry = val.get("entry") or val.get("bibtex") or val.get("BibTeX") or ""
                    if isinstance(entry, str) and entry.strip():
                        normalized.append(entry.strip())
            return normalized
        if isinstance(bib_entries, list):
            for item in bib_entries:
                if isinstance(item, str):
                    if item.strip():
                        normalized.append(item.strip())
                elif isinstance(item, dict):
                    entry = item.get("entry") or item.get("bibtex") or item.get("BibTeX") or ""
                    if isinstance(entry, str) and entry.strip():
                        normalized.append(entry.strip())
        return normalized
    # -------------------------------------------------------------------

    def create_bib_entries(
        self,
        bib_entries: Any,
        signal: Signal,
        version: Optional[int] = None,
        bib_filename: Optional[str] = None,
    ) -> None:
        source_bib_path = os.path.join(self.base_dir, 'newSignalTestBib.bib')
        if bib_filename is not None:
            destination_bib_path = os.path.join(self.base_dir, f"{bib_filename}.bib")
        elif version is not None:
            destination_bib_path = os.path.join(
                self.base_dir, f"{signal.var_name}_modified_v{version}.bib"
            )
        else:
            destination_bib_path = os.path.join(self.base_dir, f"{signal.var_name}.bib")

        normalized_entries = self._normalize_bib_entries(bib_entries)

        try:
            shutil.copy(source_bib_path, destination_bib_path)
            appended = 0
            if normalized_entries:
                with open(destination_bib_path, 'a', encoding="utf-8") as bib_file:
                    for entry in normalized_entries:
                        entry_fixed = entry.replace('\\n', '\n')
                        bib_file.write(entry_fixed + '\n')
                        appended += 1
            print(f"Appended {appended} bib entries to {destination_bib_path}")
        except FileNotFoundError:
            print(f"Source BibTeX file {source_bib_path} not found.")
