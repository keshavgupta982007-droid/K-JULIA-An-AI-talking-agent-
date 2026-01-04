"""
voice_system package

Handles:
- Audio input (mic)
- Speech-to-text (STT)
- Intent parsing & compliance
- AI bridge communication
- Text-to-speech (TTS)

This package is responsible ONLY for voice I/O.
All AI decision-making lives in ai_logic.
"""

# Optional: expose main entry functions if needed elsewhere
from .voice_controller import handle_voice_interaction

__all__ = [
    "handle_voice_interaction"
]

