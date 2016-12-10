import unittest
from OnStage.computer_dais import *

class ComputerTestCase(unittest.TestCase):

    def setUp(self):
        self.hal = Computer(1)
        self.empty_board = [0,0,0, 0,0,0, 0,0,0]
        self.hollow_board = [1,10,0, 0,0,0, 10,1,0]
        self.center_board = [10,0,0, 0,1,0, 10,0,1]
        self.diagon_board = [10,0,1, 1,1,10, 10,0,1]

        self.fill_center = [0,0,0, 0,1,0, 0,0,0]
        self.fill_hollows = [1,10,0, 0,1,0, 10,1,0]
        self.catty_corner = [0,0,10, 0,1,0, 1,0,0]
        self.fill_corners = [10,0,1, 0,1,0, 10,0,1]
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



    def test_take_center_chooses_center(self):
        test_yields = self.hal.take_the_center(self.open_4)
        self.assertEqual(test_yields, 4)

    def test_take_center_returns_false_if_taken(self):
        test_yields = self.hal.take_the_center(self.open_0)
        self.assertEqual(test_yields, False)



    def test_take_catty_corner_chooses_the_SE_corner(self):
        options = self.hal.get_legal_moves(self.NW_corner_x)
        test = self.hal.take_catty_corner(options, self.NW_corner_x)
        self.assertEqual(test, 8)

    def test_take_catty_corner_cares_whos_at_center(self): 
        options = self.hal.get_legal_moves(self.NW_corner_o)
        test = self.hal.take_catty_corner(options, self.NW_corner_o)
        self.assertEqual(test, False)

    def test_take_catty_corner_chooses_the_SW_corner(self):
        options = self.hal.get_legal_moves(self.NE_corner)
        test = self.hal.take_catty_corner(options, self.NE_corner)
        self.assertEqual(test, 6)

    def test_take_catty_corner_chooses_the_NE_corner(self):
        options = self.hal.get_legal_moves(self.SW_corner)
        test = self.hal.take_catty_corner(options, self.SW_corner)
        self.assertEqual(test, 2)

    def test_take_catty_corner_chooses_the_NW_corner(self):
        options = self.hal.get_legal_moves(self.SE_corner)
        test = self.hal.take_catty_corner(options, self.SE_corner)
        self.assertEqual(test, 0)

    def test_take_catty_corner_returns_false_otherwise(self):
        options = self.hal.get_legal_moves(self.no_corner)
        test = self.hal.take_catty_corner(options, self.no_corner)
        self.assertEqual(test, False)



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
