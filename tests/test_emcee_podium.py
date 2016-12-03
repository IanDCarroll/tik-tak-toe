import unittest
from source.emcee_podium import *
from source.announcer_chair import *

class MuteAnnouncer(Announcer):
    def show(self, what_is_said):
        return what_is_said

class Dummy(Emcee):
    announcer = MuteAnnouncer()

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
        self.signer = MuteAnnouncer()
        self.mc_dummy = Dummy()
        self.mc_human = Mc_Human()
        self.mc_computer = Mc_Computer()
        self.mc_error = Mc_Error()
        self.human_win = 'human'
        self.computer_win = 'computer'
        self.tied_game = 'tie'

    def test_open_game_human_chooses_to_go_first(self):
        self.assertEqual(self.mc_human.get_selection(), '1')

    def test_open_game_human_chooses_to_go_second(self):
        self.assertEqual(self.mc_computer.get_selection(), '2')

    def test_open_game_human_says_ni(self):
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
