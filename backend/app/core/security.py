"""Basic API key authentication utilities."""

import os

from dotenv import load_dotenv
from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

load_dotenv()

API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def _get_expected_api_key() -> str:
    """Load expected API key from environment for safer secret handling."""
    value = os.getenv("API_KEY")
    if not value:
        raise RuntimeError("Missing API_KEY. Add it to your .env file.")
    return value


def require_api_key(api_key: str | None = Security(api_key_header)) -> str:
    """Validate incoming API key header for protected endpoints."""
    if api_key != _get_expected_api_key():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
    return api_key
