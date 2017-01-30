import unittest
from BackStage.emcee_podium import *
from Scenery.cli_display import *
from OnStage.game_table import *

class MuteUI_1(TerminalInterface):
    def show(self, what_is_said):
        return what_is_said
    def ask_human(self):
        return '1'

class MuteUI_2(MuteUI_1):
    def ask_human(self):
        return '2'

class MuteUI_E(MuteUI_1):
    def ask_human(self):
        return 'Ni'

class Mc_Human(Emcee):
    def __init__(self, board):
        self.table_top = board
        self.ui = MuteUI_1()

class Mc_Computer(Mc_Human):
    def __init__(self, board):
        self.table_top = board
        self.ui = MuteUI_2()

class Mc_Error(Mc_Human):
     def __init__(self, board):
        self.table_top = board
        self.ui = MuteUI_E()   

class EmceeTestCase(unittest.TestCase):

    def setUp(self):
        self.mute1 = MuteUI_1()
        self.mute2 = MuteUI_2()
        self.muteE = MuteUI_E()
        self.table_top1 = TableTop(self.mute1)
        self.table_top2 = TableTop(self.mute2)
        self.table_topE = TableTop(self.muteE)
        self.mc_human = Mc_Human(self.table_top1)
        self.mc_computer = Mc_Computer(self.table_top2)
        self.mc_error = Mc_Error(self.table_topE)
        self.a_human_p1 = Human(1, self.mute1)
        self.a_human_p2 = Human(10, self.mute1)
        self.a_computer_p1 = Computer(1, self.mute1)
        self.a_computer_p2 = Computer(10, self.mute1)
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
        with self.assertRaises(SystemExit):
            self.mc_error.get_choice()

    def test_end_game_returns_the_tied_game(self):
        test_yields = self.mc_human.end_game(self.tied_game)
        whats_expected = self.mute1.show(self.mute1.tie)
        self.assertEqual(test_yields, whats_expected)

    def test_end_game_returns_the_computer_win(self):
        test_yields = self.mc_human.end_game(self.computer_win)
        whats_expected = self.mute1.show(self.mute1.computer)
        self.assertEqual(test_yields, whats_expected)

    def test_end_game_returns_the_human_win(self):
        test_yields = self.mc_human.end_game(self.human_win)
        whats_expected = self.mute1.show(self.mute1.human)
        self.assertEqual(test_yields, whats_expected)

if __name__ == '__main__':
    unittest.main()
