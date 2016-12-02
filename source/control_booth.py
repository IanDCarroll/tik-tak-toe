from emcee_podium import Emcee as mc

class StageManager(object):

    def play_game(self):
        play_options = mc.open_game()
        winner = ref.run_game(play_options)
        return mc.end_game(winner)      
