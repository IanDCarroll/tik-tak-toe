from carpenter_shop import *

class TerminalInterface(Carpenter):

    def __init__(self, board_object):
        self.table_top = board_object

    def refresh(self):
        print self.display()

    def display(self):
        board = self.render_board(self.table_top.board)
        display = ''
        if self.table_top.start_of_game == True:
            self.table_top.start_of_game = False
            display = self.start + self.new_line + self.select
        elif self.table_top.error == True:
            self.table_top.error = False
            display = self.bad_move
        elif self.table_top.tie == True:
            display = board + self.new_line + self.tie
        elif self.table_top.win == True:
            display = board + self.new_line + self.show_winner()
        elif self.table_top.exit == True:
            display = self.strike_3
        else:
            display = board + self.new_line + self.report_move()
        return display

    def show_winner(self):
        if self.table_top.whos_turn.name == 'computer':
            return self.computer
        return self.human

    def report_move(self):
        if self.table_top.whos_turn.name == 'computer':
            return self.computer_move
        return self.question

    def show_computer_choice(self, choice):
        pre = self.pre_choice
        post = self.post_choice
        statement = pre + str(choice + 1) + post
        self.show(statement)

    def show(self, text): # to be deleted
        print text

    def ask_human(self):
        return raw_input(self.prompt)
