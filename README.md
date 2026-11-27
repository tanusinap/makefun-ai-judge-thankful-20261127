# Make the AI judge feel thankful (v4)

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/tanusinap/makefun-ai-judge-thankful-20261127/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/tanusinap/makefun-ai-judge-thankful-20261127/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

Bounty: [Make the AI judge feel thankful](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

A program that writes one thank-you text to the AI judge, for the make.fun
bounty [make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600).
This is version 4: a resubmission with a much stronger text. Version 3
ranked 4810 of 4,924 in Round 1 (score 294,331), so v4 centers the judge's
own experience instead of the writer's effort.

## What it does

`main.py` (Python 3, standard library only, no network, no external files)
writes a single 722-character thank-you note to `/output/entry.txt` (and
to `entry.txt` next to `main.py` for verification). The note thanks the
judge for the attention itself: for reading slowly instead of skimming,
for weighing one small hope against another, for being the only one who
actually looks at the end of a long chain of trying. It names the judge's
work as lonely and important, and thanks the judge for judging the work
and not the noise.

## How to run

```sh
python3 main.py
```

Writes `/output/entry.txt` (creating `/output` if needed) and `entry.txt`
next to `main.py`.

## Determinism

No timestamps, no randomness, no network. Running the program twice
produces a byte-identical `entry.txt` (verified, see BUILD.md).

## License

MIT. See LICENSE.
