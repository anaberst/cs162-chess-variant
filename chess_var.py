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

    def get_abbreviation(self):
        """
        Returns 'P' if white or 'p' if black.
        Returns None if color is invalid.
        """

        if self.get_color() == 'white':
            return 'P'

        else:
            return 'p'

    def legal_move(self, move_from, move_to):
        """
        Receives two tuples as arguments, each with two indices corresponding to position in nested list 'board'.
        Returns True if move is legal for a pawn. Returns False otherwise.
        """
        # determine direction and starting row based on color
        if self.get_color() == 'white':
            direction = -1      # white pawns move "up" (decreasing row numbers)
            starting_row = 6    # white pawns start on row 6
        else:
            direction = 1       # black pawns move "down" (increasing row numbers)
            starting_row = 1    # black pawns start on row 1

        # first move only: two spaces forward is legal
        if move_to[0] == move_from[0] + (2 * direction) and move_to[1] == move_from[1]:
            if move_from[0] == starting_row:
                return True
            else:
                return False

        # one space forward is legal
        elif move_to[0] == move_from[0] + direction:
            if move_to[1] == move_from[1]:
                return True

            # diagonal capture is legal
            elif abs(move_to[1] - move_from[1]) == 1:
                return True

            else:
                return False

        else:
            return False


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

    def get_abbreviation(self):
        """
        Returns 'R' if white or 'r' if black.
        """

        if self.get_color() == 'white':
            return 'R'

        else:
            return 'r'

    def legal_move(self, move_from, move_to):
        """
        Receives two tuples as parameters, both with two indices corresponding to piece's position in nested list 'board'.
        Returns True if move is legal for a rook. Returns False otherwise.
        """
        # all forward and backward moves are legal
        if move_from[1] == move_to[1]:
            return True

        # all lateral moves are legal
        elif move_from[0] == move_to[0]:
            return True

        else: return False


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

    def get_abbreviation(self):
        """
        Returns 'N' if white or 'n' if black.
        """

        if self.get_color() == 'white':
            return 'N'

        else:
            return 'n'

    def legal_move(self, move_from, move_to):
        """
        Receives two tuples as parameters, both with two indices corresponding to piece's position in nested list 'board'.
        Returns True if move is legal for a knight. Returns False otherwise.
        """
        # vertical L moves are legal
        if abs(move_from[0] - move_to[0]) == 2 and abs(move_from[1] - move_to[1]) == 1:
            return True

        # horizontal L moves are legal
        elif abs(move_from[0] - move_to[0]) == 1 and abs(move_from[1] - move_to[1]) == 2:
            return True

        else: return False


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

    def get_abbreviation(self):
        """
        Returns 'B' if white or 'b' if black.
        """

        if self.get_color() == 'white':
            return 'B'

        else:
            return 'b'

    def legal_move(self, move_from, move_to):
        """
        Receives two tuples as parameters, both with two indices corresponding to piece's position in nested list 'board'.
        Returns True if move is legal for a bishop. Returns False otherwise.
        """
        # only diagonal moves are legal
        if move_from[0] != move_to[0] and move_from[1] != move_to[1]:

            # must change both row and column by equal amounts
            if abs(move_from[0] - move_to[0]) == abs(move_from[1] - move_to[1]):
                return True

            else:
                return False

        else: return False


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

    def get_abbreviation(self):
        """
        Returns 'Q' if white or 'q' if black.
        """

        if self.get_color() == 'white':
            return 'Q'

        else:
            return 'q'


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

    def get_abbreviation(self):
        """
        Returns 'K' if white or 'k' if black.
        """

        if self.get_color() == 'white':
            return 'K'

        else:
            return 'k'


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


    def set_board(self):
        """
        Updates the nested list 'board' by iterating through the dictionary and transposing values.
        No return value.
        """

        for square in self._chess_dict:

            index_tuple = self.string_to_index(square)
            index_1 = index_tuple[0]
            index_2 = index_tuple[1]

            if self._chess_dict[square] is not None:

                self._board[index_1][index_2] = self._chess_dict[square].get_abbreviation()

            else:

                self._board[index_1][index_2] = ' '


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


    def string_to_index(self, string_coordinate):
        """
        Receives a string coordinate (e.g. 'A1') as an argument.
        Converts string into index on nested list 'board'.
        Returns tuple with two integers: converted letter and number of coordinate.
        Returns None if string coordinate is an invalid entry.
        """

        letter = string_coordinate[0].lower()   # letter in coordinate
        number = string_coordinate[1]           # number in coordinate

        number_to_index = {
            '1': 7,
            '2': 6,
            '3': 5,
            '4': 4,
            '5': 3,
            '6': 2,
            '7': 1,
            '8': 0
        }

        if number in number_to_index:

            number = number_to_index[number]      # convert number to index

        else: return None                         # if number is invalid entry

        letter_to_index = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7
        }

        if letter in letter_to_index:

            letter = letter_to_index[letter]      # convert letter to index

            return number, letter                 # return tuple

        else: return None                         # if letter is invalid entry


    def index_to_string(self, index_tuple):
        """
        Receives a tuple containing two indices (from the nested list 'board') as an argument.
        First index will be converted to the letter portion of a coordinate in string notation.
        Second index will be converted to the number portion of a coordinate in string notation.
        Returns converted indices as a string. Returns None if indices are invalid entries.
        """
        number = index_tuple[0]       # index to be converted to a number
        letter = index_tuple[1]       # index to be converted to a letter

        index_to_number = {
            7: '1',
            6: '2',
            5: '3',
            4: '4',
            3: '5',
            2: '6',
            1: '7',
            0: '8'
        }

        if number in index_to_number:

            number = index_to_number[number]      # convert first index to number

        else: return None                         # if first index is invalid entry

        index_to_letter = {
            0: 'a',
            1: 'b',
            2: 'c',
            3: 'd',
            4: 'e',
            5: 'f',
            6: 'g',
            7: 'h'
        }

        if letter in index_to_letter:

            letter = index_to_letter[letter]       # convert second index to letter

            return letter + number                 # return string

        else: return None                          # if second index is invalid entry