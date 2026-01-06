"""
Keyword patterns for major service categories (Government / PSU / Large Org)
"""

INTENT_KEYWORDS = {
    "consulting_it": [
        "it", "software", "development", "consulting", "website", "app", "digital", 
        "cyber", "security", "cloud", "data", "ai", "ml", "technology solution"
    ],
    "infrastructure_engineering": [
        "road", "bridge", "building", "construction", "civil", "structure", "engineering",
        "project", "tender", "infrastructure", "water supply", "sewage", "drainage"
    ],
    "energy_power": [
        "electricity", "power", "energy", "solar", "wind", "grid", "substation",
        "transformer", "billing", "meter", "power cut", "load shedding"
    ],
    "railways": [
        "train", "railway", "rail", "ticket", "reservation", "coach", "platform",
        "pnr", "station", "freight", "wagon", "safety", "signal"
    ],
    "finance_accounts": [
        "account", "finance", "payment", "bill", "salary", "pension", "tax",
        "audit", "budget", "expenditure", "tender payment", "vendor"
    ],
    "defense_ordnance": [
        "defense", "military", "army", "navy", "airforce", "ordnance", "weapon",
        "ammunition", "equipment", "supply", "procurement", "tender defense"
    ],
    "telecommunications": [
        "telecom", "mobile", "network", "broadband", "fiber", "tower", "signal",
        "bsnl", "jio", "airtel", "internet", "connection", "recharge"
    ],
    "human_agent_request": [],  # filled from config
    "exit_conversation": [
        "exit", "stop", "bye", "goodbye", "thank you bye", "bas", "band karo"
    ],
    "yes_continue": [],
    "no_thanks": [],
    "unclear": []
}

# intents.py (corrected - end of file)

# Define the missing keyword lists directly here to avoid NameError
ESCALATION_KEYWORDS = [
    "human", "agent", "person", "executive", "officer", "supervisor", "manager",
    "connect me", "talk to someone", "real person", "senior", "escalate", "insaan",
    "sir", "madam", "kisi se", "human operator"
]

YES_KEYWORDS = [
    "yes", "yeah", "haan", "another", "one more", "bhi", "aur", "yes please", "continue"
]

NO_KEYWORDS = [
    "no", "no thanks", "nothing", "bas", "enough", "done", "thank you bye", "ok bye"
]

# Now safely merge them into the dictionary
INTENT_KEYWORDS["human_agent_request"] = ESCALATION_KEYWORDS.copy()  # or .extend() after []

INTENT_KEYWORDS["yes_continue"] = YES_KEYWORDS.copy()

INTENT_KEYWORDS["no_thanks"] = NO_KEYWORDS.copy()

# Optional: if you prefer extend style (works too)
# INTENT_KEYWORDS["human_agent_request"] = []
# INTENT_KEYWORDS["human_agent_request"].extend(ESCALATION_KEYWORDS)

# INTENT_KEYWORDS["yes_continue"] = []
# INTENT_KEYWORDS["yes_continue"].extend(YES_KEYWORDS)

# INTENT_KEYWORDS["no_thanks"] = []
# INTENT_KEYWORDS["no_thanks"].extend(NO_KEYWORDS)