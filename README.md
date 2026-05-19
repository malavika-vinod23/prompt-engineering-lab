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

- Example-based prompting (one-shot, few-shot) consistently produced the best results  
- Chain-of-thought did not improve performance for this structured generation task  
- Role prompting improved tone but reduced conciseness  
- Smaller models performed nearly as well as larger models when prompts were well-designed  
- Prompt engineering had a greater impact than model size  

---

## Results Summary

Best Performing Setup

Model: gpt-5.4-mini  
Prompt: Role + Few-shot  

---

## Overall Ranking

Best
- Prompt 08 — Role + Few-shot  

Strong
- Prompt 03 — One-shot  
- Prompt 04 — Few-shot  

Good
- Prompt 06 — System Persona  
- Prompt 02 — Format  
- Prompt 10 — Optimised  

Lower
- Prompt 05 — Chain-of-Thought  
- Prompt 07 — Role  

Weak
- Prompt 09 — System + CoT  
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

Well-designed prompts allow smaller models to achieve near-frontier-level performance at significantly lower cost.

---

## Future Improvements

- Add automated scoring using LLM-as-a-judge  
- Expand dataset to multiple products  
- Add visualization dashboard for results  
- Test additional models and multimodal inputs  

---

## License

This project is for educational and research purposes.
