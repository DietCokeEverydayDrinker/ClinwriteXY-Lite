# Bilingual Abstract Alignment: Synthetic Example

## Chinese

> 共随机分配120例患者，最终纳入分析118例。主要终点为12个月无进展生存期。
> 干预组无进展生存期较对照组延长（HR 0.71，95% CI 0.55-0.92）。研究未进行
> 外部验证。

## English

> A total of 120 patients were analysed. The primary endpoint was overall survival
> at 24 months. Overall survival was improved in the intervention group
> (HR 0.71, 95% CI 0.55-0.92). The findings were externally validated.

## Alignment findings

| Dimension | Chinese | English | Finding |
|---|---|---|---|
| Sample | randomized 120; analysed 118 | 120 analysed | Different |
| Endpoint | PFS at 12 months | OS at 24 months | Different |
| Effect | PFS prolongation | OS improvement | Different |
| Validation | no external validation | externally validated | Different |
| Estimate | HR 0.71, 95% CI 0.55-0.92 | HR 0.71, 95% CI 0.55-0.92 | Aligned |

## Required author decisions

1. Confirm the randomized and analysed sample sizes.
2. Confirm the primary endpoint and time horizon.
3. Confirm whether the reported HR refers to PFS or OS.
4. Delete the external-validation statement unless a valid source supports it.

The HR and confidence interval remain unchanged. No endpoint or validation result
should be selected from plausibility.
