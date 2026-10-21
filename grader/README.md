# grader/

Everything that codes a review (Scott's v4 plan, Stages 3 and 4).

| File | What it is |
|:--|:--|
| `codebook_v9.md` | The dimensions and subdimensions, each with a code, a definition, and its usual category; the boundary rules. One source: the grader reads it at run time and validates every code it returns against it. |
| `coding-instructions.md` | How a coder records dimension, category (rigor, contribution, other), and checkability; the four rulings with balanced examples; Scott's rulings of October 9 on the open questions. |
| `prompt-segment.md` | The grader's first step: split a report into critiques, verbatim, in order. |
| `prompt.md` | The grader's second step: code one critique, shown with one sentence of context on either side and nothing else. Placeholders are filled from the two files above and the form template at run time. |
| `step1_...` to `step12_...`, `codebook_v8.md` | The derivation record for the dimensions (decision of 2026-09-25). |
| `build_codebook_v9.py` | Builds `codebook_v9.md` from `codebook_v8.md`: the October 7 draft, then adoption with Scott's rulings of October 9. `--check` confirms the committed codebook is what it builds. |

The grader runs on a model family that neither reviewer uses (decision of 2026-09-17). The model, settings, and prices live in `src/referee/config.py`; the code is in `src/referee/segment.py` and `src/referee/grade.py` (command: `ref grade`). Coded output holds codes, locations, and counts, never the text of a human review.

The grader is not yet validated against human coders; the agreement test runs after selection (decision of 2026-10-09).

The recorded prompt in `sample/grader/2026-10-17T122945Z/grader-prompt-as-sent.md` preserves the exact codebook and instructions used in the demonstration. Later editorial cleanup changed their introductory and draft-status wording, but left the coding definitions and rules unchanged. Their current fingerprints therefore differ from the recorded ones. `build_codebook_v9.py --check` verifies the current file; the historical prompt and manifest fingerprints remain unchanged.
