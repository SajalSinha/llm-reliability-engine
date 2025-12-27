from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

JUDGE_MODEL = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(JUDGE_MODEL)
model = AutoModelForSeq2SeqLM.from_pretrained(JUDGE_MODEL)

def judge_answer(question: str, answer: str) -> bool:
    prompt = f"""
Question: {question}
Answer: {answer}

Is the answer factually correct?
Answer yes or no.
"""

    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=5)

    verdict = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return verdict.lower().startswith("yes")
