# Voice System – AI Consulting & IT Agent

## Overview
This module implements the **Voice System layer** of the AI Consulting & IT Agent.
It is responsible for capturing user voice input, converting it to text, identifying intent and domain,
applying compliance checks, and responding via synthesized speech.


It communicates with the Brain System using **text-only interfaces**.

---

## Features
- Speech-to-Text (STT)
- Domain-aware intent parsing
- Compliance filtering (Finance & Defense safe)
- Text-to-Speech (TTS)
- Modular, GitHub-ready architecture
- Designed for consulting domains:
  - Infrastructure & Engineering
  - Energy & Power
  - Railways
  - Finance & Accounts
  - Defense & Ordnance
  - Telecommunications

---

## Libraries & Dependencies Used

### 1. `SpeechRecognition`
**Purpose:**  
Handles Speech-to-Text (STT) by capturing audio from the microphone and converting it into text.

**Why used:**  
- Simple and reliable for real-time voice input
- Supports Google Speech API for accurate transcription
- Widely used and well-documented

**Used in files:**
- `audio_input.py`
- `stt_engine.py`

---

### 2. `PyAudio`
**Purpose:**  
Provides low-level access to the system’s microphone hardware.

**Why used:**  
- Required backend dependency for microphone input
- Enables real-time audio capture

**Used indirectly by:**
- `SpeechRecognition`

⚠️ Note: PyAudio must be installed correctly for your OS.

---

### 3. `pyttsx3`
**Purpose:**  
Handles Text-to-Speech (TTS) synthesis.

**Why used:**  
- Works offline (no cloud dependency)
- Cross-platform (Windows / Linux / macOS)
- Allows control over speech rate and voice properties

**Used in files:**
- `tts_engine.py`
- `app.py`

---

## Dependency Summary Table

| Library            | Role                | Offline | Domain Safe |
|-------------------|---------------------|---------|-------------|
| SpeechRecognition | Speech-to-Text      | ❌      | ✅          |
| PyAudio           | Audio Input         | ✅      | ✅          |
| pyttsx3           | Text-to-Speech      | ✅      | ✅          |

---

## Installation

```bash
pip install -r requirements.txt
