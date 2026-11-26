"""Funniest Time Machine Warning Label.

Writes a single one-line warning label (<=120 characters) for a time
machine to /output/entry.txt.

The joke turns a real time-travel hazard -- running into your own
duplicate self -- into a deadpan safety notice, saving the blame for
the last few words.
"""

import os

LABEL = (
    "WARNING: If you meet yourself during operation, do not wave. "
    "He is already running late, and it is entirely your fault."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
