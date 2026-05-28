# Architecture

This document explains how the RoutinePomodoro Assistant system is expected to fit together.

The architecture should stay simple at first. The project should prove the routine engine before adding AI, voice, or complex automation.

## Architecture principles

- Start with the smallest useful system.
- Keep the routine engine separate from the phone interface.
- Keep storage separate from Google Calendar.
- Use structured data rather than free-form notes.
- Add voice only after text commands work.
- Add AI parsing only after deterministic commands work.
- Prefer local-first storage for the serious MVP.

---

## Conceptual system flow

The intended user flow is:

```text
Samsung phone
-> phone interface
-> command handler
-> routine engine
-> storage
-> optional calendar reminder
-> response back to phone
```

Example:

```text
User says or types: "Start wake-up routine"
-> system identifies start routine command
-> routine engine creates a new routine run
-> storage records the active run
-> system replies with checklist
```

---

## Main components

## Phone interface

The phone interface is how the user interacts with the system.

Likely first option:

```text
Telegram bot
```

Reasons:

- Works on Samsung/Android.
- Supports typed messages.
- Supports voice notes later.
- Avoids building a native Android app.
- Simple enough for early testing.

Early voice workaround:

```text
Samsung or Google keyboard dictation -> Telegram text message
```

This gives useful voice input before building true transcription.

---

## Command handler

The command handler receives text commands and decides what action is required.

Early examples:

```text
/start wakeup
/current
/done take pills
/skip stretch
/finish
```

The command handler should convert messages into structured actions.

Example structured action:

```json
{
  "intent": "complete_checklist_item",
  "routine_id": "wakeup",
  "item_text": "take pills"
}
```

At first, this should use deterministic command parsing, not AI.

---

## Routine engine

The routine engine is the core of the project.

It should handle:

- listing routines
- starting a routine
- showing the current routine
- marking items done
- skipping items
- finishing routines
- logging routine results
- supporting daily, weekly, monthly, six-monthly, yearly, and one-off routines

The routine engine should not depend directly on Telegram, Google Calendar, or AI. Those should be external interfaces or integrations.

---

## Storage

Storage is where routines, checklist items, routine runs, reminders, shopping list items, and daily reviews are kept.

### Trial storage

Google Sheets may be used for manual testing because it is easy to inspect.

### Serious MVP storage

SQLite is preferred for the serious MVP.

Reasons:

- local-first
- reliable
- structured
- easy to back up
- easy to test
- better than a spreadsheet for application state

### Storage rule

Storage is the source of truth for:

- routine templates
- checklist items
- active routine runs
- routine history
- skipped and completed items
- reminders
- shopping list items
- daily reviews

---

## Google Calendar

Google Calendar should be used for reminders and schedule triggers only.

It should store:

- routine start reminders
- one-off reminders
- recurring reminders
- calendar event IDs linked back to internal reminder records

It should not store:

- checklist state
- routine run history
- daily review answers
- shopping list state
- long-term logs

Calendar is a timing tool, not the main database.

---

## AI parsing

AI parsing is a later feature.

The first version should use exact text commands.

Later, AI can help convert natural language into structured actions.

Example:

```text
"I took my pills"
```

could become:

```json
{
  "intent": "complete_checklist_item",
  "routine_id": "wakeup",
  "item_text": "take pills"
}
```

AI should not silently guess when the command is ambiguous. It should ask for confirmation.

---

## Voice input

Voice input is a later feature.

Recommended build order:

1. Typed Telegram commands.
2. Samsung/Google keyboard dictation into Telegram.
3. Telegram voice notes.
4. Speech-to-text transcription.
5. Natural language parsing of transcribed text.

Voice should be treated as another input method. It should not change the core routine engine.

---

## Suggested technology path

## v0.1 and v0.2

Documentation and manual data model trial.

Possible storage:

```text
Google Sheets
```

or

```text
SQLite
```

## v0.3 and beyond

Serious MVP direction:

```text
Samsung phone
-> Telegram bot
-> Python command handler
-> routine engine
-> SQLite
-> optional Google Calendar integration
```

## Later optional integrations

- Google Calendar
- Google Sheets export
- AI parser
- voice transcription
- Home Assistant
- local LLM

---

## Initial architecture decision

The initial architecture should not try to be a full AI assistant.

The first real build should be:

```text
Telegram text commands + routine engine + structured storage
```

Only after that works should the project add:

- Google Calendar reminders
- natural language parsing
- Telegram voice notes
- AI features
