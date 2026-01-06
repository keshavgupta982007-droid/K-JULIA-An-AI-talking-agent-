"""
main.py
Central orchestrator for K-Julia AI Voice Automation System

This is a simplified version that demonstrates the core functionality
without requiring audio hardware (PyAudio).
"""

import os
import threading
import time
import random
from datetime import datetime
from supabase import create_client

# Import AI Engine
from ai_engine.conversation_manager import JuliaBrain
from ai_engine.escalation import EscalationManager

# Import Dashboard
from dashboard_app.dashboard import app as dashboard_app

# Initialize Supabase
SUPABASE_URL = os.getenv("VITE_SUPABASE_URL")
SUPABASE_KEY = os.getenv("VITE_SUPABASE_ANON_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Global objects
brain = JuliaBrain()
escalation_manager = EscalationManager()

def log_call_to_db(
    call_type="Inbound",
    issue_category="General",
    status="Resolved",
    escalated=False,
    priority="Medium",
    duration=60,
    agent_type="AI",
    citizen_feedback="Satisfied",
    language="English"
):
    """Log call to Supabase database"""
    try:
        call_id = f"KJ{random.randint(10000, 99999)}"

        data = {
            "call_id": call_id,
            "call_type": call_type,
            "virtual_number": "TOLL_FREE",
            "issue_category": issue_category,
            "status": status,
            "escalated": escalated,
            "citizen_feedback": citizen_feedback,
            "priority": priority,
            "duration": duration,
            "agent_type": agent_type,
            "satisfaction_score": 4.5 if citizen_feedback == "Satisfied" else 2.0,
            "callback_requested": False,
            "language": language,
            "resolution_time": duration if status == "Resolved" else 0
        }

        result = supabase.table("calls").insert(data).execute()
        print(f"Logged call {call_id} to database")
        return call_id
    except Exception as e:
        print(f"Error logging call: {e}")
        return None

def simulate_text_interaction(user_text):
    """
    Simulate a text-based interaction (useful for testing without voice)
    """
    print(f"\nUser: {user_text}")

    # Get AI response
    response = brain.process_message(user_text)
    print(f"K-Julia: {response}")

    # Determine if escalated
    escalated = "human" in response.lower() or "transfer" in response.lower()

    # Extract domain from user text
    domain = "General"
    if "power" in user_text.lower() or "electricity" in user_text.lower():
        domain = "Energy & Power"
    elif "water" in user_text.lower():
        domain = "Water Supply"
    elif "road" in user_text.lower():
        domain = "Roads"

    # Log to database
    status = "Escalated" if escalated else "Resolved"
    log_call_to_db(
        call_type="Inbound",
        issue_category=domain,
        status=status,
        escalated=escalated,
        agent_type="AI" if not escalated else "Human",
        duration=random.randint(60, 300)
    )

    return response

def add_sample_data():
    """Add some sample data to the database for dashboard demonstration"""
    print("Adding sample data to database...")

    sample_interactions = [
        ("Power cut in our area since 8 hours", "Energy & Power", "Resolved"),
        ("Water supply issue for 2 days", "Water Supply", "Pending"),
        ("Road repair needed urgently", "Roads", "Resolved"),
        ("Street light not working", "Street Lights", "Resolved"),
        ("Garbage not collected", "Sanitation", "Escalated"),
    ]

    for text, category, status in sample_interactions:
        log_call_to_db(
            issue_category=category,
            status=status,
            escalated=(status == "Escalated"),
            duration=random.randint(60, 300),
            citizen_feedback="Satisfied" if status == "Resolved" else "Dissatisfied"
        )
        time.sleep(0.1)

    print("Sample data added successfully!")

def run_dashboard():
    """Run Flask dashboard"""
    print("\n" + "="*60)
    print("Dashboard running at: http://localhost:5000")
    print("="*60 + "\n")
    dashboard_app.run(
        debug=False,
        host="0.0.0.0",
        port=5000,
        use_reloader=False
    )

def run_demo_mode():
    """Run interactive demo mode"""
    print("\n" + "="*60)
    print("K-JULIA AI VOICE AUTOMATION SYSTEM - DEMO MODE")
    print("="*60)
    print("\nAvailable commands:")
    print("  - Type your complaint/query")
    print("  - Type 'sample' to add sample data")
    print("  - Type 'exit' to quit")
    print("="*60 + "\n")

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Goodbye!")
                break

            if user_input.lower() == "sample":
                add_sample_data()
                continue

            simulate_text_interaction(user_input)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

def main():
    """Main entry point"""
    print("\n" + "="*60)
    print("  K-JULIA AI VOICE AUTOMATION SYSTEM")
    print("  Civic Services Agent")
    print("="*60 + "\n")

    # Start dashboard in background thread
    dashboard_thread = threading.Thread(
        target=run_dashboard,
        daemon=True
    )
    dashboard_thread.start()

    # Give dashboard time to start
    time.sleep(2)

    # Add initial sample data
    add_sample_data()

    # Run demo mode
    run_demo_mode()

if __name__ == "__main__":
    main()
