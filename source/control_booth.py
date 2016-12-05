from emcee_podium import Emcee
from referee_2_chair import Referee
from game_table import TableTop

class StageManager(object):

    def __init__(self):
        self.table_top = TableTop()
        self.mc = Emcee(self.table_top)
        self.ref = Referee(self.table_top)

    def play_game(self):
        self.mc.choose_who_goes_first()
        winner = self.ref.facilitate_turns()
        return self.mc.end_game(winner)  
