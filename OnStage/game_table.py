from player_chair import *

class TableTop(object):
    
    def __init__(self):
        self.board = [0,0,0, 0,0,0, 0,0,0]
        self.noughts = 10
        self.crosses = 1
        self.player1 = Human(self.crosses)
        self.player2 = Computer(self.noughts)
        self.whos_turn = self.player1
        self.last_move = 0
        self.start_of_game = True
        self.tie = False
        self.win = False
        self.error = False
        self.exit = False

    def give_computer_the_first_move(self):
        self.player1 = Computer(self.crosses)
        self.player2 = Human(self.noughts)
        self.whos_turn = self.player1

    def give_next_player_a_go(self):
        if self.whos_turn == self.player1:
            self.whos_turn = self.player2
        elif self.whos_turn == self.player2:
            self.whos_turn = self.player1
