#!/usr/bin/env python3
"""Validate a Morning AI Scout Markdown report before Gmail delivery."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]+\]\(https?://[^)\s]+\)")
ITEM_RE = re.compile(r"(?m)^\s*\d+\.\s+")

def section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    start += len(heading)
    end = re.search(r"(?m)^##\s+", text[start:])
    return text[start : start + end.start()] if end else text[start:]

def items(text: str) -> list[str]:
    starts = [m.start() for m in ITEM_RE.finditer(text)]
    return [text[a : starts[i + 1] if i + 1 < len(starts) else len(text)] for i, a in enumerate(starts)]

def validate(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"Report not found: {path}"]

    text = path.read_text(encoding="utf-8")
    title = re.search(r"(?m)^# Morning AI Scout — (\d{4}-\d{2}-\d{2})\s*$", text)
    if not title:
        errors.append("Missing dated report title.")
        report_date = None
    else:
        report_date = title.group(1)
        if path.stem != report_date:
            errors.append(f"Filename must be {report_date}.md.")

    window = re.search(
        r"(?m)^\*\*Research window:\*\*\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\s+to\s+(\d{4}-\d{2}-\d{2} \d{2}:\d{2})(.*)$",
        text,
    )
    if not window:
        errors.append("Research window must give start and end timestamps.")
    else:
        try:
            start = datetime.strptime(window.group(1), "%Y-%m-%d %H:%M")
            end = datetime.strptime(window.group(2), "%Y-%m-%d %H:%M")
            if end - start != timedelta(hours=24):
                errors.append("Research window must cover exactly 24 hours.")
            if report_date and end.strftime("%Y-%m-%d") != report_date:
                errors.append("Research window end date must match the report date.")
        except ValueError:
            errors.append("Research window timestamps are invalid.")
        if not any(zone in window.group(3) for zone in ("IST", "Asia/Kolkata", "UTC+05:30")):
            errors.append("Research window must identify India time (IST / Asia/Kolkata).")

    required = [
        "## Top 5 AI tools and news",
        "## Top 5 AI research papers",
        "## Best video idea",
        "## Hook options",
        "## Five major points",
    ]
    for heading in required:
        if heading not in text:
            errors.append(f"Missing section: {heading}")

    news = items(section(text, "## Top 5 AI tools and news"))
    if len(news) > 5:
        errors.append("News/tools shortlist contains more than five items.")
    if not news and not re.search(r"(?i)\b(none|no qualifying|no items)\b", section(text, "## Top 5 AI tools and news")):
        errors.append("If no news/tools qualify, state that explicitly.")
    for i, block in enumerate(news, 1):
        if not LINK_RE.search(block):
            errors.append(f"News/tools item {i} has no source link.")

    papers_section = section(text, "## Top 5 AI research papers")
    papers = items(papers_section)
    if len(papers) > 5:
        errors.append("Research-paper shortlist contains more than five items.")
    if not papers and not re.search(r"(?i)\b(none|no qualifying|no papers)\b", papers_section):
        errors.append("If no papers qualify, state that explicitly; do not pad with older papers.")
    for i, block in enumerate(papers, 1):
        if not LINK_RE.search(block):
            errors.append(f"Research paper {i} has no primary-source link.")
        if not re.search(r"(?i)preprint|peer[- ]reviewed|conference paper|journal article", block):
            errors.append(f"Research paper {i} must state its publication status.")
        if not re.search(r"(?i)submitted|published|first posted", block):
            errors.append(f"Research paper {i} must state its first-post/publication date.")

    hooks = items(section(text, "## Hook options"))
    if len(hooks) != 3:
        errors.append("Hook section must contain exactly three options.")
    for i, block in enumerate(hooks, 1):
        for language in ("Telugu", "Hindi", "English"):
            if f"**{language}:**" not in block:
                errors.append(f"Hook {i} is missing its {language} version.")

    points = items(section(text, "## Five major points"))
    if len(points) != 5:
        errors.append("Outline must contain exactly five major points.")
    for i, block in enumerate(points, 1):
        for language in ("Telugu", "Hindi", "English"):
            if f"**{language}:**" not in block:
                errors.append(f"Major point {i} is missing its {language} version.")
        if not LINK_RE.search(block):
            errors.append(f"Major point {i} has no supporting source link.")

    return errors

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="Path to outputs/YYYY-MM-DD.md")
    args = parser.parse_args()
    errors = validate(args.report)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Report structure valid: {args.report}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
