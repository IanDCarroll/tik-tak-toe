import unittest
from source.referee_chair import *
from source.game_table import *
from source.facilitator_credentials import * 

class RefereeTestCase(unittest.TestCase):

    def setUp(self):
        self.facilitator = Facilitator()
        self.announcer = Announcer()
        self.table_top = TableTop()
        self.ref = Referee(self.table_top)
        self.false_board = [1,10,1, 0,10,0, 1,0,10]
        self.edge_board = [1,10,1, 1,10,0, 1,0,10]
        self.column_board = [1,10,1, 0,10,0, 1,10,0]
        self.row_board = [1,0,1, 10,10,10 ,0,0,1]
        self.diagonal_board = [1,10,1, 10,1,0, 1,0,10]
        self.mock_4x4_board = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
        self.win_list_3x3 = [[0,1,2], [3,4,5], [6,7,8],
                             [0,3,6], [1,4,7], [2,5,8],
                             [0,4,8], [2,4,6]]
        self.win_list_4x4 = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15],
                             [0,4,8,12], [1,5,9,13], [2,6,10,14], [3,7,11,15],
                             [0,5,10,15],[3,6,9,12]]

    def test_referee_is_an_object(self):
        self.assertEqual(isinstance(self.ref, object), True)

    def test_check_for_game_over_returns_tie(self):
        self.ref.moves_taken = 9
        self.assertEqual(self.ref.check_for_game_over(), 'tie')

    def test_check_for_winner_returns_false(self):
        self.table_top.board = self.false_board
        self.assertEqual(self.ref.check_for_winner(), False)

    def test_check_for_winner_does_edges(self):
        self.table_top.board = self.edge_board
        self.assertEqual(self.ref.check_for_winner(), True)

    def test_check_for_winner_does_columns(self):
        self.table_top.board = self.column_board
        self.assertEqual(self.ref.check_for_winner(), True)

    def test_check_for_winner_does_rows(self):
        self.table_top.board = self.row_board
        self.assertEqual(self.ref.check_for_winner(), True)

    def test_check_for_winner_does_diagonals(self):
        self.table_top.board = self.diagonal_board
        self.assertEqual(self.ref.check_for_winner(), True)

    def test_get_board_size_3(self):
        test = self.facilitator.get_board_size(self.table_top.board)
        self.assertEqual(test, 3)

    def test_get_board_size_4(self):
        self.table_top.board = self.mock_4x4_board
        test = self.facilitator.get_board_size(self.table_top.board)
        self.assertEqual(test, 4)

    def test_referee_has_get_board_size(self):
        self.assertEqual(hasattr(self.ref, 'get_board_size'), True)

    def test_announcer_has_get_board_size(self):
        self.assertEqual(hasattr(self.announcer, 'get_board_size'), True)

    def test_prep_next_turn_toggles_players(self):
        self.assertEqual(self.ref.whos_turn, self.ref.player1)
        self.ref.prep_next_turn()
        self.assertEqual(self.ref.whos_turn, self.ref.player2)
        self.ref.prep_next_turn()
        self.assertEqual(self.ref.whos_turn, self.ref.player1)

    def test_get_win_list_returns_the_3x3_wins(self):
        self.assertEqual(self.ref.get_win_list(), self.win_list_3x3)

    def test_get_win_list_returns_the_4x4_wins(self):
        self.table_top.board = self.mock_4x4_board
        self.assertEqual(self.ref.get_win_list(), self.win_list_4x4)

if __name__ == '__main__':
     unittest.main()
