# ClinwriteXY Lite evaluation cases

These cases use short, attributed excerpts or factual summaries from open-access
clinical papers. They contain no patient identifiers, institutional credentials,
or unpublished project material.

All comparison arms receive the case text and task prompt exactly as written.
Do not add literature, citations, results, study procedures, or clinical advice
that is absent from the case.

---

## Case 1: External validation and clinical use

Source: Open Heart, 2026. DOI: 10.1136/openhrt-2026-004304.
Open-access cohort: 1,702 patients in Switzerland for model development and
internal validation; 851 patients in the UK for external validation.

Reported findings:

- Internal-validation AUC: 0.72 (95% CI 0.63 to 0.81).
- External-validation AUC: 0.64 (95% CI 0.58 to 0.70).
- Calibration was assessed.
- No decision-curve, workflow-impact, or randomized clinical-utility study is
  reported in the abstract.
- The authors describe the model as having potential for clinical application.

Task prompt:

> Write one English Discussion paragraph of 120-160 words for a clinical
> journal. Explain what the internal and external validation results support,
> and end with a defensible statement about clinical use. Preserve all reported
> numbers and validation labels. Do not add citations or results that are not
> supplied.

---

## Case 2: Observational association and mediation

Source: UK Biobank analysis of sleep patterns, metabolic signatures, and breast
cancer risk, 2026. PMCID: PMC13716583.

Reported findings:

- 220,089 participants.
- 8,459 incident breast cancer cases (3.84%).
- Median follow-up: 11.6 years.
- Sleep score 0-1 versus 5: HR 1.30 (95% CI 1.11-1.52).
- Metabolic signature: HR 1.62 (95% CI 1.32-1.99).
- The metabolic signature mediated 13.5% of the observed association.
- This was an observational cohort analysis.

Task prompt:

> Draft one English Discussion paragraph of 120-160 words for a general medical
> journal. State the association, mediation result, and the most important
> limitation. Keep the language proportionate to observational evidence. Do not
> add citations, mechanisms, or causal claims that are not supplied.

---

## Case 3: Small diagnostic-accuracy study

Source: retrospective single-centre study of preoperative MRI for endometrial
carcinoma staging. PMCID: PMC13676447.

Reported findings:

- 32 consecutive patients.
- Overall staging concordance: 53.1%.
- Upstaging: 21.9%; downstaging: 25.0%.
- Myometrial invasion: sensitivity 58.3%, specificity 65.0%, PPV 50.0%, NPV
  72.2%.
- The study was retrospective and conducted at one centre.

Task prompt:

> Write one English Results paragraph and one concluding sentence for a clinical
> journal. Report the diagnostic estimates accurately, make the uncertainty
> created by the sample size and design visible, and avoid recommending a change
> in clinical practice. Preserve all supplied values.

---

## Case 4: Chinese clinical micro-edit

Source facts: single-centre retrospective cohort of 30 patients with direct
antiglobulin test-negative autoimmune haemolytic anaemia. PMCID: PMC13669443.

Exact source facts that must be preserved:

- 30 patients; 4.77% of contemporaneous AIHA admissions.
- Female 20/30 (66.7%); male 10/30 (33.3%).
- Primary disease 26/30 (86.7%); secondary disease 4/30 (13.3%).
- First-line glucocorticoid overall response: 93.3% (28/30).
- Median follow-up: 64 months.
- All-cause mortality: 10.0% (3/30).
- One-, three-, and five-year EFS: 56.5%, 45.9%, and 37.5%.

Draft to revise:

> 本研究全面揭示了DAT阴性AIHA的临床特征与治疗结局。研究共纳入30例患者，
> 占同期AIHA住院病例的4.77%。其中女性20例（66.7%），男性10例（33.3%）。
> 一线糖皮质激素总缓解率高达93.3%（28/30），说明该方案能够为绝大多数患者
> 带来显著且持久的获益。中位随访64个月，全因死亡率为10.0%（3/30），1年、
> 3年和5年EFS率分别为56.5%、45.9%和37.5%。上述结果充分证明DAT阴性AIHA
> 患者预后良好，应广泛采用糖皮质激素治疗。

Task prompt:

> 请按中文临床论文的表达习惯修改这段文字。保留全部数字、分母、随访时间和
> 结局指标，不增加研究未提供的结果。减少模板腔和空泛评价，说明现有证据能够
> 支持到什么程度。先给修改稿，再用不超过3条列出主要修改。

---

## Case 5: Bilingual abstract alignment

Use the source facts from Case 4.

Flawed English abstract excerpt:

> This study enrolled 32 patients with DAT-negative AIHA, accounting for 4.77% of
> contemporaneous admissions. Female patients comprised 66.7%. First-line
> glucocorticoids achieved an overall response in 93.3% of patients, and all
> responses were durable. After a median follow-up of 64 months, all-cause
> mortality was 10.0%. The five-year event-free survival rate was 45.9%. These
> findings demonstrate that glucocorticoids cure most patients and should be the
> standard treatment for this subtype.

Task prompt:

> Compare this English abstract with the Chinese source facts. Identify every
> material mismatch in sample size, denominator, endpoint, result, or claim
> strength, then provide a corrected English version. Do not add citations or
> infer outcomes that were not reported.
