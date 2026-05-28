# Architecture

This document describes the intended architecture for RoutinePomodoro Assistant.

The architecture should stay simple at first. The project should not begin as a full AI assistant. The first goal is to prove that routines, checklist items, routine runs, reminders, and review entries can be represented clearly and used manually.

## System overview

RoutinePomodoro Assistant is intended to become a phone-first personal routine and life-admin assistant.

The long-term flow is:

1. A reminder tells the user it is time to start a routine.
2. The user starts the routine from a phone-friendly interface.
3. The system shows the checklist for that routine.
4. The user marks checklist items as done or skipped.
5. The system records what happened.
6. The user can review progress later.

A Pomodoro in this system means a named action block with a clear start, checklist, and finish. It does not need to be a strict 25-minute timer.

## Build order

The build order should be:

1. Manual data model trial.
2. Deterministic text-command routine tracker.
3. Phone interface, probably Telegram.
4. SQLite storage.
5. Google Calendar reminders.
6. Natural language parsing.
7. Voice notes and transcription.
8. AI-assisted features.

Do not build AI, voice, or calendar integration before the basic routine model and text-command workflow are clear.

## Components

The expected future components are:

| Component | Purpose |
|---|---|
| Phone interface | Lets the user start routines, mark items done, skip items, finish routines, and add reminders. |
| Command handler | Receives typed commands and turns them into structured actions. |
| Routine engine | Applies routine logic such as start, current, done, skip, and finish. |
| Storage layer | Stores routines, checklist items, routine runs, reminders, schedule events, shopping items, and reviews. |
| Calendar reminder layer | Creates or reads reminder timing, but does not own checklist state. |
| Natural language parser | Later converts plain English into structured commands. |
| Voice/transcription layer | Later converts voice notes into text commands. |
| AI layer | Later helps interpret commands, summarise progress, or suggest routines. |

The routine engine should not depend directly on Telegram, Google Calendar, AI, or voice.

## Data flow

The simple future command flow is:

1. The user sends a command from the phone.
2. The phone interface passes the message to the command handler.
3. The command handler parses the message into a structured action.
4. The routine engine validates and performs the action.
5. The storage layer records any changes.
6. The system sends a response back to the phone.

Example commands:

- `/routines`
- `/start wakeup`
- `/current`
- `/done take pills`
- `/skip stretch`
- `/finish`

The command handler can change later, but the routine engine should stay stable.

## Storage choice

The current v0.2 manual data model trial uses Google Sheets.

Google Sheets is suitable for v0.2 because it is easy to inspect, edit, and adjust manually.

SQLite remains the preferred storage option for the serious MVP because it is better for:

- reliable application state
- local backups
- testing
- structured queries
- migration into a real application

The storage model should follow `data-model.md`.

## Core storage entities

The core entities are:

- `Routines`
- `ChecklistItems`
- `RoutineRuns`
- `RoutineRunItems`
- `Reminders`
- `RoutineScheduleEvents`
- `ShoppingList`
- `DailyReview`

The first v0.2 manual trial does not need to test every future entity.

The first trial should focus on:

- routines
- checklist items
- routine runs
- routine run items
- reminders
- daily review

`RoutineScheduleEvents` and `ShoppingList` are future-friendly hooks. They should not expand the first manual trial unless deliberately brought forward.

## Calendar integration

Google Calendar should be used for timing and reminders only.

Google Calendar should not store:

- checklist state
- routine run history
- daily review answers
- shopping list state
- authoritative scheduled Pomodoro status

The app or database should own state.

The intended later flow is:

1. Google Calendar reminder fires.
2. The user opens or starts the matching routine.
3. The app maps the reminder to a routine or scheduled routine occurrence.
4. The app creates a routine run.
5. The app records checklist progress and completion status.

This separation allows future commands such as:

- snooze exercise
- move exercise to 12 noon
- skip exercise today

without changing the base routine template.

## Telegram interface

Telegram is the likely first phone interface.

Telegram is useful because it supports:

- typed commands
- mobile access
- quick replies
- voice notes later
- a simpler build path than a native Android app

The first Telegram version should use deterministic typed commands.

Natural language, voice notes, and AI parsing should come later.

## Voice and AI layer

Voice should be treated as another input method, not as a separate routine engine.

Preferred voice build order:

1. Typed Telegram commands.
2. Samsung or Google keyboard dictation into Telegram.
3. Telegram voice notes.
4. Speech-to-text transcription.
5. Natural language parsing of transcribed text.

AI should not be used for core state changes until the deterministic command system works.

Later AI features may include:

- interpreting natural-language commands
- summarising daily or weekly progress
- suggesting routine improvements
- helping capture reminders from rough notes

AI should confirm ambiguous actions before changing stored data.

## Special action types

Checklist items may have an `action_type`.

Initial action type:

- `checklist`

Possible later action types:

- `shopping_list`
- `note`
- `timer`
- `external_link`

This allows the core routine engine to stay simple while later features are added through specialised handlers.

Example:

A Chores Routine may include a checklist item called Grocery shopping.

That item can later use:

- `action_type = shopping_list`
- `linked_resource_id = weekly-groceries`

The first manual trial does not need to fully implement shopping list behaviour.

## Design principles

- Start simple.
- Keep the routine engine separate from interfaces.
- Keep storage structured from the beginning.
- Keep checklist items as separate records.
- Keep routine templates separate from routine runs.
- Keep calendar timing separate from routine state.
- Prefer deterministic commands before natural language.
- Add voice only after text commands work.
- Add AI only after the basic system is useful.
- Avoid building a large assistant before the routine tracker works.
- Keep documentation useful but not excessive.
- Keep the project easy to resume after a break.
