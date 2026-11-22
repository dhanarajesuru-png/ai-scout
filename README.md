# Morning AI Scout

Morning AI Scout helps Dhanaraj Esuru, an MCA student pursuing Generative AI, keep up with useful AI tools and news and turn the best story into a video plan.

## What it does

- Researches AI tools and news published in the previous 24 hours across Product Hunt, Hacker News, Reddit, X, and official AI company blogs.
- Prioritizes mostly free tools Dhanaraj can try today and skips funding news, following `memory.md`.
- Shortlists up to five credible items, chooses one timely video idea, and explains why it fits his learning and audience.
- Writes three hook options and five major video points in Telugu, Hindi, and English, with source links.
- Saves each report in `outputs/YYYY-MM-DD.md`.
- When connected Google Drive and Gmail access is available, creates a dated Google Doc in `AI Scout` and emails the report as specified in the skill.

## Run the daily scout

Use the `daily-scout` skill for the morning run. It is located at `.chatgpt/skills/daily-scout/SKILL.md` and contains the step-by-step research, writing, saving, and delivery instructions.

Before every run, read `memory.md` and follow its rules. When Dhanaraj gives feedback, add a short rule dated with the feedback date so future runs can use it.

## Project files

- `CHATGPT.md` — the agent job description.
- `memory.md` — persistent preferences and feedback rules.
- `.chatgpt/skills/daily-scout/SKILL.md` — the daily run manual.
- `outputs/` — dated scout reports.

Each report covers only the previous 24 hours. If fewer than five credible items meet the criteria, the report should say so rather than pad the shortlist with older or weak stories.
