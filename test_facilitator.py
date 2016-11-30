import unittest
from facilitator_credentials import *

class FacilitatorTestCase(Unittest.TestCase):

    def setUp(self):
        faclilitator = Facilitator()
        mock_board = [1,0,10, 1,10,0, 1,10,1]
        expected_analysis = [11,11,12,3,20,11,12,21]

    def test_scan_board_returns_analyzed_list(self):
        test_yields = self.facilitator.scan_board(self.mock_board)
        self.assertEqual(test_yields, self.expected_analysis)
