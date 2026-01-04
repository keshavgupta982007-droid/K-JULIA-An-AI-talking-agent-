import csv
from datetime import datetime
from collections import defaultdict

LOG_FILE = "logs.csv"

def load_logs():
    with open(LOG_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# 1️⃣ SYSTEM OVERVIEW (Enhanced)
def overview_kpis(logs):
    total = len(logs)
    inbound = sum(1 for l in logs if l["call_type"] == "Inbound")
    outbound = total - inbound
    avg_duration = round(sum(int(l["duration"]) for l in logs) / total, 2) if total > 0 else 0
    
    # AI vs Human handling
    ai_handled = sum(1 for l in logs if l.get("agent_type", "AI") == "AI")
    human_handled = total - ai_handled
    ai_efficiency = round((ai_handled / total) * 100, 2) if total > 0 else 0

    return {
        "total_calls": total,
        "inbound_calls": inbound,
        "outbound_calls": outbound,
        "avg_duration": avg_duration,
        "ai_handled": ai_handled,
        "human_handled": human_handled,
        "ai_efficiency": ai_efficiency
    }


# 2️⃣ COMPLAINT INTELLIGENCE (Enhanced)
def complaint_kpis(logs):
    total = len(logs)
    resolved = [l for l in logs if l["status"] == "Resolved"]
    pending = [l for l in logs if l["status"] == "Pending"]
    escalated = [l for l in logs if l["status"] == "Escalated"]
    auto_resolved = [l for l in resolved if l["escalated"] == "No"]

    resolution_rate = round((len(resolved) / total) * 100, 2) if total > 0 else 0
    
    # Average resolution time for resolved complaints
    resolved_times = [int(l.get("resolution_time", 0)) for l in resolved if l.get("resolution_time")]
    avg_resolution_time = round(sum(resolved_times) / len(resolved_times), 2) if resolved_times else 0

    # Category breakdown
    category_counts = defaultdict(int)
    for l in logs:
        category_counts[l["issue_category"]] += 1
    
    top_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    return {
        "total": total,
        "resolved": len(resolved),
        "auto_resolved": len(auto_resolved),
        "pending": len(pending),
        "escalated": len(escalated),
        "resolution_rate": resolution_rate,
        "avg_resolution_time": avg_resolution_time,
        "top_categories": top_categories
    }


# 3️⃣ ESCALATION & SLA (Enhanced)
def escalation_kpis(logs):
    escalated = [l for l in logs if l["escalated"] == "Yes"]
    
    # Priority-based SLA thresholds (in seconds)
    sla_thresholds = {
        "Critical": 300,   # 5 minutes
        "High": 600,       # 10 minutes
        "Medium": 1200,    # 20 minutes
        "Low": 1800        # 30 minutes
    }
    
    sla_breached = []
    for l in escalated:
        priority = l.get("priority", "Medium")
        threshold = sla_thresholds.get(priority, 1200)
        if int(l["duration"]) > threshold:
            sla_breached.append(l)

    rate = round((len(escalated) / len(logs)) * 100, 2) if logs else 0
    sla_compliance = round(((len(escalated) - len(sla_breached)) / len(escalated)) * 100, 2) if escalated else 100

    # Priority distribution
    priority_counts = defaultdict(int)
    for l in logs:
        priority_counts[l.get("priority", "Medium")] += 1

    return {
        "calls_escalated": len(escalated),
        "escalation_rate": rate,
        "sla_breached": len(sla_breached),
        "sla_compliance": sla_compliance,
        "priority_distribution": dict(priority_counts)
    }


# 4️⃣ CITIZEN EXPERIENCE (Enhanced)
def experience_kpis(logs):
    satisfied = [l for l in logs if l["citizen_feedback"] == "Satisfied"]
    dissatisfied = [l for l in logs if l["citizen_feedback"] == "Dissatisfied"]

    csat = round((len(satisfied) / len(logs)) * 100, 2) if logs else 0
    
    # Average satisfaction score
    scores = [float(l.get("satisfaction_score", 0)) for l in logs if l.get("satisfaction_score")]
    avg_score = round(sum(scores) / len(scores), 2) if scores else 0
    
    # Callback requests
    callback_requested = sum(1 for l in logs if l.get("callback_requested", "No") == "Yes")
    
    # Language distribution
    language_counts = defaultdict(int)
    for l in logs:
        language_counts[l.get("language", "English")] += 1

    return {
        "satisfied": len(satisfied),
        "dissatisfied": len(dissatisfied),
        "csat": csat,
        "avg_satisfaction_score": avg_score,
        "callback_requested": callback_requested,
        "language_distribution": dict(language_counts)
    }


# 5️⃣ CALL ANALYTICS (Enhanced)
def call_analytics(logs):
    duration_buckets = {
        "<1 min": 0,
        "1-3 min": 0,
        "3-5 min": 0,
        "5-7 min": 0,
        "7+ min": 0
    }

    for l in logs:
        d = int(l["duration"])
        if d < 60:
            duration_buckets["<1 min"] += 1
        elif d <= 180:
            duration_buckets["1-3 min"] += 1
        elif d <= 300:
            duration_buckets["3-5 min"] += 1
        elif d <= 420:
            duration_buckets["5-7 min"] += 1
        else:
            duration_buckets["7+ min"] += 1

    # Hourly distribution (if timestamp available)
    hourly_distribution = defaultdict(int)
    for l in logs:
        if "timestamp" in l and l["timestamp"]:
            try:
                hour = datetime.strptime(l["timestamp"], "%Y-%m-%d %H:%M:%S").hour
                hourly_distribution[hour] += 1
            except:
                pass

    return {
        "inbound": sum(1 for l in logs if l["call_type"] == "Inbound"),
        "outbound": sum(1 for l in logs if l["call_type"] == "Outbound"),
        "duration_distribution": duration_buckets,
        "hourly_distribution": dict(sorted(hourly_distribution.items()))
    }


# 6️⃣ REAL-TIME INSIGHTS
def realtime_insights(logs):
    """Generate actionable insights for dashboard"""
    insights = []
    
    # High escalation rate warning
    escalated = sum(1 for l in logs if l["escalated"] == "Yes")
    escalation_rate = (escalated / len(logs)) * 100 if logs else 0
    if escalation_rate > 30:
        insights.append({
            "type": "warning",
            "message": f"High escalation rate: {escalation_rate:.1f}%. Review AI training data."
        })
    
    # Low CSAT warning
    satisfied = sum(1 for l in logs if l["citizen_feedback"] == "Satisfied")
    csat = (satisfied / len(logs)) * 100 if logs else 0
    if csat < 70:
        insights.append({
            "type": "alert",
            "message": f"CSAT below target: {csat:.1f}%. Immediate attention required."
        })
    
    # SLA compliance
    sla_data = escalation_kpis(logs)
    if sla_data["sla_compliance"] < 90:
        insights.append({
            "type": "warning",
            "message": f"SLA compliance at {sla_data['sla_compliance']:.1f}%. Resource allocation needed."
        })
    
    # High callback rate
    callbacks = sum(1 for l in logs if l.get("callback_requested") == "Yes")
    callback_rate = (callbacks / len(logs)) * 100 if logs else 0
    if callback_rate > 20:
        insights.append({
            "type": "info",
            "message": f"{callback_rate:.1f}% citizens requesting callbacks. Follow-up team capacity check."
        })
    
    # AI efficiency
    ai_handled = sum(1 for l in logs if l.get("agent_type") == "AI")
    ai_efficiency = (ai_handled / len(logs)) * 100 if logs else 0
    if ai_efficiency > 80:
        insights.append({
            "type": "success",
            "message": f"Excellent AI efficiency: {ai_efficiency:.1f}%. System performing optimally."
        })
    
    return insights


# 7️⃣ TREND ANALYSIS
def trend_analysis(logs):
    """Analyze trends over time"""
    daily_stats = defaultdict(lambda: {
        "total": 0,
        "resolved": 0,
        "escalated": 0,
        "satisfied": 0
    })
    
    for l in logs:
        if "timestamp" in l and l["timestamp"]:
            try:
                date = datetime.strptime(l["timestamp"], "%Y-%m-%d %H:%M:%S").date()
                daily_stats[str(date)]["total"] += 1
                if l["status"] == "Resolved":
                    daily_stats[str(date)]["resolved"] += 1
                if l["escalated"] == "Yes":
                    daily_stats[str(date)]["escalated"] += 1
                if l["citizen_feedback"] == "Satisfied":
                    daily_stats[str(date)]["satisfied"] += 1
            except:
                pass
    
    return dict(sorted(daily_stats.items()))