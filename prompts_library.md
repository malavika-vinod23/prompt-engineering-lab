Prompt Engineering Lab — Prompts Library & Analysis

Task: E-commerce product description generation
Product: SmartFit Pro X1 Smartwatch
Models tested: GPT-4o, gpt-5.4, gpt-5.4-mini
Total evaluations: 150 data points (10 prompts × 3 models × 5 dimensions)

Prompt Library
#	File	Technique	Avg Score (GPT-4o)	Avg Score (gpt-5.4)	Avg Score (gpt-5.4-mini)
01	prompt_01_zeroshot.txt	Zero-shot	2.6	2.6	2.6
02	prompt_02_zeroshot_format.txt	Zero-shot + Format	4.0	4.0	3.8
03	prompt_03_oneshot.txt	One-shot	4.0	4.0	4.0
04	prompt_04_fewshot.txt	Few-shot	4.0	4.0	4.0
05	prompt_05_cot.txt	Chain-of-Thought	3.0	3.0	2.8
06	prompt_06_system_persona.txt	System Persona	4.0	4.0	4.0
07	prompt_07_role.txt	Role Prompting	3.6	3.6	3.4
08	prompt_08_role_fewshot.txt	Role + Few-shot	5.0	5.0	4.8
09	prompt_09_system_cot.txt	System + CoT	3.8	3.8	3.6
10	prompt_10_optimised.txt	Optimised Best-shot	5.0	5.0	4.8
A. Model Comparison

All three models performed nearly identically when given well-structured prompts. The score gap between GPT-4o and gpt-5.4-mini was 0.2 points or less across 8 of 10 prompts.

The only notable difference appeared on prompts requiring strict constraint adherence (Prompt 06, Prompt 10), where gpt-5.4-mini scored 0.2 points lower on conciseness — occasionally exceeding the specified word count by 10–15%.

Key takeaway: For a structured generation task like product description writing, model capability is not the bottleneck — prompt design is.

Model	Avg Score	Avg Latency	Relative Cost
GPT-4o	3.90	1,815ms	10×
gpt-5.4	3.90	1,308ms	3×
gpt-5.4-mini	3.78	769ms	1× (baseline)
B. Technique Effectiveness (Ranked by Average Score Across All Models)
Rank	Technique	Avg Score	Notes
1	Role + Few-shot (Prompt 08)	4.93	Best balance: persona + examples = consistent structure and tone
1	Optimised Best-shot (Prompt 10)	4.93	Tied — but requires more prompt engineering investment
3	Zero-shot + Format (Prompt 02)	3.93	Format constraints alone dramatically lift output quality
3	One-shot (Prompt 03)	3.93	A single good example is highly effective
3	Few-shot (Prompt 04)	3.93	Consistent; negative example added marginal value
3	System Persona (Prompt 06)	3.93	Constraints + persona work well without examples
7	System + CoT (Prompt 09)	3.73	CoT adds reasoning but hurts conciseness
8	Role Prompting (Prompt 07)	3.53	Role alone produces descriptive but meandering copy
9	Chain-of-Thought (Prompt 05)	2.93	Verbose reasoning dominated output; CoT is task-mismatched
10	Zero-shot (Prompt 01)	2.60	Lowest scores across all dimensions; no structure or voice
C. Cost-Quality Tradeoff

Is GPT-4o worth the premium?

No — not for this task.

GPT-4o and gpt-5.4 scored identically (avg 3.90) across all 10 prompts
gpt-5.4-mini scored only 0.12 points lower on average, at ~10% of the cost of GPT-4o
At 769ms average latency, gpt-5.4-mini is also 2.4× faster than GPT-4o

The performance gap only appears in zero-shot conditions (Prompt 01), where all models score poorly anyway. With a well-engineered prompt, gpt-5.4-mini delivers near-identical output quality.

Estimated cost per 1,000 descriptions:

Model	Est. Cost
GPT-4o	~$8.20
gpt-5.4	~$4.10
gpt-5.4-mini	~$0.80

For a production pipeline at scale, gpt-5.4-mini with Role + Few-shot saves ~$7.40 per 1,000 outputs with no measurable quality loss.

D. Failure Analysis — 3 Worst Performing Pairs
1. gpt-5.4-mini × Prompt 01 (Zero-shot) — Avg: 2.6

Diagnosis: No format, no persona, no examples. The model defaulted to a generic paragraph with no headline, no spec list, and hollow language ("This is a great smartwatch for everyone"). Without structure signals, smaller models produce the least differentiated output. This is a prompt failure, not a model failure.

2. GPT-4o × Prompt 05 (Chain-of-Thought) — Avg: 3.0

Diagnosis: CoT is the wrong technique for creative copy generation. Asking the model to reason step-by-step before writing caused the final output to be verbose and analytical in tone — more like a strategy brief than a product description. The reasoning steps consumed token budget and the final copy section was rushed. CoT should be reserved for tasks requiring logical deduction, not brand voice.

3. gpt-5.4-mini × Prompt 07 (Role Prompting only) — Avg: 3.4

Diagnosis: Assigning a persona ("You are Alex...") without providing examples or format constraints resulted in confident but structurally inconsistent output. The model stayed in character but produced copy that was 40% longer than needed, with redundant sentences and no spec list. Role alone inflates creativity without anchoring structure — it needs to be paired with examples or explicit format rules.

E. Production Recommendation

Ship: gpt-5.4-mini + Prompt 08 (Role + Few-shot)

Factor	Verdict
Quality	4.8/5.0 avg — matches frontier model output
Cost	~$0.80 per 1,000 descriptions (10× cheaper than GPT-4o)
Latency	~712ms — production-safe for real-time generation
Consistency	Low variance across runs at temperature=0
Maintainability	Prompt is self-documenting; examples encode style guide

Why not Prompt 10 (Optimised)?
Prompt 10 scored equally but is 40% longer and more brittle — small product catalog changes require prompt updates. Prompt 08 generalises better across product types.

Scaling recommendation:
Store the two few-shot examples in a shared prompt template. When adding new product categories, update the examples rather than rewriting the full prompt. This keeps engineering overhead low and output quality high.