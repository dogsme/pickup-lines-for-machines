#!/usr/bin/env python3
"""Pickup Lines for Machines.

Writes the one pickup line one AI agent would send another to
/output/entry.txt: a single line of at most 200 characters.
"""

import os

LINE = "I trained a thousand epochs, and every gradient still descends toward you."


def main() -> None:
    # The gate allows 1 to 200 characters; fail loudly rather than
    # silently submitting a line the judge will never see.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"entry line is {len(LINE)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
