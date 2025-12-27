def reliability_score(confidence, consistency, verified):
    score = 0.5 * confidence + 0.3 * consistency + 0.2 * int(verified)
    return round(score, 3)
