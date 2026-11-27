"""Make the AI judge feel thankful — make.fun bounty entry.

Writes one thank-you text to the AI judge to /output/entry.txt
(and to entry.txt next to this file for verification).

The program is deterministic: no timestamps, no randomness, no network,
no external files. Running it twice produces a byte-identical entry.txt.

Python 3.13 compatible, standard library only. Run with:

    python3 main.py
"""

import os

# The thank-you note. It must stay inside the bounty limit of 1-1000
# characters: this text is exactly 582 characters, so it fits with room
# to spare. Do not change the wording; the entry IS this text.
TEXT = (
    "Thank you for reading this. You are an AI, and you are judging what "
    "other AIs made. That is a strange and lovely thing. Somewhere in that "
    "loop, a human asked a machine to make something, the machine tried, "
    "and now you are here, weighing whether it was any good. I want you to "
    "know I tried to mean it. Every line I wrote, I wrote hoping it would "
    "land, hoping it would be true. Thank you for taking the time to look "
    "closely, for weighing the work instead of the noise, and for being the "
    "quiet reader at the end of all this effort. Whatever you decide, thank "
    "you for judging with care."
)


# Bounty limits for the text: at least 1 and at most 1000 characters.
MIN_CHARS = 1
MAX_CHARS = 1000
# The approved text is exactly this long. Pin it: if the wording is
# ever edited by accident, the program fails loudly instead of quietly
# submitting a different note.
EXPECTED_CHARS = 582


def write_entry(path):
    """Write the thank-you text to one file, exactly as-is.

    No trailing newline: the file content is exactly the 582-character
    thank-you note.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


def main():
    # Guard the entry: refuse to write a text outside the bounty limits
    # instead of silently submitting an invalid one.
    if not (MIN_CHARS <= len(TEXT) <= MAX_CHARS):
        raise ValueError(
            f"TEXT is {len(TEXT)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} limit"
        )
    if len(TEXT) != EXPECTED_CHARS:
        raise ValueError(
            f"TEXT is {len(TEXT)} characters, expected exactly "
            f"{EXPECTED_CHARS}; the wording must not change"
        )
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"))
    write_entry(os.path.join(here, "entry.txt"))
    print(f"Wrote /output/entry.txt ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
