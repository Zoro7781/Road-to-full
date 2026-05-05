"""Versioned API routes for data ingestion."""

from fastapi import APIRouter, Depends

from backend.app.core.security import require_api_key
from backend.app.schemas.data_input import DataUploadRequest, DataUploadResponse
from backend.app.services.inference import classify_text, process_uploaded_data

router = APIRouter(prefix="/api/v1", tags=["ingestion"])


@router.get("/test/hello")
def hello_world() -> dict[str, str]:
    """Basic public test endpoint for setup verification."""
    return {"message": "Hello, World"}


@router.post(
    "/upload/healthcare",
    response_model=DataUploadResponse,
    dependencies=[Depends(require_api_key)],
)
def upload_healthcare_data(payload: DataUploadRequest) -> DataUploadResponse:
    return process_uploaded_data("healthcare", payload)


@router.post(
    "/upload/education",
    response_model=DataUploadResponse,
    dependencies=[Depends(require_api_key)],
)
def upload_education_data(payload: DataUploadRequest) -> DataUploadResponse:
    return process_uploaded_data("education", payload)


@router.get(
    "/test/pipeline",
    dependencies=[Depends(require_api_key)],
)
def test_pipeline(sample_text: str = "urgent support needed") -> dict[str, str | float]:
    """Basic integration route to verify API-to-model wiring."""
    label, score = classify_text(sample_text)
    return {
        "status": "ok",
        "sample_text": sample_text,
        "prediction_label": label,
        "prediction_score": score,
    }
