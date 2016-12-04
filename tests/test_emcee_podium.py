import unittest
from source.emcee_podium import *
from source.announcer_chair import *
from source.game_table import *

class MuteAnnouncer(Announcer):
    def show(self, what_is_said):
        return what_is_said

class Dummy(Emcee):

    def __init__(self, board):
        self.table_top = board
        self.announcer = MuteAnnouncer()

class Mc_Human(Dummy):
    def ask_human(self):
        return '1'

class Mc_Computer(Dummy):
    def ask_human(self):
        return '2'

class Mc_Error(Dummy):
    def ask_human(self):
        return 'Ni!'

class EmceeTestCase(unittest.TestCase):

    def setUp(self):
        self.table_top = TableTop()
        self.signer = MuteAnnouncer()
        self.mc_dummy = Dummy(self.table_top)
        self.mc_human = Mc_Human(self.table_top)
        self.mc_computer = Mc_Computer(self.table_top)
        self.mc_error = Mc_Error(self.table_top)
        self.a_human_p1 = Human(1)
        self.a_human_p2 = Human(10)
        self.a_computer_p1 = Computer(1)
        self.a_computer_p2 = Computer(10)
        self.human_win = 'human'
        self.computer_win = 'computer'
        self.tied_game = 'tie'

    def test_choose_who_goes_first_doesnt_change_players(self):
        self.mc_human.choose_who_goes_first()
        p1_name = self.mc_human.table_top.player1.name
        p1_code = self.mc_human.table_top.player1.marker_code
        p2_name = self.mc_human.table_top.player2.name
        p2_code = self.mc_human.table_top.player2.marker_code
        self.assertEqual(p1_name, self.a_human_p1.name)
        self.assertEqual(p1_code, self.a_human_p1.marker_code)
        self.assertEqual(p2_name, self.a_computer_p2.name)
        self.assertEqual(p2_code, self.a_computer_p2.marker_code)

    def test_choose_who_goes_first_changes_players(self):
        self.mc_computer.choose_who_goes_first()
        p1_name = self.mc_computer.table_top.player1.name
        p1_code = self.mc_computer.table_top.player1.marker_code
        p2_name = self.mc_computer.table_top.player2.name
        p2_code = self.mc_computer.table_top.player2.marker_code
        self.assertEqual(p1_name, self.a_computer_p1.name)
        self.assertEqual(p1_code, self.a_computer_p1.marker_code)
        self.assertEqual(p2_name, self.a_human_p2.name)
        self.assertEqual(p2_code, self.a_human_p2.marker_code)

    def test_get_choice_human_chooses_to_go_first(self):
        self.assertEqual(self.mc_human.get_choice(), '1')

    def test_get_choice_human_chooses_to_go_second(self):
        self.assertEqual(self.mc_computer.get_choice(), '2')

    def test_get_choice_human_says_ni(self):
        pass
        # we can try to test this later 
        # if we include a try-counter that after so many tries, 
        # returns a message and exits the game

    def test_end_game_returns_the_tied_game(self):
        test_yields = self.mc_dummy.end_game(self.tied_game)
        whats_expected = self.signer.show(self.signer.tie)
        self.assertEqual(test_yields, whats_expected)

    def test_end_game_returns_the_computer_win(self):
        test_yields = self.mc_dummy.end_game(self.computer_win)
        whats_expected = self.signer.show(self.signer.computer)
        self.assertEqual(test_yields, whats_expected)

    def test_end_game_returns_the_human_win(self):
        test_yields = self.mc_dummy.end_game(self.human_win)
        whats_expected = self.signer.show(self.signer.human)
        self.assertEqual(test_yields, whats_expected)

if __name__ == '__main__':
    unittest.main()
