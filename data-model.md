# Data Model

This document defines how RoutinePomodoro Assistant stores routines, checklist items, routine runs, reminders, shopping list items, and daily review entries.

The goal is to keep the data structured from the beginning so it can start in Google Sheets if needed and later migrate cleanly to SQLite.

## Data model principles

- Store structured records, not large free-form text blocks.
- Use stable IDs for routines, checklist items, runs, reminders, and shopping items.
- Keep checklist items as separate records.
- Keep routine templates separate from routine run history.
- Keep calendar reminders separate from checklist state.
- Include `created_at`, `updated_at`, and `active` fields where useful.
- Avoid deleting historical records unless there is a clear reason.
- Prefer marking old records inactive rather than removing them.

---

## Entity overview

The core entities are:

- `Routines`
- `ChecklistItems`
- `RoutineRuns`
- `RoutineRunItems`
- `Reminders`
- `ShoppingList`
- `DailyReview`

---

## Routines

Stores the routine template.

A routine is a named Pomodoro-style action block, such as wake-up, exercise, weekly planning, or skin check reminder.

### Fields

| Field | Purpose | Example |
|---|---|---|
| `routine_id` | Stable unique ID | `wakeup` |
| `name` | Human-readable routine name | `Wake-up Routine` |
| `frequency` | How often it occurs | `daily` |
| `default_time` | Suggested start time | `07:00` |
| `category` | Broad grouping | `health`, `admin`, `house`, `fitness` |
| `active` | Whether routine is currently used | `yes` |
| `created_at` | Created timestamp | `2026-05-28T09:00:00+10:00` |
| `updated_at` | Last updated timestamp | `2026-05-28T09:00:00+10:00` |

### Example

| routine_id | name | frequency | default_time | category | active |
|---|---|---|---|---|---|
| `wakeup` | `Wake-up Routine` | `daily` | `07:00` | `health` | `yes` |
| `exercise` | `Exercise Routine` | `daily` | `08:00` | `fitness` | `yes` |
| `weekly-planning` | `Weekly Planning` | `weekly` | `Sunday 17:00` | `admin` | `yes` |
| `skin-check` | `Skin Cancer Check` | `six-monthly` | `09:00` | `health` | `yes` |

---

## ChecklistItems

Stores the checklist items belonging to each routine.

Each checklist item should be its own record. Do not store the whole checklist as one large text block.

### Fields

| Field | Purpose | Example |
|---|---|---|
| `item_id` | Stable unique ID | `wakeup-001` |
| `routine_id` | Parent routine ID | `wakeup` |
| `item_order` | Sort order inside routine | `1` |
| `item_text` | Checklist item text | `Brush teeth` |
| `active` | Whether item is currently used | `yes` |
| `created_at` | Created timestamp | `2026-05-28T09:00:00+10:00` |
| `updated_at` | Last updated timestamp | `2026-05-28T09:00:00+10:00` |

### Example

| item_id | routine_id | item_order | item_text | active |
|---|---|---:|---|---|
| `wakeup-001` | `wakeup` | 1 | `Brush teeth` | `yes` |
| `wakeup-002` | `wakeup` | 2 | `Make coffee` | `yes` |
| `wakeup-003` | `wakeup` | 3 | `Take pills` | `yes` |
| `wakeup-004` | `wakeup` | 4 | `Drink water` | `yes` |
| `exercise-001` | `exercise` | 1 | `Put on walking or gym clothes` | `yes` |
| `exercise-002` | `exercise` | 2 | `Walk toward step goal` | `yes` |
| `exercise-003` | `exercise` | 3 | `Gym or weights if planned` | `yes` |
| `exercise-004` | `exercise` | 4 | `Stretch` | `yes` |

---

## RoutineRuns

Stores each time a routine is started.

A routine template can have many routine runs.

### Fields

| Field | Purpose | Example |
|---|---|---|
| `run_id` | Stable unique run ID | `2026-05-28-wakeup-001` |
| `routine_id` | Routine being run | `wakeup` |
| `run_date` | Date of run | `2026-05-28` |
| `start_time` | Start timestamp | `2026-05-28T07:05:00+10:00` |
| `end_time` | Finish timestamp | `2026-05-28T07:28:00+10:00` |
| `status` | Run status | `active`, `completed`, `cancelled` |
| `completed_count` | Number of completed items | `4` |
| `total_count` | Number of items in run | `4` |
| `notes` | Optional notes | `Good start` |

### Example

| run_id | routine_id | run_date | start_time | end_time | status | completed_count | total_count |
|---|---|---|---|---|---|---:|---:|
| `2026-05-28-wakeup-001` | `wakeup` | `2026-05-28` | `07:05` | `07:28` | `completed` | 4 | 4 |

---

## RoutineRunItems

Stores the completion status of each checklist item for a specific routine run.

This allows the system to record which items were done, skipped, or missed.

### Fields

| Field | Purpose | Example |
|---|---|---|
| `run_item_id` | Stable unique run item ID | `2026-05-28-wakeup-001-item-001` |
| `run_id` | Parent routine run | `2026-05-28-wakeup-001` |
| `item_id` | Original checklist item ID | `wakeup-001` |
| `item_text` | Copied item text at time of run | `Brush teeth` |
| `status` | Item status | `pending`, `done`, `skipped` |
| `completed_time` | Completion timestamp | `2026-05-28T07:08:00+10:00` |
| `notes` | Optional notes | `Skipped due to time` |

### Example

| run_item_id | run_id | item_id | item_text | status | completed_time |
|---|---|---|---|---|---|
| `2026-05-28-wakeup-001-item-001` | `2026-05-28-wakeup-001` | `wakeup-001` | `Brush teeth` | `done` | `07:08` |
| `2026-05-28-wakeup-001-item-002` | `2026-05-28-wakeup-001` | `wakeup-002` | `Make coffee` | `done` | `07:12` |

---

## Reminders

Stores one-off and recurring reminders.

Google Calendar may contain the actual reminder event, but this table stores the project’s internal reminder record.

### Fields

| Field | Purpose | Example |
|---|---|---|
| `reminder_id` | Stable reminder ID | `skin-check-2026-11` |
| `title` | Reminder title | `Book skin cancer check` |
| `frequency` | Recurrence | `one-off`, `weekly`, `monthly`, `six-monthly`, `yearly` |
| `next_due_date` | Next due date | `2026-11-28` |
| `routine_id` | Optional linked routine | `skin-check` |
| `calendar_event_id` | Optional Google Calendar event ID | `abc123` |
| `status` | Reminder status | `active`, `completed`, `cancelled` |
| `created_at` | Created timestamp | `2026-05-28T09:00:00+10:00` |
| `updated_at` | Last updated timestamp | `2026-05-28T09:00:00+10:00` |

### Example

| reminder_id | title | frequency | next_due_date | routine_id | status |
|---|---|---|---|---|---|
| `skin-check-2026-11` | `Book skin cancer check` | `six-monthly` | `2026-11-28` | `skin-check` | `active` |
| `doctor-booking-2026-06` | `Book doctor appointment` | `one-off` | `2026-06-28` |  | `active` |

---

## ShoppingList

Stores shopping list items.

This is not part of the first planning milestone, but it is included in the data model because it is a likely later feature.

### Fields

| Field | Purpose | Example |
|---|---|---|
| `shopping_item_id` | Stable item ID | `shop-2026-05-28-001` |
| `item_text` | Shopping item | `Milk` |
| `status` | Item status | `active`, `bought`, `removed` |
| `added_at` | Added timestamp | `2026-05-28T10:00:00+10:00` |
| `completed_at` | Bought/removed timestamp | `2026-05-28T17:30:00+10:00` |
| `notes` | Optional notes | `Buy Greek yoghurt if available` |

---

## DailyReview

Stores the end-of-day review.

### Fields

| Field | Purpose | Example |
|---|---|---|
| `review_id` | Stable review ID | `review-2026-05-28` |
| `review_date` | Review date | `2026-05-28` |
| `wake_up_completed` | Wake-up routine done? | `yes` |
| `exercise_completed` | Exercise routine done? | `yes` |
| `steps` | Step count if recorded | `8000` |
| `gym_completed` | Gym done? | `no` |
| `main_achievement` | Main win for the day | `Created project docs` |
| `carry_over` | Things to move to tomorrow | `Finish data model` |
| `notes` | General notes | `Good momentum` |
| `created_at` | Created timestamp | `2026-05-28T20:30:00+10:00` |

---

## Storage decision

The storage approach may change by version:

### Trial storage

Google Sheets may be used to manually test this model because it is easy to inspect and edit.

### Long-term storage

SQLite is preferred for the serious MVP because it is more reliable, easier to test, local-first, and better suited to structured app state.

### Calendar storage rule

Google Calendar should store only timing and reminders.

It should not store:

- checklist state
- routine run history
- daily review answers
- shopping list state
- long-term logs

---

## Migration rule

Migration from Google Sheets to SQLite should be straightforward if:

- each sheet tab maps to one table;
- each row represents one record;
- each record has a stable ID;
- checklist items are separate records;
- timestamps are stored consistently;
- old records are marked inactive rather than deleted.
