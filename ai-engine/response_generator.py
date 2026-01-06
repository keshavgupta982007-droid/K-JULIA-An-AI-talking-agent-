FIRST_TURN_RESPONSES = {
    "greeting": "Hi, this is K-Julia, your personal AI talking agent. How may I assist you today?",

    "collect_info": "Thank you for mentioning your problem. May I know your name, address, and contact number please?",

    "confirmation": (
        "Thank you for contacting our services. "
        "Your concern regarding {intent} has been noted and will be reported to the concerned authorities. "
        "You may receive a call from the respective officials shortly. "
        "Is there anything else I can help you with?"
    ),

    "follow_up": "Is there any other concern or request you would like to register?"
}

def generate_response(
    response_type: str,
    is_first: bool = True,
    turn_count: int = 1,
    intent: str = None
) -> str:
    if response_type == "confirmation" and intent:
        return FIRST_TURN_RESPONSES["confirmation"].format(intent=intent.replace("_", " ").title())
    
    return FIRST_TURN_RESPONSES.get(response_type, "How may I assist you further?")