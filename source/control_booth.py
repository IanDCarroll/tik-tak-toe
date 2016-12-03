from emcee_podium import Emcee as mc
from referee_2_chair import Referee
from game_table import TableTop

class StageManager(object):

    def __init__(self):
        self.table_top = TableTop()

    def play_game(self):
        play_options = mc.open_game()
        if play_options = '2':
            self.table_top.switch_players()

        ref = Referee(self.table_top)
        winner = ref.run_game()

        return mc.end_game(winner)      
