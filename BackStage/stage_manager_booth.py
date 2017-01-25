from emcee_podium import Emcee
from referee_chair import Referee
from OnStage.game_table import TableTop
from Scenery.announcer_chair import Commandline_Interface

class StageManager(object):

    def __init__(self):
        self.ui = Commandline_Interface()
        self.table_top = TableTop(self.ui)
        self.mc = Emcee(self.table_top, self.ui)
        self.ref = Referee(self.table_top, self.ui)

    def play_game(self):
        self.mc.choose_who_goes_first()
        winner = self.ref.facilitate_turns()
        return self.mc.end_game(winner)
