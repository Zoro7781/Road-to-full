"""Schemas for sector-based user data ingestion."""

from pydantic import BaseModel, Field


class DataUploadRequest(BaseModel):
    user_id: str = Field(..., min_length=1, description="Unique user identifier")
    text: str = Field(..., min_length=1, description="Raw input text to process")
    metadata: dict[str, str] = Field(default_factory=dict)


class DataUploadResponse(BaseModel):
    sector: str
    user_id: str
    accepted: bool
    classification_label: str
    classification_score: float
