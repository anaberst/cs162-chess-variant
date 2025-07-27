# :crown: CS162 Chess Variant
Final project for `CS162: Introduction to Computer Science II` at Oregon State University. It has been approved for public sharing.

This project implements an abstract board game based on the chess variant known as "King of the Hill".

In this variant, players can win by either capturing the opponent's king or by moving their own king to one of the four central squares (d4, e4, d5, e5). The game follows standard chess movement rules but excludes checks, checkmates, castling, en passant, and pawn promotion.

It consists of seven main classes:

- `ChessPiece`: Abstract parent class for all chess pieces with color and movement validation
- `Pawn`, `Rook`, `Knight`, `Bishop`, `Queen`, `King`: Individual piece classes that inherit from ChessPiece, each implementing their specific movement rules
- `ChessVar`: Main game class that manages the board state, validates moves, tracks turns, and determines win conditions

The project demonstrates object-oriented programming principles including inheritance, polymorphism, and encapsulation. It also showcases coordinate system conversion, path validation for piece movement, and complex game state management.

## :hourglass_flowing_sand: Testing

The file `test_chess_var.py` includes unit tests that cover:

- Chess piece initialization and movement validation for all piece types
- Board setup and coordinate conversion between algebraic notation and array indices
- Move validation including turn alternation, path blocking, and capture mechanics
- Win condition detection for both king capture and king reaching central squares
- Game state management and error handling for invalid moves

## :open_file_folder: File Structure
```
cs162-chess-variant/
├── README.md                 # You are here
├── chess_var.py              # Main class definitions
├── test_chess_var.py         # Unit tests for the project
└── .gitignore                # Git ignore configuration
```
