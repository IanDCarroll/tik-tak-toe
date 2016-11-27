import unittest
from source.player_chair import *

class PlayerTestCase(unittest.TestCase):

    def setUp(self):
        self.mock_board = [1,10,1, 0,10,0, 1,0,10]

    def test_that_player_can_only_make_legal_moves(self):
        philip = Player()
        mock_board = self.mock_board
        test = philip.get_legal_moves(mock_board)
        self.assertEqual(test, [3,5,7])

    def test_that_computer_player_can_make_a_move(self):
        spamBot9000 = Computer()
        mock_board = self.mock_board
        test = spamBot9000.move(mock_board)
        self.assertEqual(test, [1,10,1, 1,10,0, 1,0,10])

    def test_that_human_can_only_make_legal_moves(self):
        bernice = Human()
        mock_board = self.mock_board
        test_true = bernice.check_conscience(7, mock_board)
        self.assertEqual(test_true, None)

if __name__ == '__main__':
    unittest.main()
