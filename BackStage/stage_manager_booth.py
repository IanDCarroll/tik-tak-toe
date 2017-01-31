from emcee_podium import *
from referee_chair import *
from OnStage.game_table import *
from Scenery.cli_display import *

class StageManager(object):

    def __init__(self):
        self.table_top = TableTop()
        self.ui = TerminalInterface(self.table_top)
        self.mc = Emcee(self.table_top, self.ui)
        self.ref = Referee(self.table_top, self.ui)

    def play_game(self):
        self.mc.choose_who_goes_first()
        winner = self.ref.facilitate_turns()
        return self.mc.end_game(winner)
