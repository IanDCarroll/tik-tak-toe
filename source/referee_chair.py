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

    def start_game(self):
        announcer.show(announcer.start)
        announcer.show(announcer.render_board(self.table_top.board))
        self.facilitate_turns()

    def facilitate_turns(self):
        self.whos_turn.move(self.board)
        announcer.show(announcer.render_board(self.table_top.board))
        the_game_is_over = check_for_game_over(self.table_top.board)
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
        announcer.show(announcer.render_board(self.table_top.board))
        if winner == "tie":
            announcer.show(display.draw)
        elif winner == "computer":
            announcer.show(display.computer)
        elif winner == "human":
            announcer.show(display.human)

    def check_for_game_over(self):
        if check_for_draw() == True:
            return "draw"
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
        scan_list = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],
                     [1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        did_they_win = False
        for i in range(0, len(scan_list)):
            win_factor = 0
            for j in scan_list[i]:
                win_factor += board[j]
            if win_factor == 3 or win_factor == 30:
                did_they_win = True
        return did_they_win
