import sys
from Training.observer_abilities import *
from Training.cortex_3x3_caddy import *
from Scenery.announcer_chair import *

class Player(Observer):

    def __init__(self, marker_code, user_interface):
        self.ui = user_interface
        self.marker_code = marker_code

    def get_enemy_code(self):
        if self.marker_code == 10:
            return 1
        return 10

    def move(self, board):
        choice = self.choose(board)
        board[choice] = self.marker_code
        return board

    def choose(self, board):
        options = self.get_legal_moves(board)
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

    def choose(self, board):
        choice = self.get_good_input(board)
        if self.check_conscience(choice, board):
            return self.redo_move(board)
        else:
            self.reset_strikes()
            return choice

    def get_good_input(self, board):
        try:
            self.ui.show(self.ui.question)
            return int(self.ui.ask_human()) -1
        except(ValueError):
            return self.redo_move(board)

    def check_conscience(self, choice, board):
        if choice not in self.get_legal_moves(board):
            return True
            
    def redo_move(self, board):
        self.add_a_strike()
        self.ui.show(self.ui.bad_move)
        return self.choose(board)

    def add_a_strike(self):
        self.strikes += 1
        if self.strikes == 3:
            self.ui.show(self.ui.strike_3)
            sys.exit()

    def reset_strikes(self):
        self.strikes = 0

class Computer(Player):

    name = 'computer'
    cortex = Cortex_3x3()

    def choose(self, board):
        intel = self.get_intelligence(board)
        choice = self.cortex.direct_move(intel)
        self.display_choice(choice)
        return choice

    def get_intelligence(self, board):
        return { 'board': board, 
                 'options': self.get_legal_moves(board),
                 'analysis': self.scan_board(board),
                 'marker_code': self.marker_code, 
                 'enemy_code': self.get_enemy_code() }

    def display_choice(self, choice):
        pre = self.ui.pre_choice
        post = self.ui.post_choice
        statement = pre + str(choice + 1) + post
        self.ui.show(statement)
