"""
NOT YET SCOPED IN DETAIL — we'll go deep on this together once
rr_interval_analysis.py is done and tested.

Preview of what's coming: SDNN, RMSSD, pNN50 — standard time-domain HRV
metrics, each computed directly from the rr_intervals array produced by
rr_interval_analysis.compute_rr_intervals(). Course connection: basic
operations on discrete-time signals (differences, mean, standard deviation).
"""

import numpy as np


def compute_sdnn(rr_intervals: np.ndarray) -> float:
    """Standard deviation of NN (normal-to-normal / R-R) intervals."""
    return float(np.std(rr_intervals, ddof=1))


def compute_rmssd(rr_intervals: np.ndarray) -> float:
    """Root mean square of successive R-R interval differences."""
    return float(np.sqrt(np.mean(np.diff(rr_intervals)**2)))


def compute_pnn50(rr_intervals: np.ndarray) -> float:
    """Percentage of successive R-R interval differences greater than 50ms."""
    diffs = np.abs(np.diff(rr_intervals))
    return float(np.sum(diffs > 0.05) / len(diffs) * 100)

