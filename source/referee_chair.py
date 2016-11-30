from observer_abilities import *
from announcer_chair import Announcer
from player_chair import *
from time import sleep

class Referee(Observer):

    def __init__(self, table_top):
        self.table_top = table_top
        self.announcer = Announcer()

        self.noughts = 10
        self.crosses = 1
        self.player1 = Human(self.crosses)
        self.player2 = Computer(self.noughts)
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
            self.player1 = Computer(self.crosses)
            self.player2 = Human(self.noughts)
            self.whos_turn = self.player1
            self.facilitate_turns()
        else:
            self.announcer.show(self.announcer.bad_move)
            self.select_mode()

    def facilitate_turns(self):
        self.show_board()
        self.whos_turn.move(self.table_top.board)
        self.moves_taken += 1
        sleep(0.75)
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
            return self.whos_turn.name
        elif self.moves_taken == len(self.table_top.board):
            return "tie"
        else:
            return False

    def check_for_winner(self):
        board = self.table_top.board
        crosses_win = self.get_board_size(board)
        noughts_win = crosses_win * 10
        scan = self.scan_board(board)
        if crosses_win in scan or noughts_win in scan:
            return True
        else:
            return False
