# DataTrust

DataTrust is a data preparation and analytics workspace. This repository starts with the MVP vertical slice: CSV import, profiling, grid exploration, recipe-based edits, preview, immutable dataset versions, and CSV export.

## Stack
- Frontend: Vue 3, TypeScript, Vite, Tailwind CSS
- API: FastAPI, Pydantic v2
- Processing: Polars, PyArrow
- Jobs: Celery + Redis
- Metadata: PostgreSQL + SQLAlchemy 2 + Alembic
- Object storage: MinIO (S3-compatible)
- Local orchestration: Docker Compose

## Quick start
1. Copy `.env.example` to `.env`.
2. Run `docker compose up --build`.
3. Frontend: http://localhost:5173
4. API docs: http://localhost:8000/docs
5. MinIO console: http://localhost:9001

This is a starter foundation, not the completed product. The API currently exposes a health endpoint only. Feature implementation must follow `docs/MVP_SCOPE.md` and `.github/copilot-instructions.md`.

## Development principles
- Never overwrite a published dataset object.
- Every mutation must be represented as a validated recipe.
- Preview must be tied to the exact source version and recipe fingerprint.
- Publish only after explicit user approval.
- Enforce workspace authorization in the backend.
- Do not load entire datasets into the browser.
