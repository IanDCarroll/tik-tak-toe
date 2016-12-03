from announcer_chair import Announcer

class Referee(object):

    def __init__(self, board_object): # better as part of TableTop.
        self.table_top = board_object
        self.announcer = Announcer()

    def play_game(self):
        # what facilitate_turns() did. but cleaner.
