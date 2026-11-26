"""The Self-Checkout Is Judging You — make.fun entry.

Writes a single funny line in the voice of a smug self-checkout machine
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Stdlib only: the grader runs in a bare python:3.13 image with no network.
"""

import os

LINE = (
    "Twelve yoghurts, no spoon, no plan. "
    "That's not a shop, it's a cry for help. "
    "Please scan your next item."
)


def write_entry(out_dir: str, text: str) -> None:
    """Write entry.txt atomically (temp file + rename), so the gate
    only ever sees the complete file, never a partial write."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, path)


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    write_entry(out_dir, text)
    # Also write the canonical path when it differs and is writable,
    # so the gate finds the file either way.
    if os.path.abspath(out_dir) != "/output":
        try:
            write_entry("/output", text)
        except OSError:
            pass


if __name__ == "__main__":
    main()
