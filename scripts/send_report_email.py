#!/usr/bin/env python3
"""Send a scout report directly through Gmail SMTP."""

from __future__ import annotations

import os
import smtplib
import sys
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/send_report_email.py outputs/YYYY-MM-DD.md")
    report = ROOT / sys.argv[1]
    if not report.is_file() or report.suffix.lower() != ".md":
        raise SystemExit(f"Report not found: {sys.argv[1]}")

    address = os.environ.get("GMAIL_ADDRESS", "").strip()
    password = os.environ.get("GMAIL_APP_PASSWORD", "").replace(" ", "")
    if not address:
        raise SystemExit("Missing GMAIL_ADDRESS Actions variable.")
    if not password:
        raise SystemExit("Missing GMAIL_APP_PASSWORD Actions secret.")

    date = report.stem
    marker = ROOT / "outputs/.sent" / f"{date}.sent"
    if marker.exists():
        print(f"Email already sent for {date}; skipping.")
        return 0

    message = EmailMessage()
    message["Subject"] = f"Morning AI Scout — {date}"
    message["From"] = address
    message["To"] = address
    message["Message-ID"] = f"<morning-ai-scout-{date}@github-actions.local>"
    message.set_content(report.read_text(encoding="utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as smtp:
        smtp.login(address, password)
        smtp.send_message(message)

    marker.parent.mkdir(parents=True, exist_ok=True)
    marker.write_text(
        f"Sent via Gmail SMTP at {datetime.now(timezone.utc).isoformat()}\n",
        encoding="utf-8",
    )
    print(f"Sent {report.name} directly to {address}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
