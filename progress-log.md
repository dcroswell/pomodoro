# Progress Log

This document records what has been done and what has been decided.

## 2026-05-28 — Documentation cleanup checkpoint

### Done

- Confirmed `README.md` is the project working protocol.
- Updated `README.md` so future file changes are handled one file at a time.
- Updated `README.md` so full-file replacements are provided in a copyable format.
- Updated `README.md` so `manual-trial.md` is listed as a core project document.
- Updated `next.md` so it no longer asks whether v0.2 should use Google Sheets or SQLite.
- Updated `next.md` so the current target is documentation cleanup followed by the v0.2 manual trial.
- Replaced the placeholder `architecture.md` with real architecture notes.
- Updated `versions.md` so v0.2 clearly defines the manual trial storage decision.
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

The project is ready to continue the v0.2 manual data model trial.

### Handoff

Continue with the v0.2 manual trial using the Wake-up Routine.

---

## 2026-05-28 — Storage verification decision

### Done

- Decided that Google Sheets is not suitable for the v0.2 manual data model trial in this project.
- Reason: ChatGPT cannot directly verify Google Sheets from this project.
- Chose repo-tracked CSV files under `data/manual-trial/` for the v0.2 manual data model trial.
- Updated `versions.md` to replace Google Sheets with repo-tracked CSV files.
- Updated `manual-trial.md` to describe the CSV trial files.
- Updated `README.md` to describe the CSV-based trial and direct GitHub verification workflow.
- Updated `architecture.md` to describe repo-tracked CSV files as the v0.2 storage choice.
- Updated `next.md` to point to CSV setup and verification.

### Key decisions

- The repo remains the source of truth.
- v0.2 trial data should be directly inspectable by ChatGPT through the GitHub connector.
- Use repo-tracked CSV files for manual trial data.
- Do not use Google Sheets unless ChatGPT can directly verify the sheet in the current chat.
- Do not move to code, Telegram, Google Calendar, AI parsing, or voice yet.
- Create data files before continuing the manual trial.

### Current project documents

- `README.md`
- `requirements.md`
- `versions.md`
- `data-model.md`
- `manual-trial.md`
- `architecture.md`
- `progress-log.md`
- `next.md`
- `gpt_project_settings.txt`

### Current status

v0.2 is the active version.

The storage decision has changed from Google Sheets to repo-tracked CSV files.

The documentation now mostly reflects the CSV decision.

The initial CSV files still need to be created under `data/manual-trial/`.

### Handoff

Create the initial CSV files under `data/manual-trial/` and verify them from GitHub before continuing the v0.2 manual trial.
