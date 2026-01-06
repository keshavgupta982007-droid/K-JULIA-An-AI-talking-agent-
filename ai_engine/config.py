# File: ai_engine/config.py
"""
Configuration constants for K-Julia AI Voice Agent
All thresholds, supported intents, and system parameters
"""

# Supported intents/domains for government services
SUPPORTED_INTENTS = [
    "consulting_it",
    "infrastructure_engineering",
    "energy_power",
    "railways",
    "finance_accounts",
    "defense_ordnance",
    "telecommunications",
    "water_supply",
    "roads_infrastructure",
    "sanitation",
    "healthcare",
    "public_transport",
    "garbage_collection",
    "street_lights",
    "building_permits"
]

# Intent classification confidence thresholds
CONFIDENCE_THRESHOLD = 0.6
UNCLEAR_THRESHOLD = 0.4

# Escalation settings
MAX_TURNS_BEFORE_AUTO_ESCALATION = 15
MAX_UNCLEAR_ATTEMPTS = 3
MAX_FRUSTRATION_ATTEMPTS = 2

# Escalation keywords (explicit human agent requests)
ESCALATION_KEYWORDS = [
    "human", "agent", "officer", "person", "executive",
    "real person", "someone else", "supervisor", "manager",
    "insaan se baat", "koi aur", "adhikari"
]

# Exit/goodbye keywords
EXIT_KEYWORDS = [
    "bye", "goodbye", "exit", "end call", "hang up",
    "that's all", "nothing else", "alvida", "bas"
]

# Affirmative responses
YES_KEYWORDS = ["yes", "yeah", "haan", "ha", "sure", "ok", "another", "one more"]

# Negative responses
NO_KEYWORDS = ["no", "nahi", "nothing", "bas", "enough", "nope"]

# System messages
GREETING_MESSAGE = "Hi, this is K-Julia, your personal AI talking agent. How may I assist you today?"
CONFIRMATION_MESSAGE = "Your concern has been noted. Your reference number is {ref_num}. You may receive a call shortly from our team."
FOLLOWUP_MESSAGE = "Is there anything else I can help you with?"
GOODBYE_MESSAGE = "Thank you for contacting us. Have a great day!"
UNCLEAR_MESSAGE = "Sorry, I couldn't understand the issue clearly. Could you please describe your concern again?"
