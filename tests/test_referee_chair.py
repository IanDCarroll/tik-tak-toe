import unittest
from source.referee_chair import *
from source.player_chair import *
from source.game_table import * 

class RefereeTestCase(unittest.TestCase):

    def setUp(self):
        self.table_top = TableTop()
        self.tied_board = [1,1,10, 10,10,1, 1,10,1]
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
        referee = Referee('fake_board','fake_P1', 'fake_p2')
        self.assertEqual(isinstance(referee, object), True)

    def test_check_for_draw_returns_true(self):
        self.table_top.board = self.tied_board
        ref = Referee(self.table_top, 'P1', 'P2')
        self.assertEqual(ref.check_for_tie(), True)

    def test_check_for_draw_returns_false(self):
        self.table_top.board = self.false_board
        ref = Referee(self.table_top, 'P1', 'P2')
        self.assertEqual(ref.check_for_tie(), False)

    def test_check_for_winner_returns_false(self):
        self.table_top.board = self.false_board
        ref = Referee(self.table_top, 'P1', 'P2')
        self.assertEqual(ref.check_for_winner(), False)

    def test_check_for_winner_does_edges(self):
        self.table_top.board = self.edge_board
        ref = Referee(self.table_top, 'P1', 'P2')
        self.assertEqual(ref.check_for_winner(), True)

    def test_check_for_winner_does_columns(self):
        self.table_top.board = self.column_board
        ref = Referee(self.table_top, 'P1', 'P2')
        self.assertEqual(ref.check_for_winner(), True)

    def test_check_for_winner_does_rows(self):
        self.table_top.board = self.row_board
        ref = Referee(self.table_top, 'P1', 'P2')
        self.assertEqual(ref.check_for_winner(), True)

    def test_check_for_winner_does_diagonals(self):
        self.table_top.board = self.diagonal_board
        ref = Referee(self.table_top, 'P1', 'P2')
        self.assertEqual(ref.check_for_winner(), True)

    def test_get_board_size_3(self):
        ref = Referee(self.table_top, 'p1', 'p2')
        self.assertEqual(ref.get_board_size(self.table_top.board), 3)

    def test_get_board_size_4(self):
        self.table_top.board = self.mock_4x4_board
        ref = Referee(self.table_top, 'p1', 'p2')
        self.assertEqual(ref.get_board_size(self.table_top.board), 4)

    def test_prep_next_turn_toggles_players(self):
        bender = Computer()
        fry = Human()
        ref = Referee(self.table_top, bender, fry)
        self.assertEqual(ref.whos_turn, bender)
        ref.prep_next_turn()
        self.assertEqual(ref.whos_turn, fry)
        ref.prep_next_turn()
        self.assertEqual(ref.whos_turn, bender)

    def test_get_win_list_returns_the_3x3_wins(self):
        ref = Referee(self.table_top, 'P1', 'P2')
        expected = self.win_list_3x3
        self.assertEqual(ref.get_win_list(), expected)

    def test_get_win_list_returns_the_4x4_wins(self):
        self.table_top.board = self.mock_4x4_board
        expected = self.win_list_4x4
        ref = Referee(self.table_top, 'P1', 'P2')
        self.assertEqual(ref.get_win_list(), expected)

if __name__ == '__main__':
     unittest.main()
