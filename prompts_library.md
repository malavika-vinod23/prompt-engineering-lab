#  Prompt Engineering Lab — Prompts Library & Analysis

**Task:** E-commerce product description generation  
**Product:** SmartFit Pro X1 Smartwatch  
**Models tested:** GPT-4o, gpt-5.4, gpt-5.4-mini  
**Total evaluations:** 150 data points (10 prompts × 3 models × 5 dimensions)

---

#  Prompt Library Summary

| # | File | Technique | GPT-4o Avg | gpt-5.4 Avg | gpt-5.4-mini Avg |
|--|------|------------|------------|-------------|------------------|
| 01 | prompt_01_zeroshot.txt | Zero-shot | 2.6 | 2.6 | 2.6 |
| 02 | prompt_02_zeroshot_format.txt | Zero-shot + Format | 4.0 | 4.0 | 3.8 |
| 03 | prompt_03_oneshot.txt | One-shot | 4.0 | 4.0 | 4.0 |
| 04 | prompt_04_fewshot.txt | Few-shot | 4.0 | 4.0 | 4.0 |
| 05 | prompt_05_cot.txt | Chain-of-Thought | 3.0 | 3.0 | 2.8 |
| 06 | prompt_06_system_persona.txt | System Persona | 4.0 | 4.0 | 4.0 |
| 07 | prompt_07_role.txt | Role Prompting | 3.6 | 3.6 | 3.4 |
| 08 | prompt_08_role_fewshot.txt | Role + Few-shot | **5.0** | **5.0** | **4.8** |
| 09 | prompt_09_system_cot.txt | System + CoT | 3.8 | 3.8 | 3.6 |
| 10 | prompt_10_optimised.txt | Optimised Best-shot | **5.0** | **5.0** | **4.8** |

---

# A.  Model Comparison

All three models performed **almost identically** when given well-structured prompts.

The score gap between GPT-4o and gpt-5.4-mini was ≤ 0.2 across most prompts.

### Key Observation:
The only noticeable difference appeared in:
- Prompt 06 (System Persona)
- Prompt 10 (Optimised)

Here, gpt-5.4-mini showed slightly lower conciseness, occasionally exceeding word limits.

---

##  Key Insight

> Model capability is not the bottleneck — prompt design is.

---

##  Model Performance Summary

| Model | Avg Score | Avg Latency | Relative Cost |
|------|----------|--------------|---------------|
| GPT-4o | 3.90 | 1,815ms | 10× |
| gpt-5.4 | 3.90 | 1,308ms | 3× |
| gpt-5.4-mini | 3.78 | 769ms | 1× (baseline) |

---

# B.  Technique Effectiveness (Ranked)

| Rank | Technique | Avg Score | Insight |
|------|-----------|----------|--------|
|  1 | Role + Few-shot (P08) | 4.93 | Best balance of structure + tone |
|  1 | Optimised Best-shot (P10) | 4.93 | Equal performance, higher complexity |
| 3 | Zero-shot + Format (P02) | 3.93 | Format constraints improve clarity |
| 3 | One-shot (P03) | 3.93 | Single example is highly effective |
| 3 | Few-shot (P04) | 3.93 | Stable but marginal improvement |
| 3 | System Persona (P06) | 3.93 | Works well without examples |
| 7 | System + CoT (P09) | 3.73 | Adds reasoning but reduces conciseness |
| 8 | Role Prompting (P07) | 3.53 | Improves tone but lacks structure |
| 9 | Chain-of-Thought (P05) | 2.93 | Too verbose for creative writing |
| 10 | Zero-shot (P01) | 2.60 | No structure → weakest performance |

---

# C.  Cost–Quality Tradeoff

##  Is GPT-4o worth the premium?

**Answer: No — not for this task.**

### Key Findings:
- GPT-4o and gpt-5.4 have identical average scores (3.90)
- gpt-5.4-mini is only ~0.12 points lower
- But costs ~10× less than GPT-4o

---

##  Cost Comparison (per 1,000 outputs)

| Model | Estimated Cost |
|------|---------------|
| GPT-4o | ~$8.20 |
| gpt-5.4 | ~$4.10 |
| gpt-5.4-mini | ~$0.80 |

---

##  Conclusion

For production workloads:
> gpt-5.4-mini + good prompt engineering = best cost-performance balance

---

# D.  Failure Analysis (Top 3 Worst Cases)

---

## 1. gpt-5.4-mini × Prompt 01 (Zero-shot) — 2.6

**Issue:** No structure or constraints  
**Result:** Generic, low-quality marketing copy

 Insight: Small models depend heavily on prompt structure.

---

## 2. GPT-4o × Prompt 05 (Chain-of-Thought) — 3.0

**Issue:** CoT not suitable for creative writing  
**Result:** Verbose, analytical tone instead of marketing style

 Insight: CoT is better for reasoning tasks, not content generation.

---

## 3. gpt-5.4-mini × Prompt 07 (Role Prompting) — 3.4

**Issue:** Role without structure/examples  
**Result:** Long, inconsistent product descriptions

 Insight: Role prompts need format anchoring.

---

# E. 🚀 Production Recommendation

##  Best Setup to Ship:

> **gpt-5.4-mini + Prompt 08 (Role + Few-shot)**

---

##  Why this works best

| Factor | Result |
|------|--------|
| Quality | 4.8/5 (near frontier level) |
| Cost | ~10× cheaper than GPT-4o |
| Latency | ~769ms (production-safe) |
| Stability | Consistent outputs at temperature=0 |

---

## Why NOT Prompt 10?

- Same score as Prompt 08
- But:
  - More complex
  - Harder to maintain
  - Less modular

---

##  Final Insight

> The best systems are not the most complex prompts — but the most maintainable ones.

---

#  Scaling Strategy

- Store few-shot examples as reusable templates
- Update examples instead of rewriting full prompts
- Maintain prompt modularity across product categories

---
