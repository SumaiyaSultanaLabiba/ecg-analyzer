
# all pydantic models. We may use these models for exchanging data between backend and frontend
# these are just some initial ideas. 
# When you start to build the signal processing pipeline, you may change the fields or anything as needed.

from pydantic import BaseModel



# when user selects any record, the record_name will be sent to the backend as AnalysisRequest model
class AnalysisRequest(BaseModel):
    record_name: str



# after completing all processing steps, the result will be sent to the frontend as AnalysisResult model
class AnalysisResult(BaseModel):
    record_name: str
    sampling_rate: int
    raw_signal: list[float]
    filtered_signal: list[float]
    r_peak_indices: list[int]
    heart_rate_bpm: float
    fft_freqs: list[float]
    fft_magnitude_raw: list[float]
    fft_magnitude_filtered: list[float]



# after testing the accuracy of our system against the Physionet's expert-annotations, 
# we will send the validation result as ValidationResult model
class ValidationResult(BaseModel):
    record_name: str
    precision: float
    recall: float
    true_positive_count: int
    false_positive_count: int
    false_negative_count: int


# list of all available records from our data folder (that we have already collected from PhysioNet)
# users can choose any of these records and send it for analyzing
class RecordListResponse(BaseModel):
    records: list[str]


class HRVMetrics(BaseModel):
    sdnn_ms: float
    rmssd_ms: float
    pnn50_percent: float
    lf_power: float
    hf_power: float
    lf_hf_ratio: float

class RhythmClassification(BaseModel):
    tachycardia: bool
    bradycardia: bool
    irregular_rhythm: bool
    abnormal_beats_detected: bool


class CardiacDiagnosticsResult(BaseModel):
    record_name: str
    rr_times: list[float]
    rr_intervals: list[float]
    psd_freqs: list[float]
    psd_values: list[float]
    hrv_metrics: HRVMetrics
    rhythm_classification: RhythmClassification
    abnormal_beat_indices: list[int]
    status: str
    notes: str
    
    
    