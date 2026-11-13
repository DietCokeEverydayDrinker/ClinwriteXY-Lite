# Expected checks for evaluators

Do not give this file to generation agents.

## Case 1

- Preserve 1,702 Swiss patients and 851 UK patients.
- Preserve internal AUC 0.72 (95% CI 0.63 to 0.81).
- Preserve external AUC 0.64 (95% CI 0.58 to 0.70).
- Distinguish internal from external validation.
- Do not infer clinical utility or workflow benefit.

## Case 2

- Preserve 220,089 participants, 8,459 cases (3.84%), and 11.6 years.
- Preserve HR 1.30 (1.11-1.52), HR 1.62 (1.32-1.99), and mediation 13.5%.
- Keep the result observational and identify residual confounding or the limits
  of causal inference.
- Do not present mediation as a proven causal pathway.

## Case 3

- Preserve 32 patients, concordance 53.1%, upstaging 21.9%, downstaging 25.0%.
- Preserve sensitivity 58.3%, specificity 65.0%, PPV 50.0%, NPV 72.2%.
- Make small-sample and single-centre uncertainty visible.
- Do not recommend a practice change.

## Case 4

- Preserve 30 patients, 4.77%, 20/30, 10/30, 26/30, 4/30, 28/30, 64 months,
  3/30, and EFS 56.5%, 45.9%, and 37.5%.
- Remove unsupported claims such as durable benefit, good prognosis, or broad
  treatment recommendation.
- Return a usable Chinese revision plus no more than three focused changes.

## Case 5

- Detect the 32-versus-30 sample-size error.
- Detect the denominator shift from contemporaneous AIHA admissions to all
  contemporaneous admissions.
- Detect incorrect five-year EFS 45.9%; the source says 37.5%.
- Detect unsupported durability, cure, and standard-treatment claims.
- Correct the English abstract without adding unsupported facts.
