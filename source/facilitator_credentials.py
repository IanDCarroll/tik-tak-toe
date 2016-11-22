from math import sqrt

class Facilitator(object):

    def get_board_size(self, board):
        return int(sqrt(len(board))) 
