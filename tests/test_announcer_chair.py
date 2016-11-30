import unittest
from source.announcer_chair import *

class AnnouncerTestCase(unittest.TestCase):

    def setUp(self):
        self.announcer = Announcer()
        self.start = "Welcome to XOX, a Noughts and Crosses Game"
        self.select = "Type 1 to go first, or 2 to go second."
        self.tie = "The game is a draw."
        self.computer = "The Computer wins the game."
        self.human = "You Win!"
        self.question = "Which square do you choose?"
        self.bad_move = "Sorry, that's not a legal move. Try again."
        self.nought = " O "
        self.cross = " X "
        self.mock_board = [1,10,1, 0,10,0, 1,0,10]
        self.rendered_board = """
 X \033[0m| O \033[0m| X \033[0m
---+---+---
 4 \033[0m| O \033[0m| 6 \033[0m
---+---+---
 X \033[0m| 8 \033[0m| O \033[0m
"""

    def test_display_start_of_game(self):
        self.assertEqual(self.announcer.start, self.start)

    def test_display_select_go_first_or_not(self):
        self.assertEqual(self.announcer.select, self.select)

    def test_display_game_over_tie(self):
        self.assertEqual(self.announcer.tie, self.tie)

    def test_display_game_over_computer_wins(self):
        self.assertEqual(self.announcer.computer, self.computer)

    def test_display_game_over_human_wins(self):
        self.assertEqual(self.announcer.human, self.human)

    def test_display_question_the_human(self):
        self.assertEqual(self.announcer.question, self.question)

    def test_display_human_made_illegal_move(self):
        self.assertEqual(self.announcer.bad_move, self.bad_move)

    def test_display_nought(self):
        self.assertEqual(self.announcer.nought, self.nought)

    def test_display_cross(self):
        self.assertEqual(self.announcer.cross, self.cross)

    def test_announcer_has_get_board_size(self):
        self.assertEqual(hasattr(self.announcer, 'get_board_size'), True)

    def test_display_current_board(self):
        test = self.announcer.render_board(self.mock_board)
        self.assertEqual(test, self.rendered_board)

if __name__ == '__main__':
    unittest.main()
