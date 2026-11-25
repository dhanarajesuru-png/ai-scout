# Daily Scout

This skill is the source of truth for Morning AI Scout operations. Read `memory.md` before every run and follow all rules in it.

## Run modes

- **Daily mode:** Use for every scheduled run and ordinary “run the scout” request. Perform the research, save the dated report, validate it, then email it through Gmail.
- **Test mode:** Use only when Dhanaraj asks for a sample or test. Do not perform new web research, overwrite a daily report, or resend the full digest. Validate the latest saved report with `python scripts/validate_report.py outputs/YYYY-MM-DD.md`. If Dhanaraj explicitly asks to test email delivery, send a brief message with a clearly labeled test subject to the authenticated Gmail account. Do not use Google Drive or create Google Docs.

Scheduled runs always use Daily mode.

## Daily mode steps

1. **Read memory first.** Open `memory.md` before researching. Follow every rule. If it does not exist, create it with a `# Memory` heading.
2. **Set the window.** Use current India time (Asia/Kolkata). Include only items first published, announced, or launched within the previous 24 hours. Record the start and end time and time zone. Older items do not count as new.
3. **Collect candidates.** Check Product Hunt, Hacker News, Reddit, X, official AI company blogs, and primary research sources. Prefer official feeds/APIs where available, then use search and community sites for discovery. For every candidate record its first-post time, discovery link, primary source link, and whether it is free, has a limited free tier/trial, requires your own paid model key, or is paid.
4. **Rank tools and news.** Follow `memory.md`: prioritize mostly free tools Dhanaraj can try today and skip funding news. Score each candidate 0–3 for freshness, source evidence, practical usefulness/cost, and Gen AI learning value. Remove duplicates and unsupported claims; use score and source quality to choose up to five. Do not describe a limited trial or BYOK tool as simply free. State the access/cost caveat. If fewer than five qualify, say how many; do not pad.
5. **Find and rank research papers.** Search arXiv, OpenReview, ACL Anthology, CVF Open Access, PMLR, and official AI lab research pages. Discovery sites such as Hugging Face Daily Papers or Papers with Code may surface candidates, but verify every item at its primary publisher or author page. First-post/publication within the 24-hour window is a hard requirement; a new version of an older paper does not qualify. Score eligible papers 0–3 for Gen AI relevance, novelty, evidence quality, and reproducibility/accessibility. List up to five. If none qualify, say so plainly and stop: do not add older background papers unless Dhanaraj specifically asks for them. For each paper include title, authors, first-post/publication time, primary link, preprint or peer-reviewed status, plain-English contribution, why it matters, and one caveat. Never call a preprint peer reviewed.
6. **Choose one video idea.** Select the best timely idea from the qualifying tools/news and papers for Dhanaraj Esuru, an MCA student pursuing Gen AI. Explain why it fits his studies and audience, what viewers can learn, and whether it is based on a tool, news item, or paper.
7. **Write the outline.** Provide three hook options, each in Telugu, Hindi, and English. Then write exactly five major video points, each in all three languages with the same meaning and a supporting source link. Use natural language, preserve technical meaning, and use different reliable source platforms where available.
8. **Save the report.** Create `outputs/` if needed and save as `outputs/YYYY-MM-DD.md` using today’s India date. Include:
   - `# Morning AI Scout — YYYY-MM-DD`
   - Exact research window (Asia/Kolkata)
   - `## Top 5 AI tools and news`
   - `## Top 5 AI research papers`
   - `## Best video idea`
   - `## Hook options`
   - `## Five major points`

   Show fewer than five items when fewer qualify. If none qualify for a shortlist, state that explicitly. Do not add unrequested background items.
9. **Validate before emailing.** Run `python scripts/validate_report.py outputs/YYYY-MM-DD.md`. Fix every reported error before continuing. The validator checks the date/window, required sections, item limits, language coverage, and links. Do not claim validation passed if it did not run successfully.
10. **Email directly through Gmail.** Do not use Google Drive or create a Google Doc. Search Sent for the exact daily subject/date first; never send a duplicate daily digest for a date already delivered. If no duplicate exists, send to the authenticated Gmail account using subject `Morning AI Scout — YYYY-MM-DD`. Put a brief summary of the best video idea and shortlist counts first, followed by the complete report and `outputs/YYYY-MM-DD.md` path. If Gmail is unavailable or the authenticated recipient cannot be resolved, do not guess; report that delivery did not happen.
11. **Apply feedback next time.** When Dhanaraj gives feedback, add a short rule dated with the feedback date to `memory.md`. Keep existing rules and follow all rules in future runs.


## GitHub-hosted scheduled runs

The scheduled workflow at .github/workflows/daily-scout.yml runs on a GitHub-hosted runner at 07:00 Asia/Kolkata, so it can run when Dhanaraj's computer is off. The runner reads memory.md before doing work, loads this skill plus .agents/skills/tavily-search/SKILL.md and .agents/skills/tavily-sdk/SKILL.md, searches through the Tavily Python SDK, generates the report through the OpenAI API, and runs scripts/validate_report.py. The official Tavily skills are also kept in skills-lock.json and .agents/skills/.

For GitHub Actions delivery, use scripts/send_report_email.py with the GMAIL_ADDRESS Actions variable and GMAIL_APP_PASSWORD secret. The hosted runner cannot access the Gmail connector signed in inside ChatGPT/Codex. Send directly through Gmail SMTP; never use Google Drive. After successful email delivery, commit the report, the outputs/.sent marker, and memory.md to main. See AUTOMATION_SETUP.md for required GitHub settings and credentials.
