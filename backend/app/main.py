"""FastAPI application entrypoint."""

from fastapi import FastAPI

from backend.app.api.v1.routes import router as v1_router

app = FastAPI(title="Multi-Sector AI Platform API", version="0.2.0")
app.include_router(v1_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
