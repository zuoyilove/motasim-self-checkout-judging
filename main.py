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


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    # Also write the canonical path when it differs and is writable,
    # so the gate finds the file either way.
    if os.path.abspath(out_dir) != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(text)
        except OSError:
            pass


if __name__ == "__main__":
    main()
