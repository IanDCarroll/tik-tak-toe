from source.judge_pit import *

class JudgeTestCase(unittest.TestCase):

    def setUp(self):
        self.human_1st_board = TableTop()
        self.computer_1st_board = TableTop()
        self.computer_1st_board.give_computer_the_first_move()
        self.human_1st_judge = Judge(self.human_1st_board)
        self.computer_1st_judge = Judge(self.computer_1st_board)

    def test_check_for_winner_returns_no_winner(self):
        pass

    def test_check_for_winner_returns_computer_p1_win(self):
        pass

    def test_check_for_winner_returns_computer_p2_win(self):
        pass

    def test_check_for_winner_returns_human_p1_win(self):
        pass

    def test_check_for_winner_returns_human_p2_win(self):
        pass
