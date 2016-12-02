class Emcee(object):

    def open_game(self):
        self.announcer.show(self.announcer.start)
        self.announcer.show(self.announcer.select)
        select = self.ask_human()
        if select == '1':
            return #human goes first
        elif select == '2':
            return #computer goes first
        else:
            self.announcer.show(announcer.bad_move)
            return self.open_game()

    def ask_human(self):
        return raw_input('> ')
