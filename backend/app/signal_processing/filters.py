import numpy as np
from scipy.signal import butter,iirnotch,filtfilt

#y_n=b_o*x_n+b_1*x_(n-1)+b_2*x_(n-2)-a_1*y_(n-1)-a_2*y(n-2)
#butter a,b coefficient gulo count kore
#filtfilt puro signal er upor loop chaliye y_n hisab kore,lfilter shudhu samner dike loop chalai,ejonno right shift hoi ektu,eijonno filtfilt e forward er por backwarde ioop chalano hoi jate shiftingn 0 hoi
#order joto beshi ,cut off er por noise  toto druto kome,kintu khub beshi hole signale instability toiri hoi
def apply_bandpass_filter(data:np.ndarray,fs:float,lowcut:float=0.5,highcut:float=40.0,order:int=2)->np.ndarray:
    nyquist=0.5*fs
    low=lowcut/nyquist
    high=highcut/nyquist
    b,a=butter(order,[low,high],btype='bandpass')
    return filtfilt(b,a,data)
def apply_notch_filter(data,fs,notch_freq=60.0,Q=30.0):
    nyquist=0.5*fs
    normalized_freq=notch_freq/nyquist
    b,a=iirnotch(normalized_freq,Q)
    return filtfilt(b,a,data)
def clean_ecg_signal(raw_signal,fs):
    notched=apply_notch_filter(raw_signal,fs,60.0,30.0)
    filtered=apply_bandpass_filter(notched,fs,0.5,40.0)
    return filtered


