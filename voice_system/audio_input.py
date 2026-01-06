# audio_input.py

import speech_recognition as sr

recognizer = sr.Recognizer()

def capture_audio():
    with sr.Microphone() as source:
        print("🎙 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
    return audio
