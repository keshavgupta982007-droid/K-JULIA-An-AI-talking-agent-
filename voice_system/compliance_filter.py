# compliance_filter.py

def is_allowed(intent_data):
    domain = intent_data["domain"]
    query = intent_data["query"]

    if domain == "defense":
        restricted_keywords = ["manufacture", "weapon design", "explosive"]
        for word in restricted_keywords:
            if word in query:
                return False

    if domain == "finance":
        if "invest" in query or "stock" in query:
            return False

    return True
