#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — make.fun entry.

Writes a single word to /output/entry.txt: "never".

The joke is the word itself. Delete "never" from the dictionary and
nobody can ever say "never" again — the deletion breaks its own rule
the moment it lands. No caption, no defence, one word, spelled
correctly, nothing added around it.

Python 3.13, standard library only, no network, deterministic.
"""

import os

WORD = "never"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 77 characters, not only whitespace, and exactly one word:
    # an embedded newline or space would break the gate.
    assert 1 <= len(WORD) <= 77, f"word is {len(WORD)} chars, gate wants 1-77"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    assert "\n" not in WORD and "\r" not in WORD, "entry must be a single line"
    assert WORD.strip(), "entry must not be only whitespace"
    assert WORD.encode("utf-8").decode("utf-8") == WORD
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(WORD.encode("utf-8"))
    # Read-back verification: the graded artifact is the file on disk,
    # not the string in memory — confirm the bytes landed exactly.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == WORD.encode("utf-8"), (
        f"entry.txt on disk differs from WORD: {written!r}"
    )


if __name__ == "__main__":
    main()
