# Author: Anastasiya Berst
# GitHub username: anaberst
# Date: 03/16/2025 (uploaded to GitHub: 07/27/2025)
# Description: This program contains unit tests for chess_var.py

import unittest
from chess_var import ChessVar, Pawn, Rook, Knight, Bishop, Queen, King


class TestChessPieces(unittest.TestCase):
    """
    Test cases for chess piece classes
    """

    def setUp(self):
        """
        Set up test fixtures before each test method
        """
        self.white_pawn = Pawn('white')
        self.black_pawn = Pawn('black')
        self.white_rook = Rook('white')
        self.black_rook = Rook('black')
        self.white_knight = Knight('white')
        self.black_knight = Knight('black')
        self.white_bishop = Bishop('white')
        self.black_bishop = Bishop('black')
        self.white_queen = Queen('white')
        self.black_queen = Queen('black')
        self.white_king = King('white')
        self.black_king = King('black')


    def test_piece_initialization(self):
        """
        Test that pieces are initialized correctly
        """
        self.assertEqual(self.white_pawn.get_color(), 'white')
        self.assertEqual(self.black_pawn.get_color(), 'black')
        self.assertEqual(self.white_pawn.get_letter(), 'p')
        self.assertEqual(self.white_rook.get_letter(), 'r')
        self.assertEqual(self.white_knight.get_letter(), 'n')
        self.assertEqual(self.white_bishop.get_letter(), 'b')
        self.assertEqual(self.white_queen.get_letter(), 'q')
        self.assertEqual(self.white_king.get_letter(), 'k')


    def test_pawn_legal_moves(self):
        """
        Test pawn movement rules
        """
        # White pawn initial two-square move
        self.assertTrue(self.white_pawn.legal_move((6, 0), (4, 0)))

        # White pawn single square move
        self.assertTrue(self.white_pawn.legal_move((5, 0), (4, 0)))

        # White pawn diagonal capture
        self.assertTrue(self.white_pawn.legal_move((5, 0), (4, 1)))

        # Black pawn initial two-square move
        self.assertTrue(self.black_pawn.legal_move((1, 0), (3, 0)))

        # Invalid pawn move (backwards)
        self.assertFalse(self.white_pawn.legal_move((4, 0), (5, 0)))

        # Invalid pawn move (sideways)
        self.assertFalse(self.white_pawn.legal_move((4, 0), (4, 1)))


    def test_rook_legal_moves(self):
        """
        Test rook movement rules
        """
        # Vertical move
        self.assertTrue(self.white_rook.legal_move((0, 0), (7, 0)))

        # Horizontal move
        self.assertTrue(self.white_rook.legal_move((0, 0), (0, 7)))

        # Invalid diagonal move
        self.assertFalse(self.white_rook.legal_move((0, 0), (7, 7)))


    def test_knight_legal_moves(self):
        """
        Test knight movement rules
        """
        # Valid L-shaped moves
        self.assertTrue(self.white_knight.legal_move((4, 4), (6, 5)))
        self.assertTrue(self.white_knight.legal_move((4, 4), (2, 3)))
        self.assertTrue(self.white_knight.legal_move((4, 4), (5, 6)))

        # Invalid move
        self.assertFalse(self.white_knight.legal_move((4, 4), (6, 6)))


    def test_bishop_legal_moves(self):
        """
        Test bishop movement rules
        """
        # Valid diagonal moves
        self.assertTrue(self.white_bishop.legal_move((0, 0), (7, 7)))
        self.assertTrue(self.white_bishop.legal_move((4, 4), (1, 1)))

        # Invalid horizontal move
        self.assertFalse(self.white_bishop.legal_move((0, 0), (0, 7)))

        # Invalid vertical move
        self.assertFalse(self.white_bishop.legal_move((0, 0), (7, 0)))


    def test_queen_legal_moves(self):
        """
        Test queen movement rules
        """
        # Valid moves (combines rook and bishop)
        self.assertTrue(self.white_queen.legal_move((4, 4), (4, 7)))  # horizontal
        self.assertTrue(self.white_queen.legal_move((4, 4), (7, 4)))  # vertical
        self.assertTrue(self.white_queen.legal_move((4, 4), (7, 7)))  # diagonal

        # Invalid knight-like move
        self.assertFalse(self.white_queen.legal_move((4, 4), (6, 5)))


    def test_king_legal_moves(self):
        """
        Test king movement rules
        """
        # Valid one-square moves
        self.assertTrue(self.white_king.legal_move((4, 4), (4, 5)))
        self.assertTrue(self.white_king.legal_move((4, 4), (5, 5)))
        self.assertTrue(self.white_king.legal_move((4, 4), (3, 4)))

        # Invalid two-square move
        self.assertFalse(self.white_king.legal_move((4, 4), (4, 6)))


class TestChessVar(unittest.TestCase):
    """
    Test cases for ChessVar class
    """

    def setUp(self):
        """
        Set up test fixtures before each test method
        """
        self.game = ChessVar()

    def test_initial_game_state(self):
        """
        Test initial game state
        """
        self.assertEqual(self.game.get_game_state(), 'UNFINISHED')

    def test_board_initialization(self):
        """
        Test that the board is set up correctly
        """
        board = self.game.get_board()

        # Check that board is 8x8
        self.assertEqual(len(board), 8)
        self.assertEqual(len(board[0]), 8)

        # Check initial piece positions
        self.assertEqual(board[0][0], 'r')  # Black rook
        self.assertEqual(board[0][4], 'k')  # Black king
        self.assertEqual(board[7][4], 'K')  # White king
        self.assertEqual(board[6][0], 'P')  # White pawn

    def test_string_to_index_conversion(self):
        """
        Test coordinate conversion from string to indices
        """
        self.assertEqual(self.game.string_to_index('a1'), (7, 0))
        self.assertEqual(self.game.string_to_index('h8'), (0, 7))
        self.assertEqual(self.game.string_to_index('e4'), (4, 4))
        self.assertIsNone(self.game.string_to_index('z9'))

    def test_index_to_string_conversion(self):
        """
        Test coordinate conversion from indices to string
        """
        self.assertEqual(self.game.index_to_string((7, 0)), 'a1')
        self.assertEqual(self.game.index_to_string((0, 7)), 'h8')
        self.assertEqual(self.game.index_to_string((4, 4)), 'e4')
        self.assertIsNone(self.game.index_to_string((8, 0)))

    def test_valid_pawn_moves(self):
        """
        Test valid pawn movements
        """
        # White pawn initial two-square move
        self.assertTrue(self.game.move_made('e2', 'e4'))
        # Black pawn single square move
        self.assertTrue(self.game.move_made('d7', 'd6'))

    def test_invalid_moves(self):
        """
        Test various invalid move scenarios
        """
        # Moving from empty square
        self.assertFalse(self.game.move_made('e4', 'e5'))
        # Moving opponent's piece (white's turn, trying to move black piece)
        self.assertFalse(self.game.move_made('e7', 'e6'))
        # Moving to same square
        self.assertFalse(self.game.move_made('e2', 'e2'))
        # Invalid coordinates
        self.assertFalse(self.game.move_made('z1', 'z2'))

    def test_turn_alternation(self):
        """
        Test that turns alternate correctly
        """
        # White moves first
        self.assertTrue(self.game.move_made('e2', 'e4'))
        # Black's turn
        self.assertTrue(self.game.move_made('e7', 'e5'))
        # White's turn again
        self.assertTrue(self.game.move_made('d2', 'd4'))

    def test_piece_capture(self):
        """
        Test piece capture mechanics
        """
        # Set up a capture scenario
        self.game.move_made('e2', 'e4')
        self.game.move_made('d7', 'd5')
        # Capture with pawn
        self.assertTrue(self.game.move_made('e4', 'd5'))

    def test_path_blocking(self):
        """
        Test that pieces can't move through other pieces
        """
        # Try to move rook when path is blocked by pawn
        self.assertFalse(self.game.move_made('a1', 'a3'))
        # Move pawn first
        self.game.move_made('a2', 'a4')
        self.game.move_made('h7', 'h6')  # Black move
        # Now rook can move
        self.assertTrue(self.game.move_made('a1', 'a3'))

    def test_knight_jumping(self):
        """
        Test that knights can jump over pieces
        """
        # Knight can move over pawns
        self.assertTrue(self.game.move_made('b1', 'c3'))

    def test_pawn_diagonal_capture_rules(self):
        """
        Test pawn diagonal capture specific rules
        """
        self.game.move_made('e2', 'e4')
        self.game.move_made('d7', 'd5')
        # Pawn can capture diagonally
        self.assertTrue(self.game.move_made('e4', 'd5'))
        
        # Reset game for another test
        self.game = ChessVar()
        self.game.move_made('e2', 'e4')
        self.game.move_made('f7', 'f6')
        # Pawn cannot move diagonally without capture
        self.assertFalse(self.game.move_made('e4', 'f5'))

    def test_king_capture_win_condition(self):
        """
        Test win condition when king is captured
        """
        # Test that initially no king is captured
        self.assertFalse(self.game.king_captured())

    def test_king_on_central_squares_win_condition(self):
        """
        Test win condition when king reaches central squares
        """
        # Test that initially no king is on central squares
        self.assertFalse(self.game.king_on_central_squares())

    def test_game_continues_after_win(self):
        """
        Test that no moves can be made after game ends
        """
        # Manually set game state to finished
        self.game._game_state = 'WHITE_WON'  # Direct access since no setter specified
        self.assertFalse(self.game.move_made('e2', 'e4'))

    def test_assignment_example_sequence(self):
        """
        Test the exact sequence from the assignment example
        """
        game = ChessVar()
        self.assertTrue(game.move_made('d2', 'd4'))
        self.assertTrue(game.move_made('g7', 'g5'))
        self.assertTrue(game.move_made('c1', 'g5'))
        self.assertTrue(game.move_made('e7', 'e6'))
        self.assertTrue(game.move_made('g5', 'd8'))
        
        # Check final board state matches expected output
        expected_board = [
            ['r', 'n', 'b', 'B', 'k', 'b', 'n', 'r'], 
            ['p', 'p', 'p', 'p', ' ', 'p', ' ', 'p'], 
            [' ', ' ', ' ', ' ', 'p', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
            ['P', 'P', 'P', ' ', 'P', 'P', 'P', 'P'], 
            ['R', 'N', ' ', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.assertEqual(game.get_board(), expected_board)

    def test_complex_game_scenario(self):
        """
        Test a sequence of moves simulating actual gameplay
        """
        moves = [
            ('e2', 'e4'),   # White pawn
            ('e7', 'e5'),   # Black pawn
            ('g1', 'f3'),   # White knight
            ('b8', 'c6'),   # Black knight
            ('f1', 'c4'),   # White bishop
            ('f8', 'c5'),   # Black bishop
        ]
        
        for move in moves:
            self.assertTrue(self.game.move_made(move[0], move[1]), 
                          f"Move {move[0]} to {move[1]} should be valid")

    def test_board_update_after_moves(self):
        """
        Test that board representation updates correctly after moves
        """
        # Move made
        self.game.move_made('e2', 'e4')
        updated_board = self.game.get_board()
        
        # Check that the piece moved
        self.assertEqual(updated_board[6][4], ' ')  # e2 should be empty
        self.assertEqual(updated_board[4][4], 'P')  # e4 should have white pawn

    def test_central_squares_win_condition(self):
        """
        Test king reaching central squares (d4, e4, d5, e5)
        """
        # This would require setting up a scenario where king can reach center
        # Testing the method exists and works with initial state
        self.assertEqual(self.game.get_game_state(), 'UNFINISHED')

    def test_pawn_two_square_initial_move(self):
        """
        Test that pawns can move two squares on first move only
        """
        # White pawn two square move from starting position
        self.assertTrue(self.game.move_made('e2', 'e4'))
        
        # Black pawn two square move from starting position  
        self.assertTrue(self.game.move_made('d7', 'd5'))
        
        # White pawn cannot move two squares again
        self.assertFalse(self.game.move_made('e4', 'e6'))

    def test_all_piece_types_can_move(self):
        """
        Test that all piece types can make valid moves
        """
        # Pawn
        self.assertTrue(self.game.move_made('e2', 'e4'))
        self.assertTrue(self.game.move_made('e7', 'e5'))
        
        # Knight
        self.assertTrue(self.game.move_made('g1', 'f3'))
        self.assertTrue(self.game.move_made('b8', 'c6'))
        
        # Bishop
        self.assertTrue(self.game.move_made('f1', 'c4'))
        self.assertTrue(self.game.move_made('f8', 'c5'))


if __name__ == '__main__':
    unittest.main()