"""
Brain package initialization for K-Julia AI Voice Agent
This file makes the 'brain' directory a proper Python package
and exposes the main public interface.

Current version: January 2026 - Government/Large Organization Services Flow
"""

# Main public class that the voice module should import and use
from .conversation_manager import JuliaBrain

# Optional: expose other useful components if needed by voice/dashboard
from .escalation import EscalationManager

# Public API
__all__ = [
    'JuliaBrain',               # Main brain class
    'EscalationManager',        # Escalation logic (can be used directly if needed)
]

# Package metadata (optional but good practice)
__version__ = '0.1.0'
__author__ = 'Your College Project Team'
__description__ = 'Core decision-making brain for multilingual K-Julia voice agent'