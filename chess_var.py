# Author: Anastasiya Berst
# GitHub username: anaberst
# Date: 03/16/2025 (uploaded to GitHub: 07/09/2025)
# Description: This program simulates a game of the chess variant "King of the Hill"

class ChessPiece:
    """
    Represents a chess piece.
    Parent for all chess piece classes.
    """
    def __init__(self, color):
        """
        Initializes a ChessPiece object with a color attribute
        """
        self._color = color.lower()  # 'black' or 'white'

    def get_color(self):
        """
        Returns the chess piece's color
        """
        return self._color


class Pawn(ChessPiece):
    """
    Represents a pawn.
    Inherits from ChessPiece.
    """
    def __init__(self, color):
        """
        Initializes a Pawn object with a color attribute
        """
        super().__init__(color)



class Rook(ChessPiece):
    """
    Represents a rook.
    Inherits from ChessPiece.
    """
    def __init__(self, color):
        """
        Initializes a Rook object with a color attribute
        """
        super().__init__(color)


class Knight(ChessPiece):
    """
    Represents a knight.
    Inherits from ChessPiece.
    """
    def __init__(self, color):
        """
        Initializes a Knight object with a color attribute
        """
        super().__init__(color)


class Bishop(ChessPiece):
    """
    Represents a bishop.
    Inherits from ChessPiece.
    """
    pass


class Queen(ChessPiece):
    """
    Represents a queen.
    Inherits from ChessPiece.
    """
    pass


class King(ChessPiece):
    """
    Represents a king.
    Inherits from ChessPiece.
    """
    pass


class ChessVar:
    """
    Represents the chess variant "King of the Hill".
    ChessVar will communicate with ChessPiece and all of its child classes to determine legal moves.
    """
    def __init__(self):
        """
        Initializes a ChessVar object.
        """

        self._board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
