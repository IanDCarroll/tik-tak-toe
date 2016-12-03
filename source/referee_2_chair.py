from announcer_chair import Announcer

class Referee(object):

    def __init__(self, play_options): # better as part of TableTop.
        self.play_options = play_options
        self.table_top = TableTop()
        self.announcer = Announcer()
        self.noughts = 10
        self.crosses = 1
        self.player1 = Human(self.crosses)
        self.player2 = Computer(self.noughts)
        self.whos_turn = self.player1
        self.moves_taken = 0
        

    def play_game(self):
        set_game()
        

    def set_game(self):
        if self.play_options == '2':
           self.switch_players()
           self.play_options = 'ready'
        

    def switch_players(self):
        self.player1 = Computer(self.crosses)
        self.player2 = Human(self.noughts)
