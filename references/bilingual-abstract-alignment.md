# Bilingual Abstract Alignment

Use this reference when the author supplies both a Chinese and English abstract.
Compare propositions rather than sentence order.

## Alignment table

Check these dimensions:

| Dimension | What must align |
|---|---|
| Objective | question, population, exposure/intervention, comparator |
| Design | study type, setting, time window, data source |
| Sample | analysed N, groups, events, missingness |
| Methods | index test, model, endpoint definition, validation |
| Results | effect direction, magnitude, unit, interval, p value |
| Harms | adverse events and safety population when present |
| Limitations | main limitation and its direction |
| Conclusion | claim type and strength |

## Process

1. Segment each abstract into propositions.
2. Match propositions by meaning.
3. Mark each pair `aligned`, `missing`, `added`, or `different`.
4. Compare all numbers and qualifiers.
5. Propose the smallest correction that restores alignment.
6. Leave placeholders for facts absent from both versions.

## Common mismatches

- Chinese says “significant improvement”; English says “numerically higher”.
- English includes external validation absent from the Chinese.
- One version names a subgroup as exploratory; the other presents it as primary.
- Sample sizes differ because one uses randomized N and the other analysed N.
- One abstract reports a confidence interval and the other reports only p values.
- One conclusion says “associated”; the other says “effective”.
- The English adds a clinical recommendation not present in the study.

## Output

Use a compact table:

```text
维度 | 中文 | English | 判定 | 建议
```

Then provide:

```text
对齐后的中文摘要
aligned English abstract
```

Only rewrite when the author asks for corrected text. Otherwise deliver the
mismatch table and required decisions.
