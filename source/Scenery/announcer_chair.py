from scriptographer_desk import *

class Announcer(Scriptographer):

    def show(self, text):
        print text

    def ask_human(self):
        return raw_input(self.prompt)
