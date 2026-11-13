# Clinical Paragraph Writing Contract

Use this contract for a single clinical paragraph. It prevents language editing
from silently changing the research claim.

## 1. Identify the paragraph function

State the paragraph's job in one sentence:

- background and gap;
- objective;
- method;
- primary or secondary result;
- interpretation;
- comparison with prior work;
- limitation;
- conclusion;
- abstract summary.

If the paragraph contains several incompatible jobs, propose a split or move
only when that change remains within the author's requested scope.

## 2. Build the fact lock

Before rewriting, extract the following when present:

| Item | Examples |
|---|---|
| Population | adults aged 18-65 years; ICU admissions; internal validation cohort |
| Design | retrospective cohort; RCT; diagnostic accuracy study; animal experiment |
| Analysis set | intention-to-treat; per-protocol; complete-case; development cohort |
| Counts | 128 participants; 37 events; 14/96; 22.4% |
| Effect | HR 1.42; OR 0.78; mean difference 2.6; AUC 0.81 |
| Uncertainty | 95% CI 1.08-1.86; IQR; standard deviation; p value |
| Validation | apparent; internal; temporal; external |
| Citation | source number, author-year, quoted locator, supplied PDF |
| Claim status | association; prediction; diagnosis; causality; mechanism; utility |

Treat omissions as missing information. Do not deduce a denominator from a
percentage or a confidence interval from a p value.

## 3. Classify the main claim

Use the narrowest accurate category:

- descriptive;
- comparative;
- association;
- prediction or discrimination;
- diagnostic accuracy;
- causal;
- mechanistic;
- clinical utility;
- prognostic;
- exploratory or hypothesis-generating;
- recommendation.

Then check the verb. A study can support several claims at different strengths.
For example, a model may discriminate well but have no evidence of improved
clinical decisions.

## 4. Preserve the evidence boundary

Do not convert:

| Supplied evidence | Unsafe upgrade |
|---|---|
| cross-sectional association | predicts future outcomes |
| internal validation | externally validated |
| high AUC | improves clinical management |
| statistically significant | clinically important |
| single-centre finding | generalizable to all patients |
| exploratory subgroup | routine recommendation |
| no significant difference | proven equivalence |
| animal result | established human treatment |
| plausible mechanism | confirmed causal pathway |
| citation exists | citation supports this sentence |

If the evidence cannot support the requested wording, narrow the wording or
return `evidence-required`; do not hide the problem with a weaker adjective.

## 5. Revise in the smallest necessary unit

Preferred order:

1. correct the controlling claim;
2. restore the evidence-to-claim link;
3. remove irrelevant or duplicated material;
4. repair sentence subjects and verbs;
5. normalize terminology and punctuation.

Preserve the author's terminology, order of primary comparisons, and useful
technical detail. Avoid synonym rotation.

## 6. Final self-check

Before returning text, ask:

- Does every number retain its metric, denominator, population, and version?
- Did the revision add a citation, result, mechanism, or recommendation?
- Is the conclusion no stronger than the strongest supplied evidence?
- Did editing remove a limitation, negative finding, or uncertainty statement?
- Are Chinese and English versions making the same claim?
- Is any missing fact visible rather than invented?
