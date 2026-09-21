

def classify_rhythm(heart_rate_bpm: float, hrv_metrics: dict, abnormal_beat_count: int) -> dict:
    
    flags={
        "tachycardia" : heart_rate_bpm>100,
        "bradycardia" : heart_rate_bpm<60,
        "irregular_rhythm" : hrv_metrics.get("sdnn_ms", 0)>100,
        "abnormal_beats_detected" : abnormal_beat_count>0,     
    }
    return flags

