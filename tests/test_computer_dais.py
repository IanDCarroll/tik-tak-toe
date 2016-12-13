import unittest
from OnStage.computer_dais import *

class ComputerTestCase(unittest.TestCase):

    def setUp(self):
        self.hal = Computer(1)
        self.win_chance = [10,10,0, 0,0,0, 0,1,1]
        self.loose_chance = [10,0,1, 0,1,0, 10,0,0]
        self.empty_board = [0,0,0, 0,0,0, 0,0,0]
        self.hollow_board = [1,10,0, 0,0,0, 10,1,0]
        self.NE_corner = [0,0,10, 0,1,0, 0,0,0]
        self.center_board = [10,0,0, 1,1,10, 10,0,1]
        self.diagon_board = [10,0,1, 1,1,10, 10,0,1]

        self.win = [10,10,0, 0,0,0, 1,1,1]
        self.dont_loose = [10,0,1, 1,1,0, 10,0,0]
        self.no_win_chance = [10,0,0, 0,1,0, 0,0,0]
        self.fill_center = [0,0,0, 0,1,0, 0,0,0]
        self.fill_hollows = [1,10,0, 0,1,0, 10,1,0]
        self.catty_corner = [0,0,10, 0,1,0, 1,0,0]
        self.fill_corners = [10,0,1, 1,1,10, 10,0,1]
        self.fill_whatevs = [10,1,1, 1,1,10, 10,0,1]

    def test_computer_chooses_to_win(self):
        test_yields = self.hal.move(self.win_chance)
        self.assertEqual(test_yields, self.win)

    def test_computer_doesnt_let_you_win(self):
        test_yields = self.hal.move(self.loose_chance)
        self.assertEqual(test_yields, self.dont_loose)

    def test_computer_prefers_the_center_to_all_else(self):
        test_yields = self.hal.move(self.empty_board)
        self.assertEqual(test_yields, self.fill_center)
        test_yields = self.hal.move(self.hollow_board)
        self.assertEqual(test_yields, self.fill_hollows)

    def test_computer_prefers_oposite_corner_to_other_corners(self):
        test_yields = self.hal.move(self.NE_corner)
        self.assertEqual(test_yields, self.catty_corner)

    def test_computer_prefers_corners_to_edges(self):
        test_yields = self.hal.move(self.center_board)
        self.assertEqual(test_yields, self.fill_corners)

    def test_computer_will_choose_edges_as_a_last_resort(self):
        test_yields = self.hal.move(self.diagon_board)
        self.assertEqual(test_yields, self.fill_whatevs)
