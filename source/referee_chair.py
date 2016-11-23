from facilitator_credentials import Facilitator
from game_table import TableTop
from player_chair import *
from announcer_chair import Announcer

class Referee(Facilitator):

    def __init__(self, table_top, player1, player2):
        self.announcer = Announcer()
        self.table_top = table_top
        self.player1 = player1
        self.player2 = player2
        self.whos_turn = self.player1

    def show_board(self):
        board = self.announcer.render_board(self.table_top.board)
        self.announcer.show(board)

    def start_game(self):
        self.announcer.show(self.announcer.start)
        self.show_board()
        self.facilitate_turns()
        
    def facilitate_turns(self):
        self.whos_turn.move(self.board)
        self.show_board()
        the_game_is_over = check_for_game_over()
        if the_game_is_over != False:
            game_over(the_game_is_over)
        else:
            self.prep_next_turn()
            self.facilitate_turns()

    def prep_next_turn(self):
        if self.whos_turn == self.player1:
            self.whos_turn = self.player2
        elif self.whos_turn == self.player2:
            self.whos_turn = self.player1
        
    def game_over(self, winner): 
        self.show_board()
        if winner == "tie":
            self.announcer.show(self.announcer.tie)
        elif winner == "computer":
            self.announcer.show(self.announcer.computer)
        elif winner == "human":
            self.announcer.show(self.announcer.human)

    def check_for_game_over(self):
        if check_for_tie() == True:
            return "tie"
        elif check_for_winner() == True:
            return self.players_turn.id
        else:
            return False

    def check_for_tie(self):
        if 0 in self.table_top.board:
            return False
        else:
            return True

    def check_for_winner(self):
        board = self.table_top.board
        win_list = self.get_win_list()
        did_they_win = False
        for i in range(0, len(scan_list)):
            win_factor = 0
            for j in scan_list[i]:
                win_factor += board[j]
            if win_factor == 3 or win_factor == 30:
                did_they_win = True
        return did_they_win

    def get_win_list(self):
        pass
