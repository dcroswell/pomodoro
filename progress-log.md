# Progress Log

This document records what has been done and what has been decided.

## 2026-05-28 — Documentation cleanup checkpoint

### Done

- Confirmed `README.md` is the project working protocol.
- Updated `README.md` so future file changes are handled one file at a time.
- Updated `README.md` so full-file replacements are provided in a copyable format.
- Updated `README.md` so `manual-trial.md` is listed as a core project document.
- Updated `next.md` so it no longer asks whether v0.2 should use Google Sheets or SQLite.
- Updated `next.md` so the current target is documentation cleanup followed by the v0.2 Google Sheets manual trial.
- Replaced the placeholder `architecture.md` with real architecture notes.
- Updated `versions.md` so v0.2 clearly uses Google Sheets for the manual trial.
- Updated `versions.md` so SQLite remains the preferred serious MVP storage option.
- Updated `manual-trial.md` so future hooks are clearly marked as not required for the first trial.
- Confirmed stale duplicate `docs/` control files are not present.

### Key decisions

- Work on one project file at a time unless explicitly choosing to group files.
- When a project file needs replacement, provide the full replacement document rather than vague patch instructions.
- Use one copyable `markdown` code block for Markdown files that do not contain internal triple-backtick fences.
- Do not use `:::writing` blocks for project file replacements.
- `next.md` remains the live task pointer.
- `progress-log.md` remains historical.
- The v0.2 manual data model trial starts in Google Sheets.
- SQLite remains the preferred storage option for the serious MVP.
- `architecture.md` now describes the intended system architecture rather than only headings.
- `RoutineScheduleEvents`, `ShoppingList`, `routine_type`, `action_type`, and `linked_resource_id` are future hooks, not required for the first manual trial.

### Current project documents

- `README.md`
- `requirements.md`
- `versions.md`
- `data-model.md`
- `manual-trial.md`
- `architecture.md`
- `progress-log.md`
- `next.md`

### Current status

Documentation cleanup is mostly complete.

The project is ready to continue the v0.2 Google Sheets manual data model trial.

### Handoff

Continue with the v0.2 Google Sheets manual trial using the Wake-up Routine.
