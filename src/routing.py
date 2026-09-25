from pathlib import Path
import joblib
import re

ROOT = Path(__file__).resolve().parents[1]
MODEL = joblib.load(ROOT / "models" / "prompt_classifier.pkl")

RULES = {
    "billing": ["refund", "invoice", "charged", "payment", "subscription", "card", "fee"],
    "account": ["password", "login", "log in", "username", "account", "two factor", "2fa"],
}

def route_prompt(prompt: str):
    text = prompt.lower().strip()

    # High-confidence deterministic rules first.
    for category, keywords in RULES.items():
        if any(re.search(r"\b" + re.escape(k) + r"\b", text) for k in keywords):
            return {"category": category, "route": category + "_workflow", "confidence": 1.0, "method": "rule"}

    category = MODEL.predict([text])[0]
    probabilities = MODEL.predict_proba([text])[0]
    confidence = float(max(probabilities))
    return {
        "category": category,
        "route": category + "_workflow",
        "confidence": round(confidence, 4),
        "method": "ml"
    }
