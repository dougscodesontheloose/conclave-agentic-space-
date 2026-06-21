#!/usr/bin/env python3
"""
archive_logs.py - Archives session logs older than 30 days.
Reads _conclave/state/memory/session_logs.md. Finds logs older than 30 days
and moves them to archive files (e.g., session_logs_archive_YYYY_MM.md).
"""

import os
import re
from datetime import datetime, timedelta

def main():
    conclave_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    logs_file = os.path.join(conclave_dir, "state", "memory", "session_logs.md")
    
    if not os.path.isfile(logs_file):
        return

    with open(logs_file, "r") as f:
        content = f.read()

    # Split the file by the log header pattern
    # Pattern matches: # Session Log: 2026-04-26 or [🟢 SUCCESS] # Session Log: 2026-04-26
    header_regex = re.compile(r'^(?:\[.*\]\s*)?# Session Log: (\d{4}-\d{2}-\d{2}).*$', re.MULTILINE)
    
    sections = []
    last_idx = 0
    
    matches = list(header_regex.finditer(content))
    if not matches:
        return
        
    for i, match in enumerate(matches):
        start = match.start()
        if i < len(matches) - 1:
            end = matches[i+1].start()
        else:
            end = len(content)
            
        date_str = match.group(1)
        try:
            log_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            sections.append((content[start:end], None))
            continue
            
        sections.append((content[start:end], log_date))

    now = datetime.utcnow()
    cutoff_date = now - timedelta(days=30)
    
    recent_logs = []
    archived_by_month = {}
    
    has_archives = False
    
    for text, log_date in sections:
        if log_date and log_date < cutoff_date:
            month_key = log_date.strftime("%Y_%m")
            if month_key not in archived_by_month:
                archived_by_month[month_key] = []
            archived_by_month[month_key].append(text)
            has_archives = True
        else:
            recent_logs.append(text)
            
    if not has_archives:
        return

    # Write recent logs back
    with open(logs_file, "w") as f:
        # Prepend any content that was before the first header
        f.write(content[:matches[0].start()])
        f.write("".join(recent_logs))
        
    # Write archives
    archives_dir = os.path.join(conclave_dir, "state", "memory", "archives")
    os.makedirs(archives_dir, exist_ok=True)
    
    for month_key, texts in archived_by_month.items():
        archive_file = os.path.join(archives_dir, f"session_logs_archive_{month_key}.md")
        with open(archive_file, "a") as f:
            f.write("".join(texts))

if __name__ == "__main__":
    main()
