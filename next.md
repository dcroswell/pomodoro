# Next Actions

This document shows only the current target and the next few actions. It should stay short.

## Current target

Begin v0.3: deterministic text-command routine tracker.

## Current status

v0.1 planning and documentation baseline is complete.

v0.2 manual data model trial is complete.

Verified v0.2 outcomes:

- Repo-tracked CSV files exist under `data/manual-trial/`.
- At least one daily routine is defined.
- At least one weekly routine is defined.
- At least one longer-term recurring reminder is defined.
- Checklist items are stored as separate records.
- At least one routine run is logged.
- At least one routine run item is logged.
- Completed and skipped checklist items can be tracked.
- The CSV model is simple enough for the manual trial.
- SQLite remains the preferred storage option for the serious MVP.

The next phase is v0.3.

v0.3 should start with deterministic text commands before writing code.

## Next 3 actions

1. Define the first deterministic text-command workflow for the Wake-up Routine.
2. Decide the smallest command set needed for v0.3.
3. Only after the workflow is clear, decide whether to create a small command spec or start minimal code.

## Do not work on yet

- Telegram bot
- Google Calendar integration
- AI parsing
- Voice transcription
- Native Android app
- Home Assistant integration
