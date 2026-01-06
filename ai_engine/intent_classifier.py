# File: ai_engine/intent_classifier.py
"""
Rule-based Intent Classification for K-Julia AI Voice Agent
Uses keyword matching to detect user intent and domain
"""

from typing import Tuple
from .config import SUPPORTED_INTENTS, CONFIDENCE_THRESHOLD, UNCLEAR_THRESHOLD, ESCALATION_KEYWORDS, EXIT_KEYWORDS

# Keyword patterns for each intent/domain
INTENT_KEYWORDS = {
    "consulting_it": [
        "software", "it", "cloud", "cyber", "security", "digital", "technology",
        "app", "application", "website", "database", "server", "network", "coding"
    ],
    "infrastructure_engineering": [
        "bridge", "road", "construction", "building", "infrastructure", "civil",
        "engineering", "tender", "contract", "repair", "maintenance"
    ],
    "energy_power": [
        "power", "electricity", "energy", "bijli", "current", "transformer",
        "power cut", "outage", "solar", "grid", "meter", "bill"
    ],
    "railways": [
        "train", "railway", "station", "ticket", "reservation", "pnr",
        "platform", "coach", "rail", "metro"
    ],
    "finance_accounts": [
        "salary", "payment", "finance", "account", "pension", "money",
        "budget", "vendor", "invoice", "paisa", "rupee"
    ],
    "defense_ordnance": [
        "defense", "defence", "military", "army", "ammunition", "ordnance",
        "equipment", "procurement", "supplies"
    ],
    "telecommunications": [
        "telecom", "phone", "mobile", "broadband", "internet", "connection",
        "network", "tower", "signal", "fiber", "wifi"
    ],
    "water_supply": [
        "water", "supply", "pani", "pipeline", "leak", "tank",
        "tap", "drinking water", "water supply"
    ],
    "roads_infrastructure": [
        "road", "pothole", "street", "sadak", "highway", "pavement",
        "footpath", "traffic"
    ],
    "sanitation": [
        "sanitation", "toilet", "sewage", "drain", "cleanliness",
        "hygiene", "bathroom", "sewer"
    ],
    "healthcare": [
        "health", "hospital", "medical", "doctor", "medicine",
        "clinic", "treatment", "patient"
    ],
    "public_transport": [
        "bus", "transport", "travel", "route", "public transport"
    ],
    "garbage_collection": [
        "garbage", "waste", "trash", "kuda", "dustbin", "disposal"
    ],
    "street_lights": [
        "light", "street light", "lamp", "lighting", "batti", "pole"
    ],
    "building_permits": [
        "permit", "license", "approval", "building permit", "construction permit"
    ]
}


def classify_intent(text: str) -> Tuple[str, float]:
    """
    Classify user intent based on keyword matching
    """

    if not text or len(text.strip()) < 3:
        return "unclear", 0.0

    text_lower = text.lower().strip()

    # Check for special intents first
    if any(keyword in text_lower for keyword in ESCALATION_KEYWORDS):
        return "human_agent_request", 0.98

    if any(keyword in text_lower for keyword in EXIT_KEYWORDS):
        return "exit_conversation", 0.97

    # Score each intent based on keyword matches
    intent_scores = {}

    for intent, keywords in INTENT_KEYWORDS.items():
        score = 0
        matches = 0
        for keyword in keywords:
            if keyword in text_lower:
                matches += 1
                score += len(keyword) / len(text_lower)

        if matches > 0:
            intent_scores[intent] = min(score * 2, 0.95)

    # Return best match
    if intent_scores:
        best_intent = max(intent_scores, key=intent_scores.get)
        confidence = intent_scores[best_intent]

        if confidence >= CONFIDENCE_THRESHOLD:
            return best_intent, confidence
        elif confidence >= UNCLEAR_THRESHOLD:
            return best_intent, confidence
        else:
            return "unclear", confidence

    return "unclear", 0.2

