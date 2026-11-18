# DataTrust — Complete Product & Development Documentation

**Product:** DataTrust — Data Preparation & Analytics Workspace  
**Tagline:** From Raw Data to Meaningful Insights.  
**Document version:** 1.0  
**Status:** Baseline specification for MVP implementation  
**Last updated:** 18 November 2026

> This document consolidates seven project artifacts into one reference: PRD, MVP Scope, Technical Specification, Database Design, Development Roadmap, `AGENTS.md`, and Antigravity Development Rules. It is the primary product and implementation guide for the DataTrust MVP.

---

# Part I — Product Requirements Document (PRD)

## 1. Product Overview

DataTrust is a data preparation workspace for importing, inspecting, understanding, cleaning, transforming, and preparing tabular datasets through a controlled and reproducible workflow.

It combines a spreadsheet-like data workspace with structured cleaning operations, data profiling, version history, and export capabilities. Common preparation tasks should be accessible through a visual interface without requiring users to write code.

The first release focuses on this end-to-end flow:

**CSV upload → schema inspection → data profiling → grid workspace → cleaning/editing → preview → publish a new version → version history → CSV export.**

DataTrust is not intended to replace databases, data warehouses, BI platforms, or programming environments. It bridges spreadsheet-style usability and reliable, reproducible data preparation.

## 2. Problem Statement

Preparing real-world data often requires several disconnected tools and manual steps. Users may move between spreadsheets, scripts, databases, and visualization tools just to make a dataset usable.

Common problems include:
- Missing, duplicated, inconsistent, or incorrectly formatted values.
- Unclear column types and inconsistent formats.
- Repetitive manual cleaning that is difficult to reproduce.
- Accidental changes to source data.
- No reliable record of what changed, when, and why.
- No way to inspect the impact of a cleaning operation before applying it.
- Technical tools that are powerful but inaccessible to users who do not routinely write code.

These issues slow down preparation and increase the risk of inaccurate results.

## 3. Product Vision

Provide one clear workspace where users can move from raw tabular data to a prepared dataset while retaining control over every change.

DataTrust should make data preparation:
1. Understandable — show dataset structure and condition.
2. Controlled — do not publish a destructive change without approval.
3. Reproducible — record transformations as structured operations.
4. Traceable — preserve source files and published versions.
5. Accessible — support common workflows through a visual interface.
6. Scalable — process larger datasets on the server, not by loading everything into the browser.

## 4. Target Users

Primary users:
- Students and learners working with structured datasets.
- Data analysts preparing data before analysis.
- Business and operations staff receiving CSV exports.
- Developers and technical users who need a visual preparation workflow.

Users need to import data, understand its structure, identify quality issues, edit values, apply common cleaning operations, preview changes, retain history, and export prepared datasets.

## 5. Product Goals and Success Criteria

### MVP goals
- Upload and validate CSV files.
- Inspect schema and basic data quality indicators.
- Browse data in a responsive, paginated grid.
- Search, sort, and filter rows.
- Perform a defined set of cleaning operations.
- Edit cells through a controlled draft-and-publish workflow.
- Preview changes before publication.
- Publish changes as immutable dataset versions.
- Review version history.
- Export a published version as CSV.
- Run longer processing tasks in the background and expose their status.

### MVP success criteria
A user can:
1. Upload a valid CSV.
2. Inspect columns, inferred types, row count, and basic profile.
3. Browse the dataset.
4. Edit cells or apply a supported cleaning operation.
5. Preview changes and validation results.
6. Explicitly publish the changes.
7. See a new immutable version in history.
8. Export that published version as CSV.

## 6. Product Principles

### Preserve source data
Original uploads and previously published versions must never be overwritten by cleaning or editing operations.

### Explicit user control
A change does not become a published dataset version until the user reviews its preview and explicitly approves publication.

### Reproducible operations
All data mutations are represented as validated, allowlisted recipe operations.

### Transparent impact
Users should understand affected rows or cells, expected results, and validation failures before publication.

### Server-side processing
The browser must not load an entire large dataset. Use server-side pagination, filtering, sorting, and bounded previews.

### AI is optional
The core product must remain usable without a paid AI provider. AI is not a dependency for essential cleaning.

## 7. Product Positioning

DataTrust bridges spreadsheet usability and programming-oriented data tools. It is a preparation workspace, not a database, warehouse, BI replacement, or general-purpose coding environment.

## 8. High-Level User Journey

1. User signs in and opens a workspace.
2. User uploads a CSV.
3. DataTrust validates the file and presents an import preview.
4. User confirms import.
5. DataTrust stores the original file and creates the first dataset version.
6. User opens the dataset and reviews its profile.
7. User browses, filters, sorts, edits cells, or selects cleaning operations.
8. DataTrust creates a recipe draft.
9. User requests a preview.
10. DataTrust validates and executes the preview against the selected source version.
11. User reviews the impact and explicitly publishes.
12. DataTrust creates a new immutable version.
13. User reviews version history and exports the prepared dataset.

## 9. UX and Visual Direction

DataTrust should feel like a polished, dependable professional workspace.

Principles:
- Light interface with a white or off-white foundation.
- Clean neutral surfaces and clear information hierarchy.
- Comfortable spacing without wasting screen space.
- Professional and approachable, not childish or overly playful.
- Moderate visual density suitable for working with tables and data.
- Consistent component behavior and clear interaction states.

### Preliminary palette

| Token | Value |
|---|---|
| Background | `#FFFFFF` |
| Canvas | `#F7F9F8` |
| Surface | `#FFFFFF` |
| Border | `#E5EBE8` |
| Primary text | `#26332E` |
| Secondary text | `#697771` |
| Muted text | `#929E98` |
| Primary emerald | `#16866B` |
| Emerald hover | `#11745B` |
| Blue accent | `#3978D5` |
| Violet accent | `#8061D9` |
| Orange accent | `#E58B37` |
| Coral accent | `#D95768` |
| Gold accent | `#B18A22` |

Avoid pastel-heavy palettes, dark primary themes, random accent usage, and overly saturated surfaces. Accents communicate meaning and status, not decoration.

---

# Part II — MVP Scope

## 10. MVP Definition

The MVP is one complete vertical slice:

**CSV import → inspect/profile → grid → clean/edit → preview → publish immutable version → history → CSV export.**

The objective is to deliver a working, dependable product flow before expanding into advanced capabilities.

## 11. In-Scope Features

### 11.1 Workspace and access foundation
- Authenticated session foundation.
- One initial workspace per user is acceptable for the first implementation.
- Dataset access and mutations are authorized by the backend.
- Workspace isolation must not rely only on frontend filtering.

### 11.2 CSV import
- Validate file type and configured upload limits.
- Handle common delimiters and encodings where feasible.
- Inspect headers and sample rows.
- Infer physical column types conservatively.
- Detect malformed rows and report import issues.
- Show an import preview before committing.
- Preserve the original uploaded file.
- Create dataset metadata and initial immutable version after successful import.

### 11.3 Basic profiling
Show:
- Row and column counts.
- Column names and inferred physical types.
- Missing-value counts and percentages.
- Duplicate-row count.
- Numeric summaries such as minimum, maximum, mean, and standard deviation where applicable.
- Basic distinct-value information where practical.

Clearly distinguish full-dataset metrics from sample-based estimates.

### 11.4 Data grid
- Browse rows and columns.
- Search values.
- Sort supported columns.
- Filter using supported conditions.
- Use server-side pagination or virtualized loading.
- Support hybrid cell editing.

### 11.5 Initial cleaning operations
- Detect and remove duplicate rows.
- Handle missing values using explicitly selected strategies.
- Trim leading and trailing whitespace.
- Normalize text case.
- Convert a column to a supported data type with validation.
- Apply simple numeric range rules.
- Detect negative values when the user explicitly selects a relevant rule.

Do not assume every negative number is invalid. The user chooses the condition and intended action. The UI adapts available controls to the dataset schema and column types.

### 11.6 Recipe Engine
- Allowlisted operation types only.
- Schema-validated parameters.
- Validate referenced columns and row identities.
- Validate target physical types and nullability.
- Reject unknown columns, rows, internal fields, duplicate target references, and invalid values.
- Avoid silent truncation or unsafe coercion.
- Execute operations deterministically where practical.
- Record operation definitions and results.

The MVP uses a linear recipe sequence, not a visual branching DAG.

### 11.7 Preview
- Source dataset version.
- Proposed operations.
- Before-and-after sample rows or cells.
- Number of affected rows or cells.
- Validation errors and reasons.
- Preview validity state.

Preview is bound to workspace, user, dataset, source version, recipe fingerprint, schema fingerprint, and expiry. A stale preview cannot be published. A recipe hash alone does not prove that a preview was executed.

### 11.8 Publish and version history
- Revalidate preview and source version.
- Run processing in a background worker when appropriate.
- Create a new immutable dataset version.
- Preserve original upload and prior versions.
- Record parent version, storage object, schema fingerprint, row count, actor, timestamp, and operation metadata.
- Expose job status and failure details.

Storage and metadata DB do not share one ACID transaction. Use staging, promotion, validation, transaction boundaries, reconciliation, and orphan cleanup.

Published undo is a compensating recipe that creates a new version; never rewrite an existing version.

### 11.9 CSV export
- Export a specific published version.
- Do not represent uncommitted drafts as published data.
- Report success or failure.
- Large exports may run as background jobs.

### 11.10 Background jobs
For long import, processing, publication, and export tasks, expose job type, status, measurable progress, completion/failure, and useful safe error messages.

## 12. Hybrid Cell Editing — Accepted Product Decision

**Decision: Hybrid. Cell editing is allowed, but all changes become validated recipe operations, are previewed, and create a new version only after explicit approval.**

Behavior:
- Users can edit individual cells.
- Multiple pending edits are grouped into one `update_cells` RecipeNode.
- Edits remain frontend drafts until preview and publication.
- Pending edits are visually distinguishable from published data.
- Users can review before-and-after values.
- Invalid values are rejected with clear reasons.
- Local draft undo/redo is supported before publication.
- Successful publication creates a new immutable version.
- Original and previous versions remain untouched.

### Stable row identity
Every row has an internal stable `_dt_row_id`. Never use visible row number, sort position, or page index as row identity. Users cannot edit `_dt_row_id`.

Row-preserving operations retain IDs. Row-generating operations such as aggregation require new IDs and an explicit lineage strategy.

### Optimistic concurrency
If the current dataset version changes while the user is editing, reject publication with `VERSION_CONFLICT`. Preserve the draft and require reload/re-preview. Never silently overwrite a newer version.

### Recipe node shape
The conceptual `update_cells` operation contains references such as:
- `row_id`
- `column`
- `value`

Validate row existence, column existence, internal-field restrictions, duplicate target references, target type, nullability, precision, and allowed coercion. Reject invalid data rather than silently truncating or coercing it.

### Frontend state direction
Pinia state should track:
- Draft recipe nodes.
- Pending cell changes.
- Preview ID/token.
- Whether preview is dirty.
- Whether publication is in progress.

### Audit
Capture actor, workspace, dataset, source version, output version, recipe, affected cells, result, and timestamp.

## 13. Explicitly Out of Scope for MVP

- Excel import.
- Direct PostgreSQL/MySQL connectors.
- Advanced lookup/join/fuzzy matching.
- Full formula builder or arbitrary formulas.
- Dashboard builder and advanced charting.
- Visual branching pipeline canvas.
- Pipeline scheduling.
- AI-assisted cleaning and AI insights.
- Real-time collaboration.
- Advanced semantic inference and enterprise governance.

## 14. MVP Acceptance Checklist

- [ ] User can upload a valid CSV.
- [ ] Import validation and preview work.
- [ ] Original source file is preserved.
- [ ] Initial immutable dataset version is created.
- [ ] Basic schema and profile are displayed.
- [ ] Grid supports server-side browsing, search, sort, and filter.
- [ ] Cell edits remain drafts.
- [ ] Supported cleaning operations use the Recipe Engine.
- [ ] Preview displays impact and validation errors.
- [ ] Stale preview is rejected.
- [ ] Concurrent version conflict is rejected without losing draft.
- [ ] Explicit publication creates a new immutable version.
- [ ] Version history is visible.
- [ ] CSV export targets a published version.
- [ ] Workspace authorization is enforced by backend.
- [ ] Tests cover critical integrity rules.

---

# Part III — Technical Specification

## 15. Agreed Technology Stack

| Layer | Technology |
|---|---|
| Frontend | Vue 3 + TypeScript |
| UI styling | Tailwind CSS |
| Frontend state | Pinia |
| API | FastAPI |
| Validation | Pydantic v2 |
| Data processing | Polars + PyArrow |
| Metadata DB | PostgreSQL |
| ORM | SQLAlchemy 2 |
| Migrations | Alembic |
| Background jobs | Celery |
| Queue/cache | Redis |
| Dataset files | Parquet |
| Object storage | S3-compatible storage |
| Deployment | Docker Compose initially |
| Backend tests | Pytest |
| Frontend tests | Vitest |
| API prefix | `/api/v1/` |

The current project setup uses the S3-compatible SILO image selected for this repository. Do not assume the upstream `minio/minio:latest` Docker Hub image is available. Existing `MINIO_*` environment variable naming may be retained where compatible with the selected image.

## 16. Architecture Approach

Use a modular monolith with separate API and worker processes/containers. Do not introduce microservices prematurely.

Conceptual components:
1. Vue web application.
2. FastAPI application.
3. Celery worker.
4. PostgreSQL metadata database.
5. Redis queue/cache.
6. S3-compatible object storage for source uploads and Parquet versions.

### Data responsibilities
- PostgreSQL: users, workspaces, dataset metadata, versions, jobs, recipes, rules, audit records, and configuration.
- Parquet: tabular dataset contents and immutable processed versions.
- Object storage: original uploads and processed dataset objects.
- Redis: background job queue and suitable ephemeral cache.

## 17. Repository Structure Direction

Keep the existing starter repository and evolve it incrementally. A target structure may resemble:

```text
datatrust-starter/
├── AGENTS.md
├── .agents/
│   └── rules/
│       └── datatrust-development.md
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── workers/
│   │   └── main.py
│   ├── migrations/
│   └── tests/
├── frontend/
│   └── src/
│       ├── api/
│       ├── components/
│       ├── layouts/
│       ├── modules/
│       ├── router/
│       ├── stores/
│       └── views/
├── docs/
├── docker-compose.yml
├── .env.example
└── README.md
```

This is a direction, not a mandate to create empty folders in advance. Add modules when implementing real functionality.

## 18. Data Import and Storage Flow

1. Receive upload and validate request.
2. Store original bytes in object storage under a generated object key.
3. Inspect CSV safely; determine headers, sample, schema, and parsing issues.
4. Parse and normalize into the chosen internal representation.
5. Add stable `_dt_row_id` values.
6. Write initial Parquet object to a staging key.
7. Validate output file, schema, checksum, and row count.
8. Promote staged object to its durable version key.
9. In a DB transaction, create dataset/version metadata and set current version.
10. Reconcile staged or orphaned objects if any stage fails.

Do not overwrite the source upload.

## 19. Dataset Versioning

Each published version is immutable.

Example:
- `v001`: imported source.
- `v002`: after a cleaning recipe.
- `v003`: after subsequent edits.

A version records at least:
- Dataset ID.
- Version number or stable version identifier.
- Parent version ID.
- Object storage key.
- Schema fingerprint.
- Row count.
- Column count or schema metadata.
- Creator.
- Creation timestamp.
- Recipe/operation metadata.
- Status and checksum where applicable.

The current version pointer is metadata; it does not make older versions mutable.

## 20. Grid Data Access

- Never load the full dataset into browser memory by default.
- Provide server-side pagination or cursor-based retrieval.
- Apply sorting and filtering on the server.
- Restrict page size and preview sample size.
- Validate requested sort/filter columns against the dataset schema.
- Use stable row IDs in edit requests.
- Consider virtual scrolling in the UI, backed by bounded API requests.

## 21. Recipe Engine Design

The Recipe Engine is the only route for data mutation.

Conceptual flow:

```text
Recipe request
    ↓
Parse and validate operation schema
    ↓
Authorize workspace/dataset/source version
    ↓
Validate columns, row IDs, types, and parameters
    ↓
Create preview execution
    ↓
Return preview token and impact summary
    ↓
User explicitly approves
    ↓
Revalidate token and source version
    ↓
Execute deterministic operation
    ↓
Write and validate new Parquet version
    ↓
Commit version metadata
```

Never execute arbitrary user-supplied SQL or Python. Do not use `eval` or `exec`. AI-generated content, if introduced later, must be converted into a structured plan and validated against the same allowlist.

## 22. Preview Lifecycle

A preview is server-side state bound to:
- Workspace.
- User.
- Dataset.
- Source version.
- Recipe fingerprint.
- Schema fingerprint.
- Expiration time.

Use an opaque random token or a properly signed token that resolves to server-validated preview state. Do not treat a SHA-256 recipe hash alone as proof that execution occurred.

On publish:
- Check token validity and expiry.
- Check user/workspace authorization.
- Check dataset current version still matches preview source version.
- Check recipe and schema fingerprints.
- Reject stale or mismatched preview.
- Preserve the user's draft on conflict.

## 23. Publish Consistency

Object storage and PostgreSQL do not participate in a shared ACID transaction. Use a recoverable multi-step process:
1. Write output to staging key.
2. Validate output integrity and metadata.
3. Promote/copy to durable version key.
4. Commit version row and current-version update in a DB transaction.
5. Reconcile orphaned objects or incomplete operations with a worker/maintenance task.

Do not claim distributed atomicity. Make failures recoverable and observable.

## 24. API Design Direction

Use REST under `/api/v1/`. Keep endpoints resource-oriented and version-aware.

Suggested initial endpoint groups (exact schemas are finalized during implementation):
- `/auth/...`
- `/workspaces/...`
- `/datasets` — create/list datasets and import.
- `/datasets/{dataset_id}` — metadata and current version.
- `/datasets/{dataset_id}/profile`
- `/datasets/{dataset_id}/rows` — paginated rows and filters.
- `/datasets/{dataset_id}/versions`
- `/datasets/{dataset_id}/recipes/preview`
- `/datasets/{dataset_id}/recipes/publish`
- `/jobs/{job_id}`
- `/datasets/{dataset_id}/versions/{version_id}/export`

All endpoints must enforce workspace access on the backend. Do not trust frontend-provided IDs or filters without validation.

## 25. Background Jobs

Use Celery and Redis for work that may exceed a normal request-response time, including large imports, recipe execution, publication, and export.

Persist job metadata in PostgreSQL. Redis is the queue, not the sole source of durable job history.

Jobs should have explicit states such as queued, running, succeeded, failed, and cancelled if cancellation is supported. Progress must be honest; do not invent percentages when the task cannot measure progress.

## 26. Security and Reliability

- Validate all input with explicit schemas.
- Enforce workspace authorization on every relevant backend operation.
- Avoid arbitrary code execution.
- Keep secrets in environment configuration and out of source control.
- Do not log credentials or sensitive file contents.
- Use bounded upload, preview, and pagination limits.
- Handle malformed files and processing failures explicitly.
- Preserve original uploads and published versions.
- Test stale preview and version conflict handling.
- Add audit records for mutations.
- Reconcile object storage and database inconsistencies.

---

# Part IV — Database Design

## 27. Database Design Principles

PostgreSQL is the metadata system of record. It does not store the full tabular contents of every dataset in relational rows; those contents are stored as Parquet objects.

The schema must support:
- Workspace isolation.
- Dataset metadata.
- Immutable version history.
- Recipe definitions and preview lifecycle.
- Background job tracking.
- Auditability.

Use SQLAlchemy 2 and Alembic. Use explicit constraints and indexes. Avoid duplicating large dataset cell contents into PostgreSQL.

## 28. Core Entities

The following is the logical baseline. Exact column types, naming, and migration details can be refined while implementing each module, but the integrity requirements must remain.

### 28.1 `users`
Purpose: application identity.

Suggested fields:
- `id` — primary key.
- `email` — unique, normalized.
- `display_name`.
- `password_hash` or external identity reference.
- `is_active`.
- `created_at`.
- `updated_at`.

### 28.2 `workspaces`
Purpose: tenant and authorization boundary.

Suggested fields:
- `id` — primary key.
- `name`.
- `slug` — unique where appropriate.
- `created_by` — user FK.
- `created_at`.
- `updated_at`.

### 28.3 `workspace_members`
Purpose: user membership and role.

Suggested fields:
- `workspace_id`.
- `user_id`.
- `role` — initially owner/admin/editor/analyst/viewer model; MVP may start with a smaller supported subset.
- `joined_at`.

Constraints:
- Composite primary key or unique constraint on `(workspace_id, user_id)`.
- Foreign keys to workspace and user.
- Role must be allowlisted.

### 28.4 `datasets`
Purpose: logical dataset identity independent of its versions.

Suggested fields:
- `id`.
- `workspace_id`.
- `name`.
- `description` nullable.
- `source_filename`.
- `current_version_id` nullable during initial creation.
- `created_by`.
- `created_at`.
- `updated_at`.
- `deleted_at` nullable if soft deletion is implemented.

Workspace ownership must be enforced in backend queries and, where practical, composite database constraints.

### 28.5 `dataset_versions`
Purpose: immutable snapshot metadata for each dataset state.

Suggested fields:
- `id`.
- `workspace_id`.
- `dataset_id`.
- `version_number`.
- `parent_version_id` nullable for initial import.
- `object_key`.
- `format` — e.g. parquet.
- `row_count`.
- `column_count`.
- `schema_json`.
- `schema_fingerprint`.
- `checksum`.
- `status`.
- `created_by`.
- `created_at`.
- `operation_summary` or recipe reference.

Constraints:
- Unique `(dataset_id, version_number)`.
- Parent version must belong to the same dataset.
- Dataset and version workspace IDs must match.
- Published versions are immutable at application level; avoid update paths except carefully defined lifecycle metadata.

### 28.6 `recipes`
Purpose: structured transformation definition.

Suggested fields:
- `id`.
- `workspace_id`.
- `dataset_id`.
- `source_version_id`.
- `created_by`.
- `name` nullable.
- `definition_json`.
- `recipe_fingerprint`.
- `status` — draft/previewed/published/failed as appropriate.
- `created_at`.
- `updated_at`.

Recipe JSON must be validated against allowlisted operation schemas. Do not treat arbitrary JSON as executable code.

### 28.7 `recipe_previews`
Purpose: persisted preview lifecycle and authorization binding.

Suggested fields:
- `id`.
- `workspace_id`.
- `dataset_id`.
- `user_id`.
- `source_version_id`.
- `recipe_id` or immutable recipe snapshot.
- `recipe_fingerprint`.
- `schema_fingerprint`.
- `preview_token_hash` or secure token reference.
- `result_summary_json`.
- `sample_result_key` nullable if preview artifacts are stored externally.
- `status`.
- `expires_at`.
- `created_at`.

A preview is valid only for the exact workspace, user, dataset, source version, recipe fingerprint, schema fingerprint, and expiry context.

### 28.8 `jobs`
Purpose: durable application view of background task status.

Suggested fields:
- `id`.
- `workspace_id`.
- `dataset_id` nullable.
- `user_id`.
- `job_type`.
- `celery_task_id` nullable.
- `status`.
- `progress` nullable.
- `result_json` nullable.
- `error_code` nullable.
- `error_message` nullable and sanitized.
- `created_at`.
- `started_at` nullable.
- `finished_at` nullable.

Redis is not the durable job-history database.

### 28.9 `audit_logs`
Purpose: trace important actions.

Suggested fields:
- `id`.
- `workspace_id`.
- `actor_user_id`.
- `dataset_id` nullable.
- `action`.
- `source_version_id` nullable.
- `output_version_id` nullable.
- `recipe_id` nullable.
- `details_json`.
- `created_at`.

Do not store passwords, credentials, or unnecessary raw dataset values in audit details.

### 28.10 `source_files` (recommended)
Purpose: preserve original uploaded file metadata independently from processed versions.

Suggested fields:
- `id`.
- `workspace_id`.
- `dataset_id`.
- `original_filename`.
- `object_key`.
- `content_type`.
- `file_size`.
- `checksum`.
- `created_by`.
- `created_at`.

The original source object is immutable.

## 29. Logical Relationships

```text
users ──< workspace_members >── workspaces
workspaces ──< datasets
datasets ──< source_files
datasets ──< dataset_versions
dataset_versions ──< dataset_versions (parent_version)
datasets ──< recipes
recipes ──< recipe_previews
workspaces ──< jobs
workspaces ──< audit_logs
users ──< jobs
users ──< audit_logs
```

`datasets.current_version_id` points to the current published version. Ensure the referenced version belongs to that same dataset and workspace, using application validation and suitable constraints where feasible.

## 30. Important Constraints and Indexes

Recommended:
- Unique normalized user email.
- Unique workspace membership `(workspace_id, user_id)`.
- Unique dataset version `(dataset_id, version_number)`.
- Index dataset listing by `(workspace_id, created_at)`.
- Index versions by `(dataset_id, version_number DESC)`.
- Index jobs by `(workspace_id, status, created_at)`.
- Index audit history by `(workspace_id, created_at DESC)`.
- Index previews by `(workspace_id, dataset_id, expires_at)`.
- Foreign keys with deliberate delete behavior.
- Prevent cross-workspace references.
- Use `RESTRICT` or controlled lifecycle deletion for records whose removal could break version history.

Do not cascade-delete immutable version metadata or source objects as an accidental side effect of deleting a dataset. Define explicit retention and deletion workflows.

## 31. Data Types and Schema Metadata

Store the dataset schema as structured JSON metadata containing at least column name, physical type, nullability where known, and ordinal position. Keep a schema fingerprint for preview/version consistency checks.

Distinguish physical types (string, integer, float, boolean, date/timestamp) from semantic interpretations (email, currency, postal code). MVP primarily needs safe physical typing; semantic inference is future work.

---

# Part V — Development Roadmap

## 32. Delivery Strategy

Do not build all modules at once. Deliver a working vertical slice in small milestones. Deepen technical details just in time for the module being implemented. Avoid reopening settled decisions without a concrete reason.

### Milestone 0 — Repository and runtime baseline
- Confirm Docker Compose services start.
- Confirm frontend and API are reachable.
- Confirm PostgreSQL, Redis, object storage, and worker health.
- Keep `.env` out of Git.
- Confirm tests run.

**Exit condition:** local development environment is reproducible.

### Milestone 1 — Application foundation
- FastAPI configuration and health checks.
- SQLAlchemy session and Alembic migration baseline.
- Vue application shell and routing.
- API client and error handling.
- User/workspace foundation sufficient for MVP.
- Backend authorization dependencies.

**Exit condition:** application can identify a user and enforce workspace scope for a protected test resource.

### Milestone 2 — CSV import
- Upload endpoint and validation.
- Object storage integration.
- CSV inspection and import preview.
- Schema inference and stable `_dt_row_id`.
- Parquet creation and validation.
- Dataset/source/version metadata persistence.

**Exit condition:** user imports CSV and sees a dataset with immutable initial version.

### Milestone 3 — Profiling and grid
- Basic profile service.
- Dataset overview UI.
- Server-side row retrieval.
- Search, sort, and filter.
- Grid loading and error/empty states.

**Exit condition:** user can inspect and browse a dataset without loading all rows into browser memory.

### Milestone 4 — Recipe Engine and cleaning
- Recipe operation schemas.
- Validation layer.
- Initial cleaning operations.
- Polars execution adapters.
- Recipe draft UI and operation controls.

**Exit condition:** supported operations can be represented and validated as recipes.

### Milestone 5 — Hybrid cell editing and preview
- Draft cell-edit state.
- `update_cells` recipe operation.
- Before/after preview.
- Affected count and validation feedback.
- Preview token persistence and expiry.
- Stale preview and version conflict tests.

**Exit condition:** user can edit cells, preview safely, and cannot publish a stale preview.

### Milestone 6 — Publish, history, and export
- Background publication job.
- Staging and object promotion.
- Immutable version creation.
- Version history UI.
- CSV export of a selected published version.
- Audit records and failure reconciliation.

**Exit condition:** complete MVP acceptance flow works end to end.

### Milestone 7 — Stabilization
- Critical backend and frontend tests.
- Error handling and loading states.
- Security review of workspace access.
- Performance checks on realistic CSV sizes.
- Documentation and local setup instructions.
- Bug fixes before adding new product scope.

**Exit condition:** MVP is usable, repeatable, and demonstrably preserves data integrity.

## 33. Definition of Done

A feature is not complete merely because its UI exists.

For each feature:
- Backend validation and authorization are implemented.
- Expected success and failure paths are handled.
- Relevant tests pass.
- Loading, empty, and error states exist.
- Data integrity is preserved.
- UI matches the agreed visual direction.
- Documentation is updated only where it helps future implementation.
- The feature is demonstrated in the running application.

---

# Part VI — AGENTS.md

## 34. Instructions for AI Coding Agents

You are contributing to DataTrust, a data preparation and analytics workspace. Treat this document as the consolidated product and technical baseline.

### Before making changes
1. Inspect the existing repository and current implementation.
2. Read this document and the relevant source files.
3. Identify the smallest useful implementation step.
4. Check existing conventions before introducing new dependencies or patterns.
5. Do not overwrite working code just to impose a preferred architecture.

### Implementation behavior
- Work in small, verifiable increments.
- Prefer complete vertical slices over broad scaffolding.
- Implement real functionality, not placeholder screens presented as finished features.
- Keep frontend and backend contracts consistent.
- Add tests for important behavior and failure paths.
- Run relevant tests and report their actual results.
- Explain files changed and any migration or setup steps.
- If blocked, report the exact blocker and a practical next step.

### Product invariants
- Original uploads and published dataset versions are immutable.
- Every mutation goes through the validated Recipe Engine.
- Cell edits are drafts until previewed and explicitly published.
- Every row uses stable `_dt_row_id`; never use visible row positions as identity.
- Stale previews and concurrent version conflicts must be rejected.
- Workspace authorization is enforced on the backend.
- Large datasets are processed server-side.
- The core cleaning workflow works without AI or a paid API.

### Technical constraints
- Follow the agreed stack: Vue 3, TypeScript, Tailwind, FastAPI, Pydantic v2, Polars, PyArrow, PostgreSQL, SQLAlchemy 2, Alembic, Celery, Redis, Parquet, and S3-compatible storage.
- Use modular monolith architecture with separate API and worker processes.
- Do not introduce microservices prematurely.
- Do not execute arbitrary user-provided SQL or Python.
- Do not use `eval` or `exec` for user input.
- Keep secrets out of source control and logs.
- Use migrations for schema changes.

### Scope discipline
- MVP scope is the end-to-end CSV workflow defined in this document.
- Do not add out-of-scope features unless explicitly requested.
- Do not expand the architecture or documentation without a concrete need.
- Do not reopen accepted decisions without evidence of a real blocker.
- Do not claim tests, commands, or manual checks passed unless they were actually run.

### Communication
At the end of each implementation task, report:
1. What was implemented.
2. Important files changed.
3. Tests/commands actually run and their results.
4. Known limitations or risks.
5. The single most useful next implementation step.

---

# Part VII — Antigravity Development Rules

## 35. Working Rules

These rules apply when using Google Antigravity or another agentic coding environment.

### Rule 1 — Inspect before editing
Read the relevant files and understand the existing structure before changing code. Avoid destructive rewrites based on assumptions.

### Rule 2 — Plan only as much as needed
For a small task, implement directly. For a multi-file or risky task, provide a short plan, then execute it. Do not turn every task into a long planning exercise.

### Rule 3 — Deliver working increments
Prefer a tested, working vertical slice over generating many disconnected files. Do not create empty modules or speculative abstractions without an immediate use.

### Rule 4 — Preserve accepted decisions
Do not change the stack, architecture approach, product scope, hybrid editing model, versioning policy, or visual direction unless the user explicitly asks or a concrete technical blocker is demonstrated.

### Rule 5 — Protect data integrity
Never overwrite original uploads or published versions. Never bypass the Recipe Engine for a data mutation. Require preview and explicit approval before publication.

### Rule 6 — Validate before publish
Bind preview to the exact source version, recipe, schema, workspace, user, and expiry. Reject stale preview tokens and version conflicts. Preserve drafts after conflicts.

### Rule 7 — No unsafe execution
Never execute arbitrary SQL, Python, shell commands, or generated code originating from user dataset content or AI output. Use allowlisted operations and validated parameters. Do not use `eval` or `exec`.

### Rule 8 — Backend authorization is mandatory
Never rely on frontend hiding or filtering to enforce workspace isolation. Validate ownership and membership on every relevant API path.

### Rule 9 — Keep browser memory bounded
Do not fetch entire datasets into the frontend. Use server-side pagination, sorting, filtering, and bounded previews.

### Rule 10 — Test real behavior
Add tests for constraints, invalid inputs, permission failures, stale previews, version conflicts, and immutable version behavior. Do not claim success without running the relevant checks.

### Rule 11 — Avoid unnecessary dependencies
Before adding a package, verify that the existing stack cannot solve the problem. Explain meaningful dependency additions.

### Rule 12 — Keep secrets safe
Never commit `.env`, API keys, passwords, tokens, or storage credentials. Use `.env.example` with placeholders.

### Rule 13 — Maintain visual consistency
Follow the light, clean, professional visual direction. Use neutral surfaces and purposeful emerald/blue/violet/orange/coral/gold accents. Avoid childish, pastel-heavy, or dark-primary styling.

### Rule 14 — Report honestly
State what changed, what was tested, and what remains incomplete. Distinguish implemented behavior from planned behavior.

### Rule 15 — Do not over-plan
The project already has an agreed MVP and architecture baseline. Do not repeatedly audit or redesign everything. Deepen technical decisions only when the relevant feature is being implemented.

## 36. Recommended Task Prompt Pattern

When assigning work to Antigravity, use a focused request such as:

> Read `DataTrust_Complete_Documentation.md` first, then inspect the existing repository. Implement only the next requested milestone or task. Preserve all product and data-integrity decisions. Make the smallest complete working change, add or update tests, run the relevant checks, and report actual results. Do not expand scope or create unrelated documentation.

---

# Appendix A — Non-Negotiable Decisions

1. Modular monolith; separate API and worker processes, not premature microservices.
2. Vue 3 + TypeScript + Tailwind frontend.
3. FastAPI + Pydantic v2 backend.
4. Polars + PyArrow for tabular processing.
5. PostgreSQL metadata; Parquet dataset versions; S3-compatible object storage.
6. Celery + Redis for background jobs.
7. Immutable original uploads and published versions.
8. Hybrid cell editing: draft → validated recipe → preview → explicit publish → new version.
9. Stable `_dt_row_id`; never use visible row position as row identity.
10. All mutations through an allowlisted Recipe Engine.
11. Preview is bound to user/workspace/dataset/source version/recipe/schema/expiry.
12. Reject stale previews and concurrent version conflicts.
13. Backend-enforced workspace authorization.
14. No arbitrary SQL/Python execution, `eval`, or `exec`.
15. MVP first: CSV import through CSV export.
16. Core manual workflows do not depend on AI.
17. Light, clean, professional visual direction with controlled accent colors.
18. Implement in small working increments; avoid endless planning.

# Appendix B — Change Control

If a future requirement conflicts with this document:
1. Identify the exact conflicting decision.
2. Explain the product or technical impact.
3. Ask for explicit user approval before changing an accepted non-negotiable decision.
4. Update this consolidated document when a decision is formally changed.

Do not silently reinterpret or discard prior decisions.
