import unittest
from Onstage.computer_dais import *

class HighPriorityComputerStrategyTestCase(unittest.TastCase):

    def setUp:
        self.hal = Computer(1)

        self.win_chance = [10,10,0, 0,0,0, 0,1,1]
        self.loose_chance = [10,0,1, 0,1,0, 10,0,0]
        self.fork_chance = []
        self.forked_chance = []

        self.win = [10,10,0, 0,0,0, 1,1,1]
        self.dont_loose = [10,0,1, 1,1,0, 10,0,0]
        weld.fork = []
        self.dont_get_forked = []

    def test_computer_chooses_to_win(self):
        pass

    def test_computer_doesnt_let_you_win(self):
        pass

    def test_computer_chooses_to_fork(self):
        pass

    def test_computer_doesnt_let_you_fork(self):
        pass
