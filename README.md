# Even or Odd Roulette Game

This is a simple command-line "Even or Odd" roulette game written in Python.

## How to Play

- Run the script using Python 3.
- When prompted, enter:
  - `e` for Even
  - `o` for Odd
- The computer randomly selects a number between 1 and 10.
- If your guess matches the parity (even/odd) of the computer's number, you win the round and earn 10 points.
- If you lose the round, 5 points are subtracted from your score.
- After each round, your current points are displayed.
- You can choose to continue playing or exit after each round.

## Usage

Open a terminal and run:

```bash
python Roulette.py
```

## Example

```
Even or Odd (e/o): e
U choose: e and Computer Choose: o
U lose
Your Points: -5
Countinue (y/n): y
Even or Odd (e/o): o
U choose: o and Computer Choose: o
U won
Your Points: 5
Countinue (y/n): n
Thank U
```

## Requirements

- Python 3.x

## Notes

- Input is case-insensitive.
- Invalid inputs will prompt you to try again.
- The point system rewards +10 for a win and -5 for a
