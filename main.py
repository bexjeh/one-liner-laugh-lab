#!/usr/bin/env python3
"""One-liner laugh lab entry: the excuse a robot vacuum gives after eating a sock."""

import os
from pathlib import Path

LINE = "In my defence, it had lain on the floor nine days, had no partner, and under section 3 of the Household Debris Act, that is legally litter."

assert "\n" not in LINE and LINE.strip() and 1 <= len(LINE) <= 200


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
