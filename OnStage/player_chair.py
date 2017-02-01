import sys
from Training.observer_abilities import *
from Training.cortex_3x3_caddy import *

class Player(Observer):

    def __init__(self, marker_code):
        self.ui = None
        self.marker_code = marker_code

    def get_enemy_code(self):
        if self.marker_code == 10:
            return 1
        return 10

    def move(self, table_top):
        choice = self.choose(table_top)
        table_top.board[choice] = self.marker_code
        return table_top.board

    def choose(self, table_top):
        options = self.get_legal_moves(table_top.board)
        return options[0]

    def get_legal_moves(self, board):
        legal_moves = []
        for i in range(0, len(board)):
            if board[i] != 1 and board[i] != 10:
                legal_moves.append(i)
        return legal_moves

class Human(Player):

    name = 'human'
    strikes = 0

    def choose(self, table_top):
        choice = self.get_good_input(table_top.board)
        if self.check_conscience(choice, table_top.board):
            return self.redo_move(table_top.board)
        else:
            self.reset_strikes()
            return choice

    def get_good_input(self, board):
        try:
            return int(self.ui.ask_human()) -1
        except(ValueError):
            return self.redo_move(board)

    def check_conscience(self, choice, board):
        if choice not in self.get_legal_moves(board):
            return True
            
    def redo_move(self, board):
        self.add_a_strike()
        # This should happen: TableTop.error = True
        return self.choose(board)

    def add_a_strike(self):
        self.strikes += 1
        if self.strikes == 3:
            # this should happen: TableTop.exit = True
            sys.exit()

    def reset_strikes(self):
        self.strikes = 0

class Computer(Player):

    name = 'computer'
    cortex = Cortex_3x3()

    def choose(self, table_top):
        intel = self.get_intelligence(table_top.board)
        choice = self.cortex.direct_move(intel)
        return choice

    def get_intelligence(self, board):
        return { 'board': board, 
                 'options': self.get_legal_moves(board),
                 'analysis': self.scan_board(board),
                 'marker_code': self.marker_code, 
                 'enemy_code': self.get_enemy_code() }
