"""
NOT YET SCOPED IN DETAIL.

Preview: assembles everything above into one structured summary dict for a
given recording -- this is what the new API endpoint and frontend panel will consume.
"""


def generate_report(record_name: str, heart_rate_bpm: float, hrv_metrics: dict, rhythm_classification: dict) -> dict:
    report = {
        "record_name": record_name,
        "heart_rate_bpm": float(heart_rate_bpm),
        "hrv_metrics": hrv_metrics,
        "rhythm_classification": rhythm_classification,
        "summary": {
            "status": "normal" if not any(rhythm_classification.values()) else "abnormal",
            "notes": "Rule-based classification applied on HR and HRV metrics."
        }
    }
    return report
