# Command Workflow

This document defines the first deterministic text-command workflow for v0.3.

The goal is to describe exactly how the Wake-up Routine should behave before writing code.

## Current version

v0.3 — Text-command routine tracker.

## First routine

Routine ID: `wakeup`

Routine name: Wake-up Routine.

Checklist items:

1. Brush teeth
2. Make coffee
3. Take pills
4. Drink water

## Smallest useful command set

The first command set should be deliberately small:

- `/routines`
- `/start wakeup`
- `/current`
- `/done <item>`
- `/skip <item>`
- `/finish`

## Workflow

### 1. List routines

User enters:

`/routines`

System responds with available routines:

- `wakeup` — Wake-up Routine
- `weekly-planning` — Weekly Planning

### 2. Start the Wake-up Routine

User enters:

`/start wakeup`

System creates an active routine run for the Wake-up Routine.

System responds:

`Started Wake-up Routine.`

Then it shows the checklist:

- [ ] Brush teeth
- [ ] Make coffee
- [ ] Take pills
- [ ] Drink water

### 3. Show current routine

User enters:

`/current`

System responds with the active routine and current item states.

Example:

`Wake-up Routine is active.`

- [ ] Brush teeth
- [ ] Make coffee
- [ ] Take pills
- [ ] Drink water

### 4. Mark an item done

User enters:

`/done take pills`

System marks the matching checklist item as done.

System responds:

`Marked done: Take pills.`

Then it shows the updated checklist.

### 5. Skip an item

User enters:

`/skip make coffee`

System marks the matching checklist item as skipped.

System responds:

`Skipped: Make coffee.`

Then it shows the updated checklist.

### 6. Finish the routine

User enters:

`/finish`

System closes the active routine run.

System responds with a short summary.

Example:

`Finished Wake-up Routine: 3 done, 1 skipped.`

## Matching rules for v0.3

For the first version, item matching should be simple and deterministic.

Allowed:

- Exact item text match, case-insensitive.
- Partial match only if it matches exactly one checklist item.

Not allowed yet:

- AI guessing.
- Natural language interpretation.
- Voice commands.
- Calendar changes.
- Telegram integration.

## Error cases

### No active routine

If the user enters `/current`, `/done`, `/skip`, or `/finish` without an active routine, the system should respond:

`No routine is currently active.`

### Unknown routine

If the user enters `/start unknown-routine`, the system should respond:

`Routine not found: unknown-routine.`

### Ambiguous item match

If the user enters a partial item name that matches more than one item, the system should respond:

`That item is ambiguous. Please use the exact checklist item name.`

### Unknown item

If the user enters `/done unknown item` or `/skip unknown item`, the system should respond:

`Checklist item not found: unknown item.`

## Future interaction notes

Later versions may support natural language, voice, and calendar reminders.

Examples:

- “Hey Pomodoro, time to wake up.”
- “Okay, I’ve made coffee.”
- “Let’s skip coffee today.”
- Calendar reminder: “Hey Don, it’s time for your Wake-up Routine. Start now?”

These should eventually map to the same internal routine actions as the deterministic commands.

The routine engine should stay separate from the input method.

## Acceptance check for this workflow

This workflow is good enough for v0.3 planning when:

- The Wake-up Routine can be started.
- The active routine can be shown.
- Items can be marked done.
- Items can be skipped.
- The routine can be finished.
- Errors are handled without guessing.
- No AI, voice, Telegram, or calendar behaviour is implemented yet.
