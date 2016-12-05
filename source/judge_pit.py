from observer_abilities import *

class Judge(Observer):

    def __init__(self, board_object):
       self.table_top = board_object

    def check_for_winner(self):
        board = self.table_top.board
        crosses_win = self.get_board_size(board)
        noughts_win = crosses_win * 10
        scan = self.scan_board(board)
        if crosses_win in scan or noughts_win in scan:
           self.table_top.give_next_player_a_go() 
           # switch the winner back after Referee.take_a_turn() 
           return self.table_top.whos_turn.name
        else:
           return False
