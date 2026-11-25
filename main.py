#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Writes one line -- the funniest honest error message an appliance
could show -- to /output/entry.txt. The line must be 1-200 characters,
a single line, and not only white space.
"""

import os

LINE = (
    "ERROR: The light works. The cooling does not. "
    "I am now an expensive cupboard with a lightbulb. "
    "Please call a technician, not a priest."
)


def main() -> None:
    text = LINE.strip()
    if not text:
        raise ValueError("entry must not be empty or only white space")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
