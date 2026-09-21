from fastapi import APIRouter, HTTPException
from app.data.loader import list_available_records, load_record, load_annotation
from app.models.schemas import AnalysisResult, ValidationResult, RecordListResponse, HRVMetrics, RhythmClassification, CardiacDiagnosticsResult
from app.signal_processing.filters import clean_ecg_signal
from app.signal_processing.qrs_detector import detect_r_peaks
from app.signal_processing.heart_rate import calculate_heart_rate
from app.signal_processing.validation import calculate_validation_metrics
from app.signal_processing.spectrum import compute_frequency_spectrum
from app.config import RR_RESAMPLE_HZ
from app.cardiac_diagnostics.rr_interval_analysis import compute_rr_intervals, resample_rr_uniform
from app.cardiac_diagnostics.hrv_time_domain import compute_sdnn, compute_rmssd, compute_pnn50
from app.cardiac_diagnostics.hrv_frequency_domain import compute_psd_welch, compute_lf_hf_ratio
from app.cardiac_diagnostics.beat_template_matching import build_beat_template, flag_abnormal_beats
from app.cardiac_diagnostics.arrhythmia_rules import classify_rhythm
from app.cardiac_diagnostics.diagnostic_report import generate_report



router = APIRouter()


@router.get("/records", response_model=RecordListResponse)
def get_records():
    return RecordListResponse(records = list_available_records())



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



@router.get("/diagnose/{record_name}", response_model=CardiacDiagnosticsResult)
def diagnose(record_name:str):
    raw_signal, frequency = load_record(record_name)
    filtered_signal = clean_ecg_signal(raw_signal, frequency)
    r_peak_indices = detect_r_peaks(filtered_signal, frequency)
    heart_rate_bpm = calculate_heart_rate(r_peak_indices, frequency)
    rr_times, rr_intervals = compute_rr_intervals(r_peak_indices, frequency)
    uniform_times, uniform_rr = resample_rr_uniform(rr_times, rr_intervals, RR_RESAMPLE_HZ)
    psd_freqs, psd_values = compute_psd_welch(uniform_rr, RR_RESAMPLE_HZ)
    freq_domain_metrics = compute_lf_hf_ratio(psd_freqs, psd_values)
    
    hrv_metrics_dict = {
        "sdnn_ms": compute_sdnn(rr_intervals)*1000,
        "rmssd_ms": compute_rmssd(rr_intervals)*1000,
        "pnn50_percent": compute_pnn50(rr_intervals),
        **freq_domain_metrics,
    }
    
    template = build_beat_template(filtered_signal, r_peak_indices, frequency)
    abnormal_beat_indices = flag_abnormal_beats(filtered_signal, r_peak_indices, template, frequency)
    rhythm_classification_dict = classify_rhythm(heart_rate_bpm, hrv_metrics_dict, len(abnormal_beat_indices))
    report = generate_report(record_name, heart_rate_bpm, hrv_metrics_dict, rhythm_classification_dict)
    
    return CardiacDiagnosticsResult(
        record_name=record_name,
        rr_times=rr_times.tolist(),
        rr_intervals=rr_intervals.tolist(),
        psd_freqs=psd_freqs.tolist(),
        psd_values=psd_values.tolist(),
        hrv_metrics=HRVMetrics(**hrv_metrics_dict),
        rhythm_classification=RhythmClassification(**rhythm_classification_dict),
        abnormal_beat_indices=[int(x) for x in abnormal_beat_indices],
        status=report["summary"]["status"],
        notes=report["summary"]["notes"],
    )
    
    