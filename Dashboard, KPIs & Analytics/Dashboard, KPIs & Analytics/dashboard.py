from flask import Flask, render_template, jsonify, request
from kpi_calculations import *
import json

app = Flask(__name__)

@app.route("/")
def dashboard():
    logs = load_logs()

    return render_template(
        "dashboard.html",
        overview=overview_kpis(logs),
        complaints=complaint_kpis(logs),
        escalation=escalation_kpis(logs),
        experience=experience_kpis(logs),
        analytics=call_analytics(logs),
        insights=realtime_insights(logs),
        trends=trend_analysis(logs),
        toll_free="1800-555-909",
        virtual_numbers=["VN-10452", "VN-88319", "VN-77120", "VN-55901"]
    )


@app.route("/api/stats")
def api_stats():
    """API endpoint for real-time stats"""
    logs = load_logs()
    return jsonify({
        "overview": overview_kpis(logs),
        "complaints": complaint_kpis(logs),
        "escalation": escalation_kpis(logs),
        "experience": experience_kpis(logs),
        "analytics": call_analytics(logs),
        "insights": realtime_insights(logs)
    })


@app.route("/api/filter", methods=["POST"])
def api_filter():
    """Filter data by date range, category, or status"""
    logs = load_logs()
    filters = request.json
    
    filtered_logs = logs
    
    if "category" in filters and filters["category"]:
        filtered_logs = [l for l in filtered_logs if l["issue_category"] == filters["category"]]
    
    if "status" in filters and filters["status"]:
        filtered_logs = [l for l in filtered_logs if l["status"] == filters["status"]]
    
    if "priority" in filters and filters["priority"]:
        filtered_logs = [l for l in filtered_logs if l.get("priority") == filters["priority"]]
    
    return jsonify({
        "overview": overview_kpis(filtered_logs),
        "complaints": complaint_kpis(filtered_logs),
        "count": len(filtered_logs)
    })


@app.route("/export")
def export_report():
    """Generate downloadable report"""
    logs = load_logs()
    report = {
        "overview": overview_kpis(logs),
        "complaints": complaint_kpis(logs),
        "escalation": escalation_kpis(logs),
        "experience": experience_kpis(logs),
        "insights": realtime_insights(logs)
    }
    return jsonify(report)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
