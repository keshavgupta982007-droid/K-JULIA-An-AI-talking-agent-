# intent_classifier.py

def predict_intent(text):
    text = text.lower()

    if any(word in text for word in ["interested", "tell me more", "sounds good"]):
        return "sales_interest", 0.9

    if any(word in text for word in ["not interested", "no thanks", "stop"]):
        return "not_interested", 0.95

    if any(word in text for word in ["call me later", "callback", "tomorrow"]):
        return "callback_request", 0.9

    if any(word in text for word in ["human", "agent", "person"]):
        return "human_agent", 0.95

    if any(word in text for word in ["what", "how", "service"]):
        return "general_query", 0.7

    return "unknown", 0.4
