import game_table
import player_chair
import display

class Referee(object):

    def _init_(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.players_turn = self.player1

    def start_game(self):
        display.show(display.start)
        display.show(display.render_board(self.board))
        self.facilitate_turns()

    def facilitate_turns(self):
        self.players_turn.move(self.board)
        display.show(display.render_board(self.board))
        the_game_is_over = check_for_winner(self.board)
        if the_game_is_over != False:
           game_over(the_game_is_over)
        else:
           if self.players_turn == self.player1:
              self.players_turn = self.player2
           elif self.players_turn == self.player2:
              self.players_turn = self.player1
           facilitate_turns()
        
    def game_over(self, winner):
        display.show(display.render_board(self.board))
        if winner == "draw":
            display.show(display.draw)
        elif winner == "computer":
            display.show(display.computer)
        elif winner == "human":
            display.show(display.human)

    def check_for_winner():
        if check_for_draw() == True:
            return "draw"
        elif check_for_computer_winner() == True:
            return "computer"
        elif check_for_human_winner() == True:
            return "human"
        else:
            return False

    def check_for_draw():
        pass

    def check_for_computer_winner():
        pass

    def check_for_human_winner():
        pass
