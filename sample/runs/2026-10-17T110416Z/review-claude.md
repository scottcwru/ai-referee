# Review by claude (claude-opus-5-5)

| Row | Rating |
|:--|:--|
| Importance of Problem | Satisfactory |
| Relevance to Organization Science | Satisfactory |
| Incorporation of Relevant Literature | Marginal |
| Development of Theory | Marginal |
| Appropriateness of Design | Poor |
| Appropriateness of Analysis and Interpretation | Poor |
| Legitimacy of Conclusions | Poor |
| Writing Clarity and Organization | Marginal |

**Recommendation:** Reject

## Confidential comments to the editor

The question is practically interesting: should founders put deal terms in pitch decks? Study 1's randomized design with real accelerator decks is a promising starting point. However, I do not think the manuscript is close to publishable, and I do not see a revision path that keeps the current central claim intact.

1. Study 2 cannot test the mechanism of the Study 1 effect. Study 1 manipulates presence versus absence of a deal slide. Study 2 manipulates only high versus low values, with no no-slide condition. Yet all of H2a–H2g are stated in terms of 'deal-term inclusion.'

2. The mediation results are internally inconsistent in sign. The a path is negative (−0.27) and the b paths are negative (−0.18 to −0.24). Their product should therefore be positive, but Table 12 reports negative indirect effects. A positive indirect effect would oppose the negative total association visible in Table 9, so 'full mediation' cannot hold as described.

3. The Discussion then concludes that disclosure reduces ambiguity and so increases favorability. This directly contradicts Study 1's main finding.

4. There are several further numerical inconsistencies:
- 88 × 12 = 1,056, minus 45 is not 1,008.
- In Table 2, the pooled Model 3 coefficient (−0.11) lies outside the range of the separate high/low coefficients in Table 6 (−.16, −.13).
- Tables 6 and 7 are mislabeled relative to the text.
- Success Odds has a mean of 1.72 in Table 9 despite being defined as a sum of four 0–100 probabilities.
- Mediators whose items share wording correlate near zero.

Taken together, I would encourage the editor to request the data and analysis code if the paper proceeds in any form.

Several key results are 'available upon request' rather than reported. Many in-text citations are missing from the reference list. My recommendation is reject. A substantially redesigned project might be suitable for resubmission: a placebo-slide control, a mediation design that includes the no-disclosure condition, and properly measured or manipulated mediators.

## Comments to the author

The manuscript asks whether founders should include quantitative deal terms (valuation, raise size, equity, committed capital) in startup pitch decks, and why such disclosure matters.

Study 1 randomly adds a deal-terms slide to twelve real accelerator decks evaluated by 88 investors. It reports that the slide lowers four measures of investor favorability, whether the terms are favorable or unfavorable to investors.

Study 2 uses 216 Prolific participants and manipulates high versus low deal-term values. It measures seven candidate mediators and concludes that perceived ambiguity alone fully mediates the effect.

The practical question is genuinely interesting, and I appreciate the use of real decks and random assignment in Study 1.

Unfortunately, I see fundamental problems that prevent me from recommending further consideration in the current form.

First, Study 2 does not include a no-disclosure condition. It therefore cannot speak to the mechanism behind the Study 1 inclusion effect.

Second, the reported mediation results are inconsistent in sign. Two negative paths are reported as producing a negative indirect effect. Read correctly, the ambiguity pathway would predict that disclosure increases favorability, which is the opposite of Study 1. The General Discussion in fact draws that opposite conclusion and recommends disclosure.

Third, the coding of 'high' terms reverses between studies. Study 2's own correlations show that term magnitude matters, which undercuts the claim that substantive attractiveness is irrelevant.

Fourth, Study 1 lacks a placebo-slide control, does not test whether the high and low coefficients differ, and contains several numerical inconsistencies.

Fifth, the mediator measures have serious validity problems, and the mediation claims rest on measured, not manipulated, mediators.

I also note gaps in transparency: key results are 'available upon request.' There are also problems with the reference list and the theoretical framing.

I detail these points below in the hope that they are useful for a redesigned version of the project.

1. **Study 2, Methods, p. 20; Hypotheses H2a–H2g, p. 19.** Study 2 compares only 'high' (1) versus 'low' (0) deal-term values. Every participant sees a deal-terms slide; there is no condition without one. Yet H2a–H2g (p. 19) are each stated as mediating 'the relationship between deal-term inclusion and investor favorability.' Because inclusion is never manipulated in Study 2, none of these hypotheses is actually tested.

The Study 1 effect (presence vs. absence) and the Study 2 effect (magnitude) are different causal contrasts. A mediator of one need not mediate the other. The paper's central claim cannot be supported by this design: that ambiguity explains why disclosure reduces favorability. To identify the mechanism of the Study 1 effect, Study 2 would need to include a no-slide control and estimate mediation on the inclusion contrast. Ideally, it would also manipulate the proposed mediator, for example by varying the clarity of the deal slide independently of its presence.
   > coded as 1 and 0, respectively
   *Rows: Appropriateness of Design, Legitimacy of Conclusions, Development of Theory*

2. **Study 2 Results, pp. 22–23; Tables 10, 11, and 12.** The reported indirect effects do not follow from the reported paths. Table 10 gives a = −0.27 for perceived ambiguity. Table 11 gives b = −0.21 (Success Odds), −0.24 (Good Business), −0.19 (Next Steps), and −0.18 (Share with Others). The product of two negative coefficients is positive (roughly +0.04 to +0.06). Table 12 instead reports −0.06, −0.07, −0.05, and −0.04, with confidence intervals entirely below zero. The same problem appears in Table 13.

Either the paths, the indirect effects, or the variable coding are misreported. In substantive terms, the reported paths say that the 'high' condition lowers ambiguity and that lower ambiguity raises favorability. That would make the indirect effect positive. Please re-estimate and report the a, b, c, and c' paths with consistent coding, and provide the analysis code.
   > Indirect effects were computed as the product of the a path (High vs. Low → Mediator)
   *Rows: Appropriateness of Analysis and Interpretation, Legitimacy of Conclusions*

3. **General Discussion, p. 25 and p. 28.** The Discussion's narrative contradicts Study 1. On p. 25 the paper states that quantitative disclosure reduced perceived ambiguity and that 'this reduction in perceived ambiguity, in turn, increased investors’ willingness to engage.' The conclusion on p. 28 advises founders to clarify terms to elicit more favorable responses. Study 1, however, finds that including the deal slide lowers favorability on every measure.

If disclosure lowers ambiguity and lower ambiguity raises favorability, then ambiguity is pushing against the observed effect rather than explaining it. The paper needs a single coherent account of the direction of each path and of the practical recommendation. As written, the recommendation to founders is the opposite of what Study 1 implies.
   > founders can frame their opportunities in a way that elicits more favorable and confident investor responses
   *Rows: Legitimacy of Conclusions, Development of Theory*

4. **Study 2 Results, p. 24; Table 9; Table 13.** No total effect (c) or direct effect (c') is reported for Study 2, so the claim of full mediation cannot be evaluated. Table 9 shows negative correlations between condition and the outcomes (−.09 to −.14). The reported a and b paths, however, imply a positive indirect effect (see critique 2).

This pattern is inconsistent mediation (suppression), not full mediation. If correct, it means another unmeasured process must account for the negative total association, and that process would be larger than the ambiguity pathway.

More generally, non-significance of c' is not evidence of full mediation. Please report c, c', and the proportion mediated with confidence intervals, for each outcome. For Table 13, please state which outcome the multiple-mediator model refers to.
   > was reduced to non-significance, confirming full mediation.
   *Rows: Appropriateness of Analysis and Interpretation, Legitimacy of Conclusions*

5. **Study 1 Methods, p. 9; Study 2 Methods, p. 20; Abstract.** The meaning of 'high' reverses between studies.
- In Study 1 (p. 9), 'favorable (i.e., high) and unfavorable (i.e., low)' versions are defined 'from the investor’s perspective.'
- In Study 2, 'high' denotes entrepreneur-favorable terms.

The two studies therefore cannot be compared on the magnitude dimension without clarification of what was actually shown.

Moreover, Table 9 shows that Study 2's magnitude manipulation itself lowers favorability (r = −.09 to −.14). That is, the substantive attractiveness of terms matters. This undercuts the Abstract's conclusion that transparency alters 'perceived informational clarity rather than the substantive attractiveness of the opportunity.'

In Study 1, the claim that favorability is irrelevant rests on both high and low coefficients being negative (Tables 5–8). The paper never formally tests whether they differ, and reports no manipulation check showing that investors perceived the 'favorable' terms as favorable. Please report the actual values used for each deck and condition, a test of equality of the high and low coefficients, and a manipulation check.
   > High values were intended to represent more aggressive, entrepreneur-favorable deal positions
   *Rows: Appropriateness of Design, Appropriateness of Analysis and Interpretation, Legitimacy of Conclusions*

6. **Study 1 Methods, pp. 8–9.** The treatment confounds deal-term content with the addition of any extra slide. Possible confounds include:
- a longer deck;
- a change in narrative flow;
- a slide that may look visibly inserted.

Without a placebo condition, such as an added neutral slide of equal length and visual style, one cannot attribute the effect to deal terms specifically.

In addition, one manipulated dimension is 'the amount already committed' (p. 9). This is traction or social-proof information rather than a deal term in the sense of the research question. A low committed amount plausibly signals weak investor interest.

The manuscript never shows an example of the deal slide, states where in the deck it was placed, or explains whether each slide displayed all four terms or only the manipulated one. Please provide the stimuli (e.g., in an online appendix) and discuss these alternative explanations.
   > however, we added a single slide within the deck
   *Rows: Appropriateness of Design, Legitimacy of Conclusions*

7. **Study 1 Results, pp. 11 and 13; Table 2 vs. Table 6; Table 7; Methods p. 8.** Several numbers in Study 1 do not reconcile.
- Sample size: 88 investors × 12 decks = 1,056, and 1,056 − 45 = 1,011, not the reported 1,008.
- Table 2, Model 3: the pooled treatment coefficient for Next Steps is −0.11. In Table 6, Model 3, the separate high and low coefficients are −.16 and −.13. A pooled estimate with the same controls should lie between the two subgroup estimates.
- Table 3 and Table 7: the pooled Good Business estimate is −.12, while the subgroup estimates are −.12 and −.09.
- Table and text mismatch: the text on p. 13 assigns Good Business to Table 6 and Next Steps to Table 7, but the table titles are reversed.

Please audit all Study 1 estimates against the underlying data and correct the tables.
   > Forty-five evaluations were not completed due to a software issue
   *Rows: Appropriateness of Analysis and Interpretation, Writing Clarity and Organization*

8. **Study 1 Results, pp. 10–13; Tables 1–8; Table 9.** The coefficients are reported as β and appear to be standardized. R-squared values are 0.01–0.02 for the treatment-only models. The reader therefore cannot judge whether the effects are 'substantive.'

Please report unstandardized effects in the original scale units (Likert points; percentage points of exit probability), along with standard errors and effect sizes.

The Success Odds variable is also unclear. On p. 10 it is defined as 'the sum of the probabilities' across four exit thresholds, each elicited on a 0–100 scale. In Table 9, however, it has a mean of 1.72 and SD of 0.84. Please explain the scaling.

Finally, summing probabilities of nested events (P(exit ≥ $50M) ≥ P(exit ≥ $100M) …) produces a quantity without a clear interpretation. Consider a more defensible summary or report the thresholds separately.
   > negative, substantive, and statistically significant
   *Rows: Appropriateness of Analysis and Interpretation*

9. **Study 2 Methods, p. 21; Appendix Table S1.** The mediator measures have serious validity problems.

1. The ambiguity items are about 'missing' or 'not fully spelled out' metrics. In Study 2, every condition displays the metrics; only their magnitude varies. It is unclear what these items capture there.

2. One ambiguity item reads 'Ambiguous information about this deck reduced my willingness to invest.' This embeds the outcome in the mediator, mechanically inflating the b path.

3. The loss aversion items (e.g., 'Avoiding losses matters more to me than achieving gains') largely measure a dispositional preference. A trait is not a plausible mediator of a within-subject manipulation.

4. The 'cognitive load' items (reliance on initial impressions, accepting information without scrutiny) measure heuristic processing rather than load.

5. On p. 21 the scales are described as 'brief validated scales,' but the items appear to be newly written adaptations. No validation evidence (factor structure, discriminant validity) is presented. No alpha is reported for loss aversion in the Table S1 note.

Please provide psychometric evidence, including a confirmatory factor analysis across all seven constructs. Please also explain how items referring to missing information apply to conditions in which nothing was missing.
   > For this deck, ambiguous or missing key metrics made me uneasy
   *Rows: Appropriateness of Design, Appropriateness of Analysis and Interpretation*

10. **Table 9; Appendix Table S1 (Decision avoidance items); Study 2 Methods pp. 21–22.** The decision-avoidance items use nearly the same wording as the ambiguity items ('missing or vague key metrics'). Yet Table 9 reports r = .10 between the two constructs. More broadly, all seven mediators show near-zero intercorrelations (mostly .01–.12). For conceptually overlapping self-reports collected from the same respondent about the same deck, this pattern is unusual. It warrants explanation and a check of the data processing.

The manuscript also does not report the order in which mediators and outcomes were measured. Measured mediators also leave the b path unidentified causally: any variable that affects both perceived ambiguity and favorability would generate the observed association.

Please report measurement order and the within- and between-person correlations separately (the data are multilevel). Please also discuss the sequential-ignorability assumption, or use a design that manipulates the mediator.
   > missing or vague key metrics made me want to delay
   *Rows: Appropriateness of Analysis and Interpretation, Appropriateness of Design, Legitimacy of Conclusions*

11. **Study 1 Methods p. 8; Study 2 Methods p. 20; General Discussion p. 27.** The samples do not support the description in the limitations section.
- Study 1 'investors' (mean age 28.1) needed only to have 'previously evaluated at least one early-stage startup.' Recruitment channels, investment history, and the investor-experience controls mentioned on p. 15 are not described.
- Study 2 uses Prolific participants screened only for 'previous exposure to entrepreneurial or investment decision-making.' These are not investors.

The mechanism is thus inferred in a population that differs substantially from the one in which the effect was found. The claim on p. 26 that the findings 'hold strongly in terms of ecological validity' is not warranted.

Please describe both samples in detail, and test whether the Study 1 effect replicates in the Study 2 population, and vice versa. Please also temper the generalizability claims.
   > with professional or semi-professional investors evaluating standardized pitch materials
   *Rows: Appropriateness of Design, Legitimacy of Conclusions*

12. **Footnotes 1, 2, and 4 (pp. 10, 12, 24); Study 2 Methods p. 22.** Substantial parts of the evidence are not reported:
- models with demographic controls (fn. 1);
- the dimension-specific and item-level robustness checks (fn. 2; pp. 13–14);
- the a and b path tables for non-supported mediators (fn. 4);
- the per-deal-factor mediation models described on p. 22 ('as were each of the four deal-factor contexts');
- the random-effects and outlier-exclusion analyses mentioned on pp. 14–15.

The manuscript also does not mention preregistration, power analysis, attention checks, exclusion criteria, or ethics approval. Given the journal's emphasis on methodological transparency, these results should appear in an online appendix, together with materials, data, and code.
   > Full statistical results for these models are available upon request.
   *Rows: Appropriateness of Analysis and Interpretation, Writing Clarity and Organization*

13. **Study 2 Conceptual Framework, pp. 15–19; Introduction p. 5.** The theoretical development is a list of seven mechanisms, each summarized in a paragraph, without signed predictions. It does not say which mechanism should predict lower versus higher favorability, nor how they could be discriminated.

The ambiguity account is especially underdeveloped. On pp. 15–16 the paper argues that quantitative information reduces ambiguity, which should raise favorability. But it offers no reason why ambiguity would explain a negative effect of disclosure, or why higher (entrepreneur-favorable) values would be less ambiguous than lower ones.

The construct also slips. The paper claims to pinpoint 'ambiguity aversion' (p. 5), which is an attitude toward imprecise probabilities. What it measures is perceived ambiguity of the deck, which is a different construct.

A stronger contribution would derive differentiated predictions across conditions (presence, magnitude, precision) that distinguish the mechanisms. It would also connect the account to theory on disclosure and information in entrepreneurial finance.
   > In this study, no a priori prediction is made as to which of the mechanisms will dominate.
   *Rows: Development of Theory*

14. **Introduction pp. 2–5; Study 1 Conceptual Framework p. 7; Study 2 p. 15; References.** The reference list is incomplete. Numerous in-text citations do not appear in the reference list, including:
- Florida & Kenney (1988)
- Roure et al. (1986)
- Gompers et al. (2020)
- Miloud et al. (2012)
- Obloj & Zenger (2017)
- Drover et al. (2018)
- Zacharakis & Shepherd (2001)
- Agarwal et al. (2025)
- Camuffo et al. (2020)
- Hallen & Piezunka (2023)
- Feld & Cohen (2019)
- Shane et al. (2020), the source of the 'validated' outcome scale
- Pitching Angels (2021)
- Szymanski (2021)

'Petty and Gruber, 2021' on p. 7 appears to be the 2011 article in the reference list.

Several citations are tangential to the claims they support. Examples include Cooper & Fang (2008) on auction overbidding (p. 15), Dai, Milkman & Riis (2014, 2015) on the fresh-start effect (pp. 5, 17), and Larkin (2014) on sales incentives (p. 17).

Meanwhile, directly relevant literatures are missing. These include work on first offers and price disclosure in negotiation (e.g., Galinsky & Mussweiler, 2001) and empirical work on how investors process valuation and term information. Engaging this work would sharpen the theory about why stating an ask might lower interest.
   > which should all increase investor favorability (Petty and Gruber, 2021)
   *Rows: Incorporation of Relevant Literature*

15. **Study 1 Results p. 11; Study 2 Methods p. 20; Introduction p. 4.** The writing needs careful editing.
- There are typos and a fragmentary sentence on p. 11.
- Table numbering does not match the text (Tables 6 and 7).
- Study 2 is described inconsistently. On p. 20, participants view 'versions of the same startup pitch,' yet the same paragraph says each 'evaluated 12 independent startup pitches.' It is unclear how many distinct decks were used and whether participants saw the same deck twice.
- The Introduction (p. 4) states that the effect 'is robust across startups, industries.' No industry-level analysis is reported.
- Results sections repeat the same sentence structure model by model. A compact table of treatment effects across outcomes and specifications would communicate the findings more clearly.
   > is randomly assiged that manipulation has a negative effect
   *Rows: Writing Clarity and Organization*

## References cited that the manuscript does not cite

- Galinsky, A. D., & Mussweiler, T. (2001). First offers as anchors: The role of perspective-taking and negotiator focus. Journal of Personality and Social Psychology, 81(4), 657–669. (critique 14)
