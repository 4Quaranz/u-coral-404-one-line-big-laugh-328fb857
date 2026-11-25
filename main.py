"""One Line, Big Laugh — make.fun entry.

Writes a single funny line of at most 200 characters to /output/entry.txt.
No network, no randomness: every run writes the exact same bytes.
"""

import os

LINE = "My bank called about suspicious activity \u2014 it was just me buying groceries like a responsible adult, which has never happened before."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
