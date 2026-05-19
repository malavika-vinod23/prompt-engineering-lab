# Prompt Engineering Lab


---

## Overview

This project explores how different prompt engineering techniques impact output quality across multiple OpenAI models in an e-commerce product description generation task.

---

## Task

E-commerce Product Description Generation

Product: SmartFit Pro X1 Smartwatch  

Goal: Generate high-quality, structured, and persuasive product descriptions  

---

## Objective

To evaluate how prompt design influences:

- Output quality  
- Structure consistency  
- Factual accuracy  
- Instruction adherence  
- Conciseness  

---

## Experiment Setup

- 10 prompt engineering techniques tested  
- 3 models evaluated  
  - GPT-4o  
  - gpt-5.4  
  - gpt-5.4-mini  
- Total API calls: 30  

---

## Evaluation Metrics

Each response was scored (1–5) on:

- Task Completion  
- Output Format  
- Factual Accuracy  
- Instruction Following  
- Conciseness  

---

## Project Structure

prompts/
outputs/
scores.csv
prompts_library.md
run_experiment.py
README.md

---

## Prompt Techniques Tested

- Zero-shot  
- Zero-shot + Format  
- One-shot  
- Few-shot  
- Role Prompting  
- System Persona  
- Chain-of-Thought  
- Role + Few-shot  
- System + CoT  
- Optimised Prompt  

---

## Key Findings

- Example-based prompting (one-shot, few-shot, role + few-shot) achieved perfect 5.0 scores across all models
- Chain-of-thought performed well here (avg 4.8) — unlike typical creative tasks, the structured output format prevented reasoning from polluting the final copy
- Role prompting improved tone but slightly reduced conciseness (lowest score dimension across models for Prompt 07)
- gpt-5.4-mini matched or exceeded GPT-4o on most prompts, and outperformed it on Prompts 06 and 10
- Prompt engineering had a greater impact than model size — the zero-shot gap between models (3.0 vs 4.4) disappears entirely with structured prompts
- The only failure cases for gpt-5.4 and gpt-5.4-mini were on zero-shot, driven by format and instruction-following breakdowns, not knowledge gaps

---

## Results Summary

Model Averages (across all 10 prompts)

| Model        | Avg Score | Avg Latency | Relative Cost |
|--------------|-----------|-------------|---------------|
| GPT-4o       | 4.76      | 5,093ms     | 10×           |
| gpt-5.4      | 4.68      | 4,215ms     | 3×            |
| gpt-5.4-mini | 4.72      | 2,229ms     | 1× (baseline) |

Best Performing Setup

Model: gpt-5.4-mini  
Prompt: One-shot / Few-shot / Role + Few-shot (all tied at 5.0/5.0)

---

## Overall Ranking

Best (avg 5.00 across all models)
- Prompt 03 — One-shot  
- Prompt 04 — Few-shot  
- Prompt 08 — Role + Few-shot  

Strong (avg 4.80–4.87)
- Prompt 06 — System Persona (4.87)
- Prompt 02 — Zero-shot + Format (4.80)
- Prompt 05 — Chain-of-Thought (4.80)
- Prompt 10 — Optimised Best-shot (4.80)

Good (avg 4.67–4.73)
- Prompt 09 — System + CoT (4.73)
- Prompt 07 — Role Prompting (4.67)

Weak (avg 3.53)
- Prompt 01 — Zero-shot  

---

## Setup Instructions

1. Clone Repository

git clone https://github.com/your-username/prompt-engineering-lab.git
cd prompt-engineering-lab

2. Install Dependencies

pip install openai python-dotenv pandas

3. Configure API Key

Create a .env file:

OPENAI_API_KEY=your_key_here

4. Run Experiment

python run_experiment.py

---

## Key Insight

Prompt engineering is more impactful than model size for structured generation tasks.

With a well-engineered prompt (one-shot, few-shot, or role + few-shot), gpt-5.4-mini achieves perfect 5.0 scores at ~10% the cost of GPT-4o and roughly 2.3× lower latency. The performance gap only surfaces in zero-shot conditions — where all models perform poorly anyway.

---

## Future Improvements

- Add automated scoring using LLM-as-a-judge  
- Expand dataset to multiple products  
- Add visualization dashboard for results  
- Test additional models and multimodal inputs  

---

## License

This project is for educational and research purposes.
