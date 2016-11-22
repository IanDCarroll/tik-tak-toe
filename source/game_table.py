from math import sqrt

class TableTop(object):
    
    def __init__(self):
        self.board = [0,0,0,0,0,0,0,0,0]

    def get_board_size(self, board):
        return int(sqrt(len(board))) 
