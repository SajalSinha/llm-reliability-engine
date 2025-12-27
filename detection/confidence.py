def confidence_score(text: str) -> float:
    if not text or len(text) < 20:
        return 0.1

    unique_ratio = len(set(text.split())) / max(len(text.split()), 1)
    length_score = min(len(text) / 300, 1.0)

    return round(0.6 * unique_ratio + 0.4 * length_score, 3)
