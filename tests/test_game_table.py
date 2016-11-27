import unittest
from source.game_table import * 

class TableTopTestCase(unittest.TestCase):

    def test_that_board_returns_a_list(self):
        table_top = TableTop()
        test = isinstance(table_top.board, list)
        self.assertEqual(test, True)

    def test_the_boards_initial_state(self):
        table_top = TableTop()
        expected = [0,0,0, 0,0,0, 0,0,0]
        self.assertEqual(table_top.board, expected)

    def test_that_board_can_be_changed(self):
        table_top = TableTop()
        expected = [0,0,1, 0,0,0, 0,0,0]
        table_top.board = expected
        self.assertEqual(table_top.board, expected)

if __name__ == '__main__':
    unittest.main()
