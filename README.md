# Multi-Sector AI Platform

Scaffold for a multi-sector AI platform with:
- **Backend API** (FastAPI)
- **AI modules** (PyTorch / Hugging Face-ready)
- **Frontend** (React)
- **Security & compliance** baseline (HIPAA / GDPR-oriented)

## Project Structure

- `backend/` FastAPI service for sector data and orchestration
- `ai/` Model and pipeline modules for NLP/predictions/tasks
- `frontend/` React web app for configuring AI solutions
- `infra/` Infrastructure templates (Docker/Terraform placeholders)
- `docs/` Architecture and planning documents
- `compliance/` Compliance/security control documentation
- `scripts/` API test and integration scripts

## Secure API Key Setup

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and set your real key:
   ```bash
   API_KEY=your_real_api_key
   ```
3. Never commit `.env` to Git. It is ignored to protect secrets.
4. The backend and scripts load keys using `python-dotenv` and `os.getenv("API_KEY")`.
5. If `API_KEY` is missing, the app/scripts raise a clear error message.

## Run the project securely

1. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
2. Start FastAPI server:
   ```bash
   uvicorn backend.app.main:app --reload
   ```
3. Test hello endpoint with API key loaded from `.env`:
   ```bash
   python scripts/test_hello_client.py
   ```
