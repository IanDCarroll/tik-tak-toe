import unittest
from BackStage.judge_pit import *
from OnStage.game_table import *

class JudgeTestCase(unittest.TestCase):

    def setUp(self):
        self.ui_stub = "ui"
        self.table_top = TableTop(self.ui_stub)
        self.judge = Judge(self.table_top)
        self.mock_no_win_board = [1,10,1, 0,10,0, 1,0,10]
        self.mock_p1_win_board = [1,10,1, 1,10,0, 1,0,10]
        self.mock_p2_win_board = [10,1,10, 1,10,1, 10,0,1]

    def test_check_for_winner_returns_no_winner(self):
        self.table_top.board = self.mock_no_win_board
        test_yields = self.judge.check_for_winner()
        self.assertEqual(test_yields, False)

    def test_check_for_winner_returns_computer_p1_win(self):
        self.table_top.give_computer_the_first_move()
        self.table_top.board = self.mock_p1_win_board
        self.table_top.give_next_player_a_go() # sim sideEffect
        test_yields = self.judge.check_for_winner()
        self.assertEqual(test_yields, 'computer')

    def test_check_for_winner_returns_computer_p2_win(self):
        self.table_top.give_computer_the_first_move()
        self.table_top.board = self.mock_p2_win_board
        test_yields = self.judge.check_for_winner()
        self.assertEqual(test_yields, 'human')

    def test_check_for_winner_returns_human_p1_win(self):
        self.table_top.board = self.mock_p1_win_board
        self.table_top.give_next_player_a_go() # sim sideEffect
        test_yields = self.judge.check_for_winner()
        self.assertEqual(test_yields, 'human')

    def test_check_for_winner_returns_human_p2_win(self):
        self.table_top.board = self.mock_p2_win_board
        test_yields = self.judge.check_for_winner()
        self.assertEqual(test_yields, 'computer')
