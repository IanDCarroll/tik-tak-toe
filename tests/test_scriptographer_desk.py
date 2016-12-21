import unittest
from Scenery.scriptographer_desk import *

class ScriptographerTestCase(unittest.TestCase):

    def setUp(self):
        self.say = Scriptographer()
        self.start = "Welcome to XOX, a Noughts and Crosses Game"
        self.select = "Type 1 to go first, or 2 to go second."
        self.tie = "The game is a draw."
        self.computer = "The Computer wins the game."
        self.human = "You Win!"
        self.question = "Which square do you choose?"
        self.bad_move = "Sorry, that's not a legal move. Try again."
        self.strike_3 = "Look, if you're not going to take this seriously, I'm out."
        self.prompt = "> "

        self.nought = "\033[34m O \033[0m"
        self.cross = "\033[91m X \033[0m"
        self.pre_num = "\033[30m "
        self.post_num = " \033[0m"
        self.plank = '---'
        self.corner = '+'
        self.wall = '|'
        self.nl = '\n'

    def test_say_start_of_game(self):
        self.assertEqual(self.say.start, self.start)

    def test_say_select_go_first_or_not(self):
        self.assertEqual(self.say.select, self.select)

    def test_say_game_over_tie(self):
        self.assertEqual(self.say.tie, self.tie)

    def test_say_game_over_computer_wins(self):
        self.assertEqual(self.say.computer, self.computer)

    def test_say_game_over_human_wins(self):
        self.assertEqual(self.say.human, self.human)

    def test_say_question_the_human(self):
        self.assertEqual(self.say.question, self.question)

    def test_say_human_made_illegal_move(self):
        self.assertEqual(self.say.bad_move, self.bad_move)

    def test_say_strike_3(self):
        self.assertEqual(self.say.strike_3, self.strike_3)

    def test_provide_prompt_for_raw_input(self):
        self.assertEqual(self.say.prompt, self.prompt)

    def test_provide_nought(self):
        self.assertEqual(self.say.nought, self.nought)

    def test_provide_cross(self):
        self.assertEqual(self.say.cross, self.cross)

    def test_provide_before_num(self):
        self.assertEqual(self.say.pre_num, self.pre_num)

    def test_provide_after_num(self):
        self.assertEqual(self.say.post_num, self.post_num)

    def test_provide_plank(self):
        self.assertEqual(self.say.plank, self.plank)

    def test_provide_corner(self):
        self.assertEqual(self.say.corner, self.corner)

    def test_provide_wall(self):
        self.assertEqual(self.say.wall, self.wall)

    def test_provide_new_line(self):
        self.assertEqual(self.say.nl, self.nl)

if __name__ == '__main__':
    unittest.main()
