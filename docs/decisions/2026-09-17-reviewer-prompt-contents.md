# What the reviewer prompt contains

**Decided:** 2026-09-17 (Scott's v4 plan, Stage 1).

The reviewer prompt contains only: the journal's name; the journal's public statements of what it wants (aims and scope, author guidelines, reviewer guidelines if published); the review form; the output format; and the rule that every critique names its location in the manuscript. The same prompt is used for both models.

Excluded: human referee reports as examples; any mention of rigor, contribution, or a preferred emphasis; calibration to the journal's score or decision distributions; fine-tuning or post-training.

**Why:** the hypothesis concerns what the models do unprompted, so any tuning would make the experiment measure the tuning; human examples would make the AI imitate what it is compared against; a fine-tuned proprietary model cannot be shared, and the call requires infrastructure others can run.

**Note:** David's idea of giving the AI standard references on rigor (`parking-lot.md`, item 2) is proposed for the codebook only, which leaves this decision intact.
