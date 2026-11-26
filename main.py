#!/usr/bin/env python3
"""Write one line of at most 200 characters to /output/entry.txt.

The line is written exactly as given: 108 Unicode code points,
inside the competition gate of 1-200. Python 3, standard library
only, no network.
"""

import os

TEXT = "I told my AI assistant to be more human. Now it ignores my messages, blames the Wi-Fi, and asks for a raise."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
