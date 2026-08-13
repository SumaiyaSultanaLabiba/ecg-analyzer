
import wfdb
import numpy as np
from app.config import PHYSIONET_DB_NAME, SECONDS


# এই ফাইলটা আমি কমপ্লিট করে রাখছি,আপাতত কোনো মডিফিকেশন লাগবে না I guess। 
# পরে শুধু অনেকগুলা রেকর্ড নিয়ে কাজ করার জন্য list_available_records -কে স্কেলআপ করতে হবে।


def list_available_records():
    return ["100", "101", "102", "103", "104", "105", "106", "107", "108", "109",
    "111", "112", "113", "114", "115", "116", "117", "118", "119", "121",
    "122", "123", "124", "200", "201", "202", "203", "205", "207", "208",
    "209", "210", "212", "213", "214", "215", "217", "219", "220", "221",
    "222", "223", "228", "230", "231", "232", "233", "234",]
    

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
    

