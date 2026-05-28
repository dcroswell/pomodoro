# Manual Trial

This document records the v0.2 manual data model trial.

## Purpose

The purpose of v0.2 is to manually test how routines, checklist items, routine runs, reminders, and review entries should be stored before building code.

The goal is to confirm that the structure feels practical for real daily use.

## Storage decision

The v0.2 manual data model trial will start with Google Sheets.

Google Sheets is being used for the trial because it is easy to inspect, edit, and adjust manually.

SQLite remains the preferred storage option for the serious MVP because it is better suited to reliable application state, backups, testing, and long-term structured storage.

## Trial scope

The manual trial should include:

- at least one daily routine
- at least one weekly routine
- at least one longer-term recurring reminder
- checklist items stored as separate records
- at least one example routine run
- at least one example routine run item
- enough sample data to test whether the model feels usable

## Trial tabs

The Google Sheet should use one tab per data entity:

- `routines`
- `checklist_items`
- `routine_runs`
- `routine_run_items`
- `reminders`
- `daily_review`

Shopping list support is not required for this trial unless we deliberately bring it forward.

## Future hooks not required for first trial

The wider data model includes future-friendly hooks such as:

- `RoutineScheduleEvents`
- `ShoppingList`
- `routine_type`
- `action_type`
- `linked_resource_id`

These are useful for later support such as snoozing, rescheduling, special checklist item behaviour, and shopping list linkage.

They are not required for the first v0.2 Google Sheets trial unless we deliberately bring them forward.

Do not expand v0.2 just because the data model can support these later features.

## First routine to trial

The first routine to trial is: Wake-up Routine.

Initial checklist items:

- Brush teeth
- Make coffee
- Take pills
- Drink water

## Success criteria

The v0.2 manual trial is successful when:

- the Wake-up Routine can be represented clearly
- checklist items are separate records
- a routine run can be logged
- completed and skipped checklist items can be tracked
- the structure could be migrated to SQLite later
- the model feels simple enough to actually use
