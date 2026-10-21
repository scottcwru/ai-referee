# Meta-dimensions: decision rules and allocations

Working record of how the pilot's dimensions (`step6_pilot_dimensions.md`, 260 critiques from 44 reports in shuffled batch 01) are combined into meta-dimensions.
Each allocation below was decided by Scott Shane, with Claude proposing combinations one at a time.

**General rule.** Dimensions are combined by the *type of error* the referee asserts, not by the part of the paper the error sits in.

**Counting rule.** A meta-dimension is *proposed* once it has 3 or more sightings; below that it is *pending*. Pending items are kept, not dropped. Collection stops when a batch of 50 reports produces no new dimension and no repeat of any pending item; whatever is still pending then is dropped as idiosyncratic.

**Inclusion rule.** A dimension counts if it appears in referee reports or in at least one journal's review form.

**Structure.** A meta-dimension may hold separate sub-dimensions (for example M10a, M10b) when the critiques share a type of error but differ in a way worth keeping visible.

## M1. Writing

**Rule:** the referee asks for a correction of the writing itself: grammar, formatting, typos, spelling, style, malapropisms, unclear prose ("The butler done it").
**Boundary with M4:** misusing a technical term, such as a statistical term that belongs to a different kind of test, is not a writing error. It goes under the meta-dimension for that kind of error (for statistical terms, M4).

**M1a. Mechanics and clarity**

| Pilot dimension | Critiques |
|:--|--:|
| Typos, grammar, language, formatting, and style errors | 25 |
| Prose unclear | 12 |
| Method or results hard to follow (7 of its 8 critiques; R057-C10 moved to M7) | 7 |
| **Subtotal** | **44** |

**M1b. Organization, length, and placement:** the paper should be rearranged, shortened, or de-duplicated.

| Pilot dimension | Critiques |
|:--|--:|
| Organization, length, and placement of material (13 of its 16; R125-C05 moved to M7, R138-C14 held with "Implications underdeveloped", R315-C01 moved to M2a) | 13 |
| **Subtotal** | **13** |

**M1c. Figures, tables, or examples:** results should be shown more clearly through figures, tables, or examples.

| Pilot dimension | Critiques |
|:--|--:|
| Figures, tables, or examples missing or poorly presented (4 of its 5; R285-C03 moved to M2a) | 4 |
| **Subtotal** | **4** |

**M1d. Title or abstract:** the title or abstract does not accurately convey the study.

| Pilot dimension | Critiques |
|:--|--:|
| Title or abstract does not convey the study | 4 |
| **Subtotal** | **4** |

**M1e. Tone or terminology:** word choice or tone is inappropriate (not the misuse of a technical term).

| Pilot dimension | Critiques |
|:--|--:|
| Tone or terminology inappropriate | 4 |
| **Subtotal** | **4** |

**M1 total: 69**

## M2. Incomplete account of process or findings

**Rule:** the manuscript does not say enough for a reader to understand what the authors did (enough to replicate the test) or what they found (enough to see whether the data support the hypothesis).

**M2a. Process or findings not described**

| Pilot dimension | Critiques |
|:--|--:|
| Procedure, materials, or data source not described | 16 |
| Results not reported in enough detail | 9 |
| Data, code, or materials not available or not usable | 4 |
| R315-C01 (from "Organization, length, and placement"): the shared data page is hard to navigate | 1 |
| R285-C03 (from "Figures, tables, or examples"): the results should include tables for the central models | 1 |
| R095-C10 (from "Method choice not justified"): the reason the data were not validated is not given (too vague to place with certainty) | 1 |
| R294-C06 (from "Internal inconsistency"): the supplementary section the text refers to cannot be found | 1 |
| Ethics approval or consent not reported | 2 |
| **Subtotal** | **35** |

**Note on ethics:** these critiques go here because they say ethics approval and consent were not *reported*. A critique that the research itself was unethical would be a different type of error.

**M2b. Preregistration or deviations not transparent:** the paper does not fully account for what was planned, or for how what was done differs from the plan.

| Pilot dimension | Critiques |
|:--|--:|
| Registration status or deviations from the registered plan not transparent | 6 |
| **Subtotal** | **6** |

**M2 total: 41**

## M3. Prior literature

**Rule:** the referee's comment concerns the manuscript's treatment of prior literature.
**Boundary with M5:** "claim lacks supporting citation" belongs here. Referees write it imprecisely, but it means the authors did not read the literature and find who said this before them, the work they are building on. M5 is for a claim the paper's own evidence does not show.

| Pilot dimension | Critiques |
|:--|--:|
| Prior work or background missing | 9 |
| Citation missing or inaccurate | 7 |
| Findings not compared with prior work in the discussion | 3 |
| **Total** | **19** |

## M4. Statistical testing errors

**Rule:** the referee asserts an error in the statistical testing: the wrong analysis for the data, a model comparison that does not support the conclusion, inadequate power, inappropriate transformation of data, and similar.

| Pilot dimension | Critiques |
|:--|--:|
| Analysis wrong for the data or question | 7 |
| Model comparison doesn't support the chosen model | 6 |
| Sample size or power | 5 |
| Statistic misdescribed or misapplied (5 of its 6 critiques; R294-C01 moved to M5) | 5 |
| Method choice or assumption not justified (4 of its 6; R095-C10 moved to M2a, R315-C05 moved to M11a) | 4 |
| Practical size of the effect not assessed | 1 |
| **Total** | **28** |

## M5. Logic of inference: claim not shown

**Rule:** an error in the logic of science, not in the statistics. The authors assert something, such as that two things differ, that they never actually showed: either they never tested it, or they tested it and the result does not show it. No test is said to be wrong; what is wrong is the act of showing.

**M5a. Claim or conclusion not shown**

| Pilot dimension | Critiques |
|:--|--:|
| Difference claimed without a direct test | 4 |
| R294-C01 (from "Statistic misdescribed or misapplied"): result called consistent with the original study when its confidence interval says it is not | 1 |
| Conclusion goes beyond the evidence (8 of its 10 critiques; R233-C07 held, R272-C04 moved to M8) | 8 |
| **Subtotal** | **13** |

**M5b. Anomalous or conflicting result not addressed:** part of the evidence cuts against the authors' account and is left unexplained.

| Pilot dimension | Critiques |
|:--|--:|
| Anomalous or conflicting result not addressed | 5 |
| **Subtotal** | **5** |

**M5 total: 18**

**Levels of abstraction:** M5 covers the same error at two levels. At the claim level: "you said something about X, but you never showed it." At the conclusion level, about the whole effort: "you concluded XYZ, but you never proved XYZ."

## M6. Falsifiability (pending: 1 sighting)

**Rule:** the manuscript states nothing that could be shown false: no research questions, hypotheses, or testable predictions.

| Critique | Critiques |
|:--|--:|
| R138-C09 (from "Hypotheses absent"): the paper states no research questions or hypotheses | 1 |
| **Total** | **1** |

## M7. Theory weak

**Rule:** the argument that should lead to the test is inadequate: the theory behind the hypotheses or mechanism is too thin or too narrow, or the argument does not lead to the specific prediction being tested. This concerns the link from argument to test, before any data; M5 concerns evidence that fails to show a claim.

| Pilot dimension | Critiques |
|:--|--:|
| Theoretical grounding weak or narrow | 3 |
| R301-C14 (from "Hypotheses absent"): the hypothesis does not say that only the experimental group should change | 1 |
| R057-C10 (from "Method or results hard to follow"): the theory the models rest on is never introduced | 1 |
| R125-C05 (from "Organization, length, and placement"): two theories introduced early and two others only in the discussion | 1 |
| R233-C07 (held from "Conclusion goes beyond the evidence"): unnamed issues undermine the central conclusions; placed here from context, since the sentence sits in the report's paragraph on the weak theoretical basis and unclear framework | 1 |
| **Total** | **7** |

## M8. Sample selection

**Rule:** the referee questions how the sample was chosen, or what sample a test requires. The sample may be participants, cases, countries, studies, or sources, and the complaint may be that the choice is unexplained, unjustified, or biased, or that the sampling logic is misunderstood.
**Boundary with M3:** when a study's data are published literature, as in a review or a study of journal articles, the literature search and the choice of journals are how the sample is drawn, so they go here, not under Prior literature.

| Pilot dimension | Critiques |
|:--|--:|
| Selection of sample, cases, or sources unexplained or biased | 9 |
| R272-C04 (held from "Conclusion goes beyond the evidence"): the call for representative samples misunderstands how a general claim is tested | 1 |
| **Total** | **10** |

## M9. Analysis plan or model not specified (kept separate for now)

**Rule:** the manuscript does not fully specify how the analysis was or will be done: model structure, parameters, non-standard tests, confirmatory versus exploratory analyses, or missing-data handling. Scott kept this separate from M2 for now.

| Pilot dimension | Critiques |
|:--|--:|
| Analysis plan or model not fully specified | 6 |
| **Total** | **6** |

## M10. Alternative explanation not ruled out

**Rule:** a different explanation of the result cannot be ruled out, such as a confound or unobserved differences between units.
**Boundary with M5:** in M5 the evidence does not show the claim; here it shows the claim and a rival alike.
**Boundary with M11:** anything about how the study measures the phenomenon incorrectly, including demand effects, social desirability, and order, practice, or fatigue effects on behavior, is Measurement, not an alternative explanation.

| Sub-dimension | Critiques |
|:--|--:|
| M10a. Alternative explanation or confound not ruled out (4 of the original 9; R095-C08, R095-C09, R095-C12, R104-C06, R294-C03 moved to M11d) | 4 |
| M10b. Causal claim rests on a measured, not manipulated, variable | 3 |
| M10c. Robustness to analytic choices not shown (the rival explanation is the authors' own analytic choices) | 4 |
| **Total** | **11** |

## M11. Measurement

**Rule:** the study measures the phenomenon incorrectly. The measure may capture a different thing, measure too noisily, or be distorted by how participants respond, whether their reports (demand, social desirability) or their behavior (order, practice, fatigue).

| Sub-dimension | Critiques |
|:--|--:|
| M11a. Measure does not capture the named construct (5, plus R315-C05 from "Method choice not justified": the coding criteria are not shown to capture misinterpretation) | 6 |
| M11b. Measure reliability unreported or low | 3 |
| M11c. Participant reactivity: demand or social desirability | 3 |
| M11d. Participant state: order, practice, fatigue, or inattention (R095-C08, R095-C09, R095-C12, R104-C06, R294-C03, from M10a) | 5 |
| **Total** | **17** |

## M12. Implications underdeveloped

**Rule:** the paper does not spell out what its findings mean for practice, policy, or future research.

| Pilot dimension | Critiques |
|:--|--:|
| Implications or recommendations underdeveloped (7 of its 9; R294-C08 and R315-C04 held) | 7 |
| R138-C14 (held from "Organization, length, and placement"): no real discussion; the conclusion repeats earlier material | 1 |
| **Total** | **8** |

## M13. Finding left undeveloped

**Rule:** the authors do not fully interpret what their own results show: an unexpected finding, a promised theme, or the plain reading of the results is left undiscussed.

| Pilot dimension | Critiques |
|:--|--:|
| Finding or promised theme left undeveloped | 3 |
| R294-C08 (held from "Implications underdeveloped"): the discussion should consider openly that the original claims were wrong | 1 |
| **Total** | **4** |

## M14. Extension suggested

**Rule:** the referee suggests something worthwhile the paper could add: a further analysis, an exploration, or a feature that would extend its value.

| Pilot dimension | Critiques |
|:--|--:|
| Worthwhile extension or further analysis not pursued | 3 |
| R315-C04 (held from "Implications underdeveloped"): add a box debunking the misinterpretations, for teaching | 1 |
| **Total** | **4** |

## M15. Purpose of the research unclear

**Rule:** the referee says the purpose of the research is unclear: what the study sets out to do, the gap it fills, its hypotheses, or its key concepts.

| Pilot dimension | Critiques |
|:--|--:|
| Purpose, hypotheses, or key concepts not stated clearly | 6 |
| **Total** | **6** |

## M16. Novelty

**Rule:** the paper has not shown that it adds something new beyond what is already known.

| Pilot dimension | Critiques |
|:--|--:|
| Novelty or advance over prior work not established | 4 |
| **Total** | **4** |

## M17. Importance of the question (pending: 2 sightings in the reports; also a row on the Organization Science form, "Importance of Problem")

**Rule:** the paper does not argue why its question matters or how widely it applies.
**Boundary with M15:** M15 concerns *what* the study sets out to do; M17 concerns *why* it matters.

| Pilot dimension | Critiques |
|:--|--:|
| Importance or scope of the question not argued | 2 |
| **Total** | **2** |

## M18. Selective or misleading presentation of results

**Rule:** the results exist but are presented so they look stronger or more settled than they are, for example by highlighting only significant results or by reporting expected findings as if they were in hand.

| Pilot dimension | Critiques |
|:--|--:|
| Selective or misleading presentation of results | 3 |
| **Total** | **3** |

## M19. Internal inconsistency (pending: 2 sightings)

**Rule:** the paper contradicts itself, for example numbers or results that differ between passages, tables, or the abstract.

| Pilot dimension | Critiques |
|:--|--:|
| Internal inconsistency or broken cross-reference (2 of its 3; R294-C06 moved to M2a) | 2 |
| **Total** | **2** |

## Allocation complete

All 260 pilot critiques are allocated to 19 meta-dimensions: 69 + 41 + 19 + 28 + 18 + 1 + 7 + 10 + 6 + 11 + 17 + 8 + 4 + 4 + 6 + 4 + 2 + 3 + 2 = 260.
Under the counting rule, 16 are proposed (3 or more sightings) and 3 are pending: M6 Falsifiability (1), M17 Importance of the question (2, also a row on the Organization Science form), and M19 Internal inconsistency (2).

**Vague critiques.** A critique that says something is missing without naming it is placed by what the missing thing refers to: measurement or statistics go to those meta-dimensions, a theoretical argument or construct to theory. When the sentence itself does not say, its context in the report decides, and the placement is noted as inferred.

## Decision log

| # | Proposal | Decision | Reason |
|--:|:--|:--|:--|
| 1 | Create M1–M4 from Scott's first combinations | Yes | Scott's rules above; power added to M4 by Scott |
| 2 | "Statistic misdescribed or misapplied" (6) into M4 | Yes | All six are incorrect uses of statistics: a result misread against its confidence interval, a statistic misunderstood, and statistical terms that belong to a different kind of test. Misusing a statistical term is a statistical error, not a writing error; writing errors are grammar, typos, and malapropisms |
| 3 | "Difference claimed without a direct test" (4) into M4 | No; new M5 | Not statistical: no test is said to be wrong. It is an error in the logic of showing that two things differ, either never tested or tested without showing a difference |
| 4 | Move R294-C01 from M4 to M5 | Yes | Same error as M5: a result was tested and then claimed to show what its confidence interval does not |
| 5 | Move "claim lacks supporting citation" from M3 to M5 | No | It means failing to find and credit the prior work the paper builds on, which is a literature error; referees phrase it imprecisely |
| 6 | "Conclusion goes beyond the evidence" (10) into M5 | Yes, 8 of 10 | Same error at a higher level of abstraction: a conclusion about the whole effort that was never proved. Two critiques held: R233-C07 (too vague to place) and R272-C04 (a reasoning error about method, not an unshown claim) |
| 7 | "Hypotheses absent" (2) into M5 | No; split | R138-C09 is non-falsifiability, its own category (new M6). R301-C14 is about the logic of the argument: the argument does not lead to the test |
| 8 | Place R301-C14 with "Theoretical grounding weak or narrow" as new M7, Theory weak | Yes | Both concern the link from argument to test: the argument is too thin to support the hypotheses, or does not produce the prediction tested |
| 9 | R272-C04 into M7 | No | It concerns how a test of a theory is run, not the theory itself |
| 10 | R272-C04 with "Sample selection" as new M8 | Yes | Both concern what sample a test needs. Scott questioned the literature-search item (R225-C05) and the journal-choice item (R315-C16); both kept, because in a scoping review and in a study of journal articles the search and the journals are the sample |
| 11 | "Analysis plan or model not fully specified" (6) into M2 | Not now; kept as its own, M9 | Scott's call: leave separate for now |
| 12 | "Alternative explanation or confound not ruled out" (9) as its own meta-dimension | Yes; new M10 | The evidence fits the claim but also fits a rival; distinct from M5, where the evidence does not show the claim |
| 13 | "Causal claim from a measured variable" (3) into M10 | Yes, as a separate sub-dimension M10b | A causal claim from a measured variable leaves rival explanations open; kept visible as its own sub-dimension |
| 14 | New meta-dimension Measurement from "Measure does not capture the construct" (5) and "Reliability of measures" (3) | Yes; M11 with sub-dimensions M11a, M11b | Both say a measure does not measure what the authors claim: the wrong thing, or too noisily |
| 15 | "Findings not compared with prior work" (3) into M3 | Yes | Each says the discussion does not relate the findings to earlier studies |
| 16 | "Anomalous or conflicting result not addressed" (5) into M5 | Yes, as sub-dimension M5b | Part of the evidence cuts against the authors' account and is left unexplained, so the claim is not fully shown |
| 17 | "Robustness to analytic choices not shown" (4) into M10 | Yes, as sub-dimension M10c | The rival explanation is that the result comes from the authors' analytic choices rather than the world |
| 18 | "Demand effects or social desirability" (3) into M10 | No; into M11 as sub-dimension M11c | Measurement is any way the study measures the phenomenon incorrectly. Alternative explanation is a different concept: a different explanation cannot be ruled out |
| 19 | Order, practice, and fatigue critiques (R095-C08, R095-C12, R104-C06) out of M10a | Moved to M11 as sub-dimension M11d | Scott's rule: behavior changed by fatigue or practice is a measurement problem |
| 20 | Inattention critiques (R095-C09, R294-C03) out of M10a | Moved to M11d, renamed "Participant state: order, practice, fatigue, or inattention" | Both are measurement: participants' attention distorts what is measured |
| 21 | "Data, code, or materials not available" (4) into M2 | Yes | Without them a reader cannot replicate what the authors did |
| 22 | "Preregistration or deviations not transparent" (6) into M2 | Yes, as sub-dimension M2b | The paper does not fully account for what was planned or how it changed |
| 23 | "Method or results hard to follow" (8) into M1 | Yes, 7 of 8 | The material is in the paper but explained unclearly. R057-C10 moved to M7: saying the models' theory is never introduced is a theory critique |
| 24 | "Organization, length, and placement" (16) into M1 | Yes, 13 of 16, as sub-dimension M1b | Each asks for the paper to be rearranged, shortened, or de-duplicated. R125-C05 to M7 (a theory critique), R138-C14 held with "Implications underdeveloped" (no real discussion), R315-C01 to M2a (shared data files, not the paper's writing) |
| 25 | "Implications underdeveloped" as its own meta-dimension, plus R138-C14 | Yes, as M12 | The paper does not spell out what its findings mean. R294-C08 (how to read the results) and R315-C04 (a suggested addition) are about something else; held, home not yet decided |
| 26 | R294-C08 with "Finding or promised theme left undeveloped" | Yes; the group recorded as M13 | In all four, the authors do not fully interpret what their own results show |
| 27 | R315-C04 with "Worthwhile extension or further analysis not pursued" | Yes; the group recorded as M14 | In each, the referee suggests something worthwhile the paper could add |
| 28 | "Figures, tables, or examples" (5) into M1 | Yes, 4 of 5, as sub-dimension M1c | Each asks for results to be shown more clearly. R285-C03 (tables for the central models) moved to M2a, since those results are not reported |
| 29 | "Title or abstract does not convey the study" (4) into M1 | Yes, as sub-dimension M1d | Each says the title or abstract does not accurately convey the study |
| 30 | "Tone or terminology inappropriate" (4) into M1 | Yes, as sub-dimension M1e | Each objects to word choice or tone, not to the misuse of a technical term |
| 31 | "Purpose, hypotheses, or key concepts not stated clearly" (6) into M1 | No; its own meta-dimension, M15 | It is about the purpose of the research, not the writing |
| 32 | "Method choice or assumption not justified" (6) into M4 | Yes, 4 of 6 | An analytic choice made without justification is a statistical error; pooling studies across decades (R225-C03) stays here. R315-C05 (coding criteria) moved to M11a. R095-C10 (data not validated) moved to M2a; it is too vague to place with certainty |
| 33 | "Novelty" (4) as its own meta-dimension | Yes, M16 | Kept whole, including the two critiques phrased as literature problems |
| 34 | "Importance or scope of the question not argued" (2) as its own meta-dimension | Yes, M17, named "Importance of the question"; kept separate from M15 | Purpose is what the study sets out to do; importance is why it matters |
| 35 | "Selective or misleading presentation of results" (3) as its own meta-dimension | Yes, M18 | The results exist but are presented as stronger or more settled than they are |
| 36 | "Internal inconsistency" as its own meta-dimension | Yes, M19, 2 of 3 | The paper contradicts itself. R294-C06 (missing supplementary section) moved to M2a: missing material, not a contradiction |
| 37 | "Ethics approval or consent not reported" (2) as its own meta-dimension | No; into M2a | Both say ethics approval and consent were not reported, so they are missing information |
| 38 | "Practical size of the effect not assessed" (1) into M4 | Yes | The effect is shown to be statistically present but not shown to be large enough to matter |
| 39 | Drop R233-C07 as too vague to code | No; into M7 | It says the conclusion cannot be drawn because something is missing; the missing thing is placed by what it refers to, and here the report's context shows it is the theoretical argument |
