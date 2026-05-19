# Prompt Engineering Lab — Prompts Library & Analysis

## Task
E-commerce product description generation

**Product:** SmartFit Pro X1 Smartwatch  
**Models tested:** GPT-4o, gpt-5.4, gpt-5.4-mini  
**Total evaluations:** 150 data points (10 prompts × 3 models × 5 dimensions)

---

## A. Prompt Library Results

| #  | File                          | Technique            | GPT-4o | gpt-5.4 | gpt-5.4-mini |
|----|------------------------------|---------------------|--------|----------|--------------|
| 01 | prompt_01_zeroshot.txt       | Zero-shot           | 4.4    | 3.2      | 3.0          |
| 02 | prompt_02_zeroshot_format.txt| Zero-shot + Format  | 4.8    | 4.8      | 4.8          |
| 03 | prompt_03_oneshot.txt        | One-shot            | 5.0    | 5.0      | 5.0          |
| 04 | prompt_04_fewshot.txt        | Few-shot            | 5.0    | 5.0      | 5.0          |
| 05 | prompt_05_cot.txt            | Chain-of-Thought    | 4.8    | 4.8      | 4.8          |
| 06 | prompt_06_system_persona.txt | System Persona      | 4.8    | 4.8      | 5.0          |
| 07 | prompt_07_role.txt           | Role Prompting      | 4.6    | 4.6      | 4.8          |
| 08 | prompt_08_role_fewshot.txt   | Role + Few-shot     | 5.0    | 5.0      | 5.0          |
| 09 | prompt_09_system_cot.txt     | System + CoT        | 4.6    | 4.8      | 4.8          |
| 10 | prompt_10_optimised.txt      | Optimised Best-shot | 4.6    | 4.8      | 5.0          |

---

## B. Model Comparison

GPT-4o performs strongest in zero-shot (4.4 vs 3.2 for gpt-5.4 and 3.0 for gpt-5.4-mini), but this advantage disappears with structured prompting.

Across prompts 02–10, model performance converges tightly:

- GPT-4o and gpt-5.4 are nearly identical (≤ 0.2 difference)
- gpt-5.4-mini matches or exceeds both in multiple cases (06, 10)

Key insight: prompt design has a stronger impact than model choice for this task.

---

### Model Summary

| Model | Avg Score | Avg Latency | Relative Cost |
|------|----------|-------------|---------------|
| GPT-4o | 4.76 | 5093 ms | 10× |
| gpt-5.4 | 4.68 | 4215 ms | 3× |
| gpt-5.4-mini | 4.72 | 2229 ms | 1× |

---

## C. Technique Effectiveness

Ranked by average score across models:

### 1. One-shot (Prompt 03) — 5.00
Perfect scores across all models. A single strong example anchors format and tone effectively.

### 2. Few-shot (Prompt 04) — 5.00
Multiple examples reinforce structure and consistency.

### 3. Role + Few-shot (Prompt 08) — 5.00
Combines persona guidance with examples for maximum stability.

### 4. System Persona (Prompt 06) — 4.87
Strong control over tone and structure with minor variance.

### 5. Chain-of-Thought (Prompt 05) — 4.80
Works well due to structured output constraints preventing verbosity.

### 6. Zero-shot + Format (Prompt 02) — 4.80
Formatting alone significantly improves output quality.

### 7. Optimised Best-shot (Prompt 10) — 4.80
Strong overall but slightly lower factual accuracy in GPT-4o.

### 8. System + CoT (Prompt 09) — 4.73
Slight verbosity reduces conciseness score.

### 9. Role Prompting (Prompt 07) — 4.67
Good structure but weaker conciseness.

### 10. Zero-shot (Prompt 01) — 3.53
Worst performing setup due to lack of structure.

---

## D. Cost–Quality Tradeoff

### Is GPT-4o worth the premium?

No.

- gpt-5.4-mini average: 4.72  
- GPT-4o average: 4.76  
- Difference: negligible (0.04)

However:
- gpt-5.4-mini is significantly cheaper
- gpt-5.4-mini is faster (~2.3× vs GPT-4o)

Conclusion: model differences are minimal under good prompting.

---

### Estimated Cost per 1,000 Outputs

| Model | Cost |
|------|------|
| GPT-4o | ~$8.20 |
| gpt-5.4 | ~$4.10 |
| gpt-5.4-mini | ~$0.80 |

---

## E. Failure Analysis

### 1. gpt-5.4-mini × Prompt 01 (Zero-shot)
Score: 3.0

Failure due to missing structure. Output included irrelevant expansions and weak instruction adherence.

### 2. gpt-5.4 × Prompt 01 (Zero-shot)
Score: 3.2

Generated structured-looking markdown without following required format.

### 3. GPT-4o × Prompt 10 (Optimised)
Score: 4.6

Minor factual inconsistency due to slight over-generation.

---

## F. Production Recommendation

### Recommended Setup

**Model:** gpt-5.4-mini  
**Prompt:** Prompt 08 (Role + Few-shot)

### Reasoning

| Factor | Result |
|--------|--------|
| Quality | 5.0 average |
| Cost | Lowest |
| Latency | Fastest |
| Consistency | High |
| Maintainability | High |

---

### Secondary Options

- Prompt 03 (One-shot): best for compact prompts
- Prompt 04 (Few-shot): best for structured control

---

## G. Scaling Strategy

- Store few-shot examples as reusable templates
- Swap examples per product category
- Avoid rewriting full prompts for new products
- Maintain a single prompt framework for production consistency
