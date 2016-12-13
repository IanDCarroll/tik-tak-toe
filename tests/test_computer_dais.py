import unittest
from OnStage.computer_dais import *

class ComputerTestCase(unittest.TestCase):

    def setUp(self):
        self.hal = Computer(1)
        self.empty_board = [0,0,0, 0,0,0, 0,0,0]
        self.hollow_board = [1,10,0, 0,0,0, 10,1,0]
        self.center_board = [10,0,0, 1,1,10, 10,0,1]
        self.diagon_board = [10,0,1, 1,1,10, 10,0,1]

        self.fill_center = [0,0,0, 0,1,0, 0,0,0]
        self.fill_hollows = [1,10,0, 0,1,0, 10,1,0]
        self.catty_corner = [0,0,10, 0,1,0, 1,0,0]
        self.fill_corners = [10,0,1, 1,1,10, 10,0,1]
        self.fill_whatevs = [10,1,1, 1,1,10, 10,0,1]

        self.open_4 = [0,1,2, 3,4,5, 6,7,8]
        self.open_0 = [0,1,2, 3,  5, 6,7,8]
        self.open_2 = [  1,2, 3,  5, 6,7,8]
        self.open_6 = [  1,   3,  5, 6,7,8]
        self.open_8 = [  1,   3,  5,   7,8]
        self.open_1 = [  1,   3,  5,   7  ]
        self.open_3 = [       3,  5,   7  ]
        self.open_5 = [           5,   7  ]
        self.open_7 = [                7  ]

        self.NW_corner_x = [10,0,0, 0,1,0, 0,0,0]
        self.NW_corner_o = [1,0,0, 0,10,0, 0,0,0]
        self.NE_corner = [0,0,10, 0,1,0, 0,0,0]
        self.SW_corner = [0,0,0, 0,1,0, 10,0,0]
        self.SE_corner = [0,0,0, 0,1,0, 0,0,10]
        self.no_corner = [1,10,0, 0,1,0, 0,0,10]

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
