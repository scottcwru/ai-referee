# Pilot: dimensions from shuffled batch 01 (exploratory)

This is an exploratory pilot of Steps 6 to 8 of the derivation protocol, not the formal saturation record.
It covers 44 of shuffled batch 01's 50 reports: four OpenReview reports could not be retrieved because the site blocked them with a bot check, and two PCI Registered Reports reviews consist only of an attachment that is not in the corpus.
The critiques were extracted and labeled by Claude (Anthropic), pending the authors' choice of labeling model, and each was labeled and assigned to a side without sight of the skeleton.
The grouping below was also done by Claude, from the critiques' text and glosses, before the skeleton in `step5_skeleton.md` was read; the skeleton was then used only for the placements.
The formal run will rerun batch 01 under the final procedure, so none of the counts here should be cited as results.
The critique-level assignment file (one row per critique, with its dimension) is a working file of the pilot and is not reproduced here.

## Summary

- **Counts.** Batch 01's 44 reports yield 260 critiques. Ten reports contain none (they summarize the paper, praise it, or give only a verdict), so the critiques come from 34 reports. The Step 4 test sorts 169 critiques as rigor and 91 as contribution, a pooled rigor share of 65.0%; averaged within report, the share is 67.7%.
- **Dimensions.** Grouping gives 43 dimensions: 28 on the rigor side and 15 on the contribution side. Because this is batch 1, every dimension is new (Step 8). Thirteen of the 43 rest on three critiques or fewer, and four (PR26, PR27, PR28, and PC15) on one or two; two dimensions (PR25 and PR28) appear in a single report. These are the dimensions most likely to merge or vanish as batches are added.
- **Grain rule.** A dimension is one kind of asserted error (rigor) or one kind of value judgment (contribution) that a coder can recognize from the critique's own words without reading the manuscript. Two candidate groups were kept apart only when a one-line test separates them and the difference changes what the authors would have to do in reply (report something, justify something, reanalyze, or reframe). Groups were not split by field, by method family, or by the section of the manuscript the critique addresses.

What the authors most need to know:

1. **Version B leaves half of the critiques without a category.** 132 of the 260 critiques (51%) fall in dimensions that no Version B category covers. Eighty of these are presentation and editorial critiques, but the other 52 are substantive: unreported procedures (PR02, 16), unreported data and results (PR04, 9), registration (PR11, 6), data and code availability (PR19, 4), internal inconsistencies (PR23, 3), missing hypotheses (PR26, 2), ethics reporting (PR27, 2), novelty (PC08, 4), suggested extensions (PC14, 3), and undeveloped findings (PC13, 3). Version A misses far less: 38 critiques in six dimensions, 25 of them typographical and formatting.
2. **Reporting completeness is the largest rigor theme, and neither skeleton names it.** Three dimensions (PR02, PR04, PR12) assert that something the reader needs in order to evaluate the work is not reported; together they hold 31 critiques, 18% of the rigor side. Version B has no category for PR02 or PR04 and covers PR12 only in part; Version A reaches PR02 and PR04 only in part, through "clearly elaborated" in R15 and the disclosure items in R7.
3. **The presentation question moves the rigor share by up to 17 points.** Eighty critiques (31%) concern presentation or editing; the literal test puts 25 on the rigor side and 55 on the contribution side. Setting all 80 aside raises the pooled rigor share from 65.0% to 80.0%. The labeler flagged every one of the 80 as a hard case. See the section on the presentation question below.
4. **A few verbose reports drive many counts.** Three reports (R289, R057, R301) supply 73 of the 260 critiques (28%), and R289 alone supplies 8 of the 17 typographical critiques. Counts of critiques partly measure how finely a referee itemizes, so the saturation judgment should rest on distinct reports per dimension, which each entry below gives, as well as on critique counts.

Dimension IDs use the prefixes PR (pilot, rigor) and PC (pilot, contribution) so that they cannot be confused with the skeleton's Version A labels (R1 to R19, C1 to C15). Placements name the Version A criterion and the Version B category from `step5_skeleton.md`; "reports alone" means that no criterion in that version covers the dimension. Critique IDs have the form R<report>-C<critique>, where the report number is the collection-order number used in `step3_corpus_batch01.md` to `step3_corpus_batch07.md`.

## Rigor dimensions

### PR01. Typographical, grammatical, and language errors

**Critiques:** 17 in 8 reports.

**Definition:** The referee points to a typographical, grammatical, punctuation, tense, or proofreading error in the text.

**Version A:** reports alone (the nearest is ASR's "Minor issues" row, a report slot inside C14 on the contribution side).

**Version B:** reports alone.

**Examples:**

- “Has ‘Question 3’ been omitted following ‘Research’?” (R235-C12, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296421)
- “"consensus", not "Consensus"; not sure why this was capitalized everywhere in the revision” (R289-C13, https://rr.peercommunityin.org/articles/rec?id=1664)

**Critique IDs:** R125-C07, R157-C01, R233-C10, R235-C12, R235-C13, R245-C01, R268-C01, R289-C13, R289-C16, R289-C18, R289-C19, R289-C20, R289-C21, R289-C22, R289-C23, R294-C04, R294-C07

### PR02. Procedure, materials, setting, or data source not described

**Critiques:** 16 in 6 reports.

**Definition:** The referee asserts that the manuscript does not describe how the study was carried out (task parameters, instructions, stimuli, setting, scoring, software, or data source) in enough detail to evaluate or repeat it.

**Version A:** R15, Appropriate and well-executed methods (in part, through "clearly elaborated"); R7's disclosure items cover only conditions and exclusions.

**Version B:** reports alone (Version B has no category for completeness of reporting).

**Examples:**

- “In the method section, many essential technical design details are not reported.” (R079-C06, https://peerj.com/articles/21199/reviews/)
- “The criteria for the inclusion of the 31 handball position videos … were not clearly stated” (R104-C02, https://peerj.com/articles/19401/reviews/)

**Critique IDs:** R079-C06, R095-C01, R095-C02, R095-C03, R095-C04, R095-C05, R095-C11, R104-C02, R104-C03, R104-C04, R104-C05, R184-C03, R233-C02, R301-C07, R301-C12, R301-C13

### PR03. Conclusion goes beyond or against the evidence

**Critiques:** 10 in 7 reports.

**Definition:** The referee asserts that a conclusion, interpretation, generalization, or recommendation is not supported by, or contradicts, the evidence or logic the manuscript presents.

**Version A:** R14, Conclusions supported by the evidence (R9, External validity, for the one critique about generalizing beyond the sample).

**Version B:** No single category: internal and statistical conclusion validity together, in part, as the Step 5 crosswalk says for R14 (external validity for the generalization critique).

**Examples:**

- “Did the present paper study whether the workers were captive or coerced?” (R228-C02, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0298523)
- “it does not seem that the misinterpretation of p-values is a particularly widespread issue” (R315-C09, https://www.webofscience.com/api/gateway/wos/peer-review/10.1098/rsos.242167)

**Critique IDs:** R154-C06, R228-C02, R233-C07, R235-C03, R235-C04, R235-C05, R272-C04, R301-C21, R315-C09, R315-C11

### PR04. Data description or results not reported in enough detail

**Critiques:** 9 in 8 reports.

**Definition:** The referee asserts that descriptive statistics, attrition or compliance figures, data-quality checks, or the precision of reported results are missing or too coarse to evaluate the findings.

**Version A:** R7, Analytic flexibility, full disclosure, and preregistration (in part, through full reporting); ASQ's "Presentation of evidence" in R14 (in part).

**Version B:** reports alone.

**Examples:**

- “There is too little information about some very basic and essential aspects of the data.” (R079-C02, https://peerj.com/articles/21199/reviews/)
- “when discussing the "high dropout rate and low EMA compliance," exact numbers should be provided” (R301-C05, https://rr.peercommunityin.org/articles/rec?id=966)

**Critique IDs:** R057-C23, R079-C02, R125-C01, R154-C01, R272-C01, R285-C04, R301-C04, R301-C05, R315-C08

### PR05. Selection of sample, cases, or sources unexplained or biased

**Critiques:** 9 in 7 reports.

**Definition:** The referee asserts that the way participants, units, cases, or source documents were chosen or obtained is unexplained or may bias who or what is represented.

**Version A:** R16, Fit between question, theory, and data ("appropriateness of the data"); R9 in part; R18 for the two literature-search critiques.

**Version B:** External validity (in part: it covers whom results generalize to, not unexplained selection).

**Examples:**

- “What was the justification for selecting these specific 72 countries?” (R121-C04, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288346)
- “Were they selected randomly or based on specific criteria?” (R138-C13, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0285800)

**Critique IDs:** R121-C04, R138-C13, R184-C02, R225-C04, R225-C05, R235-C07, R235-C09, R314-C05, R315-C16

### PR06. Alternative explanation or confound not ruled out

**Critiques:** 9 in 6 reports.

**Definition:** The referee names a specific rival cause (a confound, an order, fatigue, or repetition effect, or unobserved heterogeneity) that could produce the result and asserts that it has not been ruled out.

**Version A:** R4, Internal validity and causal identification.

**Version B:** Internal validity.

**Examples:**

- “I am still concerned that there is a major confounding factor” (R048-C01, https://elifesciences.org/articles/108748/peer-reviews)
- “A possible reason for the shortened estimated time could be the factor of trial repetition.” (R095-C08, https://peerj.com/articles/19913/reviews/)

**Critique IDs:** R048-C01, R095-C07, R095-C08, R095-C09, R095-C12, R104-C06, R138-C10, R235-C06, R294-C03

### PR07. Formatting and style-convention errors

**Critiques:** 8 in 6 reports.

**Definition:** The referee asserts that the manuscript breaks a formatting or style convention (undefined abbreviations, heading or axis formatting, missing line numbers, a style-guide rule, or the conventional form of an abstract).

**Version A:** reports alone (the nearest are C9, Clarity, and ASR's "Minor issues" in C14, both on the contribution side).

**Version B:** reports alone.

**Examples:**

- “Please give abbreviations where they are first used” (R125-C06, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0290253)
- “UNFCCC has not been introduced in the introduction” (R289-C14, https://rr.peercommunityin.org/articles/rec?id=1664)

**Critique IDs:** R117-C01, R117-C02, R125-C06, R263-C02, R285-C05, R289-C09, R289-C14, R301-C18

### PR08. Citation missing or inaccurate

**Critiques:** 7 in 5 reports.

**Definition:** The referee asserts that a factual claim, or a method or idea taken from others, lacks a citation, or that a cited source is misreported.

**Version A:** R18, Engagement with prior literature and knowledge (in part; R18 concerns coverage of a literature, not support for a single claim).

**Version B:** Incorporation of Relevant Literature (in part), which sits on the contribution side.

**Examples:**

- “Reference the sentence.” (R121-C01, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288346)
- “A reference to the German Psychological Society’s position would be helpful.” (R235-C11, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296421)

**Critique IDs:** R121-C01, R235-C11, R245-C02, R289-C03, R289-C07, R289-C17, R315-C06

### PR09. Analysis wrong for the data or the question

**Critiques:** 7 in 4 reports.

**Definition:** The referee asserts that the analysis actually run is wrong for the data or the question, because it omits the key variable, ignores dependence or the distribution of the data, or uses a less suitable estimator or score.

**Version A:** R15, Appropriate and well-executed methods; R6, Statistical conclusion validity ("procedures and assumptions").

**Version B:** Statistical conclusion validity.

**Examples:**

- “…one crucial comparison. But the authors never take that into account.” (R057-C07, https://elifesciences.org/reviewed-preprints/111043/reviews)
- “Would an AR1 model have been appropriate to address correlations among repeated measures?” (R301-C01, https://rr.peercommunityin.org/articles/rec?id=966)

**Critique IDs:** R057-C07, R057-C08, R057-C18, R057-C20, R080-C01, R138-C12, R301-C01

### PR10. Method choice or assumption not justified

**Critiques:** 6 in 6 reports.

**Definition:** The referee asserts that a methodological choice or assumption is stated but not justified, without asserting that it is wrong.

**Version A:** R15, Appropriate and well-executed methods (in part); R7 for the one arbitrary threshold.

**Version B:** Statistical conclusion validity (in part: the statistical choices only; the coding-criteria critique would fall under construct validity).

**Examples:**

- “RTs are often log-transformed. It should be briefly mentioned why this was not done here.” (R057-C09, https://elifesciences.org/reviewed-preprints/111043/reviews)
- “write the reason why the data were not validated.” (R095-C10, https://peerj.com/articles/19913/reviews/)

**Critique IDs:** R057-C09, R095-C10, R138-C07, R225-C03, R289-C04, R315-C05

### PR11. Registration status or deviations from the registered plan not transparent

**Critiques:** 6 in 5 reports.

**Definition:** The referee asserts that the registration status of the study, or a departure from its registered plan, is not disclosed, explained, or traceable.

**Version A:** R7, Analytic flexibility, full disclosure, and preregistration.

**Version B:** reports alone (the Step 5 crosswalk: preregistration as a practice has no category).

**Examples:**

- “It should be made very clear early on that this study was not preregistered.” (R057-C22, https://elifesciences.org/reviewed-preprints/111043/reviews)
- “one coder analyzed the open EMA mentions, whereas two had originally been planned” (R301-C16, https://rr.peercommunityin.org/articles/rec?id=966)

**Critique IDs:** R057-C22, R271-C01, R271-C02, R272-C02, R301-C16, R314-C03

### PR12. Analysis plan or model not fully specified

**Critiques:** 6 in 4 reports.

**Definition:** The referee asserts that the statistical model or analysis plan is not specified completely enough to know what was, or will be, estimated.

**Version A:** R7, Analytic flexibility, full disclosure, and preregistration ("committing analysis in advance").

**Version B:** Statistical conclusion validity (in part, as the Step 5 crosswalk says for R7).

**Examples:**

- “the analysis plan needs further detail” (R283-C07, https://rr.peercommunityin.org/articles/rec?id=2500)
- “Clarification on the specification of random effects in the GLMER is needed.” (R301-C03, https://rr.peercommunityin.org/articles/rec?id=966)

**Critique IDs:** R057-C16, R138-C11, R283-C07, R283-C09, R283-C12, R301-C03

### PR13. Statistic or its criteria misdescribed or misapplied

**Critiques:** 6 in 3 reports.

**Definition:** The referee asserts that a statistic, a statistical term, or a classification criterion is explained, named, or applied incorrectly.

**Version A:** R6, Statistical conclusion validity and sound inference.

**Version B:** Statistical conclusion validity.

**Examples:**

- “due to unobserved confounding (it's not about measurement error)” (R289-C01, https://rr.peercommunityin.org/articles/rec?id=1664)
- “the 95% CI of [0.00, 0.15] for Cohen's w is interpreted as "consistent"” (R294-C01, https://rr.peercommunityin.org/articles/rec?id=1145)

**Critique IDs:** R272-C03, R289-C01, R289-C02, R289-C05, R289-C25, R294-C01

### PR14. Model comparison does not establish the preferred model

**Critiques:** 6 in 2 reports.

**Definition:** The referee asserts that the model comparison does not show the preferred model to be better than simpler or rival models, or that a model has more parameters than the data can support.

**Version A:** R6, Statistical conclusion validity and sound inference; R15 in part.

**Version B:** Statistical conclusion validity.

**Examples:**

- “I am not convinced that Model 3 is the winning model.” (R057-C14, https://elifesciences.org/reviewed-preprints/111043/reviews)
- “…the degraded BOM is not simply favored due to its flexibility or higher complexity” (R037-C02, https://elifesciences.org/articles/103734/peer-reviews)

**Critique IDs:** R037-C01, R037-C02, R057-C12, R057-C13, R057-C14, R057-C15

### PR15. Sample size or power inadequate or unjustified

**Critiques:** 5 in 5 reports.

**Definition:** The referee asserts that the sample size lacks a justification or that the power analysis does not match the tests on which the findings rest.

**Version A:** R6, Statistical conclusion validity and sound inference ("study power").

**Version B:** Statistical conclusion validity.

**Examples:**

- “the lack of justification for the sample size” (R314-C01, https://www.webofscience.com/api/gateway/wos/peer-review/10.1098/rsos.242167)
- “…not fully convinced that this power analysis maps onto the most important planned tests” (R283-C06, https://rr.peercommunityin.org/articles/rec?id=2500)

**Critique IDs:** R042-C03, R117-C09, R283-C06, R301-C02, R314-C01

### PR16. Anomalous or conflicting result not addressed

**Critiques:** 5 in 5 reports.

**Definition:** The referee points to a result that conflicts with another result, with prior evidence, or with the paper's own explanation, and asserts that the manuscript does not address the conflict.

**Version A:** R2, Logical coherence of the argument (in part: consistency within the paper and with accepted findings); R18 for the conflict with prior evidence.

**Version B:** Theoretical coherence (in part, through Kuhn's consistency).

**Examples:**

- “How can we reconcile this finding with the finding (presented on page 15)” (R042-C02, https://elifesciences.org/articles/87271/peer-reviews)
- “But what about the consistent behaviour condition? Shouldn't they amplify each other in that one?” (R289-C08, https://rr.peercommunityin.org/articles/rec?id=1664)

**Critique IDs:** R042-C02, R057-C17, R225-C06, R268-C03, R289-C08

### PR17. Measure does not capture the named construct

**Critiques:** 5 in 4 reports.

**Definition:** The referee asserts that a measure or task does not capture the construct the manuscript names, or that a construct the claims rely on was not measured at all.

**Version A:** R5, Construct validity and measurement.

**Version B:** Construct validity.

**Examples:**

- “The authors describe their task as an inhibition-of-return paradigm” (R079-C05, https://peerj.com/articles/21199/reviews/)
- “the primary dependent variable appears to be self-reported willingness to help” (R283-C03, https://rr.peercommunityin.org/articles/rec?id=2500)

**Critique IDs:** R057-C01, R057-C03, R079-C05, R283-C03, R289-C11

### PR18. Robustness to analytic choices not shown

**Critiques:** 4 in 3 reports.

**Definition:** The referee asserts that the results have not been shown to survive reasonable changes in analytic or classification choices.

**Version A:** R8, Robustness to assumptions (R7 for the researcher-degrees-of-freedom critique).

**Version B:** Statistical conclusion validity (in part, as the Step 5 crosswalk says for R8).

**Examples:**

- “a sensitivity analysis might still further strengthen the robustness of findings” (R034-C01, https://elifesciences.org/articles/107765/peer-reviews)
- “The results - as of now - are not robust.” (R102-C02, https://peerj.com/articles/19401/reviews/)

**Critique IDs:** R034-C01, R102-C02, R235-C08, R235-C10

### PR19. Data, code, or materials not available or not usable

**Critiques:** 4 in 3 reports.

**Definition:** The referee asserts that data, code, codebooks, or materials are not available, not linked, or not documented well enough to use.

**Version A:** reports alone (Step 5 notes that no input criterion concerns data availability; the nearest are R7's disclosure and R10's reproducibility).

**Version B:** reports alone.

**Examples:**

- “giving the script in Appendix H is essential for the reproducibility of the study” (R125-C03, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0290253)
- “a codebook is missing from the data files” (R315-C02, https://www.webofscience.com/api/gateway/wos/peer-review/10.1098/rsos.242167)

**Critique IDs:** R125-C03, R283-C13, R315-C02, R315-C03

### PR20. Difference claimed without a direct test

**Critiques:** 4 in 2 reports.

**Definition:** The referee asserts that a difference between groups, conditions, or coefficients is claimed without a direct statistical test of that difference.

**Version A:** R6, Statistical conclusion validity and sound inference.

**Version B:** Statistical conclusion validity.

**Examples:**

- “the authors say something like "this is significant, but that is not."” (R057-C06, https://elifesciences.org/reviewed-preprints/111043/reviews)
- “how can we see which is more important?” (R154-C03, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289845)

**Critique IDs:** R057-C06, R057-C21, R154-C03, R154-C05

### PR21. Measure reliability unreported or low

**Critiques:** 3 in 3 reports.

**Definition:** The referee asserts that the reliability of a measure is not reported, or is too low for the measure to be trusted.

**Version A:** R5, Construct validity and measurement ("valid, reliable measures").

**Version B:** Construct validity.

**Examples:**

- “Cronbach's alpha should be checked for each scale” (R301-C17, https://rr.peercommunityin.org/articles/rec?id=966)
- “Given the low interrater reliability among coders, this measure … may not be very reliable” (R315-C14, https://www.webofscience.com/api/gateway/wos/peer-review/10.1098/rsos.242167)

**Critique IDs:** R079-C03, R301-C17, R315-C14

### PR22. Selective or misleading presentation of results

**Critiques:** 3 in 3 reports.

**Definition:** The referee asserts that the manuscript reports or emphasizes results selectively, or presents their status misleadingly.

**Version A:** R7, Analytic flexibility, full disclosure, and preregistration ("countering selective reporting").

**Version B:** Statistical conclusion validity (in part, as for R7).

**Examples:**

- “the asymmetric reporting and highlighting of version 1 (null result) versus version 2 (rejecting null)” (R051-C01, https://elifesciences.org/articles/108748/peer-reviews)
- “The abstract sometimes reads as though the findings have already occurred” (R283-C11, https://rr.peercommunityin.org/articles/rec?id=2500)

**Critique IDs:** R051-C01, R079-C04, R283-C11

### PR23. Internal inconsistency or broken cross-reference

**Critiques:** 3 in 3 reports.

**Definition:** The referee points to two places in the manuscript that disagree on a fact or number, or to a cross-reference whose target cannot be found.

**Version A:** reports alone (R2's consistency concerns the argument, not reported numbers).

**Version B:** reports alone.

**Examples:**

- “The results as stated in the abstract are different with the results … in Table 1” (R289-C12, https://rr.peercommunityin.org/articles/rec?id=1664)
- “I can't find this section in the supplementary materials” (R294-C06, https://rr.peercommunityin.org/articles/rec?id=1145)

**Critique IDs:** R125-C02, R289-C12, R294-C06

### PR24. Participant reactivity: demand or social desirability

**Critiques:** 3 in 2 reports.

**Definition:** The referee asserts that participants' responses may reflect their awareness of the study's purpose or a wish to answer in socially acceptable ways.

**Version A:** R9, External validity and transferability (Campbell and Stanley's reactive arrangements); R5's construct-irrelevant variance in part.

**Version B:** External validity, following Version A's grouping, although the referees present these as rival explanations of the result itself.

**Examples:**

- “participants may also respond in socially desirable ways or infer the study's purpose” (R283-C04, https://rr.peercommunityin.org/articles/rec?id=2500)
- “was this due to a question-demand effect?” (R301-C15, https://rr.peercommunityin.org/articles/rec?id=966)

**Critique IDs:** R283-C04, R283-C05, R301-C15

### PR25. Causal claim rests on a measured, not manipulated, variable

**Critiques:** 3 in 1 report.

**Definition:** The referee asserts that a causal claim rests on a variable that was measured rather than manipulated, or was measured after the treatment.

**Version A:** R4, Internal validity and causal identification.

**Version B:** Internal validity.

**Examples:**

- “only the argument condition and race condition appear to be experimentally manipulated” (R283-C01, https://rr.peercommunityin.org/articles/rec?id=2500)
- “the mediators are not experimentally manipulated” (R283-C08, https://rr.peercommunityin.org/articles/rec?id=2500)
- (Both examples come from one report, the only report in which this dimension appears.)

**Critique IDs:** R283-C01, R283-C02, R283-C08

### PR26. Hypotheses absent or not stated as testable predictions

**Critiques:** 2 in 2 reports.

**Definition:** The referee asserts that the manuscript states no hypotheses, or states them without the specific prediction the design tests.

**Version A:** R1, Falsifiability and testability.

**Version B:** reports alone (R1 has no Version B category).

**Examples:**

- “No research questions or hypothesis ? provide them” (R138-C09, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0285800)
- “In the hypotheses, the expectation of an increase in the experimental (vs. control group) only…” (R301-C14, https://rr.peercommunityin.org/articles/rec?id=966)

**Critique IDs:** R138-C09, R301-C14

### PR27. Ethics approval or consent not reported

**Critiques:** 2 in 2 reports.

**Definition:** The referee asserts that ethics approval or informed consent is not reported.

**Version A:** R19, Research ethics.

**Version B:** reports alone.

**Examples:**

- “Is there no information about consent in the information section of the survey form?” (R117-C10, https://peerj.com/articles/18682/reviews/)
- “information about the ethical approval and consent procedures … could be also be included” (R245-C04, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0306629)

**Critique IDs:** R117-C10, R245-C04

### PR28. Practical size of the effect not assessed

**Critiques:** 1 in 1 report.

**Definition:** The referee asserts that the manuscript establishes that an effect is statistically significant but not how large it is in practical terms.

**Version A:** R6, Statistical conclusion validity and sound inference (a p-value is not the size or importance of an effect).

**Version B:** Statistical conclusion validity.

**Examples:**

- “…a significant impact on M&A behavior, but to what extent” (R154-C02, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289845)
- (Only one critique is in this dimension.)

**Critique IDs:** R154-C02

## Contribution dimensions

### PC01. Organization, length, and placement of material

**Critiques:** 16 in 11 reports.

**Definition:** The referee asserts that material is too long, repetitive, in the wrong section, or poorly ordered or weighted.

**Version A:** C9, Clarity and quality of presentation ("flows logically"); C10, Contribution relative to length, for the length critiques.

**Version B:** reports alone.

**Examples:**

- “The paper looks very lengthy.” (R121-C03, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288346)
- “There is no need to include the scales used in this section.” (R117-C04, https://peerj.com/articles/18682/reviews/)

**Critique IDs:** R057-C05, R104-C01, R117-C04, R117-C08, R117-C11, R117-C13, R121-C02, R121-C03, R125-C04, R125-C05, R138-C14, R245-C03, R263-C01, R301-C19, R314-C04, R315-C01

### PC02. Prose unclear, imprecise, or wordy

**Critiques:** 12 in 5 reports.

**Definition:** The referee asserts that the wording of a sentence, passage, or section is unclear, imprecise, awkward, or wordy.

**Version A:** C9, Clarity and quality of presentation.

**Version B:** reports alone.

**Examples:**

- “the abstract could benefit from more specific and concise language” (R138-C03, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0285800)
- “the whole section is a bit awkwardly written up” (R289-C06, https://rr.peercommunityin.org/articles/rec?id=1664)

**Critique IDs:** R138-C03, R138-C15, R233-C01, R233-C09, R289-C06, R289-C15, R289-C24, R289-C26, R289-C27, R294-C02, R294-C05, R315-C10

### PC03. Implications or recommendations underdeveloped

**Critiques:** 9 in 6 reports.

**Definition:** The referee asserts that the findings' implications for practice, policy, or future research, or the concreteness of the paper's recommendations, are underdeveloped.

**Version A:** C8, Practical relevance and consequences ("practical ramifications").

**Version B:** Importance of Problem (in part: only where importance means importance to practice).

**Examples:**

- “How do the findings of your study set out for future research in this area?” (R121-C05, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0288346)
- “a discussion on the broader implications of the intervention … would add valuable nuance” (R301-C22, https://rr.peercommunityin.org/articles/rec?id=966)

**Critique IDs:** R117-C15, R121-C05, R138-C16, R138-C17, R294-C08, R301-C22, R315-C04, R315-C12, R315-C13

### PC04. Prior work and background context insufficiently covered

**Critiques:** 9 in 4 reports.

**Definition:** The referee asserts that the manuscript omits relevant prior work, or background context, needed to frame the study.

**Version A:** R18, Engagement with prior literature and knowledge, which sits on the rigor side; AJPS's "Literature engagement" row in C6 in part.

**Version B:** Incorporation of Relevant Literature.

**Examples:**

- “The authors did not refer to sources that were pioneers in the research…” (R225-C01, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0307137)
- “other ESM studies in environmental psychology should be referenced to situate the study…” (R301-C10, https://rr.peercommunityin.org/articles/rec?id=966)

**Critique IDs:** R138-C01, R138-C04, R138-C05, R138-C08, R225-C01, R301-C10, R301-C11, R315-C07, R315-C15

### PC05. Method or results hard to follow

**Critiques:** 8 in 6 reports.

**Definition:** The referee asserts that a method, model, or result is present but explained too briefly or too densely for readers to follow.

**Version A:** C9, Clarity and quality of presentation.

**Version B:** reports alone.

**Examples:**

- “complex, difficult to understand 3-way interactions” (R042-C01, https://elifesciences.org/articles/87271/peer-reviews)
- “The setup of the task … should be made clearer in the main text” (R057-C02, https://elifesciences.org/reviewed-preprints/111043/reviews)

**Critique IDs:** R042-C01, R057-C02, R057-C10, R057-C11, R117-C12, R138-C02, R235-C02, R314-C02

### PC06. Purpose, hypotheses, or key concepts not stated clearly

**Critiques:** 6 in 4 reports.

**Definition:** The referee asserts that the study's purpose, research gap, hypotheses, or key concepts are not stated clearly.

**Version A:** C9, Clarity and quality of presentation.

**Version B:** reports alone.

**Examples:**

- “Your hypotheses should be stated clearly.” (R117-C06, https://peerj.com/articles/18682/reviews/)
- “the research purpose and research framework of the manuscript are unclear.” (R233-C06, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297587)

**Critique IDs:** R102-C01, R117-C03, R117-C05, R117-C06, R138-C06, R233-C06

### PC07. Figures, tables, or examples missing or poorly presented

**Critiques:** 5 in 5 reports.

**Definition:** The referee asserts that a figure, table, or illustrative example is missing from the main text or is poorly presented.

**Version A:** C9, Clarity and quality of presentation (in part).

**Version B:** reports alone.

**Examples:**

- “A correlation figure between stress and estimated waiting time seems necessary.” (R095-C06, https://peerj.com/articles/19913/reviews/)
- “large individual data points in Figure 9b” (R268-C04, https://rr.peercommunityin.org/articles/rec?id=1346)

**Critique IDs:** R095-C06, R233-C03, R268-C04, R285-C03, R301-C09

### PC08. Novelty or advance over prior work not established

**Critiques:** 4 in 3 reports.

**Definition:** The referee asserts that the manuscript does not show what is new relative to prior work, or that it is not new.

**Version A:** C2, Originality and novelty.

**Version B:** reports alone (the gap the Step 5 file ranks first).

**Examples:**

- “The novelty of this manuscript is very inadequate. There are many similar studies.” (R233-C05, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297587)
- “more literature support is needed to highlight the study's unique value.” (R117-C07, https://peerj.com/articles/18682/reviews/)

**Critique IDs:** R117-C07, R233-C05, R233-C08, R235-C01

### PC09. Title or abstract does not convey the study

**Critiques:** 4 in 3 reports.

**Definition:** The referee asserts that the title or abstract misframes the study or leaves out information readers need.

**Version A:** C9, Clarity and quality of presentation (in part).

**Version B:** reports alone.

**Examples:**

- “whether the title unintentionally frames the issue as a binary between rebellion and racism” (R283-C10, https://rr.peercommunityin.org/articles/rec?id=2500)
- “In the title, why was "young adults" deleted?” (R301-C06, https://rr.peercommunityin.org/articles/rec?id=966)

**Critique IDs:** R283-C10, R285-C01, R285-C02, R301-C06

### PC10. Tone or terminology inappropriate

**Critiques:** 4 in 3 reports.

**Definition:** The referee asserts that a word, term, or tone is value-laden, patronizing, or otherwise unsuited to scholarly writing.

**Version A:** C9, Clarity and quality of presentation (in part).

**Version B:** reports alone.

**Examples:**

- “"our advice is" reads somewhat patronising” (R289-C28, https://rr.peercommunityin.org/articles/rec?id=1664)
- “Is this an objective term?” (R228-C01, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0298523)

**Critique IDs:** R184-C05, R228-C01, R289-C10, R289-C28

### PC11. Theoretical grounding weak or narrow

**Critiques:** 3 in 3 reports.

**Definition:** The referee asserts that the theory behind the hypotheses or the proposed mechanism is weak, narrow, or undeveloped.

**Version A:** C3, Theoretical contribution, and C4, Explanatory power and utility of theory (R3 on the rigor side also matches).

**Version B:** Development of Theory.

**Examples:**

- “The theoretical basis for the mechanisms presented in this study is very weak and unconvincing.” (R233-C04, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0297587)
- “can the authors kind of theorize on what openness is doing?” (R080-C02, https://peerj.com/articles/21199/reviews/)

**Critique IDs:** R079-C01, R080-C02, R233-C04

### PC12. Findings not compared with prior work in the discussion

**Critiques:** 3 in 3 reports.

**Definition:** The referee asserts that the discussion does not compare the findings with prior literature.

**Version A:** R18, Engagement with prior literature and knowledge (rigor side); C6's accumulation of knowledge in part.

**Version B:** Incorporation of Relevant Literature.

**Examples:**

- “This section should briefly address the aim and then compare the findings with the literature.” (R117-C14, https://peerj.com/articles/18682/reviews/)
- “compare your outputs and findings in a broader context.” (R157-C02, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289845)

**Critique IDs:** R117-C14, R157-C02, R301-C08

### PC13. Finding or promised theme left undeveloped

**Critiques:** 3 in 3 reports.

**Definition:** The referee asserts that a particular finding, or a theme the paper promises, is reported but not discussed or interpreted enough.

**Version A:** reports alone (C1's surprising findings is the nearest, but no critique claims the finding is interesting).

**Version B:** reports alone.

**Examples:**

- “The decrease in collective action below baseline in both groups should be discussed…” (R301-C20, https://rr.peercommunityin.org/articles/rec?id=966)
- “The portion to Destination Sustainability haven't being discussed much in this paper.” (R184-C04, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296944)

**Critique IDs:** R184-C04, R268-C02, R301-C20

### PC14. Worthwhile extension or further analysis not pursued

**Critiques:** 3 in 2 reports.

**Definition:** The referee proposes an additional analysis or extension that would make the study more informative.

**Version A:** reports alone (the nearest is Econometrica's "Suggestions" row, a report slot inside C14).

**Version B:** reports alone.

**Examples:**

- “I would have expected some exploratory analyses regarding individual differences” (R057-C04, https://elifesciences.org/reviewed-preprints/111043/reviews)
- “whether there is a difference in time series.” (R154-C04, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0289845)

**Critique IDs:** R057-C04, R057-C19, R154-C04

### PC15. Importance or scope of the question not argued

**Critiques:** 2 in 2 reports.

**Definition:** The referee asserts that the manuscript does not argue why its question matters, or how far its relevance extends beyond the setting studied.

**Version A:** C5, Importance and timeliness of the problem; C7, Breadth of interest, in part for the scope critique.

**Version B:** Importance of Problem.

**Examples:**

- “add more justification why tourist to tourist interaction is important” (R184-C01, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0296944)
- “whether your research is relevant only in the UK” (R225-C02, https://journals.plos.org/plosone/article/peerReview?id=10.1371/journal.pone.0307137)

**Critique IDs:** R184-C01, R225-C02

## Boundary rules

These are the Step 9 rewrites: wherever a critique fit two dimensions, the definitions were narrowed until it fit one, and the rule that decides the case is recorded here.

1. **Not described versus not justified (PR02, PR12 versus PR10).** If what was done is missing from the manuscript, the critique goes to PR02 (procedure, materials, setting, data source) or PR12 (statistical model or analysis plan). If what was done is stated but the reason for it is not, it goes to PR10. If the referee says the choice is wrong, it goes to PR09 or to the more specific dimension.
2. **Procedure versus analysis (PR02 versus PR12).** PR02 covers what participants experienced and where the data came from; PR12 covers what was estimated and how.
3. **Selection of units comes first (PR05).** A critique of how participants, countries, articles, journals, or studies were chosen goes to PR05 even when phrased as "not justified" or "not explained," so PR05 takes precedence over PR10 and PR02. The selection of stimuli (R104-C02, the video clips) goes to PR02, because stimuli are materials, not units of analysis.
4. **Rival explanations (PR06, PR24, PR25).** PR24 when the rival is participants' awareness of the study's purpose or their wish to answer acceptably; PR25 when the objection is that the causal variable was measured rather than manipulated, whether or not a specific rival is named; PR06 for every other named rival cause, including order, fatigue, and repetition effects.
5. **Conclusions, conflicts, and inconsistencies (PR03, PR16, PR23).** PR23 when two statements of fact or number in the manuscript disagree and no inference is involved; PR03 when a conclusion the authors draw is unsupported by, or contradicts, their evidence (so R154-C06, where the text's conclusion contradicts the table, goes to PR03); PR16 when a result conflicts with another result or with prior evidence and the manuscript leaves the conflict unaddressed without drawing a wrong conclusion from it.
6. **Overclaiming through the measure (PR03 versus PR17).** When a claim overreaches because of what the measure captures (self-reported willingness to help described as discriminatory behaviour, R283-C03), the critique goes to PR17.
7. **Missing versus selective reporting (PR04 versus PR22).** PR22 only when the referee says the omission or emphasis favors a particular result; otherwise PR04.
8. **Reliability (PR21 versus PR04).** Any critique about the reliability of a measure goes to PR21, including "reliability is not reported."
9. **Model comparison versus misspecification (PR14 versus PR09).** Critiques about whether the preferred model beats rival or simpler models, or has too many parameters, go to PR14; other analyses said to be wrong for the data go to PR09.
10. **Robustness versus justification (PR18 versus PR10).** PR18 when the referee doubts that the result would survive a different choice; PR10 when the referee asks only for the rationale. An arbitrary threshold with no stated basis (R289-C04) goes to PR10.
11. **Misdescribed statistics (PR13 versus PR10).** PR13 when a statistic, term, or classification criterion is described or applied incorrectly; PR10 when a criterion is applied without a stated basis.
12. **Registration versus plan (PR11 versus PR12).** PR11 when the issue is the relation between the work and a registered plan (including undisclosed non-registration); PR12 when the plan itself is incomplete.
13. **Hypotheses (PR26 versus PC06).** PR26 when hypotheses are absent or lack the predicted contrast the design tests; PC06 when they exist but are explained unclearly.
14. **Citations versus literature coverage (PR08 versus PC04).** PR08 when a specific claim, method, or idea needs a source or a source is misreported; PC04 when the complaint is the coverage of prior work or background used to frame the study.
15. **Three literature dimensions (PC04, PC08, PC12).** PC08 when the referee questions whether the work is new or asks the authors to argue its advance; PC12 when the discussion does not compare the findings with prior work; PC04 otherwise.
16. **Three clarity dimensions (PC02, PC05, PC06).** PC06 for purpose, research gap, hypotheses, and key concepts; PC05 for methods, models, and results; PC02 for wording, whatever the content.
17. **Organization versus figures (PC01 versus PC07).** Moving figures or tables out of the main text to save length or improve flow (R121-C03, R125-C04) goes to PC01; a figure or table that is missing or badly drawn goes to PC07.
18. **Abstracts and titles (PR22, PR07, PC09).** An abstract that misrepresents the evidence goes to PR22; an abstract that breaks a format convention goes to PR07; a title or abstract that misframes the study or omits information goes to PC09.
19. **Undeveloped findings (PC13 versus PR16).** A finding that is reported but under-discussed, with no threat to a conclusion, goes to PC13; a finding that conflicts with another goes to PR16.
20. **Implications versus literature (PC03 versus PC12).** Implications for practice, policy, and future research go to PC03; comparison with prior findings goes to PC12.
21. **Errors, conventions, and clarity (PR01, PR07, PC02, PC10).** PR01 for errors against spelling, grammar, or punctuation; PR07 for breaches of layout or style conventions; PC02 for text that is correct but unclear; PC10 for wording judged value-laden or inappropriate in tone.
22. **Recap sentences.** R283-C13 is a closing summary that repeats earlier points; only its one new element (all materials should be available) was coded, and it goes to PR19.

## Skeleton criteria with no critiques in this batch

**Version A, rigor (6 of 19).**

| Criterion | Sources |
|:--|:--|
| R3. Explanatory specification of the theory | Literature alone (Whetten; Bacharach; Sutton and Staw). The three contribution-side critiques in PC11 would match it if they were sorted as rigor. |
| R10. Replicability and dependability | Literature alone (Open Science Collaboration; Simmons, Nelson and Simonsohn; Guba). PR19's reproducibility critiques are the nearest. |
| R11. Neutrality and reflexivity | Literature alone (Guba; Tracy; Ioannidis). |
| R12. Credibility of qualitative accounts | Literature alone (Guba; Tracy). |
| R13. Grounding of theory in data | Literature alone (Gioia, Corley and Hamilton; Eisenhardt; Tracy). |
| R17. Candor about limitations and scope | Forms alone (ASR; Psychological Science; AMPPS). Two critiques in PR25 ask for a stated limitation, but their assertion is about causal inference, so they sit under R4. |

No critique in this batch addresses a qualitative study, which is why R11 to R13 received none.

**Version A, contribution (6 of 15).**

| Criterion | Sources |
|:--|:--|
| C1. Interestingness: denying assumptions and surprising | Both (Davis; AMJ, ASQ, AMD). |
| C11. Fit with the journal | Forms alone (AMD; APA journals). |
| C12. Revisability | Forms alone (JOP; APA journals). |
| C13. Overall recommendation | Forms alone (AER; JIBS; AJPS; JOP; APA journals). |
| C14. Report structure and reviewer instructions | Forms alone (AMJ; AMD; JIBS; ASR; Econometrica). |
| C15. Integration | Forms alone (JIBS). |

C12 to C15 are rows about the verdict or the report rather than the manuscript, and the extraction excluded verdicts, so their emptiness is expected. C1 and C11 are genuine absences in this batch.

**Version B (1 of 9).** Every rigor category received critiques. On the contribution side, **Relevance to Organization Science** received none. It comes from the form (the Organization Science row itself); its Version A matches are C11, from the forms alone, and in part C7, from both the literature and the forms. None of batch 01's venues is a management journal, so this absence says little about Organization Science referees.

## The presentation question

The Step 4 test sorts a critique by whether a reader could check it against the text, a source, or a rule. Applied literally, it sends typographical and grammatical errors to rigor, because a reader can confirm them in the text, and it sends most clarity, organization, and length critiques to contribution, because no check settles whether prose is clear.

In this batch, 80 critiques (31% of 260) are presentation or editorial: 25 on the rigor side (PR01, 17 typographical and language errors; PR07, 8 formatting and style-convention errors) and 55 on the contribution side (PC01, 16; PC02, 12; PC05, 8; PC06, 6; PC07, 5; PC09, 4; PC10, 4). They appear in 24 of the 34 reports with critiques, and one report (R263) contains nothing else. The labeler flagged all 80 as hard cases, and they make up 80 of the batch's 94 hard cases.

| Treatment | Rigor critiques | All critiques | Pooled rigor share | Mean within-report share |
|:--|--:|--:|--:|--:|
| As sorted by the literal test | 169 | 260 | 65.0% | 67.7% (34 reports) |
| All 80 presentation and editorial critiques set aside as a third group | 144 | 180 | 80.0% | 80.9% (33 reports) |
| Only the 25 rigor-side editorial critiques set aside | 144 | 235 | 61.3% | 61.8% (34 reports) |
| Only the 55 contribution-side presentation critiques set aside | 169 | 205 | 82.4% | 84.6% (34 reports) |

The choice matters in two ways. First, it moves the level of the rigor share by up to 17 points, and in either direction depending on which part is set aside. Second, if AI and human reviewers differ in how many presentation critiques they write, the treatment would move the AI-human difference as well as the level. The options are to keep the literal test (and report presentation as a subdimension on each side), to set presentation and editorial critiques aside as a third group excluded from the primary outcome, or to report the rigor share both ways. This document does not choose among them.

## Sort disagreements

Each critique stays on the side it was assigned. The critiques below are ones where Claude's reading of the Step 4 test, at the grouping stage, differs from the side assigned at labeling.

Assigned contribution, but the test reads as rigor:

- **Omitted literature (PC04): R225-C01, R138-C05, R138-C08, R301-C10, R315-C07, R315-C15.** Each names specific prior work or a specific literature that is missing, which can be checked against the sources. The skeleton's own sort puts the literature rows of AMLE and JIBS on the rigor side (R18). The three background-context critiques in PC04 (R138-C01, R138-C04, R301-C11) ask for more context, which is a judgment, so they agree with their side.
- **Title against content (PC13 and PC09): R184-C04, R283-C10.** Whether the title names a theme the text barely treats, or a binary the design does not have, can be checked in the manuscript.
- **Usability of shared data (PC01): R315-C01.** The referee says the OSF page makes the data hard to understand, which bears on whether the data can be checked (compare PR19).
- **Method description (PC05): R138-C02.** Whether the model is described can be checked. Two other critiques in the same report (R138-C07 and R138-C11) make the same kind of request and were sorted as rigor.
- **Underclaiming (PC03): R294-C08.** The referee suggests the evidence supports a stronger conclusion than the authors draw, which is a question of fit between conclusion and evidence (Version A's R14).

Assigned rigor, but the test reads as contribution:

- **Critiques that name no check (PR03 and PR18): R233-C07, R102-C02.** Both are bare assertions ("unaddressed issues," "not robust") with no pointer to what is wrong; under the skeleton's rule, a critique that names no check falls on the contribution side.
- **Layout and style conventions (PR07): R289-C09, R263-C02, R301-C18, R117-C01, R117-C02.** Missing line numbers, heading format, APA numerals, and the conventional form of an abstract breach no fact and no logical or statistical rule. The other three critiques in PR07 (undefined abbreviations and unlabeled axes) leave the reader unable to check the content, so they fit rigor better.
- **Hedged approval (PR18): R034-C01.** The referee mentions that a sensitivity analysis might help but says the main concerns are resolved; it may not be a critique at all.

## What changes for the formal run

1. **Settle the presentation question before the formal run.** Eighty of 260 critiques depend on it, all were flagged as hard cases, and the answer changes the primary outcome. The codebook should say where each of PR01, PR07, and PC01 to PC10 goes.
2. **Settle the literature question as well.** The labeler put omitted-literature critiques on the contribution side, while the skeleton's Step 4 sort puts literature engagement (R18) on the rigor side, and Version B puts it on the contribution side. Twelve critiques (PC04 and PC12) sit on this line.
3. **Fix the segmentation rule.** One referee's list of five missing procedural details became five critiques (R095-C01 to C05), while another's list of many missing task parameters became one (R079-C06). A rule of one critique per asserted error, not per item listed, would make counts comparable across reports. Recap sentences (R283-C13) need a rule too.
4. **Count distinct reports per dimension in the stopping rule.** Several dimensions draw two-thirds or more of their critiques from one report (PR13, PR14, PR24, PC14) or all of them (PR25, PR28), so a new dimension from one verbose report should not count the same as one that recurs across reports.
5. **Expect merges.** Forty-three dimensions from 34 reports is fine-grained. Likely merges as batches are added: PR24 and PR25 into PR06; PR21 into PR17; PR28 into PR13; PC13 with PC12; PC05 with PC06. The grain rule should be fixed before batch 02 so that a merge is recorded as a merge rather than as a vanished dimension.
6. **Mark registered-report reviews.** Nine of the pilot's 44 reports come from PCI Registered Reports, and four of the six critiques in each of PR11 and PR12 come from them. The sample manuscript for the study is not a registered report, so venue type should be recorded with each critique.
7. **The corpus has no management journal in batch 01 and no qualitative study.** The empty Version A criteria (R11 to R13, C1, C11) and the empty Version B row (Relevance to Organization Science) may reflect the corpus rather than referees; later batches, and any management-journal reports that can be added, will show which.
8. **Give the labeler worked examples at the boundaries.** The same kind of request was sorted differently within one report (R138-C02 against R138-C07 and R138-C11). Worked examples for "method not explained," "literature omitted," and "title misframes" would reduce this.
