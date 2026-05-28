# Progress Log

This document records what has been done, what has been decided, and what should happen next.

## 2026-05-28

### Done

- Created the `dcroswell/pomodoro` repo as the source of truth for this project.
- Added `README.md`.
- Added naming conventions to `README.md`.
- Added `requirements.md`.
- Added `versions.md`.
- Added `data-model.md`.
- Added `architecture.md`.
- Added `progress-log.md`.
- Completed the v0.1 planning and documentation checklist in `versions.md`.

### Key decisions

- This project is called RoutinePomodoro Assistant.
- A Pomodoro means a named action block with a clear start, checklist, and finish.
- Pomodoros are not required to be strict 25-minute timers.
- The project should support daily, weekly, monthly, six-monthly, yearly, and one-off routines/reminders.
- The first version should stay simple and avoid coding too early.
- The routine engine should be built before AI, voice, or calendar integration.
- Text commands should work before voice input.
- Google Calendar should store reminders and timing only.
- Google Calendar should not store checklist state or routine history.
- Google Sheets may be used for a manual storage trial.
- SQLite is preferred for the serious MVP.
- Telegram is the likely first phone interface.
- Samsung or Google keyboard dictation can provide a simple early voice workaround.
- The repo root should contain the core control documents.
- `docs/` should be reserved for supporting documents later.

### Current project documents

- `README.md`
- `requirements.md`
- `versions.md`
- `data-model.md`
- `architecture.md`
- `progress-log.md`
- `next.md`

### Current status

The project is in the planning and documentation stage.

The next goal is to Start v0.2 manual data model trial.

