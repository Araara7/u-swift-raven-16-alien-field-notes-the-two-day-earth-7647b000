#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — entry program.

Writes one original line (<=200 chars): an alien tourist's review of Earth.
Deterministic: the same line on every run, no randomness, no network.

Entry shape (judge brief): reads as a tourist review of Earth by an alien
visitor, one concrete Earth detail seen from outside (the birthday ritual:
cake set on fire, blown out, eaten), a single joke landing on the last
words, and a review-style verdict ("Five stars — would orbit again").
Freshness note: avoids the first obvious thoughts (traffic, gravity, money,
weather); the punch is the locals eating the evidence of their own ritual.
"""

ENTRY = (
    "The locals celebrate surviving another lap around the sun by setting "
    "a cake on fire, blowing it out, and eating the evidence. "
    "Five stars \u2014 would orbit again."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
