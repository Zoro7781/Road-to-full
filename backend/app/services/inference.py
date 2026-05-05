"""Inference service adapters for backend API routes."""

from backend.app.schemas.data_input import DataUploadRequest, DataUploadResponse
from ai.models.text_classifier import TextClassifier

_classifier = TextClassifier()


def classify_text(text: str) -> tuple[str, float]:
    """Classify incoming text using placeholder model logic."""
    return _classifier.predict(text)


def process_uploaded_data(sector: str, payload: DataUploadRequest) -> DataUploadResponse:
    """Apply model prediction to uploaded data and shape API response."""
    label, score = classify_text(payload.text)
    return DataUploadResponse(
        sector=sector,
        user_id=payload.user_id,
        accepted=True,
        classification_label=label,
        classification_score=score,
    )
