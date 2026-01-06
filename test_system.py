"""
Test script for K-Julia AI Voice Automation System
Demonstrates core functionality without interactive mode
"""

import os
import random
from dotenv import load_dotenv
from supabase import create_client

# Load environment
load_dotenv()

# Import AI Engine
from ai_engine.conversation_manager import JuliaBrain

# Initialize
brain = JuliaBrain()
supabase = create_client(
    os.getenv("VITE_SUPABASE_URL"),
    os.getenv("VITE_SUPABASE_ANON_KEY")
)

def log_call(issue_category, status, escalated=False):
    """Log a call to the database"""
    call_id = f"KJ{random.randint(10000, 99999)}"
    data = {
        "call_id": call_id,
        "call_type": "Inbound",
        "virtual_number": "TOLL_FREE",
        "issue_category": issue_category,
        "status": status,
        "escalated": escalated,
        "citizen_feedback": "Satisfied" if status == "Resolved" else "Dissatisfied",
        "priority": "High" if escalated else "Medium",
        "duration": random.randint(60, 300),
        "agent_type": "AI" if not escalated else "Human",
        "satisfaction_score": 4.5 if status == "Resolved" else 2.5,
        "callback_requested": False,
        "language": "English",
        "resolution_time": random.randint(60, 180) if status == "Resolved" else 0
    }
    supabase.table("calls").insert(data).execute()
    return call_id

def test_conversation():
    """Test AI conversation flow"""
    print("\n" + "="*60)
    print("TESTING K-JULIA AI ENGINE")
    print("="*60 + "\n")

    test_cases = [
        "Power cut in our area for 8 hours",
        "Water supply not working for 2 days",
        "Road repair needed urgently",
        "Connect me to a human agent",
        "Thank you bye"
    ]

    for i, user_input in enumerate(test_cases, 1):
        print(f"\nTest {i}:")
        print(f"User: {user_input}")
        response = brain.process_message(user_input)
        print(f"K-Julia: {response}")

        # Log some to database
        if i <= 3:
            category = "Energy & Power" if "power" in user_input.lower() else \
                      "Water Supply" if "water" in user_input.lower() else \
                      "Roads"
            call_id = log_call(category, "Resolved")
            print(f"  [Logged as {call_id}]")

def test_database():
    """Test database operations"""
    print("\n" + "="*60)
    print("TESTING DATABASE OPERATIONS")
    print("="*60 + "\n")

    # Add sample data
    print("Adding sample complaints...")
    categories = [
        ("Energy & Power", "Resolved"),
        ("Water Supply", "Pending"),
        ("Roads", "Resolved"),
        ("Sanitation", "Escalated"),
        ("Healthcare", "Resolved"),
    ]

    for category, status in categories:
        call_id = log_call(category, status, escalated=(status == "Escalated"))
        print(f"  Added {call_id}: {category} - {status}")

    # Query data
    print("\nQuerying database...")
    result = supabase.table("calls").select("*").limit(10).execute()
    print(f"Total records in database: {len(result.data)}")

    if result.data:
        print("\nRecent calls:")
        for call in result.data[:5]:
            print(f"  {call['call_id']}: {call['issue_category']} - {call['status']}")

def main():
    print("\n" + "="*70)
    print("  K-JULIA AI VOICE AUTOMATION SYSTEM - SYSTEM TEST")
    print("="*70)

    # Test AI Engine
    test_conversation()

    # Reset brain for next test
    brain.reset()

    # Test Database
    test_database()

    print("\n" + "="*70)
    print("  ALL TESTS COMPLETED SUCCESSFULLY!")
    print("  Dashboard available at: http://localhost:5000")
    print("  Run: python3 main.py (for full interactive demo)")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
