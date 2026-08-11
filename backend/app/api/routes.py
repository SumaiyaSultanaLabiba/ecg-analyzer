
from fastapi import APIRouter, HTTPException
from app.data.loader import list_available_records, load_record, load_annotations
from app.models.schemas import AnalysisResult, ValidationResult, RecordListResponse



router = APIRouter()


@router.get("/records", response_model=RecordListResponse)
def get_records():
    return None


@router.get("/analyze/{record_name}", response_model=AnalysisResult)
def analyze(record_name: str):
    return None


@router.get("/validate/{record_name}", response_model=ValidationResult)
def validate(record_name: str):
    return None

