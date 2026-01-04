"""
dashboard package

Provides:
- Flask web dashboard
- KPI & analytics calculations
- Visualization of call logs and system performance

Reads data from logs.csv (read-only).
"""

# Optional: expose Flask app
from .dashboard import app

__all__ = [
    "app"
]