from facilitator_credentials import Facilitator
from announcer_chair import Announcer
from time import sleep

class Referee(Facilitator):

    def __init__(self, table_top, player1, player2):
        self.announcer = Announcer()
        self.table_top = table_top
        self.player1 = player1
        self.player2 = player2
        self.whos_turn = self.player1
        self.moves_taken = 0

    def start_game(self):
        self.announcer.show(self.announcer.start)
        self.select_mode()

    def select_mode(self):
        self.announcer.show(self.announcer.select)
        select = self.ask_human()
        if select == '1':
            self.facilitate_turns()
        elif select == '2':
            self.prep_next_turn()
            self.facilitate_turns()
        else:
            self.announcer.show(self.announcer.bad_move)
            self.game_menu()

    def facilitate_turns(self):
        self.show_board()
        self.whos_turn.move(self.table_top.board)
        self.moves_taken += 1
        sleep(1.25)
        the_game_is_over = self.check_for_game_over()
        if the_game_is_over != False:
            self.game_over(the_game_is_over)
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

    def ask_human(self):
        return raw_input('> ')

    def show_board(self):
        board = self.announcer.render_board(self.table_top.board)
        self.announcer.show(board)

    def check_for_game_over(self):
        winner = self.check_for_winner()
        if winner == True:
            return self.whos_turn.id
        elif self.moves_taken == 9:
            return "tie"
        else:
            return False

    def check_for_winner(self):
        board = self.table_top.board
        p1_win = self.get_board_size(board)
        p2_win = p1_win * 10
        win_list = self.get_win_list()
        did_they_win = False
        for i in range(0, len(win_list)):
            win_factor = 0
            for j in win_list[i]:
                win_factor += board[j]
            if win_factor == p1_win or win_factor == p2_win:
                did_they_win = True
        return did_they_win

    def get_win_list(self):
        board = self.table_top.board
        board_size = self.get_board_size(board)
        win_list = []
        win_list.extend(self.get_winning_rows(board_size))
        win_list.extend(self.get_winning_cols(board_size))
        win_list.extend(self.get_winning_diags(board_size))
        return win_list

    def get_winning_rows(self, board_size):
        winning_rows = self.get_empty_list(board_size)
        start_coord = 0
        for i in range(0, board_size):
            stop_coord = start_coord + board_size
            for j in range(start_coord, stop_coord):
                 winning_rows[i].append(j)
            start_coord += board_size
        return winning_rows

    def get_winning_cols(self, board_size):
        winning_cols = self.get_empty_list(board_size)
        start_coord = 0
        stop_coord = board_size * board_size
        for i in range(0, board_size):
            for j in range(start_coord, stop_coord, board_size):
                 winning_cols[i].append(j)
            start_coord += 1
        return winning_cols
 
    def get_empty_list(self, board_size):
        empty_list = []
        for i in range(0, board_size):
            empty_list.append([])
        return empty_list

    def get_winning_diags(self, board_size):
        winning_diags = []
        winning_diags.append(self.get_NW_SE_diag(board_size))
        winning_diags.append(self.get_SW_NE_diag(board_size))
        return winning_diags

    def get_NW_SE_diag(self, board_size):
        diag = []
        coord = 0
        for i in range(0, board_size):
            diag.append(coord)
            coord += board_size + 1
        return diag

    def get_SW_NE_diag(self, board_size):
        diag = []
        coord = board_size -1
        for i in range(0, board_size):
            diag.append(coord)
            coord += board_size - 1
        return diag
