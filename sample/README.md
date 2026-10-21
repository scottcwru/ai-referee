# sample/

The public demonstration (Scott's v4 plan, Stage 2): the AI reviews of one article, with the run record and the mechanical checks.

`runs/<run-id>/` holds one recorded run of `ref review`:

| File | What it is |
|:--|:--|
| `manifest.json` | Models requested and served, settings, prompt and form fingerprints, manuscript fingerprint, tokens, fees, elapsed time, failures and retries |
| `prompt-as-sent.md` | The assembled reviewer prompt exactly as sent to both models |
| `review-<reviewer>.raw.txt` | The model's output, untouched |
| `review-<reviewer>.json` | The same output parsed |
| `review-<reviewer>.md` | The completed review form, rendered for reading |
| `checks-<reviewer>.md`, `.json` | The four mechanical checks: form complete, every critique located, every Poor or Marginal score explained, possible fabrication flagged by text matching for human follow-up |
| `disposition.md` | What ran, what failed, and what was done about each check failure |

`grader/<run-id>/` holds one recorded run of `ref grade` on a reviewer run's AI reviews plus the human referee reports and the editor's letter. The referee reports and the letter are private communications between Organization Science, the authors, and the referees, so the public repository's copies of `coded-critiques.csv` and `manifest.json` hold the AI reviews' entries only; the rest are reported in the technical appendix submitted with the proposal (decision of 2026-10-21):

| File | What it is |
|:--|:--|
| `manifest.json` | Grader model and version served, settings, prices, prompt and codebook fingerprints, every call's tokens and time, failures and retries |
| `grader-prompt-as-sent.md` | The coding prompt with the codebook and instructions filled in, as sent for every critique |
| `coded-critiques.csv` | One row per critique: review, arm, dimension, category, checkability, form row, location, word count. No review text |
| `ai-critique-segments.json` | How the grader split the two AI reviews into critiques (their text is already public in `runs/`) |

`prototype-numbers.md` is written by `ref numbers` from the recorded runs: the AI reviews' critiques, rigor and contribution shares, checkability, cost and time, and form scores and recommendations. `ref numbers` also writes the full version, with the referee reports, the editor's letter, and the decision, to `confidential/`, along with the facts about the article's editorial history it needs (`sample-article.json`) and the values the proposal uses (`sample-numbers.json`). `confidential/` is never published; its contents appear in the technical appendix.

Report and critique counts, including counts per report or letter, and processing metadata may be published. The grader manifests and run narratives retain combined processing totals that include the private correspondence. Its text, substantive summaries, critique-level codes and locations, and distributions or comparisons revealing what was criticized remain withheld (`docs/decisions/2026-10-21-correspondence-publication-scope.md`).

`manuscript/manuscript.pdf` is the anonymized sample manuscript, posted with its co-authors' consent (Scott's v4 plan, Part 1); its journal manuscript ID is blanked on the cover page, so its SHA-256 differs from the fingerprint in the run manifests only by that change (both are in `manuscript/fingerprints.json`). The referee reports and the decision letter remain private and live in `sample-private/`, which git ignores; their coded critiques are kept in the working repository and reported in the technical appendix, not published. They are restricted inputs: the AI side reproduces from the public repository alone, and the comparison with the human referees reproduces for anyone who holds the reports (see "Reproducing the sample results" in the public README). Without them, `ref numbers` writes only the public numbers and says so.

To reproduce a run:

```
uv run ref review sample/manuscript/manuscript.pdf
```

with a `keys.env` file at one of the locations named in `src/referee/config.py`. The original and posted sample fingerprints are both recognized; the posted PDF's integrity is checked when generating numbers. New model outputs may differ from the saved run. `ref check` records flags for human follow-up and returns zero when reporting completes, even if a check flags an item.
