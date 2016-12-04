import unittest
from source.judge_pit import *
from source.game_table import *

class JudgeTestCase(unittest.TestCase):

    def setUp(self):
        self.human_1st_board = TableTop()
        self.computer_1st_board = TableTop()
        self.computer_1st_board.give_computer_the_first_move()
        self.human_1st_judge = Judge(self.human_1st_board)
        self.computer_1st_judge = Judge(self.computer_1st_board)
        self.mock_no_win_board = [1,10,1, 0,10,0, 1,0,10]

    def test_check_for_winner_returns_no_winner(self):
        self.human_1st_board.board = self.mock_no_win_board
        test_yields = self.human_1st_judge.check_for_winner()
        self.assertEqual(test_yields, False)

    def test_check_for_winner_returns_computer_p1_win(self):
        pass

    def test_check_for_winner_returns_computer_p2_win(self):
        pass

    def test_check_for_winner_returns_human_p1_win(self):
        pass

    def test_check_for_winner_returns_human_p2_win(self):
        pass
