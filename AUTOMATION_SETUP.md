# Hosted Daily AI Scout

This workflow runs on GitHub-hosted runners, so it can run while your computer is off or asleep. It is scheduled for 07:00 Asia/Kolkata (01:30 UTC). GitHub can delay scheduled starts during busy periods. You can also start it from the Actions tab with **Run workflow**.

## Add GitHub Actions settings

In the repository, open **Settings → Secrets and variables → Actions**.

Add these repository secrets:

- **TAVILY_API_KEY** — your Tavily API key.
- **OPENAI_API_KEY** — your OpenAI API key. API usage is billed separately from a ChatGPT plan.
- **GMAIL_APP_PASSWORD** — an app password for the Gmail account that sends the email. Google requires 2-Step Verification for app passwords and recommends Sign in with Google where supported: [Google's app password guidance](https://support.google.com/mail/answer/185833).

Add these repository variables:

- **GMAIL_ADDRESS** — the Gmail address used as both sender and recipient.
- **OPENAI_MODEL** — optional; defaults to gpt-6.2-sol.

## Allow report commits

In **Settings → Actions → General → Workflow permissions**, allow read and write permissions for repository contents. The workflow commits the validated report, its sent marker, and any change to memory.md to main.

## Run a first check

1. Add the required secrets and the GMAIL_ADDRESS variable.
2. Open **Actions → Daily AI Scout → Run workflow**.
3. Confirm the job completes, the dated report appears in outputs/, and the email arrives.

The GitHub runner cannot use the Gmail connector authenticated inside ChatGPT/Codex, so this workflow sends directly through Gmail SMTP. It does not use Google Drive. A sent marker under outputs/.sent/ prevents a same-day rerun from emailing a duplicate.

The repository is public, so reports committed under outputs/ are publicly readable.
