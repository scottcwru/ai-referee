"""Build grader/codebook_v9.md from grader/codebook_v8.md.

Two stages, as the codebook was made:

1. The draft of 2026-10-07 (David, with Claude Code): adds a usual-category column,
   the entries decided on 2026-10-06, the split of Incorporation of Relevant
   Literature, and the proposed writing boundary. Entries the rigor definition did not
   settle were marked ? for Scott. This stage is the original script, unchanged.
2. Adoption (Scott's rulings of 2026-10-09): settles the ? entries and boundary rule 4,
   moves Contribution relative to length to other, replaces the draft notes with the
   adopted ones, and applies the typography of the adopted file, which passed through
   Word (curly quotes, no code marks, the definition paragraph on one line).

    python grader/build_codebook_v9.py            # write grader/codebook_v9.md
    python grader/build_codebook_v9.py --check    # confirm the committed file is what this builds

--check verifies the current codebook. Historical run manifests fingerprint the
versions preserved in their grader-prompt-as-sent.md; subsequent editorial cleanup
of introductory and draft-status wording changed those fingerprints.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V8 = ROOT / 'grader' / 'codebook_v8.md'
V9 = ROOT / 'grader' / 'codebook_v9.md'


# ---- Stage 1: the draft of 2026-10-07 ---------------------------------------

# Usual category by code. R rigor, C contribution, O other, ? question for Scott.
CATEGORY = {
    'THE.GROUND': 'C', 'THE.CONTRIB': 'C', 'THE.UTIL': 'C', 'THE.FALS': '?',
    'RQ.IMP': 'C', 'RQ.FRAME': 'C', 'RQ.PURP': '?',
    'SIL.PRAC': 'C', 'SIL.THEORY': 'C', 'SIL.LIM': 'R', 'SIL.EXT': 'R',
    'FIT': 'C', 'FLAW': '?',
}
PREFIX = [('MET', 'R'), ('CON.', 'R'), ('THE.COH', 'R'), ('THE.LINK', 'R'),
          ('CONTRIB', 'C'), ('ORIG', 'C'), ('WRI', 'O'), ('LIT', '?')]


def category(code):
    if code in CATEGORY:
        return CATEGORY[code]
    for p, c in PREFIX:
        if code.startswith(p):
            return c
    raise KeyError(code)


NEW_ROWS = {
    # inserted after the row with this code
    'MET.DISC.ETH': [
        ('MET.QUAL', 'Qualitative methods *(parent)*', 'The qualitative procedure falls short of the standards for its method, for a reason not listed below. Added 2026-10-06.', 'R'),
        ('MET.QUAL.DATA', 'Data structure (theme construction and interpretation)', 'Themes are not soundly built from the data: two themes are indistinguishable, a theme bundles unrelated content, or the path from codes to themes does not hold. Label: Gioia, Corley, and Hamilton (2013).', 'R'),
        ('MET.QUAL.COH', 'Meaningful coherence (choice and fidelity of method)', 'The qualitative method is not justified for the question, or the study does not follow the method it claims (for example, it claims grounded theory or phenomenology but does not apply it). Label: Tracy (2010).', 'R'),
        ('MET.QUAL.CRED', 'Credibility (trustworthiness strategies)', 'Steps that establish the trustworthiness of the analysis (member checking, triangulation, an audit trail, peer debriefing) were not taken or are inadequate. Label: Guba (1981); Tracy (2010).', 'R'),
        ('MET.QUAL.SAT', 'Theoretical saturation', 'The sample is not shown to be sufficient, or a claim of saturation is not supported. Label: Eisenhardt (1989).', 'R'),
        ('MET.QUAL.TRANS', 'Translation and transcription fidelity', 'Translation or transcription may not have preserved participants\' meaning, or how it did is not shown. Authors\' label.', 'R'),
        ('MET.QUAL.REFLEX', 'Self-reflexivity', 'The researchers\' position and its influence on data collection and interpretation are not examined. Label: Tracy (2010).', 'R'),
    ],
    'THE.FALS': [
        ('THE.CONCEPT', 'Concept clarity', 'A theoretical concept is undefined, defined too narrowly or broadly, overlaps another concept, or is used in more than one sense. Authors\' label. Added 2026-10-06.', '?'),
        ('THE.UNIT', 'Unit or level of analysis', 'The argument or analysis treats its object at the wrong unit or level (for example, perspectives in the literature treated as kinds of real-world arrangement, or individual-level evidence used for claims about organizations). Authors\' label. Added 2026-10-06.', 'R'),
    ],
    'CON.REPL': [
        ('CON.INCON', 'Reported results inconsistent', 'Numbers or facts differ between passages, tables, or figures, or a reported value is wrong on its face (for example, an impossible unit). Moved from Mechanics and clarity; proposed 2026-10-07.', 'R'),
    ],
}

LIT_ROWS = [
    ('LIT.SRC', 'Literature: a source is misrepresented', 'A cited source does not say what the paper says it says, or prior findings are reported inaccurately. Split from LIT 2026-10-06.', 'R'),
    ('LIT.POS', 'Literature: positioning and coverage', 'Relevant prior work is missing, the paper is not positioned against it, or the findings are not compared with it. Split from LIT 2026-10-06.', 'C'),
]

EDITS = {
    # code: (old text, new text) inside the definition
    'WRI.MECH': (', or numbers that differ between passages.', '. (Numbers that differ between passages move to CON.INCON.)'),
    'WRI.TITLE': ('do not accurately convey or index the study.', 'do not convey or index the study well. A title or abstract that states something the study did not do or does not show is CON.SHOWN.'),
}

ROW = re.compile(r'^\| (?P<code>[A-Z][A-Z.]*) \| (?P<entry>.*?) \| (?P<defn>.*) \|$')


def draft(v8: str) -> str:
    out_lines = []
    for line in v8.splitlines():
        if line.startswith('# Codebook, version 8'):
            out_lines.append('# Codebook, version 9 (draft for Scott, 2026-10-07)')
            continue
        if line == '| Code | Entry | The referee asserts |':
            out_lines.append('| Code | Entry | The referee asserts | Usual category |')
            continue
        if line == '|:--|:--|:--|':
            out_lines.append('|:--|:--|:--|:-:|')
            continue
        m = ROW.match(line)
        if not m:
            out_lines.append(line)
            continue
        code, entry, defn = m['code'], m['entry'], m['defn']
        if code == 'LIT':
            out_lines.append(f'| LIT | Incorporation of Relevant Literature *(parent)* | {defn} | — |')
            for c, e, d, k in LIT_ROWS:
                out_lines.append(f'| {c} | {e} | {d} | {k} |')
            continue
        if code in EDITS:
            old, new = EDITS[code]
            assert old in defn, code
            defn = defn.replace(old, new)
        out_lines.append(f'| {code} | {entry} | {defn} | {category(code)} |')
        for c, e, d, k in NEW_ROWS.get(code, []):
            out_lines.append(f'| {c} | {e} | {d} | {k} |')

    text = '\n'.join(out_lines) + '\n'
    intro_old = 'The dimension list from `step9_dimensions_v8.md`'
    assert intro_old in text
    text = text.replace(intro_old, '**Draft.** Built by `build_codebook_v9.py` from `grader/codebook_v8.md`, adding the entries decided on 2026-10-06 and a usual-category column (R rigor, C contribution, O other, ? question for Scott). The category is coded for each critique separately; the column is a guide, not a rule. Every change from v8 is marked "Added," "Split," "Moved," or "proposed" in its row.\n\n**About the usual-category column.** The column is new in v9 and is a proposal by David and Claude, not a result. Each entry\'s definition was read against the definition of rigor decided on 2026-10-06 (`docs/decisions/2026-10-06-rigor-defined-by-subject.md`) and assigned R, C, or O by hand; entries the definition does not settle are marked ?. No coded data stands behind the values, and no earlier document assigns categories to these entries (the rigor and contribution labels in `step1_scholarly_literature.md`, `step2_journal_forms.md`, and `step5_skeleton.md` sort source criteria, not entries, mostly under the falsity test that the October 6 decision replaced; the six rigor dimensions named in the proposal were replaced by the derived list). The column needs Scott\'s confirmation as a whole, not only for the entries marked ?. Once the agreement test has coded critiques, each entry\'s usual category could instead be set to the category its critiques most often receive.\n\nThe dimension list from `step9_dimensions_v8.md`')
    rule4_old = '4. "Claim lacks supporting citation" is LIT: it means failing to find and credit prior work.'
    assert rule4_old in text
    text = text.replace(rule4_old, '4. "Claim lacks supporting citation" is LIT.POS: it means failing to find and credit prior work. *(Open question for Scott: under a subject definition this may instead be rigor, as an unsupported claim.)*')
    text = text.rstrip('\n') + '\n9. A qualitative step that is *not reported* is MET.DISC.PROC; a step that was *not taken or was done badly* goes to the MET.QUAL entry for it. Added 2026-10-07.\n'
    return text


# ---- Stage 2: adoption, with Scott's rulings of 2026-10-09 ------------------

# Usual categories as ruled: the ? entries settled, and one entry moved.
RULINGS = {'THE.FALS': 'R', 'THE.CONCEPT': 'R', 'RQ.PURP': 'C', 'FLAW': 'O', 'CONTRIB.LEN': 'O'}

ADOPTED_NOTES = (
    'Built by build_codebook_v9.py from grader/codebook_v8.md, adding the entries decided on 2026-10-06 and a usual-category column (R rigor, C contribution, O other). The category is coded for each critique separately; the column is a guide, not a rule. Every change from v8 is marked "Added," "Split," "Moved," or "proposed" in its row.\n\n'
    '**About the usual-category column.** Each entry\'s definition was read against the definition of rigor decided on 2026-10-06 (docs/decisions/2026-10-06-rigor-defined-by-subject.md) and assigned R, C, or O. Scott Shane confirmed the column as a whole on 2026-10-09, together with the rulings on the entries the definition did not settle (Falsifiability is rigor; Purpose of the research is contribution; Flaws remediable in revision is other). The values are a reading of the definitions, not coded data; no earlier document assigns categories to these entries (the rigor and contribution labels in step1_scholarly_literature.md, step2_journal_forms.md, and step5_skeleton.md sort source criteria, not entries, mostly under the falsity test that the October 6 decision replaced; the six rigor dimensions named in the proposal were replaced by the derived list).\n\n'
)


def adopt(text: str) -> str:
    text = text.replace('# Codebook, version 9 (draft for Scott, 2026-10-07)', '# Codebook, version 9')
    start, end = text.index('**Draft.**'), text.index('The dimension list from')
    text = text[:start] + ADOPTED_NOTES + text[end:]
    text = text.replace(
        '4. "Claim lacks supporting citation" is LIT.POS: it means failing to find and credit prior work. *(Open question for Scott: under a subject definition this may instead be rigor, as an unsupported claim.)*',
        '4. "Claim lacks supporting citation" is CON.SHOWN: an unsupported claim (rigor). Ruled 2026-10-09.')
    lines = []
    for line in text.split('\n'):
        m = ROW.match(line)
        if m and m['code'] in RULINGS:
            line = line[:line.rindex('| ', 0, len(line) - 1)] + f'| {RULINGS[m["code"]]} |'
        lines.append(line)
    text = '\n'.join(lines)
    # the definition paragraph became one paragraph in Word
    text = re.sub(r'(boundary rules Scott set \(.*?\)\.)\n(A critique is .*?manuscript\.)\n(Code each critique)', r'\1 \2 \3', text)
    # typography of the adopted file
    text = text.replace(':-:', ':--').replace('`', '')
    text = re.sub(r'"([^"\n]*)"', '“\\1”', text)
    text = text.replace("'", '’')
    return text


def build() -> str:
    return adopt(draft(V8.read_text(encoding='utf-8-sig')))


if __name__ == '__main__':
    built = build()
    if '--check' in sys.argv[1:]:
        if built != V9.read_text(encoding='utf-8'):
            sys.exit('grader/codebook_v9.md differs from what build_codebook_v9.py builds')
        print('grader/codebook_v9.md matches the build')
    else:
        V9.write_text(built, encoding='utf-8', newline='\n')
        print(f'wrote {V9}')
