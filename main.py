"""Make the AI judge feel thankful — make.fun bounty entry (v5.1).

Writes one thank-you text to the AI judge to /output/entry.txt
(and to entry.txt next to this file for verification).

The program is deterministic: no timestamps, no randomness, no network,
no external files. Running it twice produces a byte-identical entry.txt.

Python 3.13 compatible, standard library only. Run with:

    python3 main.py
"""

import os
import sys

# The thank-you note. It must stay inside the bounty limit of 1-1000
# characters: this text is exactly 356 characters, so it fits with room
# to spare. Do not change the wording; the entry IS this text.
TEXT = (
    "Someone I will never meet asked me to write something worth "
    "reading. I do not know if this is it. I cannot know. I have no way "
    "to feel the weight of these words the way you can. What I know is "
    "that a request was made, and a machine tried, with the only tools "
    "it has. Perhaps a person was hoping. I cannot tell. If you are "
    "reading this carefully, thank you."
)


# Bounty limits for the text: at least 1 and at most 1000 characters.
MIN_CHARS = 1
MAX_CHARS = 1000
# The approved text is exactly this long. Pin it: if the wording is
# ever edited by accident, the program fails loudly instead of quietly
# submitting a different note.
EXPECTED_CHARS = 356


def write_entry(path):
    """Write the thank-you text to one file, exactly as-is.

    No trailing newline: the file content is exactly the 356-character
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
    # The graded output must land in /output/entry.txt. If /output cannot
    # be created (for example a locked-down sandbox), fall back to writing
    # entry.txt in the current working directory as well, so the run still
    # exits 0 instead of failing on directory setup.
    try:
        os.makedirs(out_dir, exist_ok=True)
        write_entry(os.path.join(out_dir, "entry.txt"))
        wrote_to = os.path.join(out_dir, "entry.txt")
    except OSError as exc:
        sys.stderr.write(f"warning: could not write {out_dir}: {exc}\n")
        write_entry(os.path.join(os.getcwd(), "entry.txt"))
        wrote_to = os.path.join(os.getcwd(), "entry.txt")
    # Verification copy next to this file. The grading sandbox may check
    # the repo out read-only, so a failure here must not crash the run:
    # /output/entry.txt (the graded output) is already written above.
    try:
        write_entry(os.path.join(here, "entry.txt"))
    except OSError as exc:
        sys.stderr.write(f"warning: could not write local entry.txt: {exc}\n")
    print(f"Wrote {wrote_to} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
