import numpy as np
from scipy.signal import find_peaks
from .filters import apply_bandpass_filter

def detect_r_peaks(filtered_signal,fs):
    #qrs part tuku extract korchi
    bandpass_filtered_signal=apply_bandpass_filter(filtered_signal,fs,5.0,15.0,1)

    # 5 point derivative approximation:y_n=2x_n+x_(n-1)-x_(n-3)-2x(n-4)/8
    derivative_kernel=np.array([2,1,0,-1,-2])*fs/8.0
    derived_signal=np.convolve(bandpass_filtered_signal,derivative_kernel,mode='same')

    #squaring jate sum korar somoi plus minus katakati na hoi ebong R peak onek uchu hoi
    squared_signal=derived_signal**2

    #moving window integration 1/m *sum of x_n to x_(n-m+1)
    window_size=int(0.150*fs)
    integration_kernel=np.ones(window_size)/window_size
    integrated_signal=np.convolve(squared_signal,integration_kernel,mode='same')

    #peak detection
    min_distance=int(0.200*fs)
    threshold=np.mean(integrated_signal)*1.5
    peaks,_=find_peaks(integrated_signal, distance=min_distance, height=threshold)
    
    # find peak positions in original filtered signal
    search_window = int(0.075 * fs)  # 75ms window around detected peak
    refined_peaks = []
    
    for peak_idx in peaks:
        start = max(0, peak_idx - search_window)
        end = min(len(filtered_signal), peak_idx + search_window)
        
        # Find max in the filtered signal within this window
        local_segment = filtered_signal[start:end]
        local_max_idx = np.argmax(local_segment)
        
        refined_peak = start + local_max_idx
        refined_peaks.append(refined_peak)
    
    return np.array(refined_peaks)




