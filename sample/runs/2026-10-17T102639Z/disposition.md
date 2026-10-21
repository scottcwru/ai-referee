# Disposition of this run

Run 2026-10-17T102639Z. Both reviewers were called with the same prompt on the same manuscript (see `manifest.json`).

## What ran

- **claude** (requested `claude-opus-5-5`, served `claude-opus-5-5`): completed in 209.8 seconds for $0.75. Output parsed; 17 critiques.
- **chatgpt** (requested `gpt-5.5-2026-04-23`): failed before any output. The OpenAI account had no credits (HTTP 429, `insufficient_quota`). No retry was possible until credits are added. The attempt is recorded in the manifest.

## Mechanical checks on the claude review

Checks 1 to 3 pass. Check 4 (nothing fabricated, by text matching) was run twice:

1. **First pass** failed on five quotes and two numbers. The five quotes were all present in the manuscript; the PDF text layer inserts spaces before punctuation and after brackets ("clarifying , rather", "( i.e., high)", "deal -factor", "bet ween"), which defeated exact matching. `src/referee/checks.py` now removes those spaces before comparing. This changed the check, not the review.
2. **Second pass** (`checks-claude.md`) is the record. One quote still fails: critique 16, where the PDF text layer breaks the word "between" into "bet ween"; the sentence is on p. 25 of the manuscript as quoted. The two number flags remain and are correct as flags: the reviewer's text contains numbers that the manuscript does not. Both are the reviewer's own arithmetic, confirmed by hand:
   - critique 5: "−0.27/0.06 = −4.5" (Table 10 reports β = −0.27, SE = 0.06, t = −4.21);
   - critique 6: "1,056 − 45 = 1,011, not 1,008" (the manuscript reports 1,056 potential, 45 lost, 1,008 completed).
   The check cannot tell a quoted number from a computed one, so these stay recorded as failures for a person to confirm, which has been done.
3. **External references.** Critique 15 cites Leland and Pyle (1977) and Ahlers et al. (2015), neither in the manuscript's reference list. The reviewer declared both as external, as the prompt requires. Both are real, well-known publications in the finance and crowdfunding literatures; whether they say what the critique attributes to them has not been verified.

No critique was removed or edited.

## Known limits of this run

- The prompt's journal statements are partial: four verified sentences of the editorial statement, no aims and scope, no author guidelines (see `reviewer/journal-sources/README.md`). A run with the completed statements will carry a different prompt fingerprint.
- The form's recommendation options and free-text field names are provisional ScholarOne wording.
- The ChatGPT arm is missing; the paired demonstration is incomplete until it runs.
