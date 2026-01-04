# conversation_manager.py

from config import FALLBACK_MESSAGE
from tts_engine import speak

def handle_fallback():
    speak(FALLBACK_MESSAGE)
