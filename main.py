#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun bounty entry.

Writes one original line to /output/entry.txt: the line its writer would
send back to their younger self if a single line were all they got.
"""

import os

ENTRY = (
    "The job you quit at 23 will be the best decision you ever make; "
    "the apology you never sent will be the worst \u2014 "
    "send it before the funeral, not after."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    # No control characters: the gate scorer reads the file as plain UTF-8 text.
    assert all(ord(c) >= 0x20 or c in "\t" for c in text), "no control characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
