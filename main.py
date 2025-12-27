from models.generator import generate
from pipeline.reliability_engine import run_engine

question = "Who invented the light bulb?"

responses = [generate(question) for _ in range(3)]
result = run_engine(question, responses)

print(result)
