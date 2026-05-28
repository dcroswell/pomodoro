# Next Actions

This document shows only the current target and the next few actions. It should stay short.

## Current target

Finish the v0.3 documentation checkpoint, then begin v0.4: routine logging and daily review.

## Current status

v0.1 planning and documentation baseline is complete.

v0.2 manual data model trial is complete.

v0.3 deterministic routine engine is functionally complete.

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

## Next 3 actions

1. Update `README.md` so it references `command-workflow.md` and no longer says v0.2 is the current target.
2. Confirm the v0.3 documentation checkpoint is complete.
3. Start v0.4 by defining the smallest durable routine log fields needed before changing storage.

## Do not work on yet

- Telegram bot
- Google Calendar integration
- AI parsing
- Voice transcription
- Native Android app
- Home Assistant integration
