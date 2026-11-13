# Claim and Evidence Boundary

Use this reference when a sentence may say more than the supplied evidence.
Calibrate the scientific claim before improving prose.

## Evidence-to-language map

| Evidence actually supplied | Defensible language | Avoid |
|---|---|---|
| Cross-sectional difference | was associated with; differed between groups | caused; led to; predicted future risk |
| Prospective association | was associated with subsequent outcome | demonstrated a causal effect |
| Discrimination | discriminated; AUC was; showed discrimination | improved outcomes; improved decisions |
| Diagnostic accuracy | sensitivity/specificity; positive/negative likelihood ratio | reduced mortality; improved treatment |
| Internal validation | internally validated; optimism-corrected | externally validated; universally applicable |
| External validation | externally validated in the named setting | generalizable everywhere |
| Calibration | agreement between predicted and observed risk | improved patient outcomes |
| Decision-curve analysis | net benefit under specified thresholds | proved clinical utility in practice |
| Animal experiment | animal model showed | established human efficacy |
| Mechanistic assay | supports a possible mechanism | proved the causal pathway |
| Exploratory subgroup | exploratory finding; hypothesis-generating | practice recommendation |
| Non-significant result | no evidence of a difference in this sample | proved equivalence |
| Missing source | unverified; source not supplied | unsupported as a final assertion |

## Review unit

For each material sentence, record:

```text
sentence:
claim_type:
supplied_evidence:
missing_evidence:
current_strength:
recommended_strength:
```

Focus on title, abstract, topic sentence, result interpretation, and conclusion.
Not every descriptive sentence needs this full record.

## Claim labels

- `supported`: the supplied evidence directly supports the stated scope.
- `partially_supported`: some subclaims or populations are unsupported.
- `indirect`: support requires a material inferential step.
- `unverified`: the necessary source or record was not supplied.
- `overstated`: wording exceeds the supplied evidence.

These labels describe the supplied package. They do not certify external truth.

## Rewrite patterns

### Association

Unsafe:

> Treatment X reduced mortality.

Safe:

> Treatment X was associated with lower mortality after adjustment for the listed
> covariates.

### Prediction

Unsafe:

> The model accurately predicted outcomes and can guide treatment.

Safe:

> The model showed discrimination in the development sample (AUC [value], 95% CI
> [range]); calibration and external validation were not supplied.

### Diagnostic accuracy

Unsafe:

> The test improved patient outcomes.

Safe:

> Against the prespecified reference standard, the test had sensitivity [value] and
> specificity [value] in [population].

### Animal-to-human inference

Unsafe:

> The drug is effective in patients.

Safe:

> In the [species/model], treatment reduced [endpoint]. Human efficacy was not
> evaluated in the supplied material.

## Citation support

A citation is not evidence that the sentence is supported. With supplied source
text, check:

1. population and setting;
2. intervention or exposure;
3. outcome and time horizon;
4. direction and magnitude;
5. study design;
6. uncertainty and limitations;
7. whether the cited passage supports the exact sentence.

When the source is not supplied, write `citation_support_unverified`. Do not
invent a quotation or a locator.

## Required output discipline

Lead with the strongest defensible version. Explain only the major changes.
List missing facts that could alter the conclusion. Never use “more research is
needed” as a replacement for naming the specific missing evidence.
