# Chinese Clinical Micro-Edit

Use this reference for Chinese medical abstracts, results, discussion, limitations,
and conclusions. The goal is clear academic Chinese with stable terminology and
visible evidence boundaries.

## Intervention levels

| Level | Allowed work | Avoid |
|---|---|---|
| Proofread | punctuation, characters, units, terminology | changing structure or claim |
| Light edit | split sentences, remove redundancy, restore subjects | changing paragraph order |
| Medium edit | reorganize within the paragraph, merge repetition | adding evidence or conclusions |
| Deep rewrite | rebuild the paragraph's controlling logic | changing the study without permission |

“润色” defaults to light-to-medium editing. Escalate only when the paragraph's
logic prevents a safe local edit.

## High-value repairs

### Long attributive chain

Put the study type and action before a long list of participant conditions.

Before:

> 一项在多个中心开展的针对接受标准治疗后仍有持续症状且符合预设纳入标准的成年患者的前瞻性研究显示……

After:

> 这项多中心前瞻性研究纳入接受标准治疗后仍有持续症状、并符合预设标准的成年患者。结果显示……

### Abstract subject

Replace empty process nouns with the data, analysis, or decision that performs the
action when that actor is supported by the source.

Before:

> 相关分析工作的开展使结论可靠性得到进一步提升。

After:

> 敏感性分析显示，主要估计方向未随预设模型改变。

The second version is usable only when the source actually reports that result.

### Noun stacking

Restore the verb when it clarifies the action:

- 对数据进行分析 -> 分析数据
- 对结果进行比较 -> 比较结果
- 实现准确率的提升 -> 准确率由 A 升至 B
- 开展风险评估 -> 评估风险

Keep established technical nouns when changing them would reduce precision.

### Empty evaluation

Delete the evaluation and expose the fact. If no fact remains, request evidence.

| Empty phrase | Ask instead |
|---|---|
| 具有重要意义 | Which decision, population, or uncertainty changes? |
| 提供了新思路 | What is new relative to the named comparator? |
| 具有广阔前景 | Which application and what evidence is still missing? |
| 填补了空白 | Which specific gap, and how far does this study close it? |
| 为临床诊疗提供了依据 | Which patients and which clinical decision? |

### False transitions

Use a connector only when the relation is real:

- 因此: the preceding text supplies a reason;
- 然而: a genuine contrast exists;
- 此外: the new information advances the same point;
- 值得注意的是: the statement changes interpretation or risk;
- 综上所述: the paragraph actually synthesizes more than the prior sentence.

Remove repeated sentence-opening frames and let explicit subjects, comparisons, and
sequence carry the logic.

### Claim-strength language

Avoid vague upgrades such as:

- 显著改善 when only statistical significance is known;
- 准确预测 when only association is available;
- 证实 when the design supports suggestion;
- 普遍适用 after one centre;
- 临床价值明确 after discrimination alone;
- 安全有效 without comparative safety and outcome evidence.

Do not replace every strong claim with “可能”. State the source of uncertainty:
sample size, design, validation, measurement, or missing comparison.

## Final readability test

Read the paragraph as a clinician who has not seen the analysis. Check whether:

- the study and population are identifiable;
- the main result appears before secondary detail;
- every comparison has an explicit comparator;
- percentages have a denominator;
- the final sentence answers the paragraph's question;
- the conclusion can be defended without reading omitted material.
