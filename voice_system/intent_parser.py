# intent_parser.py

def parse_intent(text):
    text = text.lower()

    domain = "general"
    if "power" in text or "energy" in text:
        domain = "energy"
    elif "railway" in text or "train" in text:
        domain = "railways"
    elif "finance" in text or "account" in text:
        domain = "finance"
    elif "defense" in text or "weapon" in text:
        domain = "defense"
    elif "network" in text or "telecom" in text:
        domain = "telecommunications"
    elif "infrastructure" in text:
        domain = "infrastructure"

    intent = "explain"
    if text.startswith("how") or "process" in text:
        intent = "process_explanation"

    return {
        "domain": domain,
        "intent": intent,
        "query": text
    }
