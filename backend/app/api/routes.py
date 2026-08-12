
from fastapi import APIRouter, HTTPException
from app.data.loader import list_available_records, load_record, load_annotation
from app.models.schemas import AnalysisResult, ValidationResult, RecordListResponse



router = APIRouter()


@router.get("/records", response_model=RecordListResponse)
def get_records():
    return RecordListResponse(records = list_available_records())



# সাফা, তুমি নিচের দুইটা ফাংশন ইমপ্লিমেন্ট করবা। আমি এখন শুধু রান করার জন্য dummy return দিয়ে রাখতেছি।
@router.get("/analyze/{record_name}", response_model=AnalysisResult)
def analyze(record_name: str):
    raw_signal, frequency = load_record(record_name)
    return AnalysisResult(
        record_name = record_name,
        sampling_rate = frequency,
        raw_signal = raw_signal.tolist(),
        filtered_signal = raw_signal.tolist(),
        r_peak_indices = [int(x) for x in raw_signal.tolist()],
        heart_rate_bpm = 70.6,
        fft_freqs = raw_signal.tolist(),
        fft_magnitude_raw = raw_signal.tolist(),
        fft_magnitude_filtered = raw_signal.tolist(),
    )


@router.get("/validate/{record_name}", response_model=ValidationResult)
def validate(record_name: str):
    return ValidationResult(
        record_name = record_name,
        precision = 5.6,
        recall = 2.3,
        true_positive_count = 10,
        false_positive_count = 9,
        false_negative_count = 7,
    )

