from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL = "roberta-large-mnli"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL).cuda()

LABELS = ["contradiction", "neutral", "entailment"]

def verify_entailment(premise, hypothesis):
    inputs = tokenizer(premise, hypothesis, return_tensors="pt").to("cuda")
    with torch.no_grad():
        logits = model(**inputs).logits
    label = LABELS[logits.argmax()]
    return label == "entailment"
