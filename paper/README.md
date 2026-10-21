# Proposal and appendix sources

| File | What it is |
|:--|:--|
| `proposal.md` | The proposal, one sentence per line. Submitted to the journal and never published (decision of 2026-10-21). The source of truth; Word is an editing surface. Double-braced placeholders are filled at render time from `design-values.json` (sample size, alpha, power, reliability percentage, the derived detectable effect) and from `sample/confidential/sample-numbers.json` (the sample article's numbers, written by `ref numbers`; not published, because it draws on the referee reports). |
| `appendix-template.md` | The technical appendix's prose and placeholders. |
| `appendix.md` | The technical appendix, assembled from the repository by `ref appendix`: prompts, form, codebook, coding instructions, run records, sample numbers, power arithmetic, and the decisions table are read from their files. Do not edit by hand; edit the template or the source file. Submitted with the proposal and never published, because it reports the sample's referee reports and decision letter (decision of 2026-10-21). |
| `design-values.json` | The study's design numbers, in one place. |
| `render_documents.py` | Renders the proposal to Word under `docs/`, derives the power arithmetic (`paired_mde`), checks the word limit, and records fingerprints in `generated/document-build.json`. It refuses to overwrite a Word file changed since its last render. |
| `generated/` | Numbers and fingerprints written by code. |

`ref appendix` writes `appendix.md` and renders `appendix.docx` beside it; the Word file is not version-controlled.

When a human edits a Word copy, compare it with the markdown, carry the edits into the markdown, and report what was carried. Never regenerate a Word file without first checking it for edits since it was rendered.

The September 21 appendix plan that preceded the appendix is kept in `deprecated/appendix-plan-2026-09-21.md`.
