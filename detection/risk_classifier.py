def classify_risk(confidence, consistency, entropy):
    flags = []

    if confidence < 0.4:
        flags.append("LOW_CONFIDENCE")
    if consistency < 0.4:
        flags.append("INCONSISTENT")
    if entropy > 3.5:
        flags.append("HIGH_UNCERTAINTY")

    if len(flags) >= 2:
        level = "HIGH"
    elif flags:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {"level": level, "flags": flags}
