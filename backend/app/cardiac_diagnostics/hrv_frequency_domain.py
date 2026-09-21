
import numpy as np


def dft(x):
    x = np.asarray(x, dtype = complex)
    N = len(x)
    X = np.zeros(N, dtype = complex)
    
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j*np.pi*k*n/N)
    return X


def periodogram(segment, fs):
    N = len(segment)
    window = np.hamming(N)    
    U = 1/N * np.sum(window**2)    
    xw = segment * window
    X = dft(xw)
    psd = (1 / (fs*N*U)) * (np.abs(X)**2)
    freqs = np.arange(N) * fs / N
    psd_one_sided = psd[:N//2 + 1].copy()
    psd_one_sided[1:-1] *= 2
    return freqs[:N//2 +1], psd_one_sided


def compute_psd_welch(uniform_rr: np.ndarray, resample_rate_hz: float):
    nperseg = 256
    noverlap = 128
    
    if len(uniform_rr) < nperseg:
        nperseg = len(uniform_rr)
        noverlap = nperseg // 2

    if nperseg < 8:
        raise ValueError(f"Recording too short ({len(uniform_rr)} resampled samples) to compute a meaningful PSD estimate.")
               
    step = nperseg - noverlap
    psd_accum = []
    freqs = None
    
    for start in range(0, len(uniform_rr)-nperseg+1, step):
        segment = uniform_rr[start : start+nperseg]
        f, p = periodogram(segment, resample_rate_hz)
        
        if freqs is None:
            freqs = f
        psd_accum.append(p)    
    psd = np.mean(psd_accum, axis=0)    
    return freqs, psd
        


def compute_lf_hf_ratio(freqs: np.ndarray, psd: np.ndarray) -> dict:
    lf_band = (freqs >= 0.04) & (freqs < 0.15)
    hf_band = (freqs >= 0.15) & (freqs < 0.4)
    lf_power = np.trapezoid(psd[lf_band], freqs[lf_band])
    hf_power = np.trapezoid(psd[hf_band], freqs[hf_band])
    
    return{
        "lf_power" : float(lf_power),
        "hf_power" : float(hf_power),
        "lf_hf_ratio" : float(lf_power / hf_power) if hf_power > 0 else np.nan,
    }
    
