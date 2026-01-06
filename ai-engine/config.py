"""
Central configuration for k-Julia Brain (Government / Large Organization Services)
"""

SUPPORTED_INTENTS = [
    "consulting_it",
    "infrastructure_engineering",
    "energy_power",
    "railways",
    "finance_accounts",
    "defense_ordnance",
    "telecommunications",
    "human_agent_request",
    "exit_conversation",
    "unclear",
    "yes_continue",
    "no_thanks"
]

# Common escalation trigger words
ESCALATION_KEYWORDS = [
    "human", "agent", "person", "executive", "officer", "supervisor", "manager",
    "connect me", "talk to someone", "real person", "senior", "escalate"
]

MIN_CONFIDENCE = 0.50

MAX_TURNS_BEFORE_AUTO_ESCALATION = 8

# Keywords for yes/no continuation
YES_KEYWORDS = ["yes", "yeah", "haan", "another", "one more", "bhi", "aur"]
NO_KEYWORDS = ["no", "no thanks", "nothing", "bas", "enough", "done", "thank you bye"]