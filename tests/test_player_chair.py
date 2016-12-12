import unittest
from OnStage.player_chair import *
from OnStage.computer_dais import *

class Dummy(Human):
      def choose(self, board):
          return 3

class PlayerTestCase(unittest.TestCase):

    def setUp(self):
        self.player = Player(1)
        self.computer = Computer(1)
        self.human = Dummy(10)
        self.mock_board = [1,10,1, 0,10,0, 1,0,10]
        self.computer_turn = [1,10,1, 1,10,0, 1,0,10]
        self.human_turn = [1,10,1, 10,10,0, 1,0,10]

    def test_that_player_can_only_make_legal_moves(self):
        test = self.player.get_legal_moves(self.mock_board)
        self.assertEqual(test, [3,5,7])

    def test_that_computer_player_can_make_a_move(self):
        test = self.computer.move(self.mock_board)
        self.assertEqual(test, self.computer_turn)

    def test_that_human_can_make_a_move(self):
        test = self.human.move(self.mock_board)
        self.assertEqual(test, self.human_turn)

    def test_that_human_can_only_make_legal_moves(self):
        test = self.human.check_conscience(7, self.mock_board)
        self.assertEqual(test, None)

    def test_that_check_consience_flags_bad_moves(self):
        test = self.human.check_conscience(4, self.mock_board)
        self.assertEqual(test, True)

    def test_human_id_says_human(self):
        self.assertEqual(self.human.name, 'human')

    def test_computer_id_says_computer(self):
        self.assertEqual(self.computer.name, 'computer')

    def test_get_enemy_code_gets_enemy_code(self):
        self.assertEqual(self.computer.get_enemy_code(), 10)
        self.assertEqual(self.human.get_enemy_code(), 1)

if __name__ == '__main__':
    unittest.main()
