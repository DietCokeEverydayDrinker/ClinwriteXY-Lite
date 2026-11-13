---
name: clinwritexy-lite
description: Write or revise one Chinese or English clinical research paragraph with evidence-boundary checks. Use for abstracts, results, discussion, conclusions, or bilingual abstract alignment when numbers, denominators, citations, qualifiers, validation level, and claim strength must be preserved. Excludes full theses, whole-manuscript audits, live literature search, statistics, project management, reviewer responses, and document formatting.
metadata:
  short-description: Focused clinical paragraph writing and claim checks
---

# ClinwriteXY Lite

Improve one clinical research paragraph without changing the evidence behind it.
Deliver useful revised prose first, then a compact record of what changed and
what still needs author verification.

## Scope gate

Lite handles:

- one Chinese or English abstract, results, discussion, limitation, or conclusion
  paragraph;
- one paragraph drafted from author-supplied facts or analysis output;
- one Chinese-English abstract pair checked for factual and claim alignment;
- a focused claim-strength review of supplied text.

Typical limits are 800 Chinese characters or 500 English words per paragraph.
For a longer passage, process it paragraph by paragraph only when the user asks.
For a full thesis, whole manuscript, literature review, reviewer response, or
cross-file audit, state that the request is outside Lite scope and offer a
paragraph-level contribution instead.

Do not turn every request into an intake interview. Ask only for information
that can change the answer.

## Route by task

| Request | Read before editing |
|---|---|
| Revise or draft a clinical paragraph | [references/clinical-writing-contract.md](references/clinical-writing-contract.md) |
| Chinese prose feels templated, vague, or translation-like | [references/zh-clinical-micro-edit.md](references/zh-clinical-micro-edit.md) |
| The claim may be stronger than the evidence | [references/claim-and-evidence-boundary.md](references/claim-and-evidence-boundary.md) |
| Compare a Chinese and English abstract | [references/bilingual-abstract-alignment.md](references/bilingual-abstract-alignment.md) |

Load only the files needed for the current request.

## Workflow

### 1. Freeze the evidence

Identify what cannot change:

- study design, setting, population, and time window;
- sample size, events, denominators, missingness, and analysis set;
- effect direction, magnitude, unit, confidence interval, and decimal precision;
- citation positions and the source meaning;
- primary, secondary, and exploratory labels;
- internal, temporal, or external validation status;
- association, prediction, diagnostic accuracy, clinical utility, mechanism, and
  causal status;
- negative findings, uncertainty, limitations, and conclusion strength;
- ethics, registration, funding, and data-availability facts.

If the supplied material does not establish one of these items, leave an explicit
placeholder or name the missing fact. Do not fill it from plausibility.

### 2. Diagnose before polishing

Check the paragraph's controlling point, evidence, boundary, and link to the
requested section. Then inspect sentence-level language. Fluent wording cannot
repair a missing denominator, unsupported citation, or inflated claim.

Use these working labels when useful:

- `preserved`: retained without a material change;
- `clarified`: wording changed, meaning retained;
- `narrowed`: scope or strength reduced to match evidence;
- `evidence-required`: a source or fact is missing;
- `claim-changing`: the requested edit would alter the scientific claim.

### 3. Produce the requested text

For drafting, write only from supplied facts and analysis output.

For editing, preserve the author's language unless a change improves clarity,
consistency, or claim calibration. Keep terminology stable. Do not add citations,
study details, mechanisms, results, or clinical recommendations.

If the author asks only for review, do not rewrite unless they also request a
candidate text.

### 4. Run a preservation check

Compare the original and revised passage for numeric and citation-token changes.
When the local script is available, run:

```text
python <SKILL_ROOT>/scripts/check_preservation.py <original.txt> <revised.txt>
```

The script is a diagnostic. Inspect every reported difference in context.
No script can determine whether a citation semantically supports a sentence.

### 5. Return a compact result

Use this structure unless the author requests another format:

```text
修改后
[candidate text]

主要修改
- [maximum 3 concise points]

保真记录
- 数字与分母：
- 引用与限定词：
- 结论强度：

仍需补充
- [only unresolved facts that could change the result; write “无” when none]
```

For a draft request, replace `修改后` with `起草结果`.

For a review-only request, replace `修改后` with `主要问题` and list located
findings. Do not fabricate a revised paragraph the author did not request.

When the request is a direct drafting task and no unresolved fact could change
the result, keep the record shorter: give the draft first and one compact
`保真记录` line covering numbers, citations, and claim strength. Do not add an
empty section merely to match the template.

## Language rules

### Chinese

Prefer concrete actors, actions, data, and comparisons. Remove empty evaluation
and mechanical transitions only after confirming the underlying relation.
Preserve useful technical nouns and established terminology.

### English

Match tense and verb strength to the evidence. Use hedging to describe a real
source of uncertainty, not as decoration. Preserve population qualifiers,
confidence intervals, and validation labels.

### Bilingual abstracts

Compare the two texts by proposition, not by sentence shape. The English text may
use a different sentence order while remaining aligned. Report any mismatch in
sample size, endpoint, effect direction, validation, or conclusion strength.

## Hard boundaries

- Do not search the live literature, verify a DOI, or claim a citation exists
  unless a search tool was actually used.
- Do not infer clinical utility from discrimination, statistical significance,
  biological plausibility, or animal evidence.
- Do not invent ethics approval, registration, funding, authors, results, or
  study procedures.
- Do not provide patient-specific diagnosis or treatment advice.
- Do not claim to evade AI detectors or guarantee publication, acceptance, or
  thesis approval.
- Do not modify tracked changes, comments, fields, tables of contents, or complex
  Word layout. Hand those tasks to a document tool or Word/WPS.
- Do not treat the preservation script as proof of scientific correctness.

## Privacy

Use only the minimum text needed for the task. Do not ask for patient identifiers,
private institutional documents, credentials, or unpublished data that the user
has not chosen to provide. Public examples must remain synthetic.
