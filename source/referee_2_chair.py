from announcer_chair import Announcer

class Referee(Observer):

    def __init__(self, board_object): # better as part of TableTop.
        self.table_top = board_object
        self.announcer = Announcer()
        self.moves_taken = 0

    def take_turns(self): # might belong to Judge
        board_size = self.get_board_size(self.table_top.board)
        winner = check_for_winner() # definitely belongs to Judge
        if winner:
           return winner
        elif moves_taken == board_size: 
           return 'tie'
        else:
           self.moves_taken += 1
           self.next_players_turn() # maybe belongs to TableTop
           self.take_a_turn()
           

    def take_a_turn(self):
        self.show_board
        # all the rest of the steps needed to take a turn

    def show_board(self):
        board = self.announcer.render_board(self.table_top.board)
        self.announcer.show(board)
