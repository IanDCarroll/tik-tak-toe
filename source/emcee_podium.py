from announcer_chair import *

class Emcee(object):

    announcer = Announcer()

    def open_game(self):
        self.announcer.show(self.announcer.start)
        self.announcer.show(self.announcer.select)
        return self.ask_human()
        if select == '1' or select == '2':
            return select
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
