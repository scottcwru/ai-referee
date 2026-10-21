# Testing the coding rules before preregistration

Proposal for Scott’s approval

October 7, 2026

**Status:** proposal. Fills in the specifics of the decision of October 6 (docs/decisions/2026-10-06-rules-agreement-test.md): two independent AI coders, blind to the study, code 60 fresh critiques under the revised rules; kappa 0.70 before preregistration; a small sample of disagreements adjudicated. **What it tests:** whether the written rules (coding-instructions.md, codebook_v9.md) can be applied consistently. It comes before, and does not replace, the validation of the grader against two blind human coders (decision of 2026-09-17).

## Proposed specifics

1. **What must reach kappa 0.70.** Category (rigor, contribution, other) and checkability (checkable error, omission, judgment), each separately, because each defines an outcome. Dimension agreement is reported at the code and family levels without a threshold; the grader validation addresses it. Each kappa is reported with a 95 percent confidence interval, which at n = 150 is roughly plus or minus 0.09.
2. **Coders.** Two models from different families, neither from the grader’s family, so that the grader’s later validation stays independent. Each gets the instructions, the codebook, and the critique in a fixed window (the critique bracketed, one sentence of context either side), and nothing about the study or its hypothesis. Options in the codebook are presented in a shuffled order for each critique.
3. **Sample.** 150 critiques drawn with a recorded seed, in three strata of 50, so the test covers the cases that split coders on October 5:
    - quantitative empirical work: the phase 1 corpus (grader/step10_coded_critiques.csv);
    - qualitative empirical work: the BMJ Open pilot (docs/pilot-bmjopen-qual-2026-10-04-codes.csv);
    - conceptual and essay work: the PCI Organization Studies pilot (docs/pilot-pci-orgstudies-2026-10-04-codes.csv; 70 critiques remain after exclusions).
- Excluded: the 60 critiques of the October 5 session and the 22 examples in the instructions (example-ids.csv). Report text is fetched into a scratch folder and never committed, as in the pilots; the sample file records identifiers only.
4. **If the threshold is missed.** Revise the rules using the disagreements, then test again on a fresh 60 drawn the same way, never on critiques already seen. Each round is reported in the appendix, whatever its result.
5. **Adjudication.** David and Scott each adjudicate the same random 10 disagreements per round, without seeing which coder said what. Their agreement with each other gives a first human check on the rules ahead of the grader validation.

## What the repository gains

- A script that draws the sample (seeded, stratified, with exclusions) and one that computes the kappas and intervals from the two coders’ codes.
- The threshold (0.70) in paper/design-values.json, where the rendering script reads it, rather than typed into the proposal or appendix.
- The coders’ codes, one row per critique, no report text.
