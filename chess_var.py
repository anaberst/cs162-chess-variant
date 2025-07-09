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
    def __init__(self, color):
        """
        Initializes a Bishop object with a color attribute
        """
        super().__init__(color)


class Queen(ChessPiece):
    """
    Represents a queen.
    Inherits from ChessPiece.
    """
    def __init__(self, color):
        """
        Initializes a Queen object with a color attribute
        """
        super().__init__(color)


class King(ChessPiece):
    """
    Represents a king.
    Inherits from ChessPiece.
    """
    def __init__(self, color):
        """
        Initializes a King object with a color attribute
        """
        super().__init__(color)


class ChessVar:
    """
    Represents the chess variant "King of the Hill".
    ChessVar will communicate with ChessPiece and all of its child classes to determine legal moves.
    """
    def __init__(self):
        """
        Initializes a ChessVar object.
        """
        # initial game state
        self._game_state = 'UNFINISHED'

        # initial chess piece color
        self._current_color = 'white'

        # initiate all white ChessPiece objects
        self._white_pawn = Pawn('white')
        self._white_rook = Rook('white')
        self._white_knight = Knight('white')
        self._white_bishop = Bishop('white')
        self._white_queen = Queen('white')
        self._white_king = King('white')

        # initiate all black ChessPiece objects
        self._black_pawn = Pawn('black')
        self._black_rook = Rook('black')
        self._black_knight = Knight('black')
        self._black_bishop = Bishop('black')
        self._black_queen = Queen('black')
        self._black_king = King('black')

        # game board
        self._chess_dict = {
            'a8': self._black_rook,
            'b8': self._black_knight,
            'c8': self._black_bishop,
            'd8': self._black_queen,
            'e8': self._black_king,
            'f8': self._black_bishop,
            'g8': self._black_knight,
            'h8': self._black_rook,
            'a7': self._black_pawn,
            'b7': self._black_pawn,
            'c7': self._black_pawn,
            'd7': self._black_pawn,
            'e7': self._black_pawn,
            'f7': self._black_pawn,
            'g7': self._black_pawn,
            'h7': self._black_pawn,
            'a6': None,
            'b6': None,
            'c6': None,
            'd6': None,
            'e6': None,
            'f6': None,
            'g6': None,
            'h6': None,
            'a5': None,
            'b5': None,
            'c5': None,
            'd5': None,
            'e5': None,
            'f5': None,
            'g5': None,
            'h5': None,
            'a4': None,
            'b4': None,
            'c4': None,
            'd4': None,
            'e4': None,
            'f4': None,
            'g4': None,
            'h4': None,
            'a3': None,
            'b3': None,
            'c3': None,
            'd3': None,
            'e3': None,
            'f3': None,
            'g3': None,
            'h3': None,
            'a2': self._white_pawn,
            'b2': self._white_pawn,
            'c2': self._white_pawn,
            'd2': self._white_pawn,
            'e2': self._white_pawn,
            'f2': self._white_pawn,
            'g2': self._white_pawn,
            'h2': self._white_pawn,
            'a1': self._white_rook,
            'b1': self._white_knight,
            'c1': self._white_bishop,
            'd1': self._white_queen,
            'e1': self._white_king,
            'f1': self._white_bishop,
            'g1': self._white_knight,
            'h1': self._white_rook,
        }

        # for testing purposes
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

    def get_game_state(self):
        """
        Returns string representing current game state.
        3 options: UNFINISHED, WHITE_WON, BLACK_WON.
        """
        return self._game_state

    def set_game_state(self, new_state):
        """
        Receives a game state as an argument and performs validation.
        3 options: UNFINISHED, WHITE_WON, BLACK_WON.
        If valid, amends the current game state; otherwise, returns None.
        """
        if new_state == 'UNFINISHED' or 'WHITE_WON' or 'BLACK_WON':
            self._game_state = new_state

        else: return None      # invalid state

    def get_board(self):
        """
        Returns a nested list representing the current game board.
        Uppercase = white, lowercase = black.
        p = pawn
        r = rook
        n = knight
        b = bishop
        q = queen
        k = king
        '' = empty square
        """
        return self._board


    def get_dictionary(self):
        """
        Returns dictionary representing the board.
        Each square of the board is represented as a key in string notation (e.g. 'A1').
        Values are either ChessPiece objects, representing the piece on the square, or None if empty.
        """
        return self._chess_dict

    def set_dictionary(self, move_from, move_to):
        """
        Receives two string arguments: the square to move from and the square to move to.
        Updates the dictionary to reflect the move, so the object at move_from is ...
        transferred to move_to, and move_from becomes 'None' to represent an empty square.
        """
        if move_from in self._chess_dict:

            if move_to in self._chess_dict:

                self._chess_dict[move_to] = self._chess_dict[move_from]   # 'move to' square now holds ChessPiece object

                self._chess_dict[move_from] = None                        # 'move from' square now empty