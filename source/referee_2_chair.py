from announcer_chair import Announcer

class Referee(object):

    def __init__(self, play_options): # better as part of TableTop.
        self.table_top = TableTop()
        self.announcer = Announcer()

    def play_game(self):
        set_game()
        

    def set_game(self):
        if self.play_options == '2':
           self.switch_players()
           self.play_options = 'used'
        

    def switch_players(self):
        self.player1 = Computer(self.crosses)
        self.player2 = Human(self.noughts)
