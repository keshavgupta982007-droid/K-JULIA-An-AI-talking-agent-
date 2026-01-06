# K-Julia Brain Module  
**Core Decision-Making Engine for Multilingual Government/Large Organization Voice Agent**  
*Version: 0.1.0*  
*Current Date Reference: January 01, 2026*

## Overview

This module is the **brain** (AI decision core) of **K-Julia**, a voice-only AI talking agent designed for handling complaints, requests, and queries in government departments, PSUs, large organizations, and public services.

Key characteristics:
- Receives **pre-translated English text** from the Voice module
- Processes user intent using simple rule-based keyword matching
- Manages conversation state (greeting → intent detection → info collection → confirmation → follow-up)
- Generates **English responses** (Voice module translates back to user's native language)
- Includes built-in escalation logic to human agents
- Suitable for college project demonstration (lightweight, no external ML dependencies)

## Folder Structure
brain/
├── config.py                  # All constants, supported intents, thresholds
├── intents.py                 # Keyword patterns for each intent
├── intent_classifier.py       # Rule-based intent detection
├── response_generator.py      # Response templates & generation logic
├── conversation_manager.py    # Main JuliaBrain class + state machine
├── escalation.py              # Dedicated escalation rules & logic
├── init.py                # Package initialization
└── README.md                  # This file

## Main Components

| File                        | Responsibility                                                                 |
|-----------------------------|--------------------------------------------------------------------------------|
| `config.py`                 | Supported intents list, thresholds, keyword constants                         |
| `intents.py`                | Keyword lists for all intents (consulting_it, railways, power, etc.)          |
| `intent_classifier.py`      | Simple keyword-based intent classification                                     |
| `response_generator.py`     | Creates natural English responses for each conversation stage                 |
| `conversation_manager.py`   | `JuliaBrain` class — core state machine & message processing                  |
| `escalation.py`             | Decides when & how to transfer to human (explicit request, unclear turns, etc.) |

## Conversation Flow (as per requirements)

1. Greeting: "Hi, this is K-Julia, your personal AI talking agent. How may I assist you today?"
2. User describes issue → detects intent (e.g. railways, power, finance...)
3. Collects: Name, Address, Contact number (simulated for demo)
4. Confirms registration: "Your concern has been noted... You may receive a call shortly."
5. Asks: "Is there anything else I can help you with?"
   - Yes → repeats from step 2
   - No / Bye → ends politely
   - "Connect to agent" / frustration / too long → escalates

## How to Use (from Voice module)

```python
from brain import JuliaBrain

# Initialize once per call/session
k_julia = JuliaBrain()

# In your voice loop (after STT + translation to English)
user_text = "Power cut in our area since 8 hours"  # example from voice module
response = k_julia.process_message(user_text)

# Voice module will translate response back to user's language & speak it
print(response)
# Output: "Thank you for mentioning your problem. May I know your name, address, and contact number please?"