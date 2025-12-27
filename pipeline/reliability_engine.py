from detection.confidence import confidence_score
from detection.self_consistency import consistency_score
from detection.uncertainty import lexical_entropy
from detection.risk_classifier import classify_risk
from verification.nli_verifier import verify_entailment
from fallback.retry import retry_with_constraints
from fallback.abstain import abstain
from metrics.reliability_metrics import reliability_score

def run_engine(question, responses):
    conf = confidence_score(responses[0])
    cons = consistency_score(responses)
    ent = lexical_entropy(responses[0])

    risk = classify_risk(conf, cons, ent)
    verified = verify_entailment(question, responses[0])

    if risk["level"] == "HIGH" and not verified:
        return abstain()

    final = responses[0]
    if risk["level"] != "LOW":
        final = retry_with_constraints(question)

    return {
        "final_answer": final,
        "risk": risk,
        "verified": verified,
        "reliability_score": reliability_score(conf, cons, verified)
    }
