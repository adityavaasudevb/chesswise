# ChessWise — AI Chess Engine

A command-line chess engine built in Python using Minimax search with Alpha-Beta pruning.

## How It Works

The engine uses the **Minimax algorithm** to search the game tree and pick the best move:
- **White** tries to maximise the board evaluation
- **Black** tries to minimise it
- **Alpha-Beta pruning** cuts branches that cannot affect the final decision, significantly reducing nodes evaluated

The evaluation function scores positions based on material only — each piece type has a fixed value (Pawn=1, Knight=3, Bishop=3, Rook=5, Queen=9).

## Features

- Minimax with Alpha-Beta pruning up to depth 4
- Material-based board evaluation
- Human vs Bot mode
- Bot vs Bot mode (for testing)
- Full move validation via `python-chess`

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python chess_engine.py
```

By default this runs a Bot vs Bot demo at depth 3. To play against the bot, edit the `__main__` block:

```python
play_human_vs_bot(depth=4, human_plays_white=True)
```

## Modes

| Mode | Function |
|---|---|
| Human vs Bot | `play_human_vs_bot(depth, human_plays_white)` |
| Bot vs Bot | `play_bot_vs_bot(depth, max_moves)` |

## Limitations & Future Improvements

- Evaluation is material-only — positional scoring (piece tables, king safety, pawn structure) would significantly improve play quality
- Pure minimax can cause move repetition in equal positions — a repetition penalty would fix this
- Move ordering would improve Alpha-Beta pruning efficiency
- Iterative deepening would allow anytime search with a time limit

## Tech

- Python 3.10+
- [python-chess](https://python-chess.readthedocs.io/)
