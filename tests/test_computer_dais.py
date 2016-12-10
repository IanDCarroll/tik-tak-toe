import unittest
from OnStage.computer_dais import *

class ComputerTestCase(unittest.TestCase):

    def setUp(self):
        self.hal = Computer(1)
        self.hollow_board = [1,10,0, 0,0,0, 10,1,0]
        self.center_board = [10,0,0, 0,1,0, 10,0,1]
        self.diagon_board = [10,0,1, 1,1,10, 10,0,1]

        self.fill_hollows = [1,10,0, 0,1,0, 10,1,0]
        self.catty_corner = [0,0,10, 0,1,0, 1,0,0]
        self.fill_corners = [10,0,1, 0,1,0, 10,0,1]
        self.fill_whatevs = [10,1,1, 1,1,10, 10,0,1]

        self.open_4 = [0,0,0, 0,0,0, 0,0,0]
        self.open_0 = [0,0,0, 0,1,0, 0,0,0]
        self.open_2 = [1,0,0, 0,1,0, 0,0,0]
        self.open_6 = [1,0,1, 0,1,0, 0,0,0]
        self.open_8 = [1,0,1, 0,1,0, 1,0,0]
        self.open_1 = [1,0,1, 0,1,0, 1,0,1]
        self.open_3 = [1,1,1, 0,1,0, 1,0,1]
        self.open_5 = [1,1,1, 1,1,0, 1,0,1]
        self.open_7 = [1,1,1, 1,1,1, 1,0,1]

        self.NW_corner_x = [10,0,0, 0,1,0, 0,0,0]
        self.NW_corner_o = [1,0,0, 0,10,0, 0,0,0]
        self.NE_corner = [0,0,10, 0,1,0, 0,0,0]
        self.SW_corner = [0,0,0, 0,1,0, 10,0,0]
        self.SE_corner = [0,0,0, 0,1,0, 0,0,10]

    def test_computer_prefers_the_center_to_all_else(self):
        test_yields = self.hal.move(self.open_4)
        self.assertEqual(test_yields, self.open_0)
        test_yields = self.hal.move(self.hollow_board)
        self.assertEqual(test_yields, self.fill_hollows)

    def test_computer_prefers_oposite_corner_to_other_corners(self):
        test_yields = self.hal.move(self.NE_corner)
        self.assertEqual(test_yields, self.caddy_corner)

    def test_computer_prefers_corners_to_edges(self):
        test_yields = self.hal.move(self.center_board)
        self.assertEqual(test_yields, self.fill_corners)

    def test_computer_will_choose_edges_as_a_last_resort(self):
        test_yields = self.hal.move(self.diagon_board)
        self.assertEqual(test_yields, self.fill_whatevs)

    def test_take_center_chooses_center(self):
        test_yields = self.hal.take_the_center(self.open_4)
        self.assertEqual(test_yields, 4)

    def test_take_center_returns_false_if_taken(self):
        test_yields = self.hal.take_the_center(self.open_0)
        self.assertEqual(test_yields, False)

    def test_make_default_choice_chooses_NW_after_center(self):
        test_yields = self.hal.make_default_choice(self.open_0)
        self.assertEqual(test_yields, 0)

    def test_make_default_choice_chooses_NE_after_NW(self):
        test_yields = self.hal.make_default_choice(self.open_2)
        self.assertEqual(test_yields, 2)

    def test_make_default_choice_chooses_SW_after_NE(self):
        test_yields = self.hal.make_default_choice(self.open_6)
        self.assertEqual(test_yields, 6)

    def test_make_default_choice_chooses_SE_after_SW(self):
        test_yields = self.hal.make_default_choice(self.open_8)
        self.assertEqual(test_yields, 8)

    def test_make_default_choice_chooses_N_after_SW(self):
        test_yields = self.hal.make_default_choice(self.open_1)
        self.assertEqual(test_yields, 1)

    def test_make_default_choice_chooses_W_after_N(self):
        test_yields = self.hal.make_default_choice(self.open_3)
        self.assertEqual(test_yields, 3)

    def test_make_default_choice_chooses_E_after_W(self):
        test_yields = self.hal.make_default_choice(self.open_5)
        self.assertEqual(test_yields, 5)

    def test_make_default_choice_chooses_S_last(self):
        test_yields = self.hal.make_default_choice(self.open_7)
        self.assertEqual(test_yields, 7)
