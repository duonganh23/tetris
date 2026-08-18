# Tetris

A classic Tetris clone built with Python and Pygame.

## Features

- Full tetromino set (I, J, L, O, S, T, Z) with rotation and collision detection
- Next-piece preview
- Score, lines, and level tracking (level increases every 10 lines cleared)
- Background music and sound effects
- Game over detection with a "Press F to restart" screen

## Requirements

- Python 3
- Pygame

Install dependencies:
```
pip install pygame
```

## Running the Game

Run from the `code` folder:
```
cd code
python main.py
```

## Controls

| Key         | Action           |
|-------------|------------------|
| Left Arrow  | Move left        |
| Right Arrow | Move right       |
| Down Arrow  | Move down faster |
| Space       | Rotate piece     |
| F           | Restart (after game over) |

## Project Structure

```
tetris/
├── code/
│   ├── main.py       # Game loop and entry point
│   ├── game.py        # Core game logic, tetromino and block classes
│   ├── preview.py      # Next-shape preview panel
│   ├── score.py        # Score, lines, and level display
│   ├── timer.py        # Timer utility for piece movement
│   └── settings.py     # Game constants and configuration
├── graphics/           # Tetromino images and fonts
└── sound/               # Music and sound effects
```

## Notes

- Graphics and sound paths are resolved relative to each file's own location, so the game runs correctly regardless of the working directory it's launched from.
