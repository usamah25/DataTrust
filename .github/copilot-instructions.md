# DataTrust Copilot Instructions

## Product intent
Build DataTrust as a professional data preparation workspace. Follow `docs/MVP_SCOPE.md`. Prioritize a complete, tested vertical slice over speculative features.

## Architecture
- Monorepo with Vue 3 + TypeScript frontend and modular FastAPI backend.
- Polars + PyArrow for tabular processing; PostgreSQL for metadata; Parquet objects in MinIO.
- Celery + Redis for long-running jobs.
- Keep the API modular; do not introduce microservices or additional infrastructure without an explicit need.

## Data integrity
- Published dataset versions are immutable.
- Never overwrite an existing Parquet object.
- Every data mutation must be represented by an allowlisted, validated recipe operation.
- Cell editing is allowed only as a draft interaction. It must become a recipe, be validated, previewed, explicitly approved, and published as a new version.
- Use stable internal row identity, never visible row position, to target edits.
- Preview must be bound to workspace, user, dataset, source version, schema fingerprint, recipe fingerprint, and expiry.
- Reject stale previews and concurrent publication conflicts.
- Do not silently coerce invalid values or silently choose among duplicate lookup keys.

## Security
- Enforce workspace access and permissions on the backend for every workspace-scoped resource.
- Never expose secrets in logs or API responses.
- Validate uploads and enforce file/row/column/resource limits.
- Never execute user input through eval, exec, arbitrary Python, or arbitrary SQL.

## Performance
- Do not load an entire large dataset into the browser.
- Use server-side filtering, sorting, and pagination.
- Benchmark Polars execution against realistic data sizes.
- Use background jobs for expensive full-dataset operations.

## Engineering workflow
- Inspect existing code before changing it.
- Implement in small vertical slices.
- Add unit and integration tests with each feature.
- Run relevant tests and report actual results; never claim tests passed without running them.
- Avoid placeholder implementations presented as complete functionality.
- Update documentation when behavior or API contracts change.
