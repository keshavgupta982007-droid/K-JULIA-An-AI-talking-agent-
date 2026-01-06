# voice_controller.py

from stt_engine import speech_to_text
from intent_parser import parse_intent
from compliance_filter import is_allowed
from ai_bridge import send_to_brain
from tts_engine import speak
from conversation_manager import handle_fallback

def handle_voice_interaction():
    text = speech_to_text()

    if not text:
        handle_fallback()
        return

    intent_data = parse_intent(text)

    if not is_allowed(intent_data):
        speak("I am not permitted to discuss this topic.")
        return

    response = send_to_brain(intent_data)
    speak(response)
