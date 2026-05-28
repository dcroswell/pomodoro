# Manual Trial

This document records the v0.2 manual data model trial.

## Purpose

The purpose of v0.2 is to manually test how routines, checklist items, routine runs, reminders, and review entries should be stored before building code.

The goal is to confirm that the structure feels practical for real daily use.

## Storage decision

The v0.2 manual data model trial uses repo-tracked CSV files stored under `data/manual-trial/`.

Repo-tracked CSV files are being used because they are simple, structured, version-controlled, and directly inspectable by ChatGPT through the GitHub connector.

Google Sheets is not used for the trial because ChatGPT cannot directly verify Google Sheets from this project.

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

## Trial files

The repo should store one CSV file per data entity under `data/manual-trial/`:

- `data/manual-trial/routines.csv`
- `data/manual-trial/checklist_items.csv`
- `data/manual-trial/routine_runs.csv`
- `data/manual-trial/routine_run_items.csv`
- `data/manual-trial/reminders.csv`
- `data/manual-trial/daily_review.csv`

Shopping list support is not required for this trial unless we deliberately bring it forward.

## Trial simplification decisions

The v0.2 manual trial should avoid duplicate data where practical.

For the current proof of concept:

- `routine_runs` records that a routine happened.
- `routine_runs` does not store `completed_count` or `total_count`.
- `routine_run_items` records item-level completion.
- completed and skipped counts can be derived from `routine_run_items`.
- `daily_review` stays lightweight.
- `daily_review` uses only `review_id`, `review_date`, and `notes`.
- `daily_review` does not duplicate routine completion fields such as `wake_up_completed` or `exercise_completed`.

This keeps the CSV files closer to a clean relational model and makes later migration to SQLite easier.

## Future hooks not required for first trial

The wider data model includes future-friendly hooks such as:

- `RoutineScheduleEvents`
- `ShoppingList`
- `routine_type`
- `action_type`
- `linked_resource_id`

These are useful for later support such as snoozing, rescheduling, special checklist item behaviour, and shopping list linkage.

They are not required for the first v0.2 CSV trial unless we deliberately bring them forward.

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
