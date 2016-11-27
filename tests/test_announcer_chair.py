import unittest
from source.announcer_chair import *

class AnnouncerTestCase(unittest.TestCase):

    def test_display_start_of_game(self):
        announcer = Announcer()
        test = announcer.start
        self.assertEqual(test, "Welcome")

    def test_display_game_over_tie(self):
        announcer = Announcer()
        test = announcer.tie
        self.assertEqual(test, "Draw")

    def test_display_game_over_computer_wins(self):
        announcer = Announcer()
        test = announcer.computer
        self.assertEqual(test, "Computer Wins")

    def test_display_game_over_human_wins(self):
        announcer = Announcer()
        test = announcer.human
        self.assertEqual(test, "You Win")

    def test_display_current_board(self):
        announcer = Announcer()
        mock_board = [1,10,1, 0,10,0, 1,0,10]
        test = announcer.render_board(mock_board)
        expected = """
 X | O | X 
---+---+---
 4 | O | 6 
---+---+---
 X | 8 | O 
"""
        self.assertEqual(test, expected)

    def test_display_ask_for_human_input(self):
        announcer = Announcer()
        test = announcer.next_move
        self.assertEqual(test, "What is your next move?")

    def test_display_human_made_illegal_move(self):
        announcer = Announcer()
        test = announcer.bad_move
        self.assertEqual(test, "That is not a legal move.")

if __name__ == '__main__':
    unittest.main()
