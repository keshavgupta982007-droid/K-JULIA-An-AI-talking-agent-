# File: brain/escalation.py
"""
Escalation Rules for K-Julia AI Voice Agent
Decides when and how to transfer the call to a human agent
"""

from typing import Tuple, Optional
from .config import ESCALATION_KEYWORDS, MAX_TURNS_BEFORE_AUTO_ESCALATION

# Critical / emergency keywords (high priority escalation)
CRITICAL_KEYWORDS = [
    "emergency", "urgent life", "life threat", "accident", "jivan khatre", 
    "critical condition", "danger", "blast", "fire", "collapse", "medical emergency",
    "attack", "terror", "security threat"
]

# Frustration / dissatisfaction keywords
FRUSTRATION_KEYWORDS = [
    "useless", "waste time", "bakwas", "disgusted", "very bad", "gussa", 
    "angry", "frustrated", "time waste", "not helpful", "useless system"
]

class EscalationManager:
    """
    Handles all escalation decisions
    Returns: (should_escalate: bool, message: str, priority: str)
    priority levels: "normal", "high", "critical"
    """

    def __init__(self):
        self.unclear_count = 0
        self.frustration_count = 0

    def evaluate(
        self,
        user_text: str,
        intent: str,
        turn_count: int,
        state: str
    ) -> Tuple[bool, str, str]:
        """
        Main evaluation method
        :param user_text: raw user input (lowercased already)
        :param intent: detected intent
        :param turn_count: current conversation turn
        :param state: current conversation state
        :return: (should_escalate, response_message, priority)
        """

        text_lower = user_text.lower().strip()

        # ───────────────────────────────────────────────────────────────
        # 1. Explicit request to speak to human (highest user intent)
        # ───────────────────────────────────────────────────────────────
        if any(kw in text_lower for kw in ESCALATION_KEYWORDS):
            return True, (
                "Understood. Transferring your call to a human agent immediately. "
                "Please stay on the line."
            ), "high"

        # ───────────────────────────────────────────────────────────────
        # 2. Critical/Emergency keywords (immediate attention needed)
        # ───────────────────────────────────────────────────────────────
        if any(kw in text_lower for kw in CRITICAL_KEYWORDS):
            return True, (
                "I understand this is a critical/emergency situation. "
                "Transferring you directly to the emergency response/human support team right away. "
                "Please stay on the line."
            ), "critical"

        # ───────────────────────────────────────────────────────────────
        # 3. Too many unclear inputs
        # ───────────────────────────────────────────────────────────────
        if intent == "unclear":
            self.unclear_count += 1
            if self.unclear_count >= 3:
                return True, (
                    "I'm having difficulty understanding your concern despite multiple attempts. "
                    "For faster resolution, let me connect you to a human executive. Transferring now..."
                ), "normal"
        else:
            self.unclear_count = 0

        # ───────────────────────────────────────────────────────────────
        # 4. Frustration / anger detected
        # ───────────────────────────────────────────────────────────────
        if any(kw in text_lower for kw in FRUSTRATION_KEYWORDS):
            self.frustration_count += 1
            if self.frustration_count >= 2:
                return True, (
                    "I apologize for the inconvenience. "
                    "It seems you're not satisfied — let me transfer you to a senior executive immediately."
                ), "high"

        # ───────────────────────────────────────────────────────────────
        # 5. Conversation too long (safety net)
        # ───────────────────────────────────────────────────────────────
        if turn_count > MAX_TURNS_BEFORE_AUTO_ESCALATION:
            return True, (
                "This conversation has been quite long. "
                "For quicker resolution of your concern, I'm connecting you to a human agent now."
            ), "normal"

        # ───────────────────────────────────────────────────────────────
        # 6. Status/reference number request (bot can't handle yet)
        # ───────────────────────────────────────────────────────────────
        status_keywords = ["status", "reference number", "kab tak", "kitne din", "tracking", "follow up"]
        if any(kw in text_lower for kw in status_keywords) and state == "CONFIRMATION":
            return True, (
                "I understand you want to know the status of your request. "
                "Let me connect you to the concerned department/human agent for accurate information."
            ), "normal"

        # Default: no escalation needed
        return False, "", "none"