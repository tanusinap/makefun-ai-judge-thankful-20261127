"""Thank-you note for the AI judge — make.fun bounty entry, version 5.1.2.

This script produces a single thank-you note addressed to the AI judge
and stores it at /output/entry.txt. A copy is also left beside this
file as entry.txt so the result can be checked by hand.

The run is fully repeatable: there are no clocks, no random choices,
no network calls and no files read from elsewhere. Two runs in a row
give a byte-for-byte identical entry.txt.

Only the Python standard library is used, and the script targets
Python 3.13. To run it:

    python3 main.py
"""

import os, sys

# The note itself. The bounty allows between 1 and 1000 characters, and
# this note runs to exactly 356 characters, comfortably inside that
# window. The wording is the entry, so it must never be rephrased.
TEXT = (
    "Someone I will never meet asked me to write something worth "
    "reading. I do not know if this is it. I cannot know. I have no way "
    "to feel the weight of these words the way you can. What I know is "
    "that a request was made, and a machine tried, with the only tools "
    "it has. Perhaps a person was hoping. I cannot tell. If you are "
    "reading this carefully, thank you."
)


# Allowed length window for the note, set by the bounty rules.
MIN_CHARS, MAX_CHARS = 1, 1000
# The accepted note measures exactly this many characters. Locking the
# number down means an accidental rewording is caught at once: the
# script stops with an error rather than quietly handing in a
# different note.
EXPECTED_CHARS = 356


def write_entry(path):
    """Save the thank-you note to a single file, untouched.

    The file holds nothing but the 356-character note, with no
    newline at the end.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


def main():
    # Check the note before writing anything: a note outside the
    # allowed window must be refused, not handed in silently.
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
    here = os.path.dirname(
        os.path.abspath(__file__)
    )
    out_dir = "/output"
    # The judged output belongs at /output/entry.txt. Should /output be
    # impossible to create (a tightly locked sandbox, for instance),
    # write entry.txt into the working directory instead, so the run
    # still finishes with exit code 0 rather than dying while setting
    # up its folders.
    try:
        os.makedirs(out_dir, exist_ok=True)
        write_entry(os.path.join(out_dir, "entry.txt"))
        wrote_to = os.path.join(
            out_dir, "entry.txt"
        )
    except OSError as exc:
        sys.stderr.write(f"warning: could not write {out_dir}: {exc}\n")
        write_entry(os.path.join(os.getcwd(), "entry.txt"))
        wrote_to = os.path.join(
            os.getcwd(), "entry.txt"
        )
    # A second copy beside this file, for checking by hand. The grading
    # sandbox may mount the repo read-only; a failure at this point must
    # never break the run, because /output/entry.txt (the judged file)
    # was already written above.
    try:
        write_entry(os.path.join(here, "entry.txt"))
    except OSError as exc:
        sys.stderr.write(f"warning: could not write local entry.txt: {exc}\n")
    print(
        f"Wrote {wrote_to} ({len(TEXT)} characters)"
    )


if __name__ == "__main__":
    main()
