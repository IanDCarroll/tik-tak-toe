import game_table
import player_chair
import display

class Referee(object):

    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.whos_turn = self.player1

    def start_game(self):
        display.show(display.start)
        display.show(display.render_board(self.board))
        self.facilitate_turns()

    def facilitate_turns(self):
        self.whos_turn.move(self.board)
        display.show(display.render_board(self.board))
        the_game_is_over = check_for_winner(self.board)
        if the_game_is_over != False:
           game_over(the_game_is_over)
        else:
           if self.whos_turn == self.player1:
              self.whos_turn = self.player2
           elif self.whos_turn == self.player2:
              self.whos_turn = self.player1
           facilitate_turns()
        
    def game_over(self, winner):
        display.show(display.render_board(self.board))
        if winner == "draw":
            display.show(display.draw)
        elif winner == "computer":
            display.show(display.computer)
        elif winner == "human":
            display.show(display.human)

    def check_for_game_over(self):
        if check_for_draw() == True:
            return "draw"
        elif check_for_winner() == True:
            return self.players_turn.id
        else:
            return False

    def check_for_draw(self):
        if 0 in self.board:
            return False
        else:
            return True

    def check_for_winner(self):
        board = self.board
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