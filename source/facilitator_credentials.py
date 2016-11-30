from math import sqrt

class Facilitator(object):

    def scan_board(self, board):
        pass

    def get_board_size(self, board):
        return int(sqrt(len(board))) 
