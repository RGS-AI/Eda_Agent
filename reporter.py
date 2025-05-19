from transformers import pipeline

def generate_summary(prompt, model_name="google/flan-t5-small"):
    try:
        generator = pipeline("text2text-generation", model=model_name)
        output = generator(prompt, max_new_tokens=256, do_sample=False)[0]['generated_text']
        return output.strip()
    except Exception as e:
        return f"[ERROR] Summary generation failed: {e}"

def build_prompt(summary):
    shape = summary.get('shape', ('?', '?'))
    missing = summary.get('missing_values', {})
    dtypes = summary.get('dtypes', {})

    missing_str = "\n".join([f"  - {col}: {val} missing" for col, val in missing.items()]) or "  - No missing values"
    dtypes_str = "\n".join([f"  - {col}: {dtype}" for col, dtype in dtypes.items()])

    prompt = f"""
You are a data analyst. Analyze the dataset based on these characteristics:

- Shape: {shape[0]} rows × {shape[1]} columns
- Missing Values:
{missing_str}
- Column Types:
{dtypes_str}

Write a plain-English summary of the dataset.
"""
    return prompt.strip()