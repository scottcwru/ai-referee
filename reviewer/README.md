# reviewer/

Everything that produces an AI review (Scott's v4 plan, Stage 1).

| File | What it is |
|:--|:--|
| `prompt.md` | The reviewer prompt, identical for both models. Placeholders in double braces are filled from `form/template.json` and `journal-sources/` at run time, so the eight rows and five levels live in one place. The assembled prompt is saved with every run. |
| `form/template.json` | The Organization Science review form as a machine-readable template: eight scored rows, five rating levels, recommendation options, two free-text fields. Provisional parts are marked. |
| `journal-sources/` | The journal's public statements the prompt quotes, each with URL and retrieval date. |

The run script is `src/referee/review.py` (command: `ref review`). Model names, versions, settings, and prices live only in `src/referee/config.py`.

What the prompt does not contain, by decision of 2026-09-17: human referee reports as examples; any mention of rigor, contribution, or a preferred emphasis; calibration to the journal's score or decision distributions. The models are not fine-tuned.
