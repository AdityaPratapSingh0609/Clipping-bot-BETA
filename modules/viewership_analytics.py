"""Viewership Analytics Engine for India, United States, and Spain.
Calculates high-velocity peak windows for YouTube Shorts and Instagram Reels.
"""
from datetime import datetime

class ViewershipAnalytics:
    @staticmethod
    def get_peak_status():
        now = datetime.now()
        h = now.hour + now.minute / 60.0

        india_peak = (18.0 <= h <= 22.5) or (12.0 <= h <= 14.5)
        us_peak = (22.5 <= h <= 24.0) or (0.0 <= h <= 1.5) or (4.5 <= h <= 8.5)
        spain_peak = (23.5 <= h <= 24.0) or (0.0 <= h <= 4.5)

        return {
            "current_time_ist": now.strftime("%I:%M %p"),
            "india": {
                "is_peak": india_peak,
                "recommended_gap_seconds": 150 if india_peak else 1800,
                "window": "18:00 - 22:30 IST (Prime Evening) & 12:00 - 14:30 IST (Lunch)"
            },
            "united_states": {
                "is_peak": us_peak,
                "recommended_gap_seconds": 150 if us_peak else 1800,
                "window": "22:30 - 01:30 IST (US Lunch/Afternoon) & 04:30 - 08:30 IST (US Prime Evening)"
            },
            "spain_latam": {
                "is_peak": spain_peak,
                "recommended_gap_seconds": 150 if spain_peak else 1800,
                "window": "23:30 - 04:30 IST (Spain/Europe Prime Evening)"
            }
        }
