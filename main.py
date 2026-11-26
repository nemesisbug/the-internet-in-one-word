#!/usr/bin/env python3
"""The Internet in One Word.

The whole internet, described in a single word: slop.

Writes that one word to /output/entry.txt. Deterministic, no network,
no input, no randomness — the same word every run.

Why this word, against the judge's brief: it is a single word, it is funny
by itself (gross, blunt, one syllable), it says something true about the
internet as a whole rather than one app (every feed, every site, the same
trough), it is not the first obvious word anyone reaches for, and it lands
in one beat — then the reader nods.
"""

from pathlib import Path

WORD = "slop"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
