# Codebook, version 9

Built by build_codebook_v9.py from grader/codebook_v8.md, adding the entries decided on 2026-10-06 and a usual-category column (R rigor, C contribution, O other). The category is coded for each critique separately; the column is a guide, not a rule. Every change from v8 is marked “Added,” “Split,” “Moved,” or “proposed” in its row.

**About the usual-category column.** Each entry’s definition was read against the definition of rigor decided on 2026-10-06 (docs/decisions/2026-10-06-rigor-defined-by-subject.md) and assigned R, C, or O. Scott Shane confirmed the column as a whole on 2026-10-09, together with the rulings on the entries the definition did not settle (Falsifiability is rigor; Purpose of the research is contribution; Flaws remediable in revision is other). The values are a reading of the definitions, not coded data; no earlier document assigns categories to these entries (the rigor and contribution labels in step1_scholarly_literature.md, step2_journal_forms.md, and step5_skeleton.md sort source criteria, not entries, mostly under the falsity test that the October 6 decision replaced; the six rigor dimensions named in the proposal were replaced by the derived list).

The dimension list from step9_dimensions_v8.md, with a one-sentence definition for each place a critique can be coded, and the boundary rules Scott set (step7_meta_dimensions.md, step8_combined_dimensions.md). A critique is one sentence or group of consecutive sentences in a report that asserts one defect in the manuscript. Code each critique to the most specific entry that fits. An entry marked *(parent)* takes a critique only when none of its sub-dimensions fits.

## Methods *(parent)*

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| MET.DES | Appropriateness of Design *(parent)* | The design or the data cannot answer the research question, for a reason not listed below. | R |
| MET.DES.SAMP | Sample selection | How the sample (participants, cases, countries, studies, sources, journals) was chosen is unexplained, unjustified, or biased, or the sampling logic is misunderstood. When a study’s data are published literature, the literature search and the choice of journals are sample selection. | R |
| MET.ANA | Appropriateness of Analysis and Interpretation | The statistical analysis is wrong: the wrong analysis for the data or question, a model comparison that does not support the chosen model, inadequate power or sample size, a statistic misdescribed or misapplied (including a statistical term used for the wrong kind of test), an analytic choice or assumption not justified (transformations, thresholds, pooling), or the practical size of the effect not assessed. | R |
| MET.MEAS | Validity and reliability of measures *(parent)* | The study measures the phenomenon incorrectly, for a reason not listed below. | R |
| MET.MEAS.CON | Construct validity *(parent)* | The research operations do not represent the constructs they are claimed to represent (Shadish, Cook & Campbell: “inferences about the constructs that research operations represent”). | R |
| MET.MEAS.CON.MEAS | Construct validity of measures | A measure does not capture the construct it is named for, a claimed mechanism is never measured, or coding criteria are not shown to capture the concept. | R |
| MET.MEAS.CON.MANIP | Construct validity of manipulations | A manipulation, treatment, or proxy condition does not produce or represent the state it is meant to induce. Added after batch 02. | R |
| MET.MEAS.REL | Reliability | Reliability is unreported or low, including interrater reliability. | R |
| MET.MEAS.STATE | Participant state: order, practice, fatigue, or inattention | Participants’ order, practice, fatigue, or inattention distorts what is measured, including their behavior. | R |
| MET.MEAS.REACT | Reactive arrangements | Demand characteristics or social desirability distort participants’ responses. | R |
| MET.INT | Internal validity *(parent)* | A different explanation of the result cannot be ruled out, for a reason not listed below. | R |
| MET.INT.ALT | Alternative explanation or confound | A specific rival explanation, confound, or unobserved difference between units is not ruled out. | R |
| MET.INT.CAUSAL | Causal claim rests on a measured, not manipulated, variable | A causal claim is made from a variable that was measured rather than manipulated. | R |
| MET.PLAN | Analysis plan or model not specified | Model structure, parameters, a non-standard test, confirmatory versus exploratory analyses, or missing-data handling is not specified. | R |
| MET.ROB | Robustness | The result is not shown to survive other reasonable analytic choices (sensitivity analysis, researcher degrees of freedom, an artifact of a classification choice). | R |
| MET.DISC | Full disclosure *(parent)* | The paper does not report enough to see how the study was done or what it found, for a reason not listed below. | R |
| MET.DISC.PROC | Process or findings not described | A procedure, material, data source, or result is not reported in enough detail; data, code, or materials are unavailable or unusable; a referenced supplement or table is missing. | R |
| MET.DISC.PREREG | Preregistration | The study was not preregistered where it should have been, or its registration status or deviations from the registered plan are not transparent. | R |
| MET.DISC.ETH | Research ethics | Ethics approval or consent is not reported, or the research was not conducted ethically. | R |
| MET.QUAL | Qualitative methods *(parent)* | The qualitative procedure falls short of the standards for its method, for a reason not listed below. Added 2026-10-06. | R |
| MET.QUAL.DATA | Data structure (theme construction and interpretation) | Themes are not soundly built from the data: two themes are indistinguishable, a theme bundles unrelated content, or the path from codes to themes does not hold. Label: Gioia, Corley, and Hamilton (2013). | R |
| MET.QUAL.COH | Meaningful coherence (choice and fidelity of method) | The qualitative method is not justified for the question, or the study does not follow the method it claims (for example, it claims grounded theory or phenomenology but does not apply it). Label: Tracy (2010). | R |
| MET.QUAL.CRED | Credibility (trustworthiness strategies) | Steps that establish the trustworthiness of the analysis (member checking, triangulation, an audit trail, peer debriefing) were not taken or are inadequate. Label: Guba (1981); Tracy (2010). | R |
| MET.QUAL.SAT | Theoretical saturation | The sample is not shown to be sufficient, or a claim of saturation is not supported. Label: Eisenhardt (1989). | R |
| MET.QUAL.TRANS | Translation and transcription fidelity | Translation or transcription may not have preserved participants’ meaning, or how it did is not shown. Authors’ label. | R |
| MET.QUAL.REFLEX | Self-reflexivity | The researchers’ position and its influence on data collection and interpretation are not examined. Label: Tracy (2010). | R |

## Development of Theory *(parent)*

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| THE.GROUND | Theoretical grounding weak or narrow | The theory behind the hypotheses or mechanism is thin, narrow, weak, or never introduced. | C |
| THE.CONTRIB | Contribution to theory | The work does not test, create, or extend theory (a statement of importance about theory). | C |
| THE.UTIL | Utility of theory | The theory explains or predicts too little. | C |
| THE.COH | Consistency/Coherence of Conceptual Argument *(parent)* | The theoretical argument is not clear and logical. | R |
| THE.COH.ECO | Ecological validity | Realism: the theory or model rests on an assumption that is unrealistic for the agents or setting it describes, or the study’s setting or task lacks the real-world features the claims are about. Label from Scott; added after batch 04, widened to study settings after batch 05. | R |
| THE.COH.CONTRA | Internal contradictions | The theory says one thing (X causes Y) and another part of the paper says something incompatible (Y causes X, or X and Y are only correlated). | R |
| THE.LINK | Linkage between Conceptual Argument and Empirical Analysis | The hypotheses or the test do not follow from the argument, or an inductively built theory is not grounded in the data. | R |
| THE.FALS | Falsifiability | The paper states no research questions, hypotheses, or testable predictions. | R |
| THE.CONCEPT | Concept clarity | A theoretical concept is undefined, defined too narrowly or broadly, overlaps another concept, or is used in more than one sense. Authors’ label. Added 2026-10-06. | R |
| THE.UNIT | Unit or level of analysis | The argument or analysis treats its object at the wrong unit or level (for example, perspectives in the literature treated as kinds of real-world arrangement, or individual-level evidence used for claims about organizations). Authors’ label. Added 2026-10-06. | R |

## Research Questions and Goals *(parent)*

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| RQ.IMP | Importance of Problem | The paper does not argue why its question matters or how widely it applies. | C |
| RQ.FRAME | Framing of the argument | The way the paper sets up what it asks and why is wrong or unconvincing (distinct from positioning in the literature, which is Incorporation of Relevant Literature). Label from the proposal’s original list; added 2026-09-25. | C |
| RQ.PURP | Purpose of the research | What the study sets out to do (its aim, the gap it fills, its hypotheses, or its key concepts) is unclear. | C |

## Legitimacy of Conclusions *(parent)*

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| CON.SHOWN | Claim or conclusion not shown | A claim or conclusion is not shown by the evidence: never tested, tested without showing it, a difference claimed without a direct test, a result misread against its confidence interval, a generalization beyond the sample, or a conclusion about something never measured. | R |
| CON.ANOM | Anomalous or conflicting result not addressed | Part of the evidence cuts against the authors’ account and is left unexplained. | R |
| CON.UNDEV | Finding left undeveloped | The authors do not interpret what their own results show: an unexpected finding, a promised theme, or the plain reading of the results. | R |
| CON.NEUT | Neutrality | Results are presented selectively or as stronger or more settled than they are, or the findings reflect the investigator’s biases or interests. | R |
| CON.REPL | Replicability | The finding may not replicate. | R |
| CON.INCON | Reported results inconsistent | Numbers or facts differ between passages, tables, or figures, or a reported value is wrong on its face (for example, an impossible unit). Moved from Mechanics and clarity; proposed 2026-10-07. | R |

## Overall contribution *(parent)*

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| CONTRIB | Overall contribution *(parent)* | The paper adds too little to knowledge, for a reason not listed below. | C |
| CONTRIB.EXT | Extension suggested | A worthwhile further analysis or addition that would increase what the paper contributes. | C |
| CONTRIB.LEN | Contribution relative to length | The paper is too long, repetitive, or badly organized for what it contributes; material should be cut, merged, reordered, or moved to a supplement. | O |

## Writing Clarity and Organization *(parent)*

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| WRI.MECH | Mechanics and clarity | Typos, grammar, spelling, formatting, style, malapropisms, unclear prose, material that is present but explained unclearly. (Numbers that differ between passages move to CON.INCON.) | O |
| WRI.FIG | Figures, tables, or examples | Results should be shown more clearly through figures, tables, or examples. | O |
| WRI.TITLE | Title, abstract, and keywords | The title, abstract, or keywords do not convey or index the study well. A title or abstract that states something the study did not do or does not show is CON.SHOWN. Keywords added after batch 03. | O |
| WRI.TONE | Tone or terminology | Word choice or tone is inappropriate (not the misuse of a technical term). | O |

## Other dimensions

| Code | Entry | The referee asserts | Usual category |
|:--|:--|:--|:--|
| LIT | Incorporation of Relevant Literature *(parent)* | Prior literature is missing or mistreated, a citation is missing or inaccurate (failing to find and credit the work the paper builds on), or the findings are not compared with prior work. | — |
| LIT.SRC | Literature: a source is misrepresented | A cited source does not say what the paper says it says, or prior findings are reported inaccurately. Split from LIT 2026-10-06. | R |
| LIT.POS | Literature: positioning and coverage | Relevant prior work is missing, the paper is not positioned against it, or the findings are not compared with it. Split from LIT 2026-10-06. | C |
| SIL.PRAC | Implications for practice or policy | What the findings mean for practice, policy, or future research is not spelled out. | C |
| SIL.THEORY | Implications for theory | What the findings change in theory is not spelled out. | C |
| SIL.LIM | Limitations | Strengths and limitations are not stated clearly and frankly. | R |
| SIL.EXT | External validity | Whether the finding holds beyond the persons, settings, treatments, and outcomes studied is not addressed. | R |
| ORIG | Originality *(parent)* | The paper has not shown that it adds something new beyond what is known (novelty, originality, interestingness). | C |
| ORIG.BREADTH | Breadth of appeal | The work will interest too narrow an audience. | C |
| FIT | Relevance to Organization Science | The paper does not fit the journal it is submitted to. | C |
| FLAW | Flaws remediable in revision | The flaws cannot be remedied in a revision. | O |

## Dropped at the end of collection

Theories introduced inconsistently across sections (2 sightings, reports only) was still pending when collection stopped and is dropped as idiosyncratic under the stopping rule; its critiques are coded to THE.COH.

## Boundary rules

1. Code by the type of error the referee asserts, not by the part of the paper it concerns.
2. Misusing a technical term (for example, a statistical term for the wrong kind of test) is coded to that kind of error, not to Writing.
3. Something missing is MET.DISC.PROC; something present but explained unclearly is WRI.MECH.
4. “Claim lacks supporting citation” is CON.SHOWN: an unsupported claim (rigor). Ruled 2026-10-09.
5. If the evidence does not show the claim, code CON.SHOWN; if it shows the claim and a rival equally, code MET.INT.
6. A vague critique that says something is missing without naming it is coded by what the missing thing refers to, using its context in the report, and marked as inferred.
7. Do not force a critique into an entry that does not fit it. If nothing fits, code it NEW with a proposed label.
8. Code the substantive failure the referee asserts, read in context, not the rhetorical form of the complaint. “The limitations paragraph contradicts the argument for the sampling choice” is a failure of generalizability (SIL.EXT), not a contradiction (added after batch 04).
9. A qualitative step that is *not reported* is MET.DISC.PROC; a step that was *not taken or was done badly* goes to the MET.QUAL entry for it. Added 2026-10-07.
