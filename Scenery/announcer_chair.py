from carpenter_shop import *

class Commandline_Interface(Carpenter):

    def show(self, text):
        print text

    def ask_human(self):
        return raw_input(self.prompt)
