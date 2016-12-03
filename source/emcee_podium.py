from announcer_chair import *

class Emcee(object):

    announcer = Announcer()

    def choose_who_goes_first(self):
        self.announcer.show(self.announcer.start)
        self.announcer.show(self.announcer.select)
        choice = get_selection()
        if choice == '2':
           self.table_top.give_computer_the_first_move()

    def get_choice(self):
        choice = self.ask_human()
        if choice == '1' or choice == '2':
            return choice
        else:
            self.announcer.show(announcer.bad_move)
            return self.open_game()

    def end_game(self, winner):
        if winner == 'tie':
            return self.announcer.show(self.announcer.tie)
        elif winner == 'computer':
            return self.announcer.show(self.announcer.computer)
        elif winner == 'human':
            return self.announcer.show(self.announcer.human)

    def ask_human(self):
        return raw_input('> ')
