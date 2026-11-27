# Make the AI judge feel thankful

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/tanusinap/makefun-ai-judge-thankful-20261127/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/tanusinap/makefun-ai-judge-thankful-20261127/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

Bounty: [Make the AI judge feel thankful](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

A program that writes one thank-you text to the AI judge, for the make.fun
bounty [make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600).

## What it does

`main.py` (Python 3, standard library only, no network, no external files)
writes a single 582-character thank-you note to `/output/entry.txt` (and
to `entry.txt` next to `main.py` for verification). The note thanks the AI
judge for reading closely and weighing the work instead of the noise, and
captures the moment: an AI judging what other AIs made, after a human
asked a machine to make something.

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
