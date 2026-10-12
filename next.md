# Next Actions

This document shows only the current target and the next few actions. It should stay short.

## Current target

Define the minimum durable routine-run log fields for v0.4: routine logging and daily review, using `versions.md` and the existing `RoutineRuns` and `RoutineRunItems` model in `data-model.md`, before changing storage or code.

## Current status

v0.1 planning and documentation baseline is complete.

v0.2 manual data model trial is complete.

v0.3 deterministic routine engine and documentation checkpoint are complete.

Verified v0.3 outcomes:

- `command-workflow.md` defines the first deterministic command workflow.
- `src/routine_engine.py` contains the routine engine.
- `tests/test_routine_engine.py` contains automated tests.
- `requirements-dev.txt` records the test dependency.
- The routine engine is generic and user-driven.
- Example routines are sample data only, not built-in application logic.
- User-supplied routines can be listed.
- A routine can be started.
- The active routine can be viewed.
- Checklist items can be marked done.
- Checklist items can be skipped.
- A routine can be finished.
- A basic completion summary is produced.
- A finished routine can be added to a routine log.
- Automated tests pass.
- Manual end-to-end testing passed.

The next phase is v0.4: routine logging and daily review.

## Next action

1. Define the minimum durable routine-run log fields using the v0.4 roadmap in `versions.md` and `RoutineRuns` / `RoutineRunItems` in `data-model.md`. This is a field-definition task only; do not implement fields or change storage yet.

## Do not work on yet

- Telegram bot
- Google Calendar integration
- AI parsing
- Voice transcription
- Native Android app
- Home Assistant integration
