import unittest
from OnStage.computer_dais import *

class HighPriorityComputerStrategyTestCase(unittest.TestCase):

    def setUp(self):
        self.hal = Computer(1)

        self.win_chance = [10,10,0, 0,0,0, 0,1,1]
        self.loose_chance = [10,0,1, 0,1,0, 10,0,0]

        self.win = [10,10,0, 0,0,0, 1,1,1]
        self.dont_loose = [10,0,1, 1,1,0, 10,0,0]

    def test_computer_chooses_to_win(self):
        test_yields = self.hal.move(self.win_chance)
        self.assertEqual(test_yields, self.win)

    def test_computer_doesnt_let_you_win(self):
        test_yields = self.hal.move(self.loose_chance)
        self.assertEqual(test_yields, self.dont_loose)
