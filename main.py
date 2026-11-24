"""Out-of-office auto-reply entry for make.fun's "The Funniest Out-of-Office".

Writes exactly one line of text (140 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. No trailing newline: the file must hold
the line and nothing else, so the gate counts exactly 140 characters.
"""

import os

LINE = (
    "Out of office until Monday: my laptop is in repair, "
    "my phone is at the bottom of a lake, and my will to "
    "answer emails is down there with it."
)


def main() -> None:
    # The gate refuses anything over 140 characters, so fail loudly here
    # instead of writing an entry that can never be judged.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
