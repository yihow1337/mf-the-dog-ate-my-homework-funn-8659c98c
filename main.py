#!/usr/bin/env python3
"""Write this entry's excuse to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Deterministic: the text lives beside this file in entry.txt and is copied out
byte for byte, so every run produces identical output.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.txt")


def load_excuse():
    with open(SOURCE, "r", encoding="utf-8") as handle:
        return handle.read().strip()


def main():
    excuse = load_excuse()

    # The sealed gate wants 1 to 200 UTF-8 characters that are not just space,
    # and the task wants one line. No trailing newline: bytes break ties.
    if not excuse or len(excuse) > 200 or "\n" in excuse:
        sys.exit("entry.txt fails the gate: %d characters" % len(excuse))

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as handle:
        handle.write(excuse)


if __name__ == "__main__":
    main()
