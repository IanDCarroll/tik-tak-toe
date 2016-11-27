import unittest
from source.referee_chair import *
from source.player_chair import *
from source.game_table import * 

class RefereeTestCase(unittest.TestCase):

    def setUp(self):
        self.tied_board = [1,1,10, 10,10,1, 1,10,1]
        self.false_board = [1,10,1, 0,10,0, 1,0,10]
        self.edge_board = [1,10,1, 1,10,0, 1,0,10]

    def test_referee_is_an_object(self):
        referee = Referee('fake_board','fake_P1', 'fake_p2')
        self.assertEqual(isinstance(referee, object), True)

    def test_check_for_draw_returns_true(self):
        true_top = TableTop()
        true_top.board = self.tied_board
        true_ref = Referee(true_top, 'P1', 'P2')
        self.assertEqual(true_ref.check_for_tie(), True)

    def test_check_for_draw_returns_false(self):
        false_top = TableTop()
        false_top.board = self.false_board
        false_ref = Referee(false_top, 'P1', 'P2')
        self.assertEqual(false_ref.check_for_tie(), False)

    def test_check_for_winner_returns_false(self):
        false_top = TableTop()
        false_top.board = self.false_board
        false_ref = Referee(false_top, 'P1', 'P2')
        self.assertEqual(false_ref.check_for_winner(), False)

    def test_check_for_winner_does_edges(self):
        edge_top = TableTop()
        edge_top.board = self.edge_board
        edge_ref = Referee(edge_top, 'P1', 'P2')
        self.assertEqual(edge_ref.check_for_winner(), True)

    def test_check_for_winner_does_columns(self):
        column_top = TableTop()
        column_top.board = [1,10,1, 0,10,0, 1,10,0]
        column_ref = Referee(column_top, 'P1', 'P2')
        self.assertEqual(column_ref.check_for_winner(), True)

    def test_check_for_winner_does_rows(self):
        row_top = TableTop()
        row_top.board = [1,0,1, 10,10,10 ,0,0,1]
        row_ref = Referee(row_top, 'P1', 'P2')
        self.assertEqual(row_ref.check_for_winner(), True)

    def test_check_for_winner_does_diagonals(self):
        diagonal_top = TableTop()
        diagonal_top.board = [1,10,1, 10,1,0, 1,0,10]
        diagonal_ref = Referee(diagonal_top, 'P1', 'P2')
        self.assertEqual(diagonal_ref.check_for_winner(), True)

    def test_get_board_size_3(self):
        mock_3x3 = TableTop()
        referee = Referee(mock_3x3, 'p1', 'p2')
        self.assertEqual(referee.get_board_size(mock_3x3.board), 3)

    def test_get_board_size_4(self):
        mock_4x4 = TableTop()
        mock_4x4.board = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
        referee = Referee(mock_4x4, 'p1', 'p2')
        self.assertEqual(referee.get_board_size(mock_4x4.board), 4)

    def test_prep_next_turn_toggles_players(self):
        table_top = TableTop()
        bender = Computer()
        fry = Human()
        test_ref = Referee(table_top, bender, fry)
        self.assertEqual(test_ref.whos_turn, bender)
        test_ref.prep_next_turn()
        self.assertEqual(test_ref.whos_turn, fry)
        test_ref.prep_next_turn()
        self.assertEqual(test_ref.whos_turn, bender)

    def test_get_win_list_returns_the_3x3_wins(self):
        top_3x3 = TableTop()
        ref_3x3 = Referee(top_3x3, 'P1', 'P2')
        expected = [[0,1,2], [3,4,5], [6,7,8],
                    [0,3,6], [1,4,7], [2,5,8],
                    [0,4,8], [2,4,6]]
        self.assertEqual(ref_3x3.get_win_list(), expected)

    def test_get_win_list_returns_the_4x4_wins(self):
        top_4x4 = TableTop()
        top_4x4.board = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
        expected = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15],
                    [0,4,8,12], [1,5,9,13], [2,6,10,14], [3,7,11,15],
                    [0,5,10,15],[3,6,9,12]]
        ref_4x4 = Referee(top_4x4, 'P1', 'P2')
        self.assertEqual(ref_4x4.get_win_list(), expected)

if __name__ == '__main__':
     unittest.main()
