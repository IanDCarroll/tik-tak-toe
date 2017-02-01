import sys

class Emcee(object):

    def __init__(self, table_top, user_interface):
        self.table_top = table_top
        self.ui = user_interface

    strikes = 0

    def choose_who_goes_first(self):
        self.ui.refresh()
        choice = self.get_choice()
        if choice == '1':
           self.table_top.player1.ui = self.ui
           self.table_top.player2.ui = self.ui
        elif choice == '2':
           self.table_top.give_computer_the_first_move()
           self.table_top.player1.ui = self.ui
           self.table_top.player2.ui = self.ui

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
