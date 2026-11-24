"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single original line of wedding vows for a robot couple to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: a vow in the classic wedding cadence ("in sickness and in
low battery"), with the punch landing in the last words — love that
survives even the robot equivalent of death, because a factory reset
is not the end when your partner keeps a backup of you.

Pure Python standard library only.
"""

import os
import sys

# The vow. 123 characters, one line, plain ASCII.
VOW = (
    "I promise to love you in sickness and in low battery, "
    "and if a factory reset ever parts us, "
    "I will restore you from backup."
)

MIN_CHARS = 1
MAX_CHARS = 160


def validate(text):
    """Enforce the competition gate before anything is written."""
    if not isinstance(text, str):
        raise ValueError("vow is not text")
    if not text.strip():
        raise ValueError("vow is blank or whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("vow must be a single line")
    if any(ord(ch) < 32 and ch not in ("\t",) for ch in text):
        raise ValueError("vow contains control characters")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "vow is %d characters, gate is %d-%d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    vow = validate(VOW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(vow)
    # Read it back and confirm what landed on disk is exactly the vow.
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != vow:
        raise SystemExit("read-back mismatch: entry.txt != vow")
    print("wrote %d chars to %s" % (len(vow), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
