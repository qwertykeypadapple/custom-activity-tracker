#!/usr/bin/env python3
"""Write data.json so the lit dots spell WORD, centered in the last-12-months grid
(53 weeks, Sunday-first, ending the Saturday of the current week)."""
import datetime, json, os

LETTERS = {  # 7 rows (Sunday on top); width varies per letter
    "A": [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "l": ["##.", ".#.", ".#.", ".#.", ".#.", ".#.", "###"],
    "i": [".#.", "...", "##.", ".#.", ".#.", ".#.", "###"],
    "g": [".....", ".####", "#...#", "#...#", ".####", "....#", ".###."],
    "n": [".....", ".....", "#.##.", "##..#", "#...#", "#...#", "#...#"],
    "e": [".....", ".....", ".###.", "#...#", "#####", "#....", ".###."],
    "r": [".....", ".....", "#.##.", "##..#", "#....", "#....", "#...."],
}
WORD, GAP, WEEKS = "Alignerr", 1, 53

today = datetime.date.today()
end = today + datetime.timedelta(days=(5 - today.weekday()) % 7)   # Saturday of this week
start = end - datetime.timedelta(days=7 * WEEKS - 1)                # a Sunday

width = sum(len(LETTERS[c][0]) for c in WORD) + (len(WORD) - 1) * GAP
x = (WEEKS - width) // 2
days = {}
for ch in WORD:
    for row, line in enumerate(LETTERS[ch]):           # row 0 = Sunday
        for col, px in enumerate(line):
            if px == "#":
                week = x + col
                d = start + datetime.timedelta(days=7 * week + row)
                days[d.isoformat()] = {"commits": 1, "edits": 0, "projects": []}
    x += len(LETTERS[ch][0]) + GAP

out = {"generated": datetime.datetime.now().isoformat(timespec="seconds"), "days": dict(sorted(days.items()))}
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json"), "w"), indent=0)
print(f"{len(days)} dots, {min(days)} → {max(days)}")
