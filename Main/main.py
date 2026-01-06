"""
main.py
Central orchestrator for K‑JULIA AI Voice Automation System

Integrates:
1. AI Engine (ai_engine)
2. Voice System (voice_system)
3. Dashboard & KPI Analytics (dashboard)
"""

# ─────────────────────────────────────────────
# STANDARD LIBRARIES
# ─────────────────────────────────────────────
import threading
import time
import sys
import csv
import os
from datetime import datetime

# ─────────────────────────────────────────────
# AI ENGINE (UNCHANGED)
# ─────────────────────────────────────────────
from ai_engine.conversation_manager import JuliaBrain
from ai_engine.escalation import EscalationManager

# ─────────────────────────────────────────────
# VOICE SYSTEM (UNCHANGED)
# ─────────────────────────────────────────────
from voice_system.voice_controller import handle_voice_interaction
import voice_system.ai_bridge as ai_bridge

# ─────────────────────────────────────────────
# NEW DASHBOARD (UPDATED)
# ─────────────────────────────────────────────
from dashboard.dashboard import app as dashboard_app

# ─────────────────────────────────────────────
# GLOBAL OBJECTS
# ─────────────────────────────────────────────
brain = JuliaBrain()
escalation_manager = EscalationManager()

LOG_FILE = "logs.csv"

# ─────────────────────────────────────────────
# DASHBOARD LOGGING (MATCHES NEW CSV FORMAT)
# ─────────────────────────────────────────────
def log_call(
    call_id,
    call_type,
    virtual_number,
    issue_category,
    status,
    duration,
    escalated,
    citizen_feedback,
    priority,
    resolution_time,
    agent_type,
    satisfaction_score,
    callback_requested,
    language
):
    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "call_id",
                "call_type",
                "virtual_number",
                "issue_category",
                "status",
                "duration",
                "escalated",
                "citizen_feedback",
                "timestamp",
                "priority",
                "resolution_time",
                "agent_type",
                "satisfaction_score",
                "callback_requested",
                "language"
            ])

        writer.writerow([
            call_id,
            call_type,
            virtual_number,
            issue_category,
            status,
            duration,
            escalated,
            citizen_feedback,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            priority,
            resolution_time,
            agent_type,
            satisfaction_score,
            callback_requested,
            language
        ])

# ─────────────────────────────────────────────
# REAL AI ↔ VOICE BRIDGE (UNCHANGED LOGIC)
# ─────────────────────────────────────────────
def real_brain_bridge(intent_packet):
    """
    Connects Voice System → AI Engine
    Logs output to dashboard-compatible CSV
    """

    user_text = intent_packet.get("query", "")
    domain = intent_packet.get("domain", "General")

    response = brain.process_message(user_text)

    # Simple demo-safe escalation logic
    escalated = "Yes" if "human" in response.lower() else "No"
    status = "Escalated" if escalated == "Yes" else "Resolved"
    agent_type = "AI"

    call_id = f"C{int(time.time())}"

    log_call(
        call_id=call_id,
        call_type="Inbound",
        virtual_number="TOLL_FREE",
        issue_category=domain.title(),
        status=status,
        duration=180,
        escalated=escalated,
        citizen_feedback="Satisfied" if escalated == "No" else "Dissatisfied",
        priority="Medium",
        resolution_time=120 if escalated == "No" else 0,
        agent_type=agent_type,
        satisfaction_score=4.5 if escalated == "No" else 2.0,
        callback_requested="No",
        language="English"
    )

    return response

# Inject real AI logic into voice system
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
    print("==========================================")
    print("   K‑JULIA AI VOICE AUTOMATION SYSTEM")
    print("==========================================")

    # Start Dashboard (Flask)
    dashboard_thread = threading.Thread(
        target=run_dashboard,
        daemon=True
    )
    dashboard_thread.start()

    # Start Voice System (blocking)
    try:
        run_voice_system()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down system safely.")
        sys.exit(0)

# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()
