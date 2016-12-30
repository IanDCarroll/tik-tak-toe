import sys
from Scenery.announcer_chair import *

class Emcee(object):

    def __init__(self, board_object):
        self.table_top = board_object
        self.announcer = Announcer()

    strikes = 0

    def choose_who_goes_first(self):
        self.announcer.show(self.announcer.start)
        self.announcer.show(self.announcer.select)
        choice = self.get_choice()
        if choice == '2':
           self.table_top.give_computer_the_first_move()

    def get_choice(self):
        choice = self.announcer.ask_human()
        if choice == '1' or choice == '2':
            return choice
        elif self.strikes == 2:
            self.announcer.show(self.announcer.strike_3)
            sys.exit()
        else:
            self.announcer.show(self.announcer.bad_move)
            self.strikes += 1
            return self.get_choice()

    def end_game(self, winner):
        if winner == 'tie':
            return self.announcer.show(self.announcer.tie)
        elif winner == 'computer':
            return self.announcer.show(self.announcer.computer)
        elif winner == 'human':
            return self.announcer.show(self.announcer.human)

    def ask_human(self):
        return raw_input('> ')
