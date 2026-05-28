# Next Actions

This document shows only the current target and the next few actions. It should stay short.

## Current target

Finish switching the v0.2 manual data model trial from Google Sheets to repo-tracked CSV files, then create the initial CSV trial data.

## Current status

v0.1 planning and documentation baseline is complete.

The v0.2 storage decision has changed:

- Use repo-tracked CSV files under `data/manual-trial/` for the manual data model trial.
- Do not use Google Sheets for the trial because ChatGPT cannot directly verify Google Sheets from this project.
- Keep SQLite as the preferred storage option for the serious MVP.

Updated so far:

- `versions.md`
- `manual-trial.md`
- `README.md`
- `architecture.md`

Still to update or verify:

- `progress-log.md`
- initial CSV files under `data/manual-trial/`

## Next 3 actions

1. Update `progress-log.md` with the storage decision change and documentation updates.
2. Create the initial CSV files under `data/manual-trial/`.
3. Verify the CSV files from GitHub before continuing the v0.2 manual trial.

## Do not work on yet

- Code
- Telegram bot
- Google Calendar integration
- AI parsing
- Voice transcription
- Native Android app
- Home Assistant integration
