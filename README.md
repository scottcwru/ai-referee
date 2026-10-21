# AI Referee

An AI referee for journal manuscripts, and the materials for a study of whether AI and human referees are complements.

Scott Shane and David Clingingsmith, Case Western Reserve University.

This repository accompanies our Stage 1 submission to *Organization Science* for the special issue "AI-Assisted Frontiers in Organizational Science." The submission version is labeled `stage-1-submission`. The proposal and the technical appendix are separate submission documents and are not posted here; the appendix reports the sample article's referee reports and decision letter in coded form (see Confidentiality). `paper/` holds the appendix template, the design values, and the code that assembles and renders both documents; the appendix maps each of its sections to the file it reproduces.

## What the referee does

Two independent AI reviewers, Claude and ChatGPT, each read a manuscript and complete the journal's review form: a rating on each of the form's eight rows, a recommendation, and comments in which every critique names its location in the manuscript. The prompt contains only the journal's name, its public statements about what it publishes, the form, and the output format. Four mechanical checks run on every review: every form field is completed, every critique names a location, every low rating has a critique bearing on it, and text matching flags possible fabrication in the critiques' quotations, numbers, and citations. Text matching cannot establish that a review contains no fabricated material; declared external references require human verification.

A grader from a third model family, Gemini, splits each review into critiques and codes every critique with the codebook, as rigor, contribution, or other. The study compares the rigor share of the AI reviews with that of the human referee reports on the same manuscripts.

## What is here

| Folder | Contents |
|:--|:--|
| `reviewer/` | The reviewer prompt, the review form as a template, and the journal's public statements with their sources |
| `grader/` | The codebook, the coding instructions, the grader's prompts, and the record of how the codebook's dimensions were derived from published scholarship, public journal forms, and published referee reports |
| `sample/` | A demonstration on one of our own papers: the manuscript (posted with its co-authors' consent), both AI reviews, their coded critiques, and the numbers they produce. Counts and processing metadata also cover the private referee reports and decision letter; their text and substantive coded results are withheld. |
| `src/referee/` | The code: running the reviewers, the checks, the grader, the numbers, and the appendix. Model names, versions, settings, and prices are set in `config.py` and nowhere else. |
| `paper/` | The technical appendix's template, the design values, and the code that renders the proposal and appendix (both submitted, not posted) |
| `analysis/` | The analysis code and preregistration, to be added as the study proceeds |
| `docs/decisions/` | The study's design decisions, one dated file each |
| `docs/rules-agreement-test.md` | The planned test of agreement between human coders on the coding rules |
| `docs/ai-use.md` | How we used AI assistants in building the repository: the tools and models, what they did, and what we checked and decided |

## Running the referee

The referee needs Python 3.11 or later, [uv](https://docs.astral.sh/uv/), and API keys for Anthropic, OpenAI, and Google. Put the keys in `~/.config/referee/keys.env`, one per line:

```
ANTHROPIC_API_KEY=...
OPENAI_API_KEY=...
GOOGLE_API_KEY=...
```

Then, from the repository folder:

```
uv run ref review path/to/manuscript.pdf      # both reviewers; writes a run record under sample/runs/
uv run ref check sample/runs/<run-id> path/to/manuscript.pdf
uv run ref grade sample/runs/<run-id>         # codes the AI reviews; add --human-dir for human reports
uv run ref prompt                             # prints the reviewer prompt
```

Each run writes a manifest with the model requested and the version served, the settings, the prompt and manuscript fingerprints, tokens, fees, and time. `ref grade` writes the sample's numbers only for runs on the sample manuscript.

`ref check` reports its findings and records them with the run. Its exit status is zero when reporting completes, including when checks flag items; inspect the report and document human follow-up in `disposition.md`. Both recorded sample reviews have text-matching flags whose human explanations are in that file.

## Reproducing the sample results

The saved AI results can be recomputed from this repository alone: the posted manuscript (`sample/manuscript/`), the reviewer prompt as sent, both AI reviews and their mechanical checks, and the grader's codes for the AI reviews, each run with a manifest of models, versions, settings, fingerprints, tokens, and fees. From those records, `uv run ref numbers sample/grader/2026-10-17T122945Z` rebuilds `sample/prototype-numbers.md`, and `python grader/build_codebook_v9.py --check` confirms that the current codebook is what its build script makes from version 8.

The recorded grader prompt (`sample/grader/2026-10-17T122945Z/grader-prompt-as-sent.md`) preserves the exact codebook and instructions used in that run. Subsequent editorial cleanup changed their introductory and draft-status wording, so their current fingerprints differ from the recorded ones; the coding definitions and rules are unchanged. The historical prompt and manifest fingerprints are preserved.

New reviews of the posted sample PDF are also recognized as sample runs. Both the original and posted manuscript fingerprints are recorded in `sample/manuscript/fingerprints.json`; generating numbers still verifies the integrity of the posted PDF. Fresh model calls may produce different reviews or codes from the saved demonstration.

Run the local regression checks, which need no API keys or model calls, with `uv run python -m unittest discover -s tests`.

The comparison with the human referees needs the sample article's referee reports and decision letter. They are private communications between *Organization Science*, the authors, and the referees, so their text is a restricted input held outside this repository. With them saved as plain text in a folder outside the repository (`reviewer1.txt`, `reviewer2.txt`, and so on, and `decision-letter.txt`), `uv run ref grade sample/runs/2026-10-17T110416Z --human-dir <folder>` codes them alongside the AI reviews and writes the full numbers. The technical appendix submitted with the proposal reports the full numbers and lists every coded critique row by row, so the comparison can also be checked from the codes without the reports.

## Confidentiality

No journal manuscript, referee report, or decision letter is in this repository, other than our own consented sample manuscript. We withhold the substance of the sample's referee reports and decision letter: their text, quotations, paraphrases, summaries, critique-level codes and locations, and distributions or comparisons revealing what they criticized. Their coded critiques, the editor's decision, and the comparison of the AI reviews with them are in the technical appendix submitted with the proposal.

Counts of reports and critiques, including counts per report or letter, and processing metadata such as tokens, calls, failures, retries, costs, and time may be published. Combined totals may include the private correspondence; these describe its amount and processing without disclosing its substance (see `docs/decisions/2026-10-21-correspondence-publication-scope.md`). `ref numbers` rebuilds the public AI results from this repository; the full comparison and `ref appendix` require restricted inputs. In the study, the journal's manuscripts and reviews are processed outside the repository, and only coded data, with no text, are added under the data agreement.

## License

The code and documentation are released under the MIT license (`LICENSE`). The license does not cover third-party material, such as the journal's public statements in `reviewer/journal-sources/` or the published referee reports listed in `grader/`; their sources are recorded beside them.
