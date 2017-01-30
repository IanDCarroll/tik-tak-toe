from carpenter_shop import *

class TerminalInterface(Carpenter):

    def show(self, text):
        print text

    def ask_human(self):
        return raw_input(self.prompt)

    def show_computer_choice(self, choice):
        pre = self.pre_choice
        post = self.post_choice
        statement = pre + str(choice + 1) + post
        self.show(statement)
