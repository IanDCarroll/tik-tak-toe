import unittest
from source.facilitator_credentials import *

class FacilitatorTestCase(unittest.TestCase):

    def setUp(self):
        self.facilitator = Facilitator()
        self.mock_board = [1,0,10, 1,10,0, 1,10,1]
        self.expected_analysis = [11,11,12, 3,20,11, 12,21]
        self.expected_rows = [11,11,12]
        self.expected_cols = [3,20,11]

    def test_scan_board_returns_analyzed_list(self):
        test_yields = self.facilitator.scan_board(self.mock_board)
        self.assertEqual(test_yields, self.expected_analysis)

    def test_scan_rows_returns_analyzed_list(self):
        test_yields = self.facilitator.scan_rows(self.mock_board)
        self.assertEqual(test_yields, self.expected_rows)

    def test_scan_cols_returns_analyzed_list(self):
        test_yields = self.facilitator.scan_cols(self.mock_board)
        self.assertEqual(test_yields, self.expected_cols)

if __name__ == '__main__':
    unittest.main()
