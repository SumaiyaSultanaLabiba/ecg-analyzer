import numpy as np
from scipy.fft import rfft, rfftfreq


def compute_frequency_spectrum(signal, sampling_rate):
    N = len(signal)
    fft_values = rfft(signal)
    fft_magnitude = np.abs(fft_values)
    fft_freqs = rfftfreq(N, 1.0 / sampling_rate)
    return fft_freqs, fft_magnitude
