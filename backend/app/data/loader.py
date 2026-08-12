
import wfdb
import numpy as np
from app.config import PHYSIONET_DB_NAME, SECONDS


# এই ফাইলটা আমি কমপ্লিট করে রাখছি,আপাতত কোনো মডিফিকেশন লাগবে না I guess। 
# পরে শুধু অনেকগুলা রেকর্ড নিয়ে কাজ করার জন্য list_available_records -কে স্কেলআপ করতে হবে।


def list_available_records():
    return ['100']
    

def load_record(record_name: str):
    header = wfdb.rdheader(record_name = record_name, pn_dir = PHYSIONET_DB_NAME)
    frequency = header.fs
    n_samples = SECONDS * frequency
    record = wfdb.rdrecord(record_name = record_name, sampfrom = 0, sampto = n_samples, pn_dir = PHYSIONET_DB_NAME)
    signal = record.p_signal[:, 0]
    return np.array(signal), frequency


def load_annotation(record_name: str):
    header = wfdb.rdheader(record_name = record_name, pn_dir = PHYSIONET_DB_NAME)
    frequency = header.fs
    n_samples = SECONDS * frequency
    annotation = wfdb.rdann(record_name= record_name, extension= 'atr', sampfrom= 0, sampto= n_samples, pn_dir=PHYSIONET_DB_NAME)
    return np.array(annotation.sample)
    

