# Progress Log

This document records what has been done and what has been decided.

## 2026-05-29 — v0.3 deterministic routine engine complete

### Done

- Created `command-workflow.md` to define the first deterministic text-command workflow for v0.3.
- Created the initial Python project structure:
  - `src/routine_engine.py`
  - `tests/test_routine_engine.py`
  - `requirements-dev.txt`
  - `.gitignore`
- Added `pytest` as the development test dependency.
- Added automated tests for the v0.3 routine engine.
- Implemented generic routine listing.
- Implemented routine start behaviour.
- Implemented clear error handling for unknown routine IDs.
- Implemented current routine retrieval.
- Implemented checklist item status handling:
  - mark item done
  - skip item
- Implemented routine finishing with a basic summary:
  - done count
  - skipped count
  - pending count
- Implemented simple routine completion logging.
- Ran automated tests successfully.
- Ran a manual end-to-end test successfully using a sample Morning Routine.
- Verified committed code from GitHub after each major checkpoint.

### Key decisions

- v0.3 is a deterministic routine engine, not a Telegram bot, calendar integration, voice system, or AI parser.
- The routine engine should be generic and user-driven.
- Example routines such as Wake-up Routine or Morning Routine are sample data only, not built-in application logic.
- Routine data should be supplied to the engine, not hard-coded inside the engine.
- The engine should work with any user-created routine name and checklist items.
- The first v0.3 log behaviour can remain simple: append the finished routine to an in-memory routine log.
- More durable storage can come later when the project moves toward SQLite.
- `command-workflow.md` should be added to the core documentation list during the v0.3 documentation checkpoint.

### Current project documents

- `README.md`
- `requirements.md`
- `versions.md`
- `data-model.md`
- `manual-trial.md`
- `architecture.md`
- `command-workflow.md`
- `progress-log.md`
- `next.md`
- `gpt_project_settings.txt`

### Current status

v0.3 code behaviour is functionally complete.

The deterministic routine engine supports:

- listing supplied routines
- starting a routine
- viewing the current routine
- marking checklist items done
- skipping checklist items
- finishing a routine
- producing a basic completion summary
- logging a finished routine

Automated tests and a manual end-to-end test have passed.

### Handoff

Continue the v0.3 documentation checkpoint.

Next documentation targets:

1. Update `versions.md` so v0.3 acceptance is marked complete.
2. Update `next.md` so the next target moves beyond v0.3.
3. Update `README.md` so it references `command-workflow.md` and no longer says v0.2 is the current target.

---

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

---

## 2026-05-28 — v0.2 manual data model trial complete

### Done

- Created repo-tracked CSV files under `data/manual-trial/`.
- Added a daily Wake-up Routine to `routines.csv`.
- Added a Weekly Planning routine to `routines.csv`.
- Added separate checklist item records to `checklist_items.csv`.
- Added example Wake-up Routine runs to `routine_runs.csv`.
- Added item-level completion records to `routine_run_items.csv`.
- Added both `done` and `skipped` checklist item examples.
- Added a six-monthly skin cancer check reminder to `reminders.csv`.
- Added a lightweight daily review row to `daily_review.csv`.
- Fixed a relational consistency issue by adding the missing parent routine run for a skipped item.
- Verified the v0.2 CSV data from GitHub.
- Updated `versions.md` so all v0.2 acceptance checklist items are complete.
- Updated `gpt_project_settings.txt` with a handoff rule for breaks, pauses, and continuing later.

### Key decisions

- v0.2 is complete.
- The repo-tracked CSV model is simple enough for the manual trial.
- CSV is suitable for proving the structure but is not intended as the serious long-term app storage.
- SQLite remains the preferred storage option for the serious MVP.
- Do not move directly to Telegram, Google Calendar, AI parsing, or voice.
- The next phase is v0.3: deterministic text-command routine tracker.

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

v0.2 manual data model trial is complete.

The project is ready to begin v0.3.

### Handoff

Start v0.3 by defining the first deterministic text-command workflow before writing code.
