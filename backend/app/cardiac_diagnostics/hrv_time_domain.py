
import numpy as np


def compute_sdnn(rr_intervals: np.ndarray) -> float:
    return float(np.std(rr_intervals, ddof=1))


def compute_rmssd(rr_intervals: np.ndarray) -> float:
    return float(np.sqrt(np.mean(np.diff(rr_intervals)**2)))


def compute_pnn50(rr_intervals: np.ndarray) -> float:
    diffs = np.abs(np.diff(rr_intervals))
    return float(np.sum(diffs > 0.05) / len(diffs) * 100)

