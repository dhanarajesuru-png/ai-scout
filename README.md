# Morning AI Scout

Morning AI Scout helps Dhanaraj Esuru, an MCA student pursuing Generative AI, find useful AI tools, news, and research and turn the strongest item into a video plan.

## Workflow

- Daily mode runs on the 24-hour India-time window, prioritizes tools that are mostly free to try, skips funding news, and verifies papers at primary sources.
- Test mode validates the latest saved report without repeating research or resending the daily digest.
- Each report includes up to five tools/news items, up to five eligible papers, one video idea, three trilingual hooks, and five trilingual outline points.
- Reports are saved in `outputs/YYYY-MM-DD.md`, validated before delivery, and emailed directly through Gmail. The workflow does not use Google Drive.

## Instructions

The operational source of truth is `.chatgpt/skills/daily-scout/SKILL.md`. Read `memory.md` before every run; it stores Dhanaraj’s persistent preferences and feedback rules.

## Project files

- `CHATGPT.md` — short agent description.
- `memory.md` — preferences and feedback.
- `.chatgpt/skills/daily-scout/SKILL.md` — daily and test procedures.
- `scripts/validate_report.py` — pre-email report checks.
- `outputs/` — dated reports.
