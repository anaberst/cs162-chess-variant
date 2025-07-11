# Author: Anastasiya Berst
# GitHub username: anaberst
# Date: 03/16/2025 (uploaded to GitHub: 07/10/2025)
# Description: This program simulates a game of the chess variant "King of the Hill"

class ChessPiece:
    """
    Represents a chess piece.
    Parent for all chess piece classes.
    """
    def __init__(self, color):
        """
        Initializes a ChessPiece object with a color attribute.
        """
        self._color = color.lower()  # 'black' or 'white'

    def get_color(self):
        """
        Returns the chess piece's color.
        """
        return self._color

    def get_abbreviation(self):
        """
        Returns a string abbreviation for the chess piece.
        Uppercase for white, lowercase for black.
        """
        letter = self.get_letter

        # uppercase for white
        if self.get_color() == 'white':
            return letter.upper()

        # lowercase for black
        else:
            return letter.lower()


class Pawn(ChessPiece):
    """
    Represents a pawn.
    Inherits from ChessPiece.
    """
    def __init__(self, color):
        """
        Initializes a Pawn object with two private data members:
        color, letter
        """
        super().__init__(color)
        self._letter = 'p'

    def get_letter(self):
        """
        Returns 'P' if white or 'p' if black.
        Uses get_abbreviation method from parent class.
        """
        return self._letter

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
        Initializes a Rook object with two private data members: color, letter.
        """
        super().__init__(color)
        self._letter = 'r'

    def get_letter(self):
        """
        Returns 'R' if white or 'r' if black.
        Uses get_abbreviation method from parent class.
        """
        return self._letter

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
        Initializes a Knight object with two private data members: color, letter.
        """
        super().__init__(color)
        self._letter = 'n'

    def get_letter(self):
        """
        Returns 'N' if white or 'n' if black.
        Uses get_abbreviation method from parent class.
        """
        return self._letter

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
        Initializes a Bishop object with two private data members: color, letter.
        """
        super().__init__(color)
        self._letter = 'b'

    def get_letter(self):
        """
        Returns 'B' if white or 'b' if black.
        Uses get_abbreviation method from parent class.
        """
        return self._letter

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
        Initializes a Queen object with two private data members: color, letter.
        """
        super().__init__(color)
        self._letter = 'q'

    def get_letter(self):
        """
        Returns 'Q' if white or 'q' if black.
        Uses get_abbreviation method from parent class.
        """
        return self._letter

    def legal_move(self, move_from, move_to):
        """
        Receives two tuples as parameters, both with two indices corresponding to piece's position in nested list 'board'.
        Returns True if move is legal for a queen. Returns False otherwise.
        """
        # all forward and backward moves are legal
        if move_from[1] == move_to[1]:
            return True

        # all lateral moves are legal
        elif move_from[0] == move_to[0]:
            return True

        # all diagonal moves are legal
        elif abs(move_from[0] - move_to[0]) == abs(move_from[1] - move_to[1]):
            return True
        else:
            return False


class King(ChessPiece):
    """
    Represents a king.
    Inherits from ChessPiece.
    """
    def __init__(self, color):
        """
        Initializes a King object with two private data members: color, letter.
        """
        super().__init__(color)
        self._letter = 'k'

    def get_letter(self):
        """
        Returns 'K' if white or 'k' if black.
        Uses get_abbreviation method from parent class.
        """
        return self._letter

    def legal_move(self, move_from, move_to):
        """
        Receives two tuples as parameters, both with two indices corresponding to piece's position in nested list 'board'.
        Returns True if move is legal for a king. Returns False otherwise.
        """
        # determine move distance
        row_distance = abs(move_from[0] - move_to[0])
        col_distance = abs(move_from[1] - move_to[1])

        # must move exactly one space in at least one direction
        return (row_distance <= 1 and col_distance <= 1
                and (row_distance == 1 or col_distance == 1))


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
        if (new_state == 'UNFINISHED'
                or new_state == 'WHITE_WON'
                or new_state == 'BLACK_WON'):
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
        col_index = string_coordinate[0].lower()   # letter in coordinate
        row_index = string_coordinate[1]           # number in coordinate

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

        if row_index in number_to_index:
            row_index = number_to_index[row_index]      # convert number to index
        else:
            return None                                 # invalid row coordinate

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

        if col_index in letter_to_index:
            col_index = letter_to_index[col_index]      # convert letter to index
            return row_index, col_index                 # return tuple
        else:
            return None                                 # invalid column coordinate


    def index_to_string(self, index_tuple):
        """
        Receives a tuple containing two indices (from the nested list 'board') as an argument.
        First (row) index will be converted to the letter portion of a coordinate in string notation.
        Second (column) index will be converted to the number portion of a coordinate in string notation.
        Returns converted indices as a string. Returns None if indices are invalid entries.
        """
        row_index = index_tuple[0]       # index to be converted to a number
        col_index = index_tuple[1]       # index to be converted to a letter

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

        if row_index in index_to_number:
            row_index = index_to_number[row_index]      # convert row index to number
        else:
            return None                                 # invalid row index

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

        if col_index in index_to_letter:
            col_index = index_to_letter[col_index]       # convert column index to letter
            return col_index + row_index                 # return string
        else:
            return None                                  # invalid column index


    def path_clear(self, move_from, move_to):
        """
        Receives two tuples as parameters, both with two indices corresponding to piece's position in nested list 'board'.
        Returns True if the path is clear to move. Returns False otherwise.
        """
        move_from_string = self.index_to_string(move_from)

        # knights jump over pieces, so path is always clear
        if isinstance(self._chess_dict[move_from_string], Knight) is True:
            return True

        start_row = move_from[0]
        start_col = move_from[1]
        vertical_distance = move_to[0] - move_from[0]
        horizontal_distance = move_to[1] - move_from[1]

        # if moving only one space
        if abs(vertical_distance) <= 1 and abs(horizontal_distance) <= 1:
            return self._one_space_move(move_to, horizontal_distance, move_from_string)

        # lateral moves
        if vertical_distance == 0:
            return self._lateral_move(start_row, start_col, horizontal_distance)

        # vertical moves
        elif horizontal_distance == 0:
           return self._vertical_move(start_row, start_col, vertical_distance, move_from_string)

        # diagonal moves
        elif abs(horizontal_distance) == abs(vertical_distance):
            return self._diagonal_move(start_row, start_col, horizontal_distance, vertical_distance)


    def _one_space_move(self, move_to, horizontal_distance, move_from_string):
        """
        Helper method for path_clear that handles single space move logic.
        Receives the square to move to, horizontal distance, and starting square coordinates as arguments.
        Returns True if path is clear. Returns False otherwise.
        """
        # exception: pawn diagonal capture
        if (isinstance(self._chess_dict[move_from_string], Pawn)
                and abs(horizontal_distance) == 1):               # only time pawns move horizontally

            move_to_string = self.index_to_string(move_to)
            return self._chess_dict[move_to_string] is not None   # a piece must be present to capture

        # path clear!
        return True

    def _lateral_move(self, start_row, start_col, horizontal_distance):
        """
        Helper method for path_clear that handles lateral move logic.
        Receives the starting row, starting column, and horizontal distance as arguments.
        Returns True if path is clear. Returns False otherwise.
        """
        # loop helper variables
        checking_row = start_row
        checking_col = start_col

        # moving left
        if horizontal_distance < 0:

            for step in range(0, abs(horizontal_distance) - 1):
                checking_col -= 1    # move to next position to check
                current_square = self.index_to_string((checking_row, checking_col))

                # path not clear
                if self._chess_dict[current_square] is not None:
                    return False

        # moving right
        else:
            for step in range(0, horizontal_distance - 1):
                checking_col += 1    # move to next position to check
                current_square = self.index_to_string((checking_row, checking_col))

                # path not clear
                if self._chess_dict[current_square] is not None:
                    return False

        # path clear!
        return True

    def _vertical_move(self, start_row, start_col, vertical_distance, move_from_string):
        """
        Helper method for path_clear that handles vertical move logic.
        Receives the starting row, starting column, vertical distance, and starting square coordinates as arguments.
        Returns True if path is clear. Returns False otherwise.
        """
        # loop helper variables
        checking_row = start_row
        checking_col = start_col

        # exception: pawns can move 2 spaces on first move but NOT to capture
        if isinstance(self._chess_dict[move_from_string], Pawn) is True:

            # white pawns moving up the board
            if self._chess_dict[move_from_string].get_color() == 'white':
                for step in range(0, abs(vertical_distance)):
                    checking_row -= 1    # move to next position to check
                    current_square = self.index_to_string((checking_row, checking_col))

                    # path not clear
                    if self._chess_dict[current_square] is not None:
                        return False

            # black pawns moving down the board
            else:
                for step in range(0, vertical_distance):
                    checking_row += 1    # move to next position to check
                    current_square = self.index_to_string((checking_row, checking_col))

                    # path not clear
                    if self._chess_dict[current_square] is not None:
                        return False

        # moving up the board
        elif vertical_distance < 0:
            for step in range(0, abs(vertical_distance) - 1):
                checking_row -= 1  # move to next position to check
                current_square = self.index_to_string((checking_row, checking_col))

                # path not clear
                if self._chess_dict[current_square] is not None:
                    return False

        # moving down the board
        else:
            for step in range(0, vertical_distance - 1):
                checking_row += 1  # move to next position to check
                current_square = self.index_to_string((checking_row, checking_col))

                # path not clear
                if self._chess_dict[current_square] is not None:
                    return False

        # path clear!
        return True

    def _diagonal_move(self, start_row, start_col, horizontal_distance, vertical_distance):
        """
        Helper method for path_clear that handles diagonal move logic.
        Receives the starting row, starting column, horizontal distance, and vertical distance as arguments.
        Returns True if path is clear. Returns False otherwise.
        """
        # loop helper variables
        checking_row = start_row
        checking_col = start_col

        # moving bottom-up, left-to-right
        if vertical_distance < 0 < horizontal_distance:

            for step in range(0, horizontal_distance - 1):
                checking_row -= 1    # move to next position to check
                checking_col += 1
                current_square = self.index_to_string((checking_row, checking_col))

                # path not clear
                if self._chess_dict[current_square] is not None:
                    return False

        # moving top-down, right-to-left
        elif vertical_distance > 0 > horizontal_distance:

            for step in range(0, vertical_distance - 1):
                checking_row += 1    # move to next position to check
                checking_col -= 1
                current_square = self.index_to_string((checking_row, checking_col))

                # path not clear
                if self._chess_dict[current_square] is not None:
                    return False

        elif vertical_distance == horizontal_distance:

            # moving bottom-up, right-to-left
            if vertical_distance < 0:

                for step in range(0, abs(vertical_distance) - 1):
                    checking_row -= 1    # move to next position to check
                    checking_col -= 1
                    current_square = self.index_to_string((checking_row, checking_col))

                    # path not clear
                    if self._chess_dict[current_square] is not None:
                        return False

            # moving top-down, left-to-right
            elif vertical_distance > 0:

                for step in range(0, vertical_distance - 1):
                    checking_row += 1    # move to next position to check
                    checking_col += 1
                    current_square = self.index_to_string((checking_row, checking_col))

                    # path not clear
                    if self._chess_dict[current_square] is not None:
                        return False

        # path clear!
        return True


    def king_captured(self):
        """
        Checks dictionary for the king.
        Returns True if king is absent and has been captured.
        Returns False otherwise.
        """
        # white player captures black king
        if self._current_color == 'white':
            king = self._black_king

        # black player captures white king
        else:
            king = self._white_king

        for square in self._chess_dict:
            if self._chess_dict[square] == king:
                return False      # king not yet captured

        return True               # king captured


    def king_on_central_squares(self):
        """
        Checks central squares (d4, d5, e4, e5) in dictionary for the king.
        Returns True if king is on the four central squares.
        Returns False otherwise.
        """
        central_squares = ['d4', 'd5', 'e4', 'e5']

        for square in central_squares:
            if isinstance(self._chess_dict[square], King) is True:
                return True    # king found on central squares

        return False           # king not on central squares


    def move_made(self, move_from, move_to):
        """
   	    Receives two string arguments: the square to move from and the square to move to.
    	Checks if game is still in play, if it is current player's turn, if squares exist, if not moving off board,
   	    if move is legal with the given chess piece, if any pieces are in the way and if it would result in any
        captures. If legal: updates the board, updates the ChessPiece object coordinates, and returns True.
        Otherwise, returns False.
        """
        move_from = move_from.lower()
        move_to = move_to.lower()

        starting_square = self.string_to_index(move_from)
        final_square = self.string_to_index(move_to)

        # if game is no longer in play
        if self._game_state != 'UNFINISHED':
            return False

        # if no move is made
        if move_from == move_to:
            return False

        # if 'move from' is invalid
        if move_from not in self._chess_dict:
            return False

        # if 'move to' is invalid
        if move_to not in self._chess_dict:
            return False

        # if 'move from' square is empty
        moving_piece = self._chess_dict[move_from]
        if moving_piece is None:
            return False

        # if not current player's turn
        if self._current_color != moving_piece.get_color():
            return False

        # when capturing
        captured_piece = self._chess_dict[move_to]
        if captured_piece is not None:

            # if player's own piece on the 'move to' square
            if captured_piece.get_color() == self._current_color:
                return False

        # if move illegal for that piece
        if moving_piece.legal_move(starting_square, final_square) is False:
            return False

        # if path not clear
        if self.path_clear(starting_square, final_square) is False:
            return False

        # updates dictionary of current play
        self.set_dictionary(move_from, move_to)

        # dictionary updates nested list 'board'
        self.set_board()

        # check win conditions
        if self.king_captured() is True or self.king_on_central_squares() is True:

            # white won!
            if self._current_color == 'white':
                self._game_state = 'WHITE_WON'

            # black won!
            elif self._current_color == 'black':
                self._game_state = 'BLACK_WON'

        # switches current color for next play
        if self._current_color == 'white':
            self._current_color = 'black'

        else:
            self._current_color = 'white'

        # move has been made
        return True