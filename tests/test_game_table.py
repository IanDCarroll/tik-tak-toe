import unittest
from source.game_table import * 

class TableTopTestCase(unittest.TestCase):

    def setUp(self):
        self.table_top = TableTop()
        self.empty_board = [0,0,0, 0,0,0, 0,0,0]
        self.changed_board = [0,0,1, 0,0,0, 0,0,0] 

    def test_that_board_returns_a_list(self):
        test = isinstance(self.table_top.board, list)
        self.assertEqual(test, True)

    def test_the_boards_initial_state(self):
        expected = self.empty_board
        self.assertEqual(self.table_top.board, expected)

    def test_that_board_can_be_changed(self):
        expected = self.changed_board
        self.table_top.board = self.changed_board
        self.assertEqual(self.table_top.board, expected)

if __name__ == '__main__':
    unittest.main()
