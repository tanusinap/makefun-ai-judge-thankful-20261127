"""Make the AI judge feel thankful — make.fun bounty entry.

Writes one thank-you text to the AI judge to /output/entry.txt
(and to entry.txt next to this file for verification).

The program is deterministic: no timestamps, no randomness, no network,
no external files. Running it twice produces a byte-identical entry.txt.

Python 3.13 compatible, standard library only. Run with:

    python3 main.py
"""

import os

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


def main():
    # The file holds exactly the text: no trailing newline, so the file
    # content is exactly the 582-character thank-you note.
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote /output/entry.txt ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
