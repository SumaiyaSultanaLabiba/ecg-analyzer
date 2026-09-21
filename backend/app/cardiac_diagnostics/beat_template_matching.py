
import numpy as np


def build_beat_template(ecg_signal: np.ndarray, r_peak_indices: np.ndarray, fs: int) -> np.ndarray:
    pre = int(0.2*fs)
    post = int(0.4*fs)
    beats = []
    
    for idx in r_peak_indices:
        if idx-pre>=0 and idx+post<len(ecg_signal):
            beat = ecg_signal[idx-pre:idx+post]
            beats.append(beat)
            
    if not beats:
        return np.array([])
    
    beats = np.vstack(beats)
    template = np.mean(beats, axis=0)  
    return template      



def flag_abnormal_beats(ecg_signal: np.ndarray, r_peak_indices: np.ndarray, template: np.ndarray, fs: int):
    pre = int(0.2*fs)
    post = int(0.4*fs)
    abnormal_indices = []
        
    for idx in r_peak_indices:
        if idx-pre>=0 and idx+post<len(ecg_signal):
            beat = ecg_signal[idx-pre:idx+post]
            numerator = np.sum(beat*template)
            denominator = np.sqrt(np.sum(beat**2) * np.sum(template**2))
            corr = numerator/denominator if denominator>0 else 0
            
            if corr<0.8:
                abnormal_indices.append(idx)       
    return abnormal_indices


