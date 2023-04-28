import unittest
from Piece import Knight, Queen, King
from enums import Player
import chess_engine


class TestGame(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        # define game board to test on
        self.game_state = chess_engine.game_state()
        self.game_state.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]

    def empty_board(self):
        for col in range(8):
            for row in range(8):
                if self.game_state.board[col][row] != Player.EMPTY:
                    self.game_state.board[col][row] = Player.EMPTY

    def test_knight_get_valid_peaceful_moves_knight_in_the_middle(self):
        self.empty_board()
        # create knight and place it on the board
        test_knight = Knight('n', 3, 4, Player.PLAYER_1)
        self.game_state.board[3][4] = test_knight
        # get moves
        moves = test_knight.get_valid_peaceful_moves(self.game_state)
        self.assertEqual(len(moves), 8)
        self.assertEqual(moves, [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 5), (5, 3)])

    def test_knight_get_valid_peaceful_moves_knight_in_the_corner(self):
        self.empty_board()
        # create knight and place it on the board
        test_knight = Knight('n', 0, 0, Player.PLAYER_1)
        self.game_state.board[0][0] = test_knight
        # get moves
        moves = test_knight.get_valid_peaceful_moves(self.game_state)
        self.assertEqual(len(moves), 2)
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
        self.assertEqual(len(moves), 4)
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
        self.assertEqual(len(moves), 4)
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
        self.assertEqual(len(moves), 2)
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


