#!/usr/bin/env python3
"""Compare the Talks page (_pages/talks.md) with the talk notes in the Obsidian vault.

Usage:
    python3 scripts/check_talks_sync.py "/path/to/Obsidian/Notes/2 Areas/talks"

Reports talks missing on either side (from SINCE onward), title differences, and
invited/contributed mismatches. Nothing is modified.
"""
import re
import sys
from pathlib import Path

SINCE = "2022-08-01"  # the vault covers talks since joining Ohio University
MONTHS = "January February March April May June July August September October November December".split()
WEBSITE = Path(__file__).resolve().parent.parent / "_pages" / "talks.md"


def norm(s):
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)  # strip markdown links
    s = s.replace("&", "and").replace("–", "-").replace(":", " - ")
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def kind(s):
    s = s.lower()
    return "contributed" if "contributed" in s else "invited" if "invited" in s else "other"


def website_talks():
    talks, year = {}, None
    date_re = re.compile(r", (" + "|".join(MONTHS) + r") (\d{1,2}), (.*)$")
    for line in WEBSITE.read_text(encoding="utf-8").splitlines():
        if m := re.match(r"^## (\d{4})\b", line):
            year = m.group(1)
        elif line.startswith("* ") and year and (m := date_re.search(line)):
            date = f"{year}-{MONTHS.index(m.group(1)) + 1:02d}-{int(m.group(2)):02d}"
            talks[date] = (line[2:m.start()], kind(m.group(3)))
    return talks


def vault_talks(folder):
    talks = {}
    for p in Path(folder).glob("*.md"):
        fm = p.read_text(encoding="utf-8").split("---")[1]
        get = lambda k: (re.search(rf"^{k}:[ \t]*(.*)$", fm, re.M) or [None, ""])[1].strip().strip('"')
        talks[get("date")] = (get("title"), kind(get("type")))
    return talks


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    web = {d: v for d, v in website_talks().items() if d >= SINCE}
    vault = {d: v for d, v in vault_talks(sys.argv[1]).items() if d >= SINCE}
    problems = 0
    for d in sorted(set(web) | set(vault)):
        if d not in vault:
            print(f"{d}  only on website: {web[d][0]}"); problems += 1
        elif d not in web:
            print(f"{d}  only in vault:   {vault[d][0]}"); problems += 1
        else:
            (wt, wk), (vt, vk) = web[d], vault[d]
            if norm(wt) != norm(vt):
                print(f"{d}  title differs:\n    website: {wt}\n    vault:   {vt}"); problems += 1
            if wk != vk:
                print(f"{d}  type differs: website {wk}, vault {vk}"); problems += 1
    print(f"\n{len(web)} talks on website, {len(vault)} in vault since {SINCE}: "
          + ("in sync." if not problems else f"{problems} difference(s)."))


if __name__ == "__main__":
    main()
