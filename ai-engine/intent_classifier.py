from typing import Tuple
from .intents import INTENT_KEYWORDS
from .config import MIN_CONFIDENCE


def classify_intent(text: str) -> Tuple[str, float]:
    """
    Simple keyword-based intent classifier
    Returns: (intent_name, confidence_score)
    """
    if not text or not isinstance(text, str):
        return "unclear", 0.0

    text = text.lower().strip()

    # Quick priority checks
    if any(kw in text for kw in INTENT_KEYWORDS["exit_conversation"]):
        return "exit_conversation", 1.0

    if any(kw in text for kw in INTENT_KEYWORDS["human_agent_request"]):
        return "human_agent_request", 0.96

    best_intent = "unclear"
    best_score = 0.0

    for intent, keywords in INTENT_KEYWORDS.items():
        if intent in {"exit_conversation", "human_agent_request", "unclear"}:
            continue

        matches = sum(1 for word in keywords if word in text)
        if matches == 0:
            continue

        score = matches / max(len(keywords), 1)
        # Simple boosting to make confident matches stronger
        score = min(0.45 + score * 1.8, 0.95)

        if score > best_score:
            best_score = score
            best_intent = intent

    if best_score >= MIN_CONFIDENCE:
        return best_intent, best_score
    else:
        return "unclear", best_score