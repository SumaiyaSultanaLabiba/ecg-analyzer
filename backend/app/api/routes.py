
from fastapi import APIRouter, HTTPException
from app.data.loader import list_available_records, load_record, load_annotation
from app.models.schemas import AnalysisResult, ValidationResult, RecordListResponse
from app.signal_processing.filters import clean_ecg_signal
from app.signal_processing.qrs_detector import detect_r_peaks
from app.signal_processing.heart_rate import calculate_heart_rate
from app.signal_processing.validation import calculate_validation_metrics
from app.signal_processing.spectrum import compute_frequency_spectrum



router = APIRouter()


@router.get("/records", response_model=RecordListResponse)
def get_records():
    return RecordListResponse(records = list_available_records())



# সাফা, তুমি নিচের দুইটা ফাংশন ইমপ্লিমেন্ট করবা। আমি এখন শুধু রান করার জন্য dummy return দিয়ে রাখতেছি।
@router.get("/analyze/{record_name}", response_model=AnalysisResult)
def analyze(record_name: str):
    raw_signal, frequency = load_record(record_name)
    
    filtered_signal = clean_ecg_signal(raw_signal, frequency)
    
    r_peak_indices = detect_r_peaks(filtered_signal, frequency)
    
    heart_rate_bpm = calculate_heart_rate(r_peak_indices, frequency)
    
    
    fft_freqs_raw, fft_magnitude_raw = compute_frequency_spectrum(raw_signal, frequency)
    
    fft_freqs_filtered, fft_magnitude_filtered = compute_frequency_spectrum(filtered_signal, frequency)
    
    return AnalysisResult(
        record_name=record_name,
        sampling_rate=frequency,
        raw_signal=raw_signal.tolist(),
        filtered_signal=filtered_signal.tolist(),
        r_peak_indices=[int(x) for x in r_peak_indices],
        heart_rate_bpm=heart_rate_bpm,
        fft_freqs=fft_freqs_raw.tolist(),
        fft_magnitude_raw=fft_magnitude_raw.tolist(),
        fft_magnitude_filtered=fft_magnitude_filtered.tolist(),
    )


@router.get("/validate/{record_name}", response_model=ValidationResult)
def validate(record_name: str):
    raw_signal, frequency = load_record(record_name)
    filtered_signal = clean_ecg_signal(raw_signal, frequency)
    detected_peaks = detect_r_peaks(filtered_signal, frequency)
    
    ground_truth_peaks = load_annotation(record_name)
    
    metrics = calculate_validation_metrics(detected_peaks, ground_truth_peaks)
    
    return ValidationResult(
        record_name=record_name,
        precision=metrics['precision'],
        recall=metrics['recall'],
        true_positive_count=metrics['true_positive_count'],
        false_positive_count=metrics['false_positive_count'],
        false_negative_count=metrics['false_negative_count'],
    )

