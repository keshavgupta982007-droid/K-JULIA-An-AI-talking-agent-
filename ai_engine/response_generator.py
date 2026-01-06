# File: ai_engine/response_generator.py
"""
Response Generation Logic for K-Julia AI Voice Agent
Creates natural English responses for each conversation stage
"""

import random
from typing import Optional

def generate_response(
    response_type: str,
    is_first: bool = True,
    turn_count: int = 0,
    intent: Optional[str] = None,
    ref_num: Optional[str] = None
) -> str:
    """
    Generate appropriate response based on conversation state
    """
    from .config import GREETING_MESSAGE, CONFIRMATION_MESSAGE, FOLLOWUP_MESSAGE, GOODBYE_MESSAGE

    if response_type == "greeting":
        if is_first:
            return GREETING_MESSAGE
        else:
            return "Hello again. What can I help you with?"

    elif response_type == "collect_info":
        return "Thank you for mentioning your concern. May I know your name, address, and contact number please?"

    elif response_type == "confirmation":
        if not ref_num:
            ref_num = f"KJ{random.randint(10000, 99999)}"

        domain_messages = {
            "consulting_it": "regarding your IT consulting request",
            "infrastructure_engineering": "regarding your infrastructure issue",
            "energy_power": "regarding your power supply issue",
            "railways": "regarding your railway service request",
            "finance_accounts": "regarding your finance query",
            "defense_ordnance": "regarding your defense procurement query",
            "telecommunications": "regarding your telecom service issue",
            "water_supply": "regarding your water supply complaint",
            "roads_infrastructure": "regarding your road infrastructure issue",
            "sanitation": "regarding your sanitation complaint",
            "healthcare": "regarding your healthcare concern",
            "public_transport": "regarding your public transport issue",
            "garbage_collection": "regarding your garbage collection complaint",
            "street_lights": "regarding your street lighting issue",
            "building_permits": "regarding your building permit query"
        }

        domain_msg = domain_messages.get(intent, "regarding your concern")

        return f"{CONFIRMATION_MESSAGE.format(ref_num=ref_num)} {FOLLOWUP_MESSAGE}"

    elif response_type == "follow_up":
        return FOLLOWUP_MESSAGE

    elif response_type == "goodbye":
        return GOODBYE_MESSAGE

    elif response_type == "unclear":
        variations = [
            "Sorry, I couldn't understand that clearly. Could you please repeat?",
            "I didn't quite catch that. Could you please describe your issue again?",
            "Could you please rephrase that? I want to make sure I understand correctly."
        ]
        return random.choice(variations)

    elif response_type == "escalation":
        return "Understood. Transferring your call to a human agent immediately. Please stay on the line."

    else:
        return "I'm here to help. Please tell me your concern."
