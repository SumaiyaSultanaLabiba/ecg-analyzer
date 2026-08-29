import numpy as np

def calculate_heart_rate(r_peaks,fs):
    if len(r_peaks)<2:
        return 0.0
    rr_intervals=np.diff(r_peaks)/fs
    mean_rr_interval=np.mean(rr_intervals)
    heart_rate_bpm=60.0/mean_rr_interval
    return float(np.round(heart_rate_bpm,2))