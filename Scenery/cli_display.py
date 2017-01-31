from carpenter_shop import *

class TerminalInterface(Carpenter):

    def __init__(self, board_object):
        self.table_top = board_object

    def refresh(self):
        print self.display()

    def display(self):
        return "a board and message"

    def show_computer_choice(self, choice):
        pre = self.pre_choice
        post = self.post_choice
        statement = pre + str(choice + 1) + post
        self.show(statement)

    def show(self, text): # to be deleted
        print text

    def ask_human(self):
        return raw_input(self.prompt)
