import unittest
from source.announcer_chair import *

class AnnouncerTestCase(unittest.TestCase):

    def setUp(self):
        self.announcer = Announcer()
        self.start = "Welcome"
        self.tie = "Draw"
        self.computer = "Computer Wins"
        self.human = "You Win"
        self.next_move = "What is your next move?"
        self.bad_move = "That is not a legal move."
        self.mock_board = [1,10,1, 0,10,0, 1,0,10]
        self.rendered_board = """
 X | O | X 
---+---+---
 4 | O | 6 
---+---+---
 X | 8 | O 
"""

    def test_display_start_of_game(self):
        self.assertEqual(self.announcer.start, self.start)

    def test_display_game_over_tie(self):
        self.assertEqual(self.announcer.tie, self.tie)

    def test_display_game_over_computer_wins(self):
        self.assertEqual(self.announcer.computer, self.computer)

    def test_display_game_over_human_wins(self):
        self.assertEqual(self.announcer.human, self.human)

    def test_display_ask_for_human_input(self):
        self.assertEqual(self.announcer.next_move, self.next_move)

    def test_display_human_made_illegal_move(self):
        self.assertEqual(self.announcer.bad_move, self.bad_move)

    def test_display_current_board(self):
        test = self.announcer.render_board(self.mock_board)
        self.assertEqual(test, self.rendered_board)


if __name__ == '__main__':
    unittest.main()
