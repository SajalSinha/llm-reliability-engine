def simple_fact_check(answer: str) -> bool:
    red_flags = [
        "as an ai",
        "i am not sure",
        "cannot verify",
        "might be incorrect"
    ]
    return not any(flag in answer.lower() for flag in red_flags)
