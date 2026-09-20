"""
Builds the R-R interval (tachogram) signal from detected R-peaks, and resamples
it onto a uniform time grid — the necessary first step before any HRV metric
(time-domain or frequency-domain) can be validly computed.

Course connection: Sampling theorem, interpolation (from your syllabus's
"Sampling: the sampling theorem, interpolation, aliasing" topic).

Input to this module: r_peak_indices (from your teammate's qrs_detector.py) + fs
Output: everything downstream (hrv_time_domain.py, hrv_frequency_domain.py) is
built on what this file produces — get this one right first.
"""

import numpy as np
from app.config import RR_RESAMPLE_HZ


def compute_rr_intervals(r_peak_indices: np.ndarray, fs: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Convert R-peak sample indices into R-R intervals (in seconds), each
    timestamped at the point in time it "belongs to".

    Args:
        r_peak_indices: sample indices of detected heartbeats (from qrs_detector.py)
        fs: sampling rate in Hz
    Returns:
        rr_times: timestamps (in seconds) for each R-R interval — convention:
                  use the time of the SECOND peak in each pair, since that's
                  when the interval "completes"
        rr_intervals: R-R interval durations in seconds, same length as rr_times

    Hints:
        - len(rr_intervals) will be len(r_peak_indices) - 1 (intervals are GAPS
          between peaks, so N peaks gives N-1 intervals)
        - rr_intervals[i] = (r_peak_indices[i+1] - r_peak_indices[i]) / fs
        - rr_times[i] = r_peak_indices[i+1] / fs   (timestamp of the second peak)
        - np.diff() is your friend for computing the intervals in one line
    """
    # TODO: implement using np.diff(r_peak_indices) / fs for the intervals,
    # and r_peak_indices[1:] / fs for the corresponding timestamps
    rr_times = r_peak_indices[1:]/fs
    rr_intervals = np.diff(r_peak_indices)/fs
    return rr_times, rr_intervals



def resample_rr_uniform(
    rr_times: np.ndarray,
    rr_intervals: np.ndarray,
    resample_rate_hz: float = RR_RESAMPLE_HZ,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Resample the irregularly-timed R-R interval signal onto a UNIFORM time grid,
    using interpolation. This is the step that makes frequency-domain HRV
    analysis (Welch's method / FFT) mathematically valid later.

    Args:
        rr_times: irregular timestamps from compute_rr_intervals()
        rr_intervals: R-R interval values at those timestamps
        resample_rate_hz: target uniform sampling rate. 4 Hz is a standard
                           choice in HRV literature — think about why: it must
                           satisfy Nyquist for the highest HRV frequency band
                           you care about (HF band goes up to 0.4 Hz, so even
                           1 Hz would technically satisfy Nyquist — 4 Hz gives
                           comfortable margin and smoother interpolation)
    Returns:
        uniform_times: evenly-spaced timestamps at resample_rate_hz
        uniform_rr: interpolated R-R interval values at those timestamps

    Hints:
        - Build uniform_times with np.arange(rr_times[0], rr_times[-1], 1/resample_rate_hz)
        - Use np.interp(uniform_times, rr_times, rr_intervals) to do the
          actual interpolation (linear interpolation — fine for this use case)
    """
    # TODO: implement using np.arange + np.interp as hinted above
    uniform_times = np.arange(rr_times[0], rr_times[-1], 1/resample_rate_hz)
    uniform_rr = np.interp(uniform_times, rr_times, rr_intervals)
    
    return uniform_times, uniform_rr


