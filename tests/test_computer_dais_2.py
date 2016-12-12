import unittest
from OnStage.computer_dais import *

class HighPriorityComputerStrategyTestCase(unittest.TestCase):

    def setUp(self):
        self.hal = Computer(1)

        self.win_chance = [10,10,0, 0,0,0, 0,1,1]
        self.loose_chance = [10,0,1, 0,1,0, 10,0,0]

        self.win = [10,10,0, 0,0,0, 1,1,1]
        self.dont_loose = [10,0,1, 1,1,0, 10,0,0]

        self.no_win_chance = [10,0,0, 0,1,0, 0,0,0]

    def test_computer_chooses_to_win(self):
        test_yields = self.hal.move(self.win_chance)
        self.assertEqual(test_yields, self.win)

    def test_computer_doesnt_let_you_win(self):
        test_yields = self.hal.move(self.loose_chance)
        self.assertEqual(test_yields, self.dont_loose)

    def test_take_win_chances_returns_false(self):
        opt = self.hal.get_legal_moves(self.no_win_chance)
        test = self.hal.take_win_chances(opt, self.no_win_chance)
        self.assertEqual(test, False)

    def test_avoid_losing_returns_false(self):
        opt = self.hal.get_legal_moves(self.no_win_chance)
        test = self.hal.avoid_losing(opt, self.no_win_chance)
        self.assertEqual(test, False)
