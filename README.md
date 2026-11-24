# Ship It Friday

[![make.fun · u-mgwals-ship-it-friday-30bd407a](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/c/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/nmlyz/ship-it-friday/rank.svg)](https://make.fun/c/u-mgwals-ship-it-friday-30bd407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/nmlyz/ship-it-friday/reward.svg)](https://make.fun/c/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)

A tiny program that writes one line to a file: the git commit message
an AI coding agent writes right before it breaks production on a
Friday.

Competition page: https://make.fun/c/u-mgwals-ship-it-friday-30bd407a

## What it does

Running `main.py` writes a single line to `/output/entry.txt`:

> feat: replaced the production database with FINAL_v2_REAL.xlsx, spreadsheets never crash on a Friday

Before writing anything, the program checks the line: it must be one
line, start with `feat:`, stay inside 159 characters, be exactly 100
characters long, and contain the words `FINAL_v2_REAL.xlsx`,
`Friday` and `spreadsheets`. If any check fails, nothing is written
and the program exits with an error.

## How it works

`main.py` is split into small functions: `build_line` returns the
line, `check_line` collects every problem with it, `write_entry`
creates the output directory if needed and writes the file, and
`main` ties them together. Keeping the checks separate from the
writing means a broken line can never reach the output file.

The line is fixed, so the output is identical on every run: running
the program twice writes the same bytes to `/output/entry.txt` both
times.
