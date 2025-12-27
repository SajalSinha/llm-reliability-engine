from models.llm import generate

def retry_with_constraints(question: str) -> str:
    prompt = f"""
Answer the question.
Rules:
- Be concise
- Say "I don't know" if unsure
- Do not guess

Question: {question}
"""
    return generate(prompt, temperature=0.0)
