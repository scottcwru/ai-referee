# Codebook, version 8

The dimension list from `step9_dimensions_v8.md`, with a one-sentence definition for each place a critique can be coded, and the boundary rules Scott set (`step7_meta_dimensions.md`, `step8_combined_dimensions.md`).
A critique is one sentence or group of consecutive sentences in a report that asserts one defect in the manuscript.
Code each critique to the most specific entry that fits. An entry marked *(parent)* takes a critique only when none of its sub-dimensions fits.

## Methods *(parent)*

| Code | Entry | The referee asserts |
|:--|:--|:--|
| MET.DES | Appropriateness of Design *(parent)* | The design or the data cannot answer the research question, for a reason not listed below. |
| MET.DES.SAMP | Sample selection | How the sample (participants, cases, countries, studies, sources, journals) was chosen is unexplained, unjustified, or biased, or the sampling logic is misunderstood. When a study's data are published literature, the literature search and the choice of journals are sample selection. |
| MET.ANA | Appropriateness of Analysis and Interpretation | The statistical analysis is wrong: the wrong analysis for the data or question, a model comparison that does not support the chosen model, inadequate power or sample size, a statistic misdescribed or misapplied (including a statistical term used for the wrong kind of test), an analytic choice or assumption not justified (transformations, thresholds, pooling), or the practical size of the effect not assessed. |
| MET.MEAS | Validity and reliability of measures *(parent)* | The study measures the phenomenon incorrectly, for a reason not listed below. |
| MET.MEAS.CON | Construct validity *(parent)* | The research operations do not represent the constructs they are claimed to represent (Shadish, Cook & Campbell: "inferences about the constructs that research operations represent"). |
| MET.MEAS.CON.MEAS | Construct validity of measures | A measure does not capture the construct it is named for, a claimed mechanism is never measured, or coding criteria are not shown to capture the concept. |
| MET.MEAS.CON.MANIP | Construct validity of manipulations | A manipulation, treatment, or proxy condition does not produce or represent the state it is meant to induce. Added after batch 02. |
| MET.MEAS.REL | Reliability | Reliability is unreported or low, including interrater reliability. |
| MET.MEAS.STATE | Participant state: order, practice, fatigue, or inattention | Participants' order, practice, fatigue, or inattention distorts what is measured, including their behavior. |
| MET.MEAS.REACT | Reactive arrangements | Demand characteristics or social desirability distort participants' responses. |
| MET.INT | Internal validity *(parent)* | A different explanation of the result cannot be ruled out, for a reason not listed below. |
| MET.INT.ALT | Alternative explanation or confound | A specific rival explanation, confound, or unobserved difference between units is not ruled out. |
| MET.INT.CAUSAL | Causal claim rests on a measured, not manipulated, variable | A causal claim is made from a variable that was measured rather than manipulated. |
| MET.PLAN | Analysis plan or model not specified | Model structure, parameters, a non-standard test, confirmatory versus exploratory analyses, or missing-data handling is not specified. |
| MET.ROB | Robustness | The result is not shown to survive other reasonable analytic choices (sensitivity analysis, researcher degrees of freedom, an artifact of a classification choice). |
| MET.DISC | Full disclosure *(parent)* | The paper does not report enough to see how the study was done or what it found, for a reason not listed below. |
| MET.DISC.PROC | Process or findings not described | A procedure, material, data source, or result is not reported in enough detail; data, code, or materials are unavailable or unusable; a referenced supplement or table is missing. |
| MET.DISC.PREREG | Preregistration | The study was not preregistered where it should have been, or its registration status or deviations from the registered plan are not transparent. |
| MET.DISC.ETH | Research ethics | Ethics approval or consent is not reported, or the research was not conducted ethically. |

## Development of Theory *(parent)*

| Code | Entry | The referee asserts |
|:--|:--|:--|
| THE.GROUND | Theoretical grounding weak or narrow | The theory behind the hypotheses or mechanism is thin, narrow, weak, or never introduced. |
| THE.CONTRIB | Contribution to theory | The work does not test, create, or extend theory (a statement of importance about theory). |
| THE.UTIL | Utility of theory | The theory explains or predicts too little. |
| THE.COH | Consistency/Coherence of Conceptual Argument *(parent)* | The theoretical argument is not clear and logical. |
| THE.COH.ECO | Ecological validity | Realism: the theory or model rests on an assumption that is unrealistic for the agents or setting it describes, or the study's setting or task lacks the real-world features the claims are about. Label from Scott; added after batch 04, widened to study settings after batch 05. |
| THE.COH.CONTRA | Internal contradictions | The theory says one thing (X causes Y) and another part of the paper says something incompatible (Y causes X, or X and Y are only correlated). |
| THE.LINK | Linkage between Conceptual Argument and Empirical Analysis | The hypotheses or the test do not follow from the argument, or an inductively built theory is not grounded in the data. |
| THE.FALS | Falsifiability | The paper states no research questions, hypotheses, or testable predictions. |

## Research Questions and Goals *(parent)*

| Code | Entry | The referee asserts |
|:--|:--|:--|
| RQ.IMP | Importance of Problem | The paper does not argue why its question matters or how widely it applies. |
| RQ.FRAME | Framing of the argument | The way the paper sets up what it asks and why is wrong or unconvincing (distinct from positioning in the literature, which is Incorporation of Relevant Literature). Label from the proposal's original list; added 2026-09-25. |
| RQ.PURP | Purpose of the research | What the study sets out to do (its aim, the gap it fills, its hypotheses, or its key concepts) is unclear. |

## Legitimacy of Conclusions *(parent)*

| Code | Entry | The referee asserts |
|:--|:--|:--|
| CON.SHOWN | Claim or conclusion not shown | A claim or conclusion is not shown by the evidence: never tested, tested without showing it, a difference claimed without a direct test, a result misread against its confidence interval, a generalization beyond the sample, or a conclusion about something never measured. |
| CON.ANOM | Anomalous or conflicting result not addressed | Part of the evidence cuts against the authors' account and is left unexplained. |
| CON.UNDEV | Finding left undeveloped | The authors do not interpret what their own results show: an unexpected finding, a promised theme, or the plain reading of the results. |
| CON.NEUT | Neutrality | Results are presented selectively or as stronger or more settled than they are, or the findings reflect the investigator's biases or interests. |
| CON.REPL | Replicability | The finding may not replicate. |

## Overall contribution *(parent)*

| Code | Entry | The referee asserts |
|:--|:--|:--|
| CONTRIB | Overall contribution *(parent)* | The paper adds too little to knowledge, for a reason not listed below. |
| CONTRIB.EXT | Extension suggested | A worthwhile further analysis or addition that would increase what the paper contributes. |
| CONTRIB.LEN | Contribution relative to length | The paper is too long, repetitive, or badly organized for what it contributes; material should be cut, merged, reordered, or moved to a supplement. |

## Writing Clarity and Organization *(parent)*

| Code | Entry | The referee asserts |
|:--|:--|:--|
| WRI.MECH | Mechanics and clarity | Typos, grammar, spelling, formatting, style, malapropisms, unclear prose, material that is present but explained unclearly, or numbers that differ between passages. |
| WRI.FIG | Figures, tables, or examples | Results should be shown more clearly through figures, tables, or examples. |
| WRI.TITLE | Title, abstract, and keywords | The title, abstract, or keywords do not accurately convey or index the study. Keywords added after batch 03. |
| WRI.TONE | Tone or terminology | Word choice or tone is inappropriate (not the misuse of a technical term). |

## Other dimensions

| Code | Entry | The referee asserts |
|:--|:--|:--|
| LIT | Incorporation of Relevant Literature | Prior literature is missing or mistreated, a citation is missing or inaccurate (failing to find and credit the work the paper builds on), or the findings are not compared with prior work. |
| SIL.PRAC | Implications for practice or policy | What the findings mean for practice, policy, or future research is not spelled out. |
| SIL.THEORY | Implications for theory | What the findings change in theory is not spelled out. |
| SIL.LIM | Limitations | Strengths and limitations are not stated clearly and frankly. |
| SIL.EXT | External validity | Whether the finding holds beyond the persons, settings, treatments, and outcomes studied is not addressed. |
| ORIG | Originality *(parent)* | The paper has not shown that it adds something new beyond what is known (novelty, originality, interestingness). |
| ORIG.BREADTH | Breadth of appeal | The work will interest too narrow an audience. |
| FIT | Relevance to Organization Science | The paper does not fit the journal it is submitted to. |
| FLAW | Flaws remediable in revision | The flaws cannot be remedied in a revision. |

## Dropped at the end of collection

Theories introduced inconsistently across sections (2 sightings, reports only) was still pending when collection stopped and is dropped as idiosyncratic under the stopping rule; its critiques are coded to THE.COH.

## Boundary rules

1. Code by the type of error the referee asserts, not by the part of the paper it concerns.
2. Misusing a technical term (for example, a statistical term for the wrong kind of test) is coded to that kind of error, not to Writing.
3. Something missing is MET.DISC.PROC; something present but explained unclearly is WRI.MECH.
4. "Claim lacks supporting citation" is LIT: it means failing to find and credit prior work.
5. If the evidence does not show the claim, code CON.SHOWN; if it shows the claim and a rival equally, code MET.INT.
6. A vague critique that says something is missing without naming it is coded by what the missing thing refers to, using its context in the report, and marked as inferred.
7. Do not force a critique into an entry that does not fit it. If nothing fits, code it NEW with a proposed label.
8. Code the substantive failure the referee asserts, read in context, not the rhetorical form of the complaint. "The limitations paragraph contradicts the argument for the sampling choice" is a failure of generalizability (SIL.EXT), not a contradiction (added after batch 04).
