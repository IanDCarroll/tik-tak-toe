from math import sqrt

class TableTop(object):
    
    def __init__(self):
        self.board = [0,0,0,0,0,0,0,0,0]

    # Why pass an argument here?
    # This way the TableTop can be instantiated by Referee
    # Referee can pass the board's value to Display
    # and the board size can be known by Display
    # even though Display was not passed the TableTop object

    def get_board_size(self, board):
        return int(sqrt(len(board))) 
