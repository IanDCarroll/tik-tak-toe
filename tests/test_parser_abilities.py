import unittest
from OnStage.parser_abilities import *

class ParserTestCase(unittest.TestCase):

    def setUp(self):
        self.test = Parser()
        self.row_0 = [0,1,2]
        self.row_1 = [3,4,5]
        self.row_2 = [6,7,8]
        self.col_3 = [0,3,6]
        self.col_4 = [1,4,7]
        self.col_5 = [2,5,8]
        self.diag6 = [0,4,8]
        self.diag7 = [2,4,6]

    def test_get_empty_square_gets_an_empty_square(self):
        test_yields = self.test.get_empty_square(self.col_4, 1)
        self.assertEqual(test_yields, 4)

    def test_find_empty_spot_returns_0(self):
        test_1 = self.test.find_empty_spot(self.col_3, self.row_0)
        test_2 = self.test.find_empty_spot(self.row_0, self.col_3)
        test_3 = self.test.find_empty_spot(self.col_3, self.diag6)
        self.assertEqual(test_1, 0)
        self.assertEqual(test_2, 0)
        self.assertEqual(test_3, 0)

    def test_find_empty_spot_returns_1(self):
        test_1 = self.test.find_empty_spot(self.col_4, self.row_0)
        test_2 = self.test.find_empty_spot(self.row_0, self.col_4)
        self.assertEqual(test_1, 1)
        self.assertEqual(test_2, 1)

    def test_find_empty_spot_returns_2(self):
        test_1 = self.test.find_empty_spot(self.col_5, self.row_0)
        test_2 = self.test.find_empty_spot(self.row_0, self.col_5)
        test_3 = self.test.find_empty_spot(self.col_5, self.diag7)
        self.assertEqual(test_1, 2)
        self.assertEqual(test_2, 2)
        self.assertEqual(test_3, 2)

    def test_find_empty_spot_returns_3(self):
        test_1 = self.test.find_empty_spot(self.col_3, self.row_1)
        test_2 = self.test.find_empty_spot(self.row_1, self.col_3)
        self.assertEqual(test_1, 3)
        self.assertEqual(test_2, 3)

    def test_find_empty_spot_returns_4(self):
        test_1 = self.test.find_empty_spot(self.col_4, self.row_1)
        test_2 = self.test.find_empty_spot(self.row_1, self.col_4)
        test_3 = self.test.find_empty_spot(self.diag7, self.diag6)
        test_4 = self.test.find_empty_spot(self.diag6, self.diag7)
        self.assertEqual(test_1, 4)
        self.assertEqual(test_2, 4)
        self.assertEqual(test_3, 4)
        self.assertEqual(test_4, 4)

    def test_find_empty_spot_returns_5(self):
        test_1 = self.test.find_empty_spot(self.col_5, self.row_1)
        test_2 = self.test.find_empty_spot(self.row_1, self.col_5)
        self.assertEqual(test_1, 5)
        self.assertEqual(test_2, 5)

    def test_find_empty_spot_returns_6(self):
        test_1 = self.test.find_empty_spot(self.col_3, self.row_2)
        test_2 = self.test.find_empty_spot(self.row_2, self.col_3)
        test_3 = self.test.find_empty_spot(self.col_3, self.diag7)
        self.assertEqual(test_1, 6)
        self.assertEqual(test_2, 6)
        self.assertEqual(test_3, 6)

    def test_find_empty_spot_returns_7(self):
        test_1 = self.test.find_empty_spot(self.col_4, self.row_2)
        test_2 = self.test.find_empty_spot(self.row_2, self.col_4)
        self.assertEqual(test_1, 7)
        self.assertEqual(test_2, 7)

    def test_find_empty_spot_returns_8(self):
        test_1 = self.test.find_empty_spot(self.col_5, self.row_2)
        test_2 = self.test.find_empty_spot(self.row_2, self.col_5)
        test_3 = self.test.find_empty_spot(self.col_5, self.diag6)
        self.assertEqual(test_1, 8)
        self.assertEqual(test_2, 8)
        self.assertEqual(test_3, 8)
