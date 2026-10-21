# Technical Appendix

Rigor and Contribution: A Test of Whether an AI Referee Complements Human Referees

Scott Shane and David Clingingsmith
Case Western Reserve University

This appendix is assembled by code from the repository {{repository_name}} ({{repository_url}}, tag {{repository_tag}}) (command `ref appendix`); every prompt, table, and number below is read from the file named beside it, and nothing is typed in by hand. Built {{built_date}} from reviewer run {{reviewer_run}} and grader run {{grader_run}}.

## Map of this appendix to the repository

| Section of this appendix | Repository file |
|:--|:--|
| A1. The reviewer prompt | `reviewer/prompt.md`, filled from `reviewer/form/template.json` and `reviewer/journal-sources/` |
| A2. The Organization Science review form | `reviewer/form/template.json` |
| A3. Model families, versions, settings, cost, and time for the sample run | `src/referee/config.py`; `sample/runs/{{reviewer_run}}/manifest.json`; `sample/grader/{{grader_run}}/manifest.json` |
| A4. The codebook | `grader/codebook_v9.md`; derivation record in `grader/step1_…` to `grader/step12_…` |
| A5. The grader prompt | `grader/prompt-segment.md`, `grader/prompt.md` |
| A6. The human coder instructions and the validation plan | `grader/coding-instructions.md`; `docs/rules-agreement-test.md`; `docs/decisions/2026-10-09-rules-test-deferred.md` |
| A7. The sample results | `sample/manuscript/manuscript.pdf`; `sample/confidential/prototype-numbers.md` (not published; the public `sample/prototype-numbers.md` covers the AI reviews only); `sample/runs/{{reviewer_run}}/`; `sample/grader/{{grader_run}}/coded-critiques.csv` |
| A8. The power arithmetic | `paper/render_documents.py` (function `paired_mde`); `paper/design-values.json` |
| A9. The three measures | this appendix; analysis code to be added under `analysis/` |
| A10. The preregistration | to be added under `analysis/` with its registry link |
| Settled design decisions | `docs/decisions/`, one dated file each |
| Run records | `sample/runs/<run-id>/manifest.json`, `sample/grader/<run-id>/manifest.json` |

The sample manuscript is in the repository with its co-authors' consent (`sample/manuscript/`). Its referee reports and decision letter are private communications between Organization Science, the authors, and the referees. Their coded critiques appear in this appendix only, with no text (A7). The public repository holds the AI reviews' coded critiques and numbers and may also report counts and processing metadata from the private correspondence. Its substantive content, critique-level codes and locations, and distributions or comparisons revealing what was criticized remain withheld (`docs/decisions/2026-10-21-correspondence-publication-scope.md`).

## A1. The reviewer prompt

The prompt below is identical for both AI reviewers. It contains only the journal's name, the journal's public statements, the review form, the output format, and the rule that every critique names its location in the manuscript (decision of 2026-09-17). It contains no human referee reports as examples, no mention of rigor or contribution, and no calibration to the journal's decisions; neither model is fine-tuned. The journal statements were copied by hand from the journal's pages on 2026-10-17 because the journal's website refuses automated readers. The text is reproduced exactly as assembled; its SHA-256 is {{prompt_sha256}}, which matches the prompt recorded in the sample run.

**Placeholder sections marked.** The recommendation options and the names of the two free-text fields use generic ScholarOne wording and are provisional until the journal's blank reviewer page is transcribed (Scott's v4 plan, Stage 1). The eight scored rows and the five rating levels are as received.

```
{{reviewer_prompt}}
```

## A2. The Organization Science review form

Source: {{form_source_note}}

| Row | Ratings |
|:--|:--|
{{form_rows_table}}

Recommendation (provisional wording): {{recommendation_options}}.

Free-text fields (provisional wording): {{free_text_fields}}.

The form is encoded once, in `reviewer/form/template.json`; the reviewer prompt, the grader prompt, the mechanical checks, and the tables in this appendix read the rows and levels from that file.

## A3. Model families, versions, settings, cost, and time for the sample run

Every run writes a manifest recording the model requested, the model string the API served, the settings, the prompt and manuscript fingerprints, tokens, fees, elapsed time, failures, and retries. Model names, settings, and prices live only in `src/referee/config.py`.

### The two reviewers (run {{reviewer_run}})

| | Claude | ChatGPT |
|:--|:--|:--|
{{reviewer_table}}

Prices are the vendors' published per-token rates on 2026-10-17; {{price_source_note}}

### The grader (run {{grader_run}})

| | Grader |
|:--|:--|
{{grader_table}}

{{grader_model_note}}

### Mechanical checks on the AI reviews

Four checks run on every completed review (Scott's v4 plan, Stage 2): every form field is completed; every critique names a location; every Poor or Marginal score has at least one critique bearing on that row; nothing is fabricated, tested by matching every quoted passage and number in the critiques to the manuscript text and every citation to the manuscript's reference list, with citations the reviewer declares as external listed for a person to verify. Results and their disposition are in `sample/runs/{{reviewer_run}}/checks-*.md` and `disposition.md`.

{{checks_summary}}

## A4. The codebook

Each critique is coded to one entry of the dimension list and, separately, as rigor, contribution, or other, with a checkability attribute (checkable error, omission, or judgment). Rigor is defined by subject: a critique is rigor if it concerns whether the manuscript's claims are supported by its evidence, design, analysis, or reasoning; contribution if it concerns the value of the work to the field; other if it concerns writing and presentation (decisions of 2026-10-06). This supersedes the earlier falsity test. The dimensions were derived from three sources, the review forms of 17 journals, 24 scholarly works on rigor and contribution, and 1,852 critiques in 299 published referee reports coded in seven shuffled batches to saturation (decision of 2026-09-25); the derivation record is in `grader/step1_scholarly_literature.md` through `grader/step12_phase1_list.md`. Each entry carries its usual category as a guide; the coder decides the category for each critique. The form row each critique bears on is recorded by the grader. A stakes attribute (central result, local, cosmetic) named in the proposal is not yet in the codebook and will be added before preregistration.

The codebook is reproduced from `grader/codebook_v9.md` (SHA-256 {{codebook_sha256}}).

{{codebook}}

## A5. The grader prompt

The grader runs on a model family that neither reviewer uses (decision of 2026-09-17). It works in two steps. First it splits a report into critiques, verbatim and in order (`grader/prompt-segment.md`). Then it codes each critique alone, shown with one sentence of context on either side and told nothing about who wrote the report (`grader/prompt.md`). The placeholders in the second prompt are filled at run time from the coding instructions (A6), the codebook (A4), and the form (A2); the filled prompt as sent is saved with every grader run.

### Step 1: segmentation

```
{{grader_prompt_segment}}
```

### Step 2: coding one critique

```
{{grader_prompt}}
```

## A6. The human coder instructions and the validation plan

### Coder instructions

Human coders and the grader follow the same instructions, reproduced from `grader/coding-instructions.md` (SHA-256 {{instructions_sha256}}). The examples are paraphrases of critiques from public referee reports, with identifiers.

{{coding_instructions}}

### Validation: planned, not yet run

No agreement statistics exist yet. Two tests are planned, in this order.

1. **The rules-agreement test** (decision of 2026-10-09, superseding the test of 60 critiques decided on 2026-10-06). It runs after the proposal is selected, before preregistration. Two independent AI coders from model families other than the grader's code 150 critiques drawn with a recorded seed in three strata of 50, from quantitative empirical, qualitative empirical, and conceptual or essay work. Category and checkability are each tested separately against a threshold of Cohen's kappa 0.70, reported with 95 percent confidence intervals; dimension agreement is reported at the code and family levels without a threshold. If the threshold is missed, the rules are revised using the disagreements and tested again on a fresh draw. A random 10 disagreements per round are adjudicated by both authors, blind to which coder said what. The procedure is in `docs/rules-agreement-test.md`.
2. **Validation of the grader** (decision of 2026-09-17). Before the grader codes any journal review, two human coders, blind to whether an AI or a human wrote each critique, code the same critiques; kappa is computed between the grader and each coder and between the coders; the codebook is revised and the cycle repeated until kappa reaches the preregistered threshold. In the study, human coders and a second AI grader also code a random {{reliability_percent}} percent of critiques.

## A7. The sample results

One article was reviewed and graded: a manuscript submitted to Organization Science, {{editorial_history}}, used in the anonymized version the referees saw. The manuscript's co-authors have consented to its public posting (Scott's v4 plan, Part 1), and the anonymized PDF is in the repository at `sample/manuscript/manuscript.pdf` ({{manuscript_pages}} pages). The reviewers read it with the journal's manuscript ID on the cover page (SHA-256 {{manuscript_sha256}}, the fingerprint recorded in the run manifest); the posted copy has that ID blanked and nothing else changed (SHA-256 {{posted_manuscript_sha256}}; both fingerprints are in `sample/manuscript/fingerprints.json`). The {{human_review_count}} referee reports and the decision letter remain private: their coded critiques, with no text, are reported in this appendix and are not in the public repository. Both AI reviewers passed the first three mechanical checks; the fabrication check flagged one item in each review, both verified by hand as genuine (the reviewer's own arithmetic in one case and a quotation split across a page break in the other).

The tables below are written by code (`ref numbers`) from the run records; the public repository's `sample/prototype-numbers.md` is the same file without the referee reports and decision letter. They demonstrate that the pipeline runs and is inspectable; they are not a result of the study, and the grader that produced the codes is not yet validated.

{{prototype_numbers}}

### The coded critiques

Every critique the grader coded in the sample run, {{coded_rows_count}} rows, read from `sample/grader/{{grader_run}}/coded-critiques.csv`. Each row gives the review it came from, the critique's position in that review, and its codes; no review text is reproduced. Every number in the tables above can be recomputed from these rows. The public repository's copy of the file holds the AI reviews' rows only; the referee reports and decision letter are restricted inputs that Organization Science holds, and with them `ref grade --human-dir` reproduces these rows and the full numbers (the public README, "Reproducing the sample results").

{{coded_rows_table}}

### AI-found errors confirmed real

The secondary outcome requires a human coder to confirm each rigor error the AI referee found as real or not, and to record whether any human review mentions it. This step has not yet been run on the sample article. In the sample run, {{ai_checkable_errors}} of the {{ai_rigor_critiques}} AI rigor critiques were coded checkable error by the grader; these are the candidates for confirmation.

## A8. The power arithmetic

The primary test is a paired t-test on the manuscript-level difference between the mean rigor share of the AI reviews and the mean rigor share of the human reviews.

| Input | Value | Source |
|:--|:--|:--|
| Manuscript pairs | {{sample_size}} | `paper/design-values.json` |
| Two-sided alpha | {{alpha}} | `paper/design-values.json` |
| Power | {{power}} | `paper/design-values.json` |
| Minimum detectable standardized paired difference | {{minimum_detectable_effect}} (precisely {{minimum_detectable_effect_precise}}) | computed |
| Critical t ({{df}} degrees of freedom) | {{t_critical}} | computed |

Method: exact power of the paired t-test under the noncentral t distribution, computed by numerical integration in `paper/render_documents.py` (function `paired_mde`): the test statistic is T = (Z + δ√n) / √(V/df) with Z standard normal and V chi-square on df = n − 1; the rejection probability is integrated over √(V/df) by Simpson's rule on 6,000 intervals, cross-checked at 3,000; the critical value is solved so that the rejection probability under δ = 0 equals alpha, then δ is solved so that the rejection probability equals the target power. The standardized difference is the mean paired difference divided by the standard deviation of the paired differences.

## A9. The three measures

| Measure | Unit | Coder instruction | Test |
|:--|:--|:--|:--|
| 1. Rigor share (primary outcome) | One review; averaged within reviewer type per manuscript (decisions of 2026-09-16 and 2026-09-17) | Code each critique as rigor, contribution, or other by subject (A4, A6); rigor share is rigor divided by rigor plus contribution; other is excluded | Paired t-test on the manuscript-level difference between the AI mean and the human mean; {{sample_size}} pairs, two-sided alpha {{alpha}}, power {{power}} for a standardized difference of {{minimum_detectable_effect}} (A8) |
| 2. Missed errors (secondary outcome) | One manuscript | For each AI rigor critique, a human coder confirms the error as real or not; for each confirmed error, the grader records whether any human review or the decision letter mentions it; the same in reverse for rigor errors the human referees found that neither AI review mentions | Counts per manuscript, reported with confidence intervals; confirmed AI-found errors absent from every human review are the cost of reviewing without the AI referee, and human-found errors absent from both AI reviews the cost of reviewing without them. Mentions in the decision letter are reported descriptively |
| 3. Agreement (reliability) | One critique | Human coders and a second AI grader code a random {{reliability_percent}} percent of critiques, each critique shown without its surrounding review | Cohen's kappa between the primary grader and each coder and between coders, with 95 percent confidence intervals, against the preregistered threshold |

Descriptive results by dimension and by form row are reported with confidence intervals. Checkability (checkable error, omission, judgment) is reported as an attribute of each rigor critique (decision of 2026-10-06); the secondary outcome is measure 2, missed errors. The reviewer prompt is fixed and preregistered, so the AI cannot be tuned toward either kind of critique.

## A10. The preregistration

The hypothesis, the codebook, the coding instructions, and the analysis plan will be registered before the grader codes any journal review, after the rules-agreement test (A6). The registered document and its registry link will be added under `analysis/` and reproduced here.

## Settled design decisions

{{decisions_table}}
