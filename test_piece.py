import unittest
from Piece import Knight, Queen, King, Pawn, Rook, Bishop
from enums import Player
import chess_engine
import ai_engine


class TestGame(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        # define game board to test on
        self.game_state = chess_engine.game_state()
        self.game_state.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
        self.chess_ai = ai_engine.chess_ai()

    def empty_board(self):
        return [[Player.EMPTY for _ in range(8)] for _ in range(8)]

    """                              UNIT TESTS FOR KNIGHT CLASS                                     """
    def test_knight_get_valid_peaceful_moves_knight_in_the_middle(self):
        self.empty_board()
        # create knight and place it on the board
        test_knight = Knight('n', 3, 4, Player.PLAYER_1)
        self.game_state.board[3][4] = test_knight
        # get moves
        moves = test_knight.get_valid_peaceful_moves(self.game_state)
        self.assertEqual(moves, [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 5), (5, 3)])

    def test_knight_get_valid_peaceful_moves_knight_in_the_corner(self):
        self.empty_board()
        # create knight and place it on the board
        test_knight = Knight('n', 0, 0, Player.PLAYER_1)
        self.game_state.board[0][0] = test_knight
        # get moves
        moves = test_knight.get_valid_peaceful_moves(self.game_state)
        self.assertEqual(moves, [(1, 2), (2, 1)])

    def test_knight_get_valid_peaceful_moves_knight_in_the_corner_with_allies(self):
        self.empty_board()
        # create knight and place it on the board
        test_knight = Knight('n', 0, 0, Player.PLAYER_1)
        self.game_state.board[0][0] = test_knight
        # add allies
        self.game_state.board[1][2] = Knight('n', 1, 2, Player.PLAYER_2)
        self.game_state.board[2][1] = Knight('n', 2, 1, Player.PLAYER_2)
        # get moves
        moves = test_knight.get_valid_peaceful_moves(self.game_state)
        self.assertEqual(len(moves), 0)

    def test_knight_get_valid_peaceful_moves_knight_in_the_edge(self):
        self.empty_board()
        # create knight and place it on the board
        test_knight = Knight('n', 5, 0, Player.PLAYER_1)
        self.game_state.board[5][0] = test_knight
        # get moves
        moves = test_knight.get_valid_peaceful_moves(self.game_state)
        self.assertEqual(moves, [(3, 1), (4, 2), (6, 2), (7, 1)])

    def test_knight_get_valid_piece_takes_knight_in_the_middle_with_enemies(self):
        self.empty_board()
        # create knight and place it on the board
        test_knight = Knight('n', 3, 4, Player.PLAYER_1)
        self.game_state.board[3][4] = test_knight
        # add enemies
        self.game_state.board[1][3] = Knight('n', 1, 3, Player.PLAYER_2)
        self.game_state.board[2][6] = Knight('n', 2, 6, Player.PLAYER_2)
        self.game_state.board[4][2] = Queen('q', 4, 2, Player.PLAYER_2)
        self.game_state.board[5][5] = King('k', 5, 5, Player.PLAYER_2)
        # get moves
        moves = test_knight.get_valid_piece_takes(self.game_state)
        self.assertEqual(moves, [(1, 3), (2, 6), (4, 2), (5, 5)])

    def test_knight_get_valid_piece_takes_knight_in_the_middle_without_allies(self):
        self.empty_board()
        # create knight and place it on the board
        test_knight = Knight('n', 3, 4, Player.PLAYER_1)
        self.game_state.board[3][4] = test_knight
        # get moves
        moves = test_knight.get_valid_piece_takes(self.game_state)
        self.assertEqual(len(moves), 0)

    def test_knight_get_valid_piece_takes_knight_in_the_corner_with_enemies(self):
        self.empty_board()
        # create knight and place it on the board
        test_knight = Knight('n', 0, 0, Player.PLAYER_1)
        self.game_state.board[0][0] = test_knight
        # add enemies
        self.game_state.board[1][2] = Knight('n', 1, 2, Player.PLAYER_2)
        self.game_state.board[2][1] = Knight('n', 2, 1, Player.PLAYER_2)
        # get moves
        moves = test_knight.get_valid_piece_takes(self.game_state)
        self.assertEqual(moves, [(1, 2), (2, 1)])

    def test_knight_get_valid_piece_takes_knight_in_the_corner_with_same_team_allies(self):
        self.empty_board()
        # create knight and place it on the board
        test_knight = Knight('n', 0, 0, Player.PLAYER_1)
        self.game_state.board[0][0] = test_knight
        # add allies of the same team
        self.game_state.board[1][2] = Knight('n', 1, 2, Player.PLAYER_1)
        self.game_state.board[2][1] = Queen('q', 2, 1, Player.PLAYER_1)
        # get moves
        moves = test_knight.get_valid_piece_takes(self.game_state)
        self.assertEqual(len(moves), 0)


    """                                 INTEGRATION TESTS                                """
    def test_knight_get_valid_piece_moves(self):
        self.empty_board()
        # create knight and place it on the board
        test_knight = Knight('n', 3, 4, Player.PLAYER_1)
        self.game_state.board[3][4] = test_knight
        # add allies
        self.game_state.board[1][3] = Knight('n', 1, 3, Player.PLAYER_1)
        self.game_state.board[2][6] = Knight('n', 2, 6, Player.PLAYER_1)
        self.game_state.board[4][2] = Queen('q', 4, 2, Player.PLAYER_1)
        self.game_state.board[5][5] = King('k', 5, 5, Player.PLAYER_1)
        # add enemies
        self.game_state.board[1][2] = Knight('n', 1, 2, Player.PLAYER_2)
        self.game_state.board[2][1] = Knight('n', 2, 1, Player.PLAYER_2)
        self.game_state.board[4][6] = Queen('q', 4, 6, Player.PLAYER_2)
        self.game_state.board[5][3] = King('k', 5, 3, Player.PLAYER_2)
        # get moves
        moves = test_knight.get_valid_piece_moves(self.game_state)
        self.assertEqual(moves, [(1, 5), (2, 2), (4, 6), (5, 3)])

    def test_evaluate_board(self):
        self.empty_board()
        # create knights and place them on the board
        self.get_full_board()
        # get evaluation
        evaluation_b = self.chess_ai.evaluate_board(self.game_state, Player.PLAYER_1)
        evaluation_w = self.chess_ai.evaluate_board(self.game_state, Player.PLAYER_2)
        # check evaluation
        self.assertEqual(evaluation_b, -1 * evaluation_w)
        self.assertEqual(evaluation_b + evaluation_w, 0)

    def get_full_board(self):
        self.empty_board()
        self.game_state.board[0][0] = Rook('r', 0, 0, Player.PLAYER_1)
        self.game_state.board[0][1] = Knight('n', 0, 1, Player.PLAYER_1)
        self.game_state.board[0][2] = Bishop('b', 0, 2, Player.PLAYER_1)
        self.game_state.board[0][3] = Queen('q', 0, 3, Player.PLAYER_1)
        self.game_state.board[0][4] = King('k', 0, 4, Player.PLAYER_1)
        self.game_state.board[0][5] = Bishop('b', 0, 5, Player.PLAYER_1)
        self.game_state.board[0][6] = Knight('n', 0, 6, Player.PLAYER_1)
        self.game_state.board[0][7] = Rook('r', 0, 7, Player.PLAYER_1)
        self.game_state.board[1][0] = Pawn('p', 1, 0, Player.PLAYER_1)
        self.game_state.board[1][1] = Pawn('p', 1, 1, Player.PLAYER_1)
        self.game_state.board[1][2] = Pawn('p', 1, 2, Player.PLAYER_1)
        self.game_state.board[1][3] = Pawn('p', 1, 3, Player.PLAYER_1)
        self.game_state.board[1][3] = Pawn('p', 1, 4, Player.PLAYER_1)
        self.game_state.board[1][5] = Pawn('p', 1, 5, Player.PLAYER_1)
        self.game_state.board[1][6] = Pawn('p', 1, 6, Player.PLAYER_1)
        self.game_state.board[1][7] = Pawn('p', 1, 7, Player.PLAYER_1)
        self.game_state.board[7][0] = Rook('r', 7, 0, Player.PLAYER_2)
        self.game_state.board[7][1] = Knight('n', 7, 1, Player.PLAYER_2)
        self.game_state.board[7][2] = Bishop('b', 7, 2, Player.PLAYER_2)
        self.game_state.board[7][3] = Queen('q', 7, 3, Player.PLAYER_2)
        self.game_state.board[7][4] = King('k', 7, 4, Player.PLAYER_2)
        self.game_state.board[7][5] = Bishop('b', 7, 5, Player.PLAYER_2)
        self.game_state.board[7][6] = Knight('n', 7, 6, Player.PLAYER_2)
        self.game_state.board[7][7] = Rook('r', 7, 7, Player.PLAYER_2)
        self.game_state.board[6][0] = Pawn('p', 6, 0, Player.PLAYER_2)
        self.game_state.board[6][1] = Pawn('p', 6, 1, Player.PLAYER_2)
        self.game_state.board[6][2] = Pawn('p', 6, 2, Player.PLAYER_2)
        self.game_state.board[6][3] = Pawn('p', 6, 3, Player.PLAYER_2)
        self.game_state.board[6][4] = Pawn('p', 6, 4, Player.PLAYER_2)
        self.game_state.board[6][5] = Pawn('p', 6, 5, Player.PLAYER_2)
        self.game_state.board[6][6] = Pawn('p', 6, 6, Player.PLAYER_2)
        self.game_state.board[6][7] = Pawn('p', 6, 7, Player.PLAYER_2)

    """                                 SYSTEM TESTS                                 """
    def test_mat_fools(self):
        self.game_state.move_piece((6, 4), (4, 4), False)  # w
        self.game_state.move_piece((1, 3), (3, 3), False)  # b
        self.game_state.move_piece((7, 5), (2, 0), False)  # w
        self.game_state.move_piece((6, 5), (4, 5), False)  # b - checkmate
        self.assertEqual(self.game_state.checkmate_stalemate_checker(), 0)
