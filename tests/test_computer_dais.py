import unittest
from OnStage.computer_dais import *

class ComputerTestCase(unittest.TestCase):

    def setUp(self):
        self.hal = Computer(1)
        self.empty_board = [0,0,0, 0,0,0, 0,0,0]
        self.hollow_board = [1,10,0, 0,0,0, 10,1,0]
        self.center_board = [10,0,0, 0,1,0, 10,0,1]
        self.diagon_board = [10,0,1, 1,1,10, 10,0,1]

        self.take_center = [0,0,0, 0,1,0, 0,0,0]
        self.fill_hollows = [1,10,0, 0,1,0, 10,1,0]
        self.fill_corners = [10,0,1, 0,1,0, 10,0,1]
        self.fill_whatevs = [10,1,1, 1,1,10, 10,0,1]

    def test_the_computer_prefers_the_center_to_all_else(self):
        test_yields = self.hal.move(self.empty_board)
        self.assertEqual(test_yields, self.take_center)
        test_yields = self.hal.move(self.hollow_board)
        self.assertEqual(test_yields, self.fill_hollows)

    def test_the_computer_prefers_corners_to_edges(self):
        pass

    def test_the_computer_will_choose_edges_as_a_last_resort(self):
        pass
