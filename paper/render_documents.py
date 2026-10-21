"""Render the proposal and appendix plan, deriving power and checking word count.

Requires python-docx. Refuses to overwrite a Word file changed since rendering.
The model pipeline remains to be built; this script only prepares documents.
"""
from pathlib import Path
import hashlib
import json
import math
import re

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / 'paper'
OUTPUTS = {
    'proposal': ROOT / 'docs/proposal-2026-09-21.docx',
}
# The technical appendix is assembled and rendered by `ref appendix` (src/referee/appendix.py).
# The September 21 appendix plan it replaced is kept in deprecated/.
MANIFEST = PAPER / 'generated/document-build.json'


def paired_mde(n, alpha, target, intervals=6000):
    """Integrate T=(Z+delta)/sqrt(V/df), V~chi-square(df); solve exact t power.

    Simpson integration over sqrt(V/df) in [0,3]. This interval suffices for
    the specified n=100; this routine is not a general small-sample library.
    """
    if n != 100:
        raise ValueError('Revalidate integration bounds before changing sample size.')
    df = n - 1
    step = 3 / intervals
    log_constant = math.log(2) + df / 2 * math.log(df / 2) - math.lgamma(df / 2)
    grid = []
    for k in range(1, intervals + 1):
        y = k * step
        density = math.exp(log_constant + (df - 1) * math.log(y) - df * y * y / 2)
        coefficient = 1 if k == intervals else (4 if k % 2 else 2)
        grid.append((y, density * coefficient * step / 3))
    assert abs(sum(w for _, w in grid) - 1) < 1e-10
    def rejection(cutoff, delta):
        return sum(w * (math.erfc((cutoff*y-delta)/math.sqrt(2))
                         + math.erfc((cutoff*y+delta)/math.sqrt(2))) / 2
                   for y, w in grid)
    def solve(fn, target_value, lo, hi):
        for _ in range(55):
            mid = (lo + hi) / 2
            if fn(mid) < target_value:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    critical = solve(lambda c: 1-rejection(c, 0), 1-alpha, 0, 5)
    effect = solve(lambda d: rejection(critical, d*math.sqrt(n)), target, 0, 1)
    return effect, critical


def resolve(text, values):
    text = re.sub(r'\{\{(\w+)\}\}', lambda m: str(values[m.group(1)]), text)
    assert '{{' not in text
    return text


def no_split(row):
    trpr = row._tr.get_or_add_trPr()
    trpr.append(OxmlElement('w:cantSplit'))


def make_doc(text, output):
    doc = Document()
    for border in list(doc.styles.element.iter(qn('w:pBdr'))):
        border.getparent().remove(border)
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    sec.top_margin = sec.bottom_margin = Inches(.85)
    sec.left_margin = sec.right_margin = Inches(.95)
    normal = doc.styles['Normal']
    normal.font.name = 'Times New Roman'
    normal.font.size = Pt(11)
    normal.paragraph_format.line_spacing = 1.06
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.widow_control = True
    for name, size in [('Title',18),('Subtitle',13),('Heading 1',12),('Heading 2',11)]:
        st = doc.styles[name]
        st.font.name = 'Times New Roman'
        st.font.size = Pt(size)
        st.font.color.rgb = RGBColor(0,0,0)
        st.font.bold = name != 'Subtitle'
        fonts = st.element.get_or_add_rPr().find(qn('w:rFonts'))
        if fonts is not None:
            for attr in list(fonts.attrib):
                if attr.endswith('Theme'):
                    del fonts.attrib[attr]
        st.paragraph_format.space_before = Pt(12 if 'Heading' in name else 0)
        st.paragraph_format.space_after = Pt(5)
        st.paragraph_format.keep_with_next = True
    footer = sec.footer.paragraphs[0]
    footer.alignment = 2
    field = OxmlElement('w:fldSimple')
    field.set(qn('w:instr'),'PAGE')
    footer._p.append(field)
    refs = False
    for block in text.strip().split('\n\n'):
        if block.startswith('|'):
            rows = [line for line in block.splitlines() if not re.match(r'^\|\s*:?-+',line)]
            cells = [[s.strip() for s in line.strip('|').split('|')] for line in rows]
            table = doc.add_table(rows=0, cols=len(cells[0]))
            table.style = 'Table Grid'
            for i, vals in enumerate(cells):
                row = table.add_row()
                no_split(row)
                if i == 0:
                    row._tr.get_or_add_trPr().append(OxmlElement('w:tblHeader'))
                for cell, value in zip(row.cells, vals):
                    cell.text = value
                    for p in cell.paragraphs:
                        p.paragraph_format.space_after = Pt(4)
                        p.paragraph_format.space_before = Pt(3)
                        for run in p.runs:
                            run.font.size = Pt(9.5)
                            run.bold = i == 0
            doc.add_paragraph().paragraph_format.space_after = Pt(0)
        elif block.startswith('# '):
            doc.add_paragraph(block[2:], 'Title')
        elif block.startswith('## Testing'):
            doc.add_paragraph(block[3:], 'Subtitle')
        elif block.startswith('## '):
            title = block[3:]
            refs = title in ('References','Reference')
            doc.add_paragraph(title, 'Heading 1')
        elif block.startswith('### '):
            doc.add_paragraph(block[4:], 'Heading 2')
        else:
            p = doc.add_paragraph(('\n' if block.startswith('Scott Shane') else ' ').join(block.splitlines()))
            if block.startswith('Scott Shane'):
                p.paragraph_format.space_after = Pt(12)
            if refs:
                for r in p.runs:
                    r.font.size = Pt(9.5)
    doc.core_properties.author = 'Scott Shane and David Clingingsmith'
    doc.core_properties.title = text.splitlines()[0].lstrip('# ')
    doc.core_properties.subject = 'Organization Science proposal and research artifact'
    doc.save(output)


def main():
    old = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    for name, path in OUTPUTS.items():
        if path.exists():
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != old.get('outputs',{}).get(name,{}).get('sha256'):
                raise RuntimeError(f'{path.name} has edits or an unknown origin; compare before overwriting.')
    values = json.loads((PAPER/'design-values.json').read_text())
    mde, critical = paired_mde(values['sample_size'],values['alpha'],values['power'])
    check, _ = paired_mde(values['sample_size'],values['alpha'],values['power'],3000)
    assert abs(mde-check) < 1e-8
    values.update(minimum_detectable_effect=f'{mde:.2f}',
                  minimum_detectable_effect_precise=f'{mde:.4f}')
    # the public repository's address and Stage 1 label (src/referee/config.py, PUBLIC_REPOSITORY)
    import sys
    sys.path.insert(0, str(ROOT/'src'))
    from referee.config import PATHS, PUBLIC_REPOSITORY
    values.update(repository_url=PUBLIC_REPOSITORY['url'], repository_tag=PUBLIC_REPOSITORY['tag'])
    # numbers from the recorded sample runs, written by `ref numbers` (src/referee/numbers.py);
    # confidential, so absent from the public repository
    sample = PATHS['sample_numbers']
    if sample.exists():
        values.update({k:v for k,v in json.loads(sample.read_text()).items() if not isinstance(v,(dict,float)) and k != 'what'})
    resolved = {name:resolve((PAPER/f'{name}.md').read_text(),values) for name in OUTPUTS}
    body = resolved['proposal'].split('## The opportunity')[1].split('## References')[0]
    count = len(body.split()) + len('The opportunity'.split())
    assert 1500 <= count <= 2000, count
    MANIFEST.parent.mkdir(exist_ok=True)
    out = {}
    for name, path in OUTPUTS.items():
        make_doc(resolved[name], path)
        out[name] = {'path':str(path.relative_to(ROOT)),
                     'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    report = {'proposal_body_words_including_section_headings':count,
              'word_count_method':'Whitespace-separated tokens; excludes title, subtitle, byline, references.',
              'power_inputs':json.loads((PAPER/'design-values.json').read_text()),
              'minimum_detectable_paired_standardized_effect':mde,
              't_critical':critical,
              'quadrature_crosscheck_absolute_difference':abs(mde-check),
              'outputs':out}
    MANIFEST.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
