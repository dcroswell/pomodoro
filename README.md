# RoutinePomodoro Assistant

RoutinePomodoro Assistant is a personal routine and life-admin assistant project. The aim is to manage daily, weekly, monthly, half-yearly, yearly, and one-off Pomodoro-style routine blocks from a phone-friendly interface.

A Pomodoro in this project does not have to mean a strict 25-minute timer. It means a named action block with a clear start, checklist, and finish.

## Core idea

- Calendar reminders tell me when to start a routine.
- Routine checklists tell me what to do inside the block.
- A log records what actually happened.
- A phone interface lets me start routines, mark items done, add reminders, and review progress.

## Example routines

- Wake-up routine: brush teeth, make coffee, take pills, drink water, check the day.
- Exercise routine: walk, gym, stretch, log steps or activity.
- Daily review: record what was completed and what should move to tomorrow.
- Weekly planning: review the calendar, admin tasks, house reset, and upcoming commitments.
- Health/admin reminders: skin cancer checks, doctor appointments, dentist, blood tests, insurance reviews.

## Current status

Ready to begin v0.2: manual data model trial.

See `next.md` for the current target and next actions.

## Intended build direction

Early trial:

- Use structured data to define routines and checklist items.
- Consider Google Sheets for a simple manual storage trial.

Serious MVP:

- Samsung phone interface via Telegram or similar.
- Python/FastAPI backend or simple automation workflow.
- SQLite as the long-term source of truth.
- Google Calendar for reminders only.
- Voice and AI parsing added later, after text commands work reliably.

## Key design principles

- Start simple.
- Keep the routine engine working before adding AI or voice.
- Calendar stores reminders, not checklist state.
- Data should be structured and easy to migrate.
- The repo is the single source of truth.

## Core project documents

- `requirements.md` — what the system must and must not do.
- `versions.md` — staged roadmap from v0.1 to v1.0.
- `data-model.md` — how routines, checklists, logs, and reminders are stored.
- `architecture.md` — how phone, backend, storage, and calendar fit together.
- `progress-log.md` — historical record of completed work and decisions.
- `next.md` — current target and next actions only.

## Naming conventions

This repo uses simple, consistent file naming:

- `README.md` stays uppercase because it is the standard GitHub entry file.
- Markdown documentation files use lowercase kebab-case, for example `data-model.md` and `progress-log.md`.
- Folders use lowercase names, for example `docs/`, `src/`, `tests/`, and `data/`.
- Python files will use lowercase snake_case, for example `routine_engine.py`.
- Avoid mixed styles such as camelCase, PascalCase, random capitals, or spaces in filenames.

## Working protocol

### Markdown file output rule

When providing a full Markdown file for copy/paste:

- Do not wrap the whole file in an outer fenced code block if the file itself contains fenced code blocks.
- Prefer a downloadable `.md` file for full-file replacements.
- If copy/paste text is provided instead, avoid nested triple-backtick fences.
- Check the Markdown before providing it for:
  - accidental wrapper text such as `:::writing`
  - unbalanced triple-backtick fences
  - broken tables
  - incorrect first or last lines
- For full-file replacements, state the expected first and last line of the file.

Each work session should follow this simple pattern:

### Start of session

- Read `README.md` for the project overview and working protocol.
- Read `next.md` to confirm the current target and next actions.
- Read the latest entry in `progress-log.md` for recent decisions and handoff notes.
- Read specialist documents only when relevant:
  - `requirements.md` when changing scope or behaviour.
  - `versions.md` when changing roadmap, milestones, or checklists.
  - `data-model.md` when changing storage, fields, examples, or trial data.
  - `architecture.md` when changing system design, components, or integrations.
- Work on one small step at a time.

### During session

- Work on the project first; documentation should support the work, not replace it.
- Work in small, clear steps, but group related edits together where practical.
- If multiple changes belong in the same file, make them in one edit and commit once.
- Update documents only when a decision, milestone, target, requirement, data model, or architecture changes.
- Prefer one end-of-session documentation checkpoint over frequent small documentation edits.
- Verify completed steps where possible.
- Avoid expanding scope unless it is deliberately added to the roadmap.
- Do not update `next.md` after every tiny action.

### End of session

- Update `progress-log.md` only when meaningful progress or decisions were made.
- Update `next.md` only if the next target has changed or the session is ending.
- Commit and push the documentation checkpoint if documents changed.
