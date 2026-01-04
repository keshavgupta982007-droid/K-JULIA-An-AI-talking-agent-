"""
main.py
Unified entry point for K‑Julia AI Voice Automation System

Integrates:
1. AI Engine (ai_engine / JuliaBrain)
2. Voice System (voice_system)
3. Dashboard & KPI Analytics (dashboard)
"""

# ─────────────────────────────────────────────
# STANDARD LIBS
# ─────────────────────────────────────────────
import threading
import time
import sys
from datetime import datetime
import csv
import os

# ─────────────────────────────────────────────
# AI ENGINE IMPORTS
# ─────────────────────────────────────────────
from ai_engine import JuliaBrain
from ai_engine.escalation import EscalationManager

# ─────────────────────────────────────────────
# VOICE SYSTEM IMPORTS
# ─────────────────────────────────────────────
from voice_system.voice_controller import handle_voice_interaction
import voice_system.ai_bridge as ai_bridge

# ─────────────────────────────────────────────
# DASHBOARD IMPORT
# ─────────────────────────────────────────────
from dashboard.dashboard import app as dashboard_app


# ─────────────────────────────────────────────
# GLOBAL OBJECTS
# ─────────────────────────────────────────────
brain = JuliaBrain()
escalation_manager = EscalationManager()

LOG_FILE = "logs.csv"


# ─────────────────────────────────────────────
# LOGGING UTIL (feeds KPI + Dashboard)
# ─────────────────────────────────────────────
def log_call(
    call_type="Inbound",
    issue_category="General",
    status="Resolved",
    escalated="No",
    priority="Medium",
    duration=60,
    agent_type="AI",
    citizen_feedback="Satisfied",
    language="English"
):
    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "timestamp", "call_type", "issue_category", "status",
                "escalated", "priority", "duration", "agent_type",
                "citizen_feedback", "language"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            call_type,
            issue_category,
            status,
            escalated,
            priority,
            duration,
            agent_type,
            citizen_feedback,
            language
        ])


# ─────────────────────────────────────────────
# REAL AI BRIDGE (PATCH VOICE → BRAIN)
# ─────────────────────────────────────────────
def real_brain_bridge(intent_packet):
    """
    This replaces the placeholder AI bridge.
    Voice system → JuliaBrain → text response
    """

    user_text = intent_packet.get("query", "")
    domain = intent_packet.get("domain", "general")

    # Brain response
    response = brain.process_message(user_text)

    # Basic escalation check (simplified for demo)
    escalated = "Yes" if "human" in response.lower() else "No"

    # Log for dashboard/KPIs
    log_call(
        call_type="Inbound",
        issue_category=domain.title(),
        status="Escalated" if escalated == "Yes" else "Resolved",
        escalated=escalated,
        agent_type="AI"
    )

    return response


# Inject real brain into voice system
ai_bridge.send_to_brain = real_brain_bridge


# ─────────────────────────────────────────────
# THREAD RUNNERS
# ─────────────────────────────────────────────
def run_voice_system():
    print("🎧 Voice system started...")
    while True:
        handle_voice_interaction()
        time.sleep(0.5)


def run_dashboard():
    print("📊 Dashboard running at http://localhost:5000")
    dashboard_app.run(
        debug=False,
        host="0.0.0.0",
        port=5000,
        use_reloader=False
    )


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main():
    print("========================================")
    print("   K‑JULIA AI VOICE AUTOMATION SYSTEM   ")
    print("========================================")

    # Start dashboard in background
    dashboard_thread = threading.Thread(target=run_dashboard, daemon=True)
    dashboard_thread.start()

    # Start voice system (blocking)
    try:
        run_voice_system()
    except KeyboardInterrupt:
        print("\n🛑 System shutting down.")
        sys.exit(0)


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()
