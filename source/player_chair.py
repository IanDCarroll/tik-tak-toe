from announcer_chair import *

class Player(object):

    def __init__(self, marker_code):
        self.announcer = Announcer()
        self.marker_code = marker_code

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

    def choose(self, board):
        choice = self.get_good_input(board)
        if self.check_conscience(choice, board):
            return self.redo_move(board)
        else:
            return choice

    def get_good_input(self, board):
        try:
           self.announcer.show(self.announcer.question)
           return int(raw_input("> ")) -1
        except(ValueError):
           return self.redo_move(board)

    def check_conscience(self, choice, board):
        if choice not in self.get_legal_moves(board):
            return True
            
    def redo_move(self, board):
        self.announcer.show(self.announcer.bad_move)
        return self.choose(board)

class Computer(Player):

    name = 'computer'
