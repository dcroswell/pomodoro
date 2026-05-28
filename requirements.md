# Requirements

## Goal

Build a phone-first personal routine assistant that helps manage daily, weekly, monthly, half-yearly, yearly, and one-off Pomodoro-style routine blocks.

A Pomodoro in this project means a named action block with a clear start, checklist, and finish. It does not have to be a strict 25-minute timer.

## Core use cases

### Daily routines

The system should support routines such as:

- Wake-up routine
- Exercise routine
- Admin routine
- Evening reset
- Daily review

### Weekly routines

The system should support weekly planning and maintenance routines such as:

- Review the week ahead
- Check calendar
- Pay or review bills
- House reset
- Meal planning
- Family/admin check-in

### Monthly routines

The system should support monthly life-admin routines such as:

- Budget review
- Subscriptions review
- File/photo backup
- Book or check appointments
- Review health habits

### Half-yearly and yearly routines

The system should support longer-term recurring reminders such as:

- Skin cancer check
- GP appointment or blood test review
- Dentist check-up
- Eye test
- Insurance review
- Tax preparation
- Passport or ID check
- Smoke alarm check

### One-off future reminders

The system should support one-off future reminders such as:

- In one month, remind me to book a doctor appointment.
- Next Friday, remind me to call someone.
- Tomorrow morning, remind me to follow up an admin task.

## MVP requirements

The first usable version should allow the user to:

- Define routine templates.
- Add checklist items to routines.
- Start a routine.
- View the current routine checklist.
- Mark checklist items as done.
- Mark checklist items as skipped.
- Finish a routine.
- Log the routine result.
- Record basic notes.
- Use structured storage that can later migrate to SQLite if needed.

## Later requirements

Later versions may add:

- Telegram bot interface.
- Google Calendar reminders.
- Shopping list support.
- Daily review summaries.
- Weekly and monthly reports.
- Natural language command parsing.
- Voice note transcription.
- AI-assisted interpretation of commands.
- Home Assistant integration.
- Local LLM support.

## Out of scope for now

The following are deliberately out of scope for the first version:

- Native Android app.
- Wake word activation.
- Full AI memory system.
- Complex dashboard.
- Voice transcription.
- Advanced natural language processing.
- Multi-user support.
- Home Assistant integration.
- Automatic health device integration.
