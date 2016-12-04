from observer_abilities import *

class Judge(Observer):

    def __init__(self, board_object):
       self.table_top = board_object

    def check_for_winner(self):
        pass
