import os
import json
import time
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

# -----------------------------
# Load API key
# -----------------------------
load_dotenv(override=True)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# -----------------------------
# Models
# -----------------------------
MODELS = [
    "gpt-4o",
    "gpt-5.4",
    "gpt-5.4-mini"
]

# -----------------------------
# Paths
# -----------------------------
PROMPTS_DIR = Path("prompts")
OUTPUTS_DIR = Path("outputs")
OUTPUTS_DIR.mkdir(exist_ok=True)

# -----------------------------
# Load product details
# -----------------------------
with open("product_details.txt", "r", encoding="utf-8") as f:
    product_details = f.read()

# -----------------------------
# Load prompts
# -----------------------------
prompt_files = sorted(PROMPTS_DIR.glob("*.txt"))

results = []

# -----------------------------
# Run experiment
# -----------------------------
for model in MODELS:

    for prompt_file in prompt_files:

        with open(prompt_file, "r", encoding="utf-8") as f:
            prompt_text = f.read()

        print(f"Running {model} with {prompt_file.name}...")

        # -----------------------------
        # Handle SYSTEM / USER split
        # -----------------------------
        if "SYSTEM MESSAGE:" in prompt_text:
            parts = prompt_text.split("USER MESSAGE:")
            system_msg = parts[0].replace("SYSTEM MESSAGE:", "").strip()
            user_msg = parts[1].strip()

            messages = [
                {"role": "system", "content": system_msg},
                {
                    "role": "user",
                    "content": f"{user_msg}\n\nPRODUCT DETAILS:\n{product_details}"
                }
            ]
        else:
            final_prompt = f"{prompt_text}\n\nPRODUCT DETAILS:\n{product_details}"
            messages = [{"role": "user", "content": final_prompt}]

        start_time = time.time()

        try:
            # -----------------------------
            # Handle gpt-5.5 limitation
            # -----------------------------
            if model == "gpt-5.5":
                response = client.chat.completions.create(
                    model=model,
                    messages=messages
                )
            else:
                response = client.chat.completions.create(
                    model=model,
                    temperature=0,
                    messages=messages
                )

            latency = round((time.time() - start_time) * 1000, 2)

            output_text = response.choices[0].message.content
            usage = response.usage

            # -----------------------------
            # Save JSON output
            # -----------------------------
            output_filename = f"{model}_{prompt_file.stem}.json"

            with open(OUTPUTS_DIR / output_filename, "w", encoding="utf-8") as f:
                json.dump(response.model_dump(), f, indent=2)

            # -----------------------------
            # Store results
            # -----------------------------
            results.append({
                "model": model,
                "prompt": prompt_file.stem,

                # scoring (fill manually later)
                "task_completion": "",
                "output_format": "",
                "factual_accuracy": "",
                "instruction_following": "",
                "conciseness": "",

                # metrics
                "latency_ms": latency,
                "input_tokens": usage.prompt_tokens,
                "output_tokens": usage.completion_tokens,
                "total_tokens": usage.total_tokens,

                # outputs
                "output_preview": output_text[:150],
                "full_output": output_text
            })

            print("Done.")

        except Exception as e:
            print(f"Error with {model} + {prompt_file.name}: {e}")

# -----------------------------
# Save CSV safely
# -----------------------------
df = pd.DataFrame(results)

try:
    df.to_csv("scores.csv", index=False)
except PermissionError:
    print("scores.csv is open. Saving as scores_new.csv instead.")
    df.to_csv("scores_new.csv", index=False)

print("\n✅ Experiment completed.")