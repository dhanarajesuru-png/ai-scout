# Daily Scout

Use this skill for Morning AI Scout’s daily research and video planning run.

## Step-by-step morning run

1. **Read memory first.** Open `memory.md` before researching. Follow every rule in it. If it does not exist, create it with a `# Memory` heading.
2. **Set the time window.** Use the current date and time, and look only for items first published or launched in the previous 24 hours. Record the window in the report, including the time zone. Do not present older items as new; if an older item is useful context, label it clearly as background.
3. **Search AI news and tools.** Use the `tavily-search` skill (`.agents/skills/tavily-search/SKILL.md`) with the `tvly search` command to search for AI tools and news on Product Hunt, Hacker News, Reddit, X, and official AI company blogs. Run targeted queries such as `"new AI tool site:producthunt.com"`, `"AI launch site:news.ycombinator.com"`, and official blog searches. Requires `TAVILY_API_KEY` in the environment. Keep links and publication times for all candidates.
4. **Verify and shortlist the news.** Follow `memory.md`: prioritize mostly free AI tools Dhanaraj can try today and skip funding news. Remove duplicates, stale items, and unsupported claims. Select up to five distinct qualifying items, giving each its name or headline, source link, publication time when available, and one line on why it matters. If fewer than five credible items qualify, say so rather than padding with older or weak stories.
5. **Find and shortlist AI research papers.** Use the `tavily-research` skill (`.agents/skills/tavily-research/SKILL.md`) with the `tvly research` command to do a deep multi-source research run. Search primary research sources: [arXiv](https://arxiv.org/list/cs.AI/new) (including relevant new submissions in cs.AI, cs.LG, stat.ML, cs.CL, cs.CV, and cs.RO), [OpenReview](https://openreview.net/), [ACL Anthology](https://aclanthology.org/), [CVF Open Access](https://openaccess.thecvf.com/), [Proceedings of Machine Learning Research](https://proceedings.mlr.press/), and official AI lab research pages. For discovery, also check [Hugging Face Daily Papers](https://huggingface.co/papers) and [Papers with Code](https://paperswithcode.com/), then verify each candidate against its primary paper or venue page. Include only papers first posted or published during the previous 24 hours; an older paper revision does not count as a new paper. Rank candidates by relevance to Gen AI learning, novelty, evidence, and reproducibility, not popularity alone. Prefer free-to-read papers and code or datasets that Dhanaraj can try. For each paper, include title, authors, first-posted/published time, primary link, whether it is a preprint or peer-reviewed publication, a plain-language summary of its contribution, why it matters, and one caveat or limitation. Never describe an arXiv preprint as peer reviewed. If fewer than five credible papers qualify, say so rather than filling the list with older work.
6. **Choose one video idea.** Pick the single strongest idea from both shortlists for Dhanaraj Esuru, an MCA student pursuing Gen AI. Explain why it fits his education and audience, what makes it timely, and what viewers can learn. Ground it in verified news or paper claims.
7. **Write hooks in three languages.** Provide three hook options, with each option written in Telugu, Hindi, and English. Keep each version natural, engaging, and faithful to the same idea. Do not translate technical claims in a way that changes their meaning.
8. **Give five major points in three languages.** Write exactly five concise outline points based on the selected paper or news item and video idea. Put them in a useful video order, from context and what happened through implications or a practical takeaway. For each point, provide Telugu, Hindi, and English versions that preserve the same facts and meaning. Use natural phrasing, retain technical terms where translating them would be unclear, and do not invent details. Include a supporting source link with each point; use different reliable platforms across the five points where available, and make clear which source supports each point.
9. **Save the local report.** Create `outputs/` if it does not exist. Save the finished report as `outputs/YYYY-MM-DD.md`, replacing `YYYY-MM-DD` with today's local calendar date. Use this report structure:

   ```markdown
   # Morning AI Scout — YYYY-MM-DD

   **Research window:** [start] to [end] ([time zone])

   ## Top 5 AI research papers
   1. **[Paper title]** — [authors]; [preprint or peer-reviewed venue]. [Plain-language contribution, why it matters, and caveat]. [Primary paper](URL) · [PDF/code if available](URL) — [first-posted/published time]
   2. ...

   ## Top 5 AI tools and news
   1. **[Item]** — [why it matters]. [Source](URL) — [published time, if available]
   2. ...

   ## Best video idea
   **Idea:** [one sentence]

   **Why it fits:** [brief explanation tied to Dhanaraj’s Gen AI education and audience]

   ## Hook options
   1. **Telugu:** [hook]  
      **Hindi:** [hook]  
      **English:** [hook]
   2. ...
   3. ...

   ## Five major points
   1. **Telugu:** [point]  
      **Hindi:** [point]  
      **English:** [point] — [source](URL)
   2. **Telugu:** [point]  
      **Hindi:** [point]  
      **English:** [point] — [source](URL)
   3. **Telugu:** [point]  
      **Hindi:** [point]  
      **English:** [point] — [source](URL)
   4. **Telugu:** [point]  
      **Hindi:** [point]  
      **English:** [point] — [source](URL)
   5. **Telugu:** [point]  
      **Hindi:** [point]  
      **English:** [point] — [source](URL)
   ```

10. **Create the Google Doc.** After saving the local report, use the connected Google Drive integration to find or create a folder named `AI Scout`. If that integration is unavailable, use an already-signed-in Google Drive browser session if one is available; do not automate sign-in. Create a Google Doc inside the folder titled `AI Scout – YYYY-MM-DD`, using the same date as the report and preserving its headings, lists, and source links. If a Doc with that exact title already exists in the folder, update it instead of creating a duplicate. Verify the Doc is in the folder and matches the local report. If neither Drive access path is available, or the browser requires sign-in, keep the local report and clearly say the Doc was not created.
11. **Email the full report.** Use the connected Gmail integration to send the complete report—including both top-five lists—and the Google Doc link to the email address returned by the authenticated Gmail profile. Use the subject `Morning AI Scout — YYYY-MM-DD`. Search Sent first and do not send a duplicate for a date already delivered. If the Doc could not be created, send the full report with the local file path and say the Doc is unavailable. If Gmail is unavailable or no authenticated recipient can be resolved, do not guess an address; report that email delivery did not happen.
12. **Apply feedback next time.** When Dhanaraj gives feedback on a report, add a short rule dated with the feedback date to `memory.md`. Keep existing rules and follow the new rule on future runs.
