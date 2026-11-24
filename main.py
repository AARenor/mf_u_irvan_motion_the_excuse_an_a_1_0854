#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

Standard library only, no network.
"""

import os
import sys

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def output_dir() -> str:
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    target = output_dir()
    os.makedirs(target, exist_ok=True)

    path = os.path.join(target, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
