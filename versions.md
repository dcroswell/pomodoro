# Versions

This document defines the staged roadmap for RoutinePomodoro Assistant.

The purpose of versioning is to keep the project small, clear, and achievable. Each version should have a clear goal, acceptance checklist, and things deliberately not included.

## Version principles

- Build the routine engine before adding AI.
- Build text commands before adding voice.
- Use calendar reminders only after the routine data model is clear.
- Keep each version small enough to finish.
- Do not start the next version until the current version acceptance checklist is complete.
- Avoid expanding the current version just because a future feature has been discussed.

---

## v0.1 — Planning and documentation baseline

### Goal

Create the core project documents and define the project clearly before building code.

### Includes

- Project README.
- Requirements document.
- Version roadmap.
- Data model document.
- Architecture document.
- Progress log.
- Next actions document.
- Naming conventions.
- Working protocol.

### Acceptance checklist

- [x] `README.md` exists.
- [x] `requirements.md` exists.
- [x] `versions.md` exists.
- [x] `data-model.md` exists.
- [x] `architecture.md` exists and contains real architecture notes.
- [x] `progress-log.md` exists.
- [x] `next.md` exists.
- [x] Naming conventions are documented.
- [x] Working protocol is documented.
- [x] First example routine is defined.
- [x] Initial storage decision is recorded.
- [x] Next build step is clearly identified.

### Not included

- Code.
- Telegram bot.
- Voice input.
- AI parsing.
- Google Calendar integration.

---

## v0.2 — Manual data model trial

### Goal

Test how routines, checklist items, routine runs, reminders, and review entries should be stored before building code.

The purpose is to prove that the model feels practical for real daily use.

### Storage decision

The v0.2 manual data model trial uses repo-tracked CSV files stored under `data/manual-trial/`.

Repo-tracked CSV files are being used because they are simple, structured, version-controlled, and directly inspectable by ChatGPT through the GitHub connector.

Google Sheets is not used for the trial because ChatGPT cannot directly verify Google Sheets from this project.

SQLite remains the preferred storage option for the serious MVP.

### Includes

- Use `manual-trial.md` to record the v0.2 trial notes.
- Define example routines manually.
- Define checklist items manually.
- Store trial data in repo-tracked CSV files under `data/manual-trial/`.
- Create at least one daily routine.
- Create at least one weekly routine.
- Create at least one longer-term recurring reminder.
- Create at least one example routine run.
- Create at least one example routine run item.
- Confirm the fields needed for routine templates and routine runs.
- Confirm whether the model feels simple enough to use.

### Acceptance checklist

- [ ] `manual-trial.md` records the trial scope and decisions.
- [ ] Repo-tracked CSV files are set up under `data/manual-trial/`.
- [ ] At least one daily routine is defined.
- [ ] At least one weekly routine is defined.
- [ ] At least one longer-term recurring reminder is defined.
- [ ] Checklist items are stored as separate records, not as one large text block.
- [ ] At least one routine run is logged.
- [ ] At least one routine run item is logged.
- [ ] Completed and skipped checklist items can be tracked.
- [ ] Storage format can be migrated later.
- [ ] The model feels simple enough to actually use.

### Not included

- Code.
- Automation.
- Telegram bot.
- Calendar integration.
- Voice input.
- AI parsing.
- Full shopping list implementation.
- Full scheduled occurrence implementation.

---

## v0.3 — Text-command routine tracker

### Goal

Create the first usable routine tracker using deterministic text commands.

### Includes

- Start a routine.
- Show the current routine.
- Mark checklist items done.
- Mark checklist items skipped.
- Finish a routine.
- Save a basic routine log.

### Example commands

- `/routines`
- `/start wakeup`
- `/current`
- `/done take pills`
- `/skip stretch`
- `/finish`

### Acceptance checklist

- [ ] User can list available routines.
- [ ] User can start a routine.
- [ ] User can view the active routine.
- [ ] User can mark an item done.
- [ ] User can skip an item.
- [ ] User can finish the routine.
- [ ] Routine completion is logged.
- [ ] Basic manual testing passes.

### Not included

- Natural language parsing.
- Voice transcription.
- Calendar integration.
- Weekly summaries.
- Mobile app.

---

## v0.4 — Routine logging and daily review

### Goal

Improve logging so the system records what actually happened each day.

### Includes

- Routine run history.
- Checklist item completion history.
- Basic notes.
- Daily review routine.
- Ability to record steps, gym, main achievement, and carry-over items.

### Acceptance checklist

- [ ] Each routine run has a start time and finish time.
- [ ] Completed and skipped items are recorded.
- [ ] Daily review can be completed.
- [ ] Daily review notes are stored.
- [ ] User can inspect the log.

### Not included

- AI-generated summaries.
- Voice input.
- Complex analytics dashboard.

---

## v0.5 — Shopping list support

### Goal

Add simple shopping list functionality.

### Includes

- Add item to shopping list.
- Show shopping list.
- Mark item bought.
- Remove item from list.
- Link a routine checklist item to a shopping list where useful.

### Example commands

- `/shopping add milk`
- `/shopping show`
- `/shopping bought milk`
- `/shopping remove milk`

### Acceptance checklist

- [ ] User can add shopping items.
- [ ] User can view active shopping items.
- [ ] User can mark items bought.
- [ ] Bought items are recorded or removed consistently.
- [ ] A routine checklist item can link to a shopping list.

### Not included

- Recipe planning.
- Supermarket categories.
- Barcode scanning.

---

## v0.6 — Calendar reminders

### Goal

Use Google Calendar to remind the user when routine blocks or future tasks are due.

### Includes

- Create one-off reminders.
- Create recurring reminders.
- Link reminders to routines where appropriate.
- Keep checklist state outside the calendar.
- Store reminder ID or calendar event ID where useful.

### Acceptance checklist

- [ ] User can create a one-off reminder.
- [ ] User can create a recurring reminder.
- [ ] Google Calendar event is created successfully.
- [ ] Calendar stores timing only, not checklist state.
- [ ] Reminder ID or calendar event ID is stored.
- [ ] Routine state remains owned by the app/database, not by Google Calendar.

### Not included

- Calendar as primary data store.
- Full calendar assistant.
- Complex rescheduling logic.

---

## v0.7 — Natural language parsing

### Goal

Allow simple natural language commands after deterministic commands are stable.

### Includes

- Interpret simple phrases.
- Convert phrases into structured actions.
- Confirm ambiguous actions before changing data.
- Keep deterministic commands working.

### Example phrases

- “Start my wake-up routine.”
- “I took my pills.”
- “I bought the milk.”
- “Remind me in six months to book a skin cancer check.”

### Acceptance checklist

- [ ] Common natural language phrases map to the correct action.
- [ ] Ambiguous phrases are not guessed silently.
- [ ] The structured action is logged or inspectable.
- [ ] Deterministic commands still work.

### Not included

- Full conversational memory.
- Complex agent autonomy.
- Wake word activation.

---

## v0.8 — Voice input

### Goal

Add voice as an input method once text commands and parsing are stable.

### Includes

- Accept Telegram voice notes or equivalent.
- Transcribe audio to text.
- Pass transcribed text through the same parser used for typed input.
- Reply with a text confirmation.

### Acceptance checklist

- [ ] User can send a voice note.
- [ ] Voice note is transcribed.
- [ ] Transcribed text is processed as a command.
- [ ] System confirms the action.
- [ ] Failed transcription is handled safely.

### Not included

- Voice replies.
- Wake word activation.
- Always-listening assistant.

---

## v1.0 — Useful daily assistant

### Goal

Create a stable version useful enough for daily personal use.

### Includes

- Routine templates.
- Routine tracking.
- Completion logging.
- Daily review.
- Shopping list.
- Calendar reminders.
- Basic natural language support.
- Optional voice input.

### Acceptance checklist

- [ ] User can use the system for daily routines.
- [ ] User can use the system for weekly, monthly, and life-admin reminders.
- [ ] Logs are reliable.
- [ ] Data is easy to back up.
- [ ] Setup instructions are clear.
- [ ] Known limitations are documented.

### Not included

- Native Android app unless separately justified.
- Full home assistant platform.
- Complex autonomous agent behaviour.
