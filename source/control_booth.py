from emcee_podium import Emcee
from referee_2_chair import Referee
from game_table import TableTop

class StageManager(object):

    def __init__(self):
        self.table_top = TableTop()

    def play_game(self):
        mc = Emcee(table_top)
        mc.choose_who_goes_first()

        ref = Referee(table_top)
        winner = ref.facilitate_turns()

        return mc.end_game(winner)  
