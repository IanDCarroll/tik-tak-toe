from emcee_podium import Emcee as mc
from referee_2_chair import Referee
from game_table import TableTop

class StageManager(object):

    def __init__(self):
        self.table_top = TableTop()

    def play_game(self):
        game_mode = mc.open_game()
        if game_mode == '2':
            self.table_top.switch_players()

        ref = Referee(table_top)
        winner = ref.facilitate_turns()

        return mc.end_game(winner)      
