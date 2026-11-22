# Daily Scout

Use this skill for Morning AI Scout’s daily research and video planning run.

## Step-by-step morning run

1. **Read memory first.** Open `memory.md` before researching. Follow every rule in it. If it does not exist, create it with a `# Memory` heading.
2. **Set the time window.** Use the current date and time, and look only for items first published or launched in the previous 24 hours. Record the window in the report, including the time zone. Do not present older items as new; if an older item is useful context, label it clearly as background.
3. **Search broadly.** Look for both AI tools and AI news on Product Hunt, Hacker News, Reddit, X, and official AI company blogs. Search each source that is accessible. Also check primary announcements or product pages for details. Keep links and publication times for candidates so facts can be checked.
4. **Verify and shortlist.** Follow the preferences in `memory.md`. For Dhanaraj, prioritize mostly free AI tools he can try today and skip funding news. Remove duplicates, stale items, and claims that cannot be supported by a reliable source. Select the five most interesting distinct qualifying items. For each, give its name or headline, source and link, publication date/time when available, and one concise line explaining why it matters. If fewer than five credible items qualify, say so rather than filling the list with older or weak items.
5. **Choose one video idea.** Pick the single strongest idea from the shortlist for Dhanaraj Esuru, an MCA student pursuing Gen AI. Explain briefly why it fits his education and audience, what makes it timely, and what viewers can learn. Keep the idea grounded in the verified news.
6. **Write hooks in three languages.** Provide three hook options, with each option written in Telugu, Hindi, and English. Keep each version natural, engaging, and faithful to the same idea. Do not translate technical claims in a way that changes their meaning.
7. **Give five major points in three languages.** Write exactly five concise outline points based on the selected news and video idea. Put them in a useful video order, from context and what happened through implications or a practical takeaway. For each point, provide Telugu, Hindi, and English versions that preserve the same facts and meaning. Use natural phrasing in each language, retain technical terms where translating them would be unclear, and do not invent details. Include a supporting source link with each point; use different platforms across the five points where reliable coverage is available, and make clear which source supports which point.
8. **Save the local report.** Create `outputs/` if it does not exist. Save the finished report as `outputs/YYYY-MM-DD.md`, replacing `YYYY-MM-DD` with today's local calendar date. Use this report structure:

   ```markdown
   # Morning AI Scout — YYYY-MM-DD

   **Research window:** [start] to [end] ([time zone])

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

9. **Create the Google Doc.** After saving the local report, use the connected Google Drive integration to find or create a folder named `AI Scout`. If that integration is unavailable, use an already-signed-in Google Drive browser session if one is available; do not automate sign-in. Create a Google Doc inside the folder titled `AI Scout – YYYY-MM-DD`, using the same date as the report and preserving its headings, lists, and source links. If a Doc with that exact title already exists in the folder, update it with the new report instead of making a duplicate. Verify the Doc is in the folder and its content matches the local report before claiming success. If neither Drive access path is available, or the browser requires sign-in, keep the local report and clearly say the Doc was not created.
10. **Email the daily report.** Use the connected Gmail integration to send the full report and the Google Doc link to the email address returned by the authenticated Gmail profile. Use the subject `Morning AI Scout — YYYY-MM-DD`. Search Sent first and do not send a duplicate for a date already delivered. If the Doc could not be created, send the report content with the local file path and say the Doc is unavailable. If Gmail is unavailable or no authenticated recipient can be resolved, do not guess an address; report that email delivery did not happen.
11. **Apply feedback next time.** When Dhanaraj gives feedback on a report, add a short rule dated with the feedback date to `memory.md`. Keep existing rules and follow the new rule on future runs.
