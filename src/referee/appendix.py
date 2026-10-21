"""Assemble the technical appendix from the repository and render it to Word.

paper/appendix-template.md holds the prose and placeholders; this module fills
them from the prompts, the form, the codebook, the run manifests, and the
generated numbers, writes paper/appendix.md, and renders paper/appendix.docx.
Nothing in the appendix is typed in by hand.
"""

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

from . import config
from .form import assemble_prompt, load_form
from .grade import grader_prompt_template, instructions_with_rulings
from .numbers import manuscript_fingerprints
from .review import sha256_text

PAPER = config.ROOT / "paper"


# How the appendix words the editor's decision recorded in sample/confidential/sample-article.json.
DECISION_PHRASE = {"Reject": "rejected", "Accept": "accepted"}

def _body_without_title(md: str) -> str:
    """Drop the file's own H1, strip HTML comments, and push headings down one level for inclusion."""
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    lines = []
    for line in md.splitlines():
        if line.startswith("# "):
            continue
        if line.startswith("### "):
            lines.append("**" + line[4:].strip() + "**")
        elif line.startswith("## "):
            lines.append("### " + line[3:])
        else:
            lines.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def _latest(folder: Path) -> Path:
    runs = sorted(p for p in folder.iterdir() if p.is_dir() and (p / "manifest.json").exists())
    if not runs:
        raise FileNotFoundError(f"no recorded run under {folder}")
    return runs[-1]


def _money(x) -> str:
    return f"${x:.2f}" if isinstance(x, (int, float)) else str(x)


def build_values(reviewer_run: Path | None = None, grader_run: Path | None = None) -> dict:
    form = load_form()
    prompt = assemble_prompt(form)
    reviewer_run = Path(reviewer_run) if reviewer_run else _latest(config.PATHS["runs"])
    grader_run = Path(grader_run) if grader_run else _latest(config.PATHS["grader_runs"])
    rm = json.loads((reviewer_run / "manifest.json").read_text(encoding="utf-8"))
    gm = json.loads((grader_run / "manifest.json").read_text(encoding="utf-8"))
    design = json.loads((PAPER / "design-values.json").read_text(encoding="utf-8"))

    sys.path.insert(0, str(PAPER))
    import render_documents as rd  # the power arithmetic lives there

    mde, crit = rd.paired_mde(design["sample_size"], design["alpha"], design["power"])

    # reviewer table
    names = list(rm["reviewers"])
    recs = [rm["reviewers"][n] for n in names]

    def row(label, f):
        return "| " + label + " | " + " | ".join(str(f(r)) for r in recs) + " |"

    reviewer_table = "\n".join(
        [
            row("Vendor", lambda r: r["vendor"]),
            row("Model requested", lambda r: f"`{r['model_requested']}`"),
            row("Model served", lambda r: f"`{r.get('model_served', 'none')}`"),
            row("Status", lambda r: r["status"]),
            row("Settings", lambda r: "; ".join(f"{k}: {v}" for k, v in r["settings"].items())),
            row("Price per million tokens (input / output)", lambda r: f"${r['price_per_million']['input']:.2f} / ${r['price_per_million']['output']:.2f}"),
            row("Input tokens", lambda r: f"{r['usage']['input_tokens']:,}" if r.get("usage") else "none"),
            row("Output tokens", lambda r: f"{r['usage']['output_tokens']:,}" if r.get("usage") else "none"),
            row("Fees", lambda r: _money(r.get("cost_usd", "none"))),
            row("Elapsed", lambda r: f"{r['elapsed_seconds']:.0f} s" if r.get("elapsed_seconds") else "none"),
            row("Retries", lambda r: str(sum(1 for a in r["attempts"] if "error" in a))),
        ]
    )
    g = gm["grader"]
    t = gm["totals"]
    grader_table = "\n".join(
        [
            f"| Vendor | {g['vendor']} |",
            f"| Model requested | `{g['model']}` |",
            f"| Model served | `{', '.join(t['models_served'])}` |",
            "| Settings | " + "; ".join(f"{k}: {v}" for k, v in g["settings"].items()) + " |",
            f"| Price per million tokens (input / output) | ${g['price_per_million']['input']:.2f} / ${g['price_per_million']['output']:.2f} |",
            f"| Calls | {t['calls']} ({t['failed_calls']} failed; {sum(c.get('retries', 0) for c in gm['calls'])} retried) |",
            f"| Input tokens | {t['input_tokens']:,} |",
            f"| Output tokens (including thinking) | {t['output_tokens']:,} |",
            f"| Fees | {_money(t['cost_usd'])} |",
            f"| Model time | {t['elapsed_seconds'] / 60:.1f} min |",
            f"| Critiques coded | {sum(1 for _ in csv.DictReader((grader_run / 'coded-critiques.csv').open(encoding='utf-8')))} |",
        ]
    )

    # coded rows for A3 and A7 counts
    rows = list(csv.DictReader((grader_run / "coded-critiques.csv").open(encoding="utf-8")))
    ai_rigor = [r for r in rows if r["arm"] == "ai" and r["category"] == "rigor"]
    n_human = len({r["review"] for r in rows if r["arm"] == "human"})
    # every coded critique, so the numbers in A7 can be recomputed from the codes (no review text)
    def cell(s: str) -> str:
        return (s or "").replace("|", "/").replace("\n", " ")
    coded_rows_table = "\n".join(
        ["| Review | Arm | Critique | Dimension | Category | Checkability | Form row | Location | Words |",
         "|:--|:--|--:|:--|:--|:--|:--|:--|--:|"]
        + [f"| {r['review']} | {r['arm']} | {r['critique']} | {cell(r['dimension'])} | {cell(r['category'])} | {cell(r['checkability'])} | "
           f"{cell(r['form_row'])} | {cell(r['location'])} | {r['words']} |" for r in rows]
    )
    human_count = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}.get(n_human, str(n_human))
    segmented = {n: sum(1 for r in rows if r["review"] == n) for n in names}

    # checks summary
    disposition = f"`sample/runs/{rm['run_id']}/disposition.md`"
    checks = []
    for n in names:
        p = reviewer_run / f"checks-{n}.json"
        if p.exists():
            c = json.loads(p.read_text(encoding="utf-8"))
            parts = []
            for x in c["checks"]:
                if x["pass"]:
                    parts.append(f"{x['name']}: pass")
                elif isinstance(x["failures"], dict):
                    k = sum(len(v) for v in x["failures"].values())
                    parts.append(f"{x['name']}: flagged {k} item{'s' if k != 1 else ''}, verified by hand as accurate ({disposition})")
                else:
                    parts.append(f"{x['name']}: {len(x['failures'])} failures ({disposition})")
            checks.append(
                f"- **{n}** ({c['critique_count']} numbered points; {segmented.get(n, 0)} critiques as the grader segmented them): "
                + "; ".join(parts) + "."
            )
    checks_summary = "\n".join(checks)

    # form
    rows_table = "\n".join(f"| {r['label']} | {' / '.join(form['rating_levels'])} |" for r in form["rows"])

    # decisions table
    dec_rows = []
    for f in sorted((config.ROOT / "docs" / "decisions").glob("20*.md")):
        title = next((l[2:].strip() for l in f.read_text(encoding="utf-8").splitlines() if l.startswith("# ")), f.stem)
        dec_rows.append(f"| {f.stem[:10]} | {title} | `docs/decisions/{f.name}` |")
    decisions_table = "| Date | Decision | File |\n|:--|:--|:--|\n" + "\n".join(dec_rows)

    # the full numbers, with the referee reports and decision letter, which only the appendix carries
    numbers_md = config.PATHS["numbers_full"].read_text(encoding="utf-8")
    numbers_body = _body_without_title(numbers_md)
    numbers_body = re.sub(r"^Generated by `ref numbers`.*?\n\n", "", numbers_body, count=1, flags=re.S)

    article = json.loads(config.PATHS["sample_article"].read_text(encoding="utf-8"))
    gtemplate, gmeta = grader_prompt_template()

    def fence_safe(s: str) -> str:
        # the prompts contain their own code fences; mark them so the appendix's fence stays intact
        return s.strip().replace("```", "'''")

    return {
        "built_date": date.today().isoformat(),
        "reviewer_run": rm["run_id"],
        "grader_run": gm["run_id"],
        "prompt_sha256": sha256_text(prompt),
        "reviewer_prompt": fence_safe(prompt),
        "form_source_note": form["source_note"],
        "form_rows_table": rows_table,
        "recommendation_options": ", ".join(form["recommendation_options"]),
        "free_text_fields": "; ".join(f["label"] for f in form["free_text_fields"]),
        "reviewer_table": reviewer_table,
        "price_source_note": "Anthropic: " + config.PRICE_SOURCE["anthropic"] + ". OpenAI: " + config.PRICE_SOURCE["openai"] + ".",
        "grader_table": grader_table,
        "grader_model_note": config.GRADER.get("price_note", "") + " " + config.GRADER.get("model_note", ""),
        "manuscript_sha256": rm["manuscript"]["sha256"],
        "posted_manuscript_sha256": manuscript_fingerprints(rm)["posted_sha256"],
        "repository_name": config.PUBLIC_REPOSITORY["name"],
        "repository_url": config.PUBLIC_REPOSITORY["url"],
        "repository_tag": config.PUBLIC_REPOSITORY["tag"],
        "checks_summary": checks_summary,
        "codebook_sha256": gmeta["codebook_sha256"],
        "codebook": _body_without_title(config.PATHS["codebook"].read_text(encoding="utf-8")),
        "grader_prompt_segment": fence_safe(config.PATHS["grader_prompt_segment"].read_text(encoding="utf-8")),
        "grader_prompt": fence_safe(config.PATHS["grader_prompt"].read_text(encoding="utf-8")),
        "instructions_sha256": gmeta["instructions_sha256"],
        "coding_instructions": _body_without_title(instructions_with_rulings(config.PATHS["coding_instructions"].read_text(encoding="utf-8"))),
        "reliability_percent": design["reliability_percent"],
        "decision_date": article["decision_date"],
        # the outcome and the number of reports are read from the confidential facts, so the public template states neither
        "editorial_history": f"{DECISION_PHRASE.get(article['editor_decision'], 'decided (' + article['editor_decision'] + ')')} "
                             f"on {article['decision_date']} after {human_count} referee reports",
        "human_review_count": human_count,
        "coded_rows_table": coded_rows_table,
        "coded_rows_count": len(rows),
        "manuscript_sha256_short": rm["manuscript"]["sha256"][:16] + "…",
        "manuscript_pages": rm["manuscript"]["pages"],
        "prototype_numbers": numbers_body,
        "ai_checkable_errors": sum(1 for r in ai_rigor if r["checkability"] == "checkable error"),
        "ai_rigor_critiques": len(ai_rigor),
        "sample_size": design["sample_size"],
        "alpha": design["alpha"],
        "power": design["power"],
        "minimum_detectable_effect": f"{mde:.2f}",
        "minimum_detectable_effect_precise": f"{mde:.4f}",
        "df": design["sample_size"] - 1,
        "t_critical": f"{crit:.3f}",
        "decisions_table": decisions_table,
    }


def assemble(values: dict) -> str:
    text = (PAPER / "appendix-template.md").read_text(encoding="utf-8")
    for k, v in values.items():
        text = text.replace("{{" + k + "}}", str(v))
    # the grader prompts reproduced inside code fences legitimately contain their own placeholders
    outside_code = re.sub(r"```.*?```", "", text, flags=re.S)
    left = re.findall(r"\{\{(\w+)\}\}", outside_code)
    if left:
        raise ValueError("unfilled placeholders: " + ", ".join(sorted(set(left))))
    return text.strip() + "\n"


# --- Word rendering -----------------------------------------------------------


def _add_runs(paragraph, text: str, size=None):
    """Add text with **bold**, *italic*, and `code` runs."""
    from docx.shared import Pt

    for part in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)", text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2]); run.bold = True
        elif part.startswith("`") and part.endswith("`"):
            run = paragraph.add_run(part[1:-1]); run.font.name = "Consolas"
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            run = paragraph.add_run(part[1:-1]); run.italic = True
        else:
            run = paragraph.add_run(part)
        if size:
            run.font.size = Pt(size)


def render_docx(text: str, output: Path) -> None:
    from docx import Document
    from docx.enum.text import WD_BREAK
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt, RGBColor

    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    sec.top_margin = sec.bottom_margin = Inches(0.85)
    sec.left_margin = sec.right_margin = Inches(0.95)
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(11)
    normal.paragraph_format.space_after = Pt(6)
    for name, size in [("Title", 18), ("Heading 1", 13), ("Heading 2", 11.5), ("Heading 3", 11)]:
        st = doc.styles[name]
        st.font.name = "Times New Roman"; st.font.size = Pt(size); st.font.bold = True
        st.font.color.rgb = RGBColor(0, 0, 0)
        fonts = st.element.get_or_add_rPr().find(qn("w:rFonts"))
        if fonts is not None:
            for attr in list(fonts.attrib):
                if attr.endswith("Theme"):
                    del fonts.attrib[attr]
        st.paragraph_format.space_before = Pt(12); st.paragraph_format.space_after = Pt(5)
        st.paragraph_format.keep_with_next = True
    footer = sec.footer.paragraphs[0]; footer.alignment = 2
    fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), "PAGE"); footer._p.append(fld)

    lines = text.splitlines()
    i = 0
    first_h1_done = False
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            for code_line in lines[i + 1:j]:
                p = doc.add_paragraph()
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.left_indent = Inches(0.25)
                run = p.add_run(code_line if code_line.strip() else " ")
                run.font.name = "Consolas"; run.font.size = Pt(8.5)
            doc.add_paragraph()
            i = j + 1
            continue
        if line.startswith("|"):
            j = i
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            rows = [l for l in lines[i:j] if not re.match(r"^\|\s*:?-+", l)]
            cells = [[s.strip() for s in r.strip().strip("|").split("|")] for r in rows]
            ncols = max(len(c) for c in cells)
            table = doc.add_table(rows=0, cols=ncols); table.style = "Table Grid"
            for k, vals in enumerate(cells):
                r = table.add_row()
                r._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
                if k == 0:
                    r._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
                for cell, value in zip(r.cells, vals + [""] * (ncols - len(vals))):
                    cell.text = ""
                    p = cell.paragraphs[0]
                    p.paragraph_format.space_after = Pt(2); p.paragraph_format.space_before = Pt(2)
                    _add_runs(p, value, size=9)
                    if k == 0:
                        for run in p.runs:
                            run.bold = True
            doc.add_paragraph()
            i = j
            continue
        if line.startswith("# "):
            doc.add_paragraph(line[2:], "Title"); first_h1_done = True
        elif line.startswith("## "):
            title = line[3:]
            if title.startswith("A1."):  # the map is page one; the body starts on a new page
                doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
            doc.add_paragraph(title, "Heading 1")
        elif line.startswith("### "):
            doc.add_paragraph(line[4:], "Heading 2")
        elif re.match(r"^\s*- ", line):
            p = doc.add_paragraph(style="List Bullet"); _add_runs(p, re.sub(r"^\s*- ", "", line))
        elif re.match(r"^\s*\d+\. ", line):
            # numbered by hand so that each list starts at 1 (Word's List Number style continues across lists)
            m = re.match(r"^\s*(\d+)\. (.*)", line)
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.3)
            p.paragraph_format.first_line_indent = Inches(-0.3)
            p.paragraph_format.space_after = Pt(3)
            _add_runs(p, m.group(1) + ".\t" + m.group(2))
        elif line.startswith(">"):
            p = doc.add_paragraph(); p.paragraph_format.left_indent = Inches(0.3); _add_runs(p, line.lstrip("> "))
            for run in p.runs:
                run.italic = True
        elif line.strip():
            # join consecutive prose lines (one sentence per line) into one paragraph
            j = i
            buf = []
            while j < len(lines) and lines[j].strip() and not re.match(r"^(#|\||```|\s*- |\s*\d+\. |>)", lines[j]):
                buf.append(lines[j].strip()); j += 1
            p = doc.add_paragraph(); _add_runs(p, " ".join(buf))
            i = j
            continue
        i += 1
    doc.core_properties.author = "Scott Shane and David Clingingsmith"
    doc.core_properties.title = "Technical Appendix"
    doc.save(str(output))


def build(reviewer_run: Path | None = None, grader_run: Path | None = None) -> tuple[Path, Path]:
    values = build_values(reviewer_run, grader_run)
    text = assemble(values)
    md = PAPER / "appendix.md"
    md.write_text(text, encoding="utf-8", newline="\n")
    docx = PAPER / "appendix.docx"
    render_docx(text, docx)
    return md, docx
