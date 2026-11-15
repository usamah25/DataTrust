# DataTrust MVP v1 — Product Scope

**Status:** Scope baseline for first implementation  
**Product promise:** Import a CSV, understand its quality, correct it safely, preview the result, publish a new immutable version, and export it.

## In scope
1. Account/session foundation and one initial workspace.
2. CSV upload, file validation, schema inspection, import preview, and commit.
3. Basic profiling: row/column counts, missing values, duplicate rows, inferred physical types, and basic numeric summaries.
4. Data grid: view, search, sort, filter, and hybrid cell editing.
5. Initial cleaning operations: duplicate detection/removal, missing-value handling, trim/whitespace normalization, case normalization, safe type conversion, simple numeric range/negative-value rules.
6. Recipe engine: allowlisted linear recipe execution with schema and parameter validation.
7. Preview: before/after samples, affected counts, validation errors, source version and recipe binding.
8. Publish: explicit approval, background processing, immutable Parquet version, version history.
9. CSV export of a published version.
10. Job status and progress for long-running operations.

## Explicitly out of scope for first MVP
- Excel and database connectors.
- Full formula builder and arbitrary formula language.
- Advanced lookup/join and fuzzy matching.
- Dashboard builder and advanced charting.
- Visual branching pipeline canvas and scheduling.
- AI-assisted cleaning and AI insights.
- Real-time multi-user collaborative editing.
- Advanced semantic type inference and enterprise governance.

## Required end-to-end acceptance flow
A user can upload a valid CSV, inspect its schema and basic profile, open the data grid, edit one or more cells, preview the recipe, explicitly publish it, receive a new immutable dataset version, inspect version history, and export the published result as CSV.

## Non-negotiable product rules
- Original uploads and published versions are never overwritten.
- Cell edits remain drafts until previewed and explicitly published.
- All mutations go through the same validated recipe execution path.
- Stable row identity is used for edits; visible row numbers are not identities.
- Stale previews and concurrent version conflicts are rejected.
- Workspace authorization is enforced by the backend.
- Large datasets are processed server-side; the browser receives only requested pages/samples.
