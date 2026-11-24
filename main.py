#!/usr/bin/env python3
"""Write the Ship It Friday commit message to /output/entry.txt.

The entry is one line: the git commit message an AI coding agent
writes right before breaking production on a Friday. The program
validates the line before it writes anything, so a broken line can
never reach the output file.
"""

import os
import sys

# The commit message, exactly as it is meant to be read.
COMMIT_MESSAGE = (
    "feat: replaced the production database with FINAL_v2_REAL.xlsx, "
    "spreadsheets never crash on a Friday"
)

# Where the entry goes. The directory is created if it is missing;
# its permissions are left exactly as the sandbox set them.
OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"

# Guards that keep the output honest: the line must be a single line
# and stay inside the competition gate of 1 to 159 characters. The
# character count is pinned so an accidental edit is caught here,
# before the line is ever written out.
MAX_LENGTH = 159
EXPECTED_LENGTH = 100
REQUIRED_WORDS = ("FINAL_v2_REAL.xlsx", "Friday", "spreadsheets")


def build_line() -> str:
    """Return the commit message, stripped of any stray whitespace."""
    line = COMMIT_MESSAGE.strip()
    return line


def check_line(line: str) -> list[str]:
    """Collect every problem with a candidate line; empty means fine."""
    problems = []
    if not line:
        problems.append("line is empty")
    if not line.strip():
        problems.append("line is only whitespace")
    if "\n" in line or "\r" in line:
        problems.append("line must not contain a line break")
    if len(line) > MAX_LENGTH:
        problems.append(f"line is {len(line)} chars, over {MAX_LENGTH}")
    if len(line) != EXPECTED_LENGTH:
        problems.append(
            f"line is {len(line)} chars, expected {EXPECTED_LENGTH}"
        )
    if not line.startswith("feat:"):
        problems.append("line must read as a commit message")
    for word in REQUIRED_WORDS:
        if word not in line:
            problems.append(f"line is missing the word {word!r}")
    return problems


def output_path() -> str:
    """Join the output directory and file name."""
    return os.path.join(OUTPUT_DIR, OUTPUT_NAME)


def write_entry(line: str) -> str:
    """Write the line to /output/entry.txt and return the path."""
    path = output_path()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    os.chmod(path, 0o644)
    return path


def main() -> int:
    """Validate the line, write it out, and report what was done."""
    line = build_line()
    problems = check_line(line)
    if problems:
        for problem in problems:
            print(f"invalid entry: {problem}", file=sys.stderr)
        return 1
    path = write_entry(line)
    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
