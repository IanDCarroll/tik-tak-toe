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
        win_list = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],
                    [1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        did_they_win = False
        for i in range(0, len(win_list)):
            win_factor = 0
            for j in win_list[i]:
                win_factor += board[j]
            if win_factor == 3 or win_factor == 30:
                did_they_win = True
        return did_they_win

    def get_win_list(self):
        board = self.table_top.board
        board_size = self.get_board_size(board)
        win_list = []
        win_list.extend(self.get_winning_rows(board, board_size))
        win_list.extend(self.get_winning_cols(board, board_size))
        win_list.extend(self.get_winning_diags(board, board_size))
        print win_list
        return win_list

    def get_winning_rows(self, board, board_size):
        winning_rows = self.get_empty_list(board_size)
        start = 0
        for i in range(0, board_size):
            stop = start + board_size
            for j in range(start, stop):
                 winning_rows[i].append(j)
            start += board_size
        return winning_rows

    def get_winning_cols(self, board, board_size):
        winning_cols = self.get_empty_list(board_size)
        col = 0
        for i in range(0, board_size):
            for j in range(col, len(board), board_size):
                 winning_cols[i].append(j)
            col += 1
        return winning_cols
 
    def get_empty_list(self, board_size):
        empty_list = []
        for i in range(0, board_size):
            empty_list.append([])
        return empty_list

    def get_winning_diags(self, board, board_size):
        winning_diags = [[],[]]
        diag = 0
        for i in range(0, board_size):
            winning_diags[0].append(diag)
            diag += board_size + 1
        diag = board_size - 1
        for j in range(0, board_size):
            winning_diags[1].append(diag)
            diag += board_size - 1
        return winning_diags        
