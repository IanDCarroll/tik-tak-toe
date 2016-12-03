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
        self.mc_human = Mc_Human()
        self.mc_computer = Mc_Computer()
        self.mc_error = Mc_Error()
        self.human_win = 'human'
        self.computer_win = 'computer'
        self.tied_game = 'tie'

    def test_open_game_human_chooses_to_go_first(self):
        self.assertEqual(self.mc_human.open_game(), '1')

    def test_open_game_human_chooses_to_go_second(self):
        self.assertEqual(self.mc_computer.open_game(), '2')

    def test_open_game_human_says_ni(self):
        pass
        # we can try to test this later 
        # if we include a try-counter that after so many tries, 
        # returns a message and exits the game

if __name__ == '__main__':
    unittest.main()
