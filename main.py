#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes one original funny line to /output/entry.txt (falling back to
./output/entry.txt when /output cannot be written), reads it back, and
verifies the round trip so the file on disk is exactly the line.
"""

import os
import sys

# One original line, invented for this entry: a smart fridge with a
# conscience (and a doctor on speed-dial). Sharpened from the first
# draft — "ratted me out" lands the betrayal harder than "emailed".
ENTRY = "My smart fridge ratted me out to my doctor over midnight ice cream, so now we're both on a diet."


def resolve_output_path() -> str:
    """Prefer /output/entry.txt; fall back to ./output/entry.txt."""
    candidates = (
        "/output/entry.txt",
        os.path.join(os.getcwd(), "output", "entry.txt"),
    )
    for candidate in candidates:
        try:
            os.makedirs(os.path.dirname(candidate), exist_ok=True)
            return candidate
        except OSError:
            continue
    return candidates[-1]


def main() -> int:
    line = ENTRY
    assert 1 <= len(line) <= 140, f"entry must be 1-140 chars, got {len(line)}"
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"

    path = resolve_output_path()
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)

    with open(path, "r", encoding="utf-8", newline="") as fh:
        round_tripped = fh.read()
    assert round_tripped == line, "round-trip verification failed"

    print(line)
    print(f"({len(line)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
