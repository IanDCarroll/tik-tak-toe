from Scenery.announcer_chair import *
from judge_pit import Judge

class Referee(object):

    def __init__(self, board_object, user_interface):
        self.table_top = board_object
        self.judge = Judge(self.table_top)
        self.ui = user_interface
        self.moves_taken = 0

    def facilitate_turns(self):
        self.show_board()
        winner = self.judge.check_for_winner()
        if winner:
           return winner
        elif self.moves_taken == len(self.table_top.board):
           return 'tie'
        else:
           self.take_a_turn()
           return self.facilitate_turns()

    def take_a_turn(self):
        self.table_top.whos_turn.move(self.table_top.board)
        self.moves_taken += 1
        self.table_top.give_next_player_a_go()

    def show_board(self):
        board = self.ui.render_board(self.table_top.board)
        return self.ui.show(board)
