import unittest
from OnStage.game_table import * 

class TableTopTestCase(unittest.TestCase):

    def setUp(self):
        self.table_top = TableTop()
        self.empty_board = [0,0,0, 0,0,0, 0,0,0]
        self.changed_board = [0,0,1, 0,0,0, 0,0,0] 

    def test_that_board_returns_a_list(self):
        self.assertEqual(isinstance(self.table_top.board, list), True)

    def test_the_boards_initial_state(self):
        self.assertEqual(self.table_top.board, self.empty_board)

    def test_that_board_can_be_changed(self):
        self.table_top.board = self.changed_board
        self.assertEqual(self.table_top.board, self.changed_board)

if __name__ == '__main__':
    unittest.main()
