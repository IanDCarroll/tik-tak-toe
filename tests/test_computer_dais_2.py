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
        self.row_0 = [0,1,2]
        self.row_1 = [3,4,5]
        self.row_2 = [6,7,8]
        self.col_3 = [0,3,6]
        self.col_4 = [1,4,7]
        self.col_5 = [2,5,8]

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

    def test_parse_analysis_returns_0(self):
        test_1 = self.hal.parse_analysis(self.col_3, 0)
        test_2 = self.hal.parse_analysis(self.row_0, 3)
        test_3 = self.hal.parse_analysis(self.row_0, 6)
        self.assertEqual(test_1, 0)
        self.assertEqual(test_2, 0)
        self.assertEqual(test_3, 0)

    def test_parse_analysis_returns_1(self):
        test_1 = self.hal.parse_analysis(self.col_4, 0)
        test_2 = self.hal.parse_analysis(self.row_0, 4)
        self.assertEqual(test_1, 1)
        self.assertEqual(test_2, 1)

    def test_parse_analysis_returns_2(self):
        test_1 = self.hal.parse_analysis(self.col_5, 0)
        test_2 = self.hal.parse_analysis(self.row_0, 5)
        test_3 = self.hal.parse_analysis(self.row_0, 7)
        self.assertEqual(test_1, 2)
        self.assertEqual(test_2, 2)
        self.assertEqual(test_3, 2)

    def test_parse_analysis_returns_3(self):
        test_1 = self.hal.parse_analysis(self.col_3, 1)
        test_2 = self.hal.parse_analysis(self.row_1, 3)
        self.assertEqual(test_1, 3)
        self.assertEqual(test_2, 3)

    def test_parse_analysis_returns_4(self):
        test_1 = self.hal.parse_analysis(self.col_4, 1)
        test_2 = self.hal.parse_analysis(self.row_1, 4)
        test_3 = self.hal.parse_analysis(self.col_4, 6)
        test_4 = self.hal.parse_analysis(self.row_1, 7)
        self.assertEqual(test_1, 4)
        self.assertEqual(test_2, 4)
        self.assertEqual(test_3, 4)
        self.assertEqual(test_4, 4)

    def test_parse_analysis_returns_5(self):
        test_1 = self.hal.parse_analysis(self.col_5, 1)
        test_2 = self.hal.parse_analysis(self.row_1, 5)
        self.assertEqual(test_1, 5)
        self.assertEqual(test_2, 5)

    def test_parse_analysis_returns_6(self):
        test_1 = self.hal.parse_analysis(self.col_3, 2)
        test_2 = self.hal.parse_analysis(self.row_2, 3)
        test_3 = self.hal.parse_analysis(self.row_2, 7)
        self.assertEqual(test_1, 6)
        self.assertEqual(test_2, 6)
        self.assertEqual(test_3, 6)

    def test_parse_analysis_returns_7(self):
        test_1 = self.hal.parse_analysis(self.col_4, 2)
        test_2 = self.hal.parse_analysis(self.row_2, 4)
        self.assertEqual(test_1, 7)
        self.assertEqual(test_2, 7)

    def test_parse_analysis_returns_8(self):
        test_1 = self.hal.parse_analysis(self.col_5, 2)
        test_2 = self.hal.parse_analysis(self.row_2, 5)
        test_3 = self.hal.parse_analysis(self.row_2, 6)
        self.assertEqual(test_1, 8)
        self.assertEqual(test_2, 8)
        self.assertEqual(test_3, 8)
