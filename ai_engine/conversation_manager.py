from typing import Optional, Dict
from .intent_classifier import classify_intent
from .response_generator import generate_response
from .config import MAX_TURNS_BEFORE_AUTO_ESCALATION


class JuliaBrain:
    """
    Main brain class - k-Julia
    Follows the new government/large organization complaint registration flow
    """

    def __init__(self):
        self.state: str = "INITIAL_GREETING"          # states: INITIAL_GREETING → WAITING_INTENT → COLLECTING_INFO → CONFIRMATION → FOLLOW_UP
        self.current_intent: Optional[str] = None
        self.complaints: list = []                    # list of registered intents
        self.customer_info: Dict[str, str] = {}       # name, address, contact
        self.turn_count: int = 0

    def process_message(self, user_text: str) -> str:
        self.turn_count += 1
        text_lower = user_text.lower().strip()

        intent, confidence = classify_intent(user_text)

        # Handle special yes/no/continue/exit early
        if any(kw in text_lower for kw in ["yes", "yeah", "haan", "another", "one more"]):
            if self.state in ["CONFIRMATION", "FOLLOW_UP"]:
                return self._ask_for_new_complaint()
        
        if any(kw in text_lower for kw in ["no", "nothing", "bas", "enough"]):
            return "Thank you for contacting us. Have a great day!"

        if intent == "human_agent_request":
            return "Understood. Transferring your call to a human agent right away. Please stay on the line."

        if intent == "exit_conversation":
            return "Thank you for contacting us. Goodbye!"

        # Main state machine
        if self.state == "INITIAL_GREETING":
            self.state = "WAITING_INTENT"
            return generate_response("greeting", is_first=True, turn_count=self.turn_count)

        elif self.state == "WAITING_INTENT":
            if intent in ["unclear", None]:
                return "Sorry, I couldn't understand the issue clearly. Could you please describe your concern again?"

            if intent in ["consulting_it", "infrastructure_engineering", "energy_power", 
                          "railways", "finance_accounts", "defense_ordnance", "telecommunications"]:
                self.current_intent = intent
                self.state = "COLLECTING_INFO"
                self.complaints.append(intent)
                return generate_response("collect_info", is_first=True, turn_count=self.turn_count)
            
            else:
                return "I can help you register complaints/requests related to our major services. Could you please tell me your concern?"

        elif self.state == "COLLECTING_INFO":
            # In real system this would use STT/NLP to extract, here we simulate
            # For college project we just pretend we got the info
            self.customer_info = {
                "name": "Demo User",           # ← In real system: extract from speech
                "address": "Demo Address, City",
                "contact": "99999xxxxx"
            }
            self.state = "CONFIRMATION"
            return generate_response("confirmation", is_first=True, turn_count=self.turn_count,
                                  intent=self.current_intent)

        elif self.state == "CONFIRMATION" or self.state == "FOLLOW_UP":
            self.state = "FOLLOW_UP"
            return generate_response("follow_up", is_first=True, turn_count=self.turn_count)

        # Safety net
        if self.turn_count > MAX_TURNS_BEFORE_AUTO_ESCALATION:
            return "I'm having difficulty understanding the conversation. It's best to connect you to a human agent now."

        return "I'm still here. How may I assist you further?"

    def _ask_for_new_complaint(self) -> str:
        self.current_intent = None
        self.state = "WAITING_INTENT"
        return "Sure! Please tell me about the next issue or request."

    def reset(self):
        self.__init__()