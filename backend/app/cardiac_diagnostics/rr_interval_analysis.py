
import numpy as np
from app.config import RR_RESAMPLE_HZ


def compute_rr_intervals(r_peak_indices: np.ndarray, fs: int) -> tuple[np.ndarray, np.ndarray]:
    rr_times = r_peak_indices[1:]/fs
    rr_intervals = np.diff(r_peak_indices)/fs
    return rr_times, rr_intervals



def resample_rr_uniform(
    rr_times: np.ndarray,
    rr_intervals: np.ndarray,
    resample_rate_hz: float = RR_RESAMPLE_HZ,
) -> tuple[np.ndarray, np.ndarray]:
    uniform_times = np.arange(rr_times[0], rr_times[-1], 1/resample_rate_hz)
    uniform_rr = np.interp(uniform_times, rr_times, rr_intervals)
    
    return uniform_times, uniform_rr


