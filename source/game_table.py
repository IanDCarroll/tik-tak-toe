from player_chair import *

class TableTop(object):
    
    def __init__(self):
        self.board = [0,0,0, 0,0,0, 0,0,0]
        self.noughts = 10
        self.crosses = 1
        self.player1 = Human(self.crosses)
        self.player2 = Computer(self.noughts)
        self.whos_turn = self.player1

    def switch_players(self):
        self.player1 = Computer(self.crosses)
        self.player2 = Human(self.noughts)
