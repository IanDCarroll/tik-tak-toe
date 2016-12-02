from emcee_podium import Emcee as mc
from referee_2_chair import Referee

class StageManager(object):

    def play_game(self):
        play_options = mc.open_game()

        ref = Referee(play_options)
        winner = ref.run_game()

        return mc.end_game(winner)      
