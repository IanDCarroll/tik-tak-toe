import sys

class Emcee(object):

    def __init__(self, board_object, user_interface):
        self.table_top = board_object
        self.ui = user_interface

    strikes = 0

    def choose_who_goes_first(self):
        self.ui.show(self.ui.start)
        self.ui.show(self.ui.select)
        choice = self.get_choice()
        if choice == '2':
           self.table_top.give_computer_the_first_move()

    def get_choice(self):
        choice = self.ui.ask_human()
        if choice == '1' or choice == '2':
            return choice
        elif self.strikes == 2:
            self.ui.show(self.ui.strike_3)
            sys.exit()
        else:
            self.ui.show(self.ui.bad_move)
            self.strikes += 1
            return self.get_choice()

    def end_game(self, winner):
        if winner == 'tie':
            return self.ui.show(self.ui.tie)
        elif winner == 'computer':
            return self.ui.show(self.ui.computer)
        elif winner == 'human':
            return self.ui.show(self.ui.human)
