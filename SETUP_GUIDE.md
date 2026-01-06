# K-JULIA AI Voice Automation System - Setup Guide

## System Status: WORKING PROTOTYPE

The system has been successfully fixed and is now fully functional!

## Project Structure

```
project/
├── ai_engine/              # AI Decision Engine
│   ├── config.py          # Configuration & constants
│   ├── intent_classifier.py  # Intent detection logic
│   ├── response_generator.py # Response templates
│   ├── conversation_manager.py # Main conversation logic
│   └── escalation.py      # Escalation rules
│
├── voice_system/          # Voice Interface (optional)
│   ├── audio_input.py     # Microphone capture
│   ├── stt_engine.py      # Speech-to-text
│   ├── tts_engine.py      # Text-to-speech
│   └── voice_controller.py # Voice orchestration
│
├── dashboard_app/         # Analytics Dashboard
│   ├── dashboard.py       # Flask web server
│   ├── kpi_calculations.py # KPI & analytics logic
│   ├── templates/         # HTML templates
│   └── static/            # CSS & JS files
│
├── main.py               # Main application entry point
├── test_system.py        # Automated test script
└── requirements.txt      # Python dependencies
```

## What Was Fixed

1. **Folder Structure**: Removed spaces from folder names for proper Python imports
2. **AI Engine**: Completed missing configuration and logic files
3. **Database**: Migrated from CSV to Supabase database
4. **Import Paths**: Fixed all import errors and module references
5. **RLS Policies**: Configured proper security policies for public access
6. **Dependencies**: Installed all required packages

## Quick Start

### 1. Run System Test
```bash
python3 test_system.py
```

This will:
- Test the AI conversation engine
- Create sample complaint records
- Verify database connectivity
- Show the system is working

### 2. Run Interactive Demo
```bash
python3 main.py
```

This starts:
- Interactive text-based interface
- Web dashboard at http://localhost:5000
- Live complaint logging

### 3. Test Individual Components

**Test AI Engine Only:**
```python
from ai_engine.conversation_manager import JuliaBrain

brain = JuliaBrain()
response = brain.process_message("Power cut in our area")
print(response)
```

**Test Database Only:**
```python
from dashboard_app.kpi_calculations import load_logs
logs = load_logs()
print(f"Total calls: {len(logs)}")
```

## Features Demonstrated

### AI Engine Capabilities
- Greeting and conversation flow
- Intent classification (15+ categories)
- Multi-turn conversation management
- Human agent escalation
- Complaint registration with reference numbers

### Supported Complaint Categories
- Energy & Power
- Water Supply
- Roads & Infrastructure
- Sanitation
- Healthcare
- Public Transport
- Telecommunications
- Railways
- Finance & Accounts
- And more...

### Dashboard Analytics
Access at http://localhost:5000:
- Real-time call statistics
- Complaint resolution tracking
- Escalation metrics
- Citizen satisfaction scores
- Interactive charts and visualizations

## Database Schema

The system uses Supabase with the following table:

**Table: calls**
- id (UUID, primary key)
- call_id (text) - Human-readable reference
- call_type (Inbound/Outbound)
- issue_category (complaint category)
- status (Resolved/Pending/Escalated)
- escalated (boolean)
- citizen_feedback (Satisfied/Dissatisfied)
- priority (Critical/High/Medium/Low)
- duration (seconds)
- agent_type (AI/Human)
- satisfaction_score (0-5)
- language (English/Hindi/etc.)
- created_at (timestamp)

## Voice System (Optional)

The voice system requires audio hardware and is optional. The core system works perfectly with text input for demonstration purposes.

To enable voice (requires microphone):
```bash
pip install SpeechRecognition PyAudio pyttsx3
```

Then modify main.py to use voice_system components.

## Testing Different Scenarios

```python
# Example test cases
test_inputs = [
    "Power cut in our area for 8 hours",
    "Water supply not working",
    "Road repair needed urgently",
    "Connect me to a human agent",
    "Yes, another complaint",
    "No, thank you"
]
```

## Environment Variables

The system automatically uses Supabase credentials from `.env`:
- VITE_SUPABASE_URL
- VITE_SUPABASE_ANON_KEY

## Security

- Row Level Security (RLS) enabled
- Public can file complaints (insert)
- Public can view analytics (read)
- Appropriate for civic service use case

## Known Limitations

1. Voice system requires audio hardware (not needed for demo)
2. Simplified AI logic using keyword matching (can be enhanced with ML)
3. Demo uses English language (multilingual support can be added)

## Next Steps for Enhancement

1. Add ML-based intent classification
2. Integrate actual telephony system
3. Add multilingual voice support
4. Connect to government backend systems
5. Add SMS/email notifications

## Success Indicators

When running `python3 test_system.py`, you should see:
- AI Engine responding correctly
- Database records being created
- All tests passing
- "ALL TESTS COMPLETED SUCCESSFULLY" message

## Troubleshooting

**Import Errors:**
- Make sure you're in the project root directory
- Check that all folders have `__init__.py` files

**Database Errors:**
- Verify .env file has correct Supabase credentials
- Check RLS policies allow public insert

**Dashboard Not Loading:**
- Ensure Flask is installed
- Check port 5000 is not in use
- Wait 2-3 seconds for server startup

## Contact & Support

This is a college project demonstrating an AI voice automation system for civic services. The prototype is fully functional and ready for demonstration.

---
**System Status**: ✅ WORKING
**Last Updated**: January 2026
