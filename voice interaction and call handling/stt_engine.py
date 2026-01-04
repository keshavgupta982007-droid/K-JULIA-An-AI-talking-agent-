# stt_engine.py

from audio_input import capture_audio
import speech_recognition as sr

recognizer = sr.Recognizer()

def speech_to_text():
    audio = capture_audio()
    try:
        text = recognizer.recognize_google(audio)
        print("📝 Transcript:", text)
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None
