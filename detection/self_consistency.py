def consistency_score(responses: list[str]) -> float:
    normalized = [r.lower().strip() for r in responses]
    return round(1 / len(set(normalized)), 3)
