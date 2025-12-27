import math

def lexical_entropy(text: str) -> float:
    tokens = text.split()
    freqs = {t: tokens.count(t) / len(tokens) for t in set(tokens)}
    entropy = -sum(p * math.log(p + 1e-9) for p in freqs.values())
    return round(entropy, 3)
