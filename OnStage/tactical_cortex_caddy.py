from parser_abilities import *

class TacticalCortex(Parser):

    def take_win_chance(self, intel):
        for condition in intel['analysis']:
            if condition == intel['marker_code'] * 2:
               code = intel['analysis'].index(condition)
               return self.get_empty_square(intel['options'], code)
        return False

    def avoid_losing(self, intel):
        for condition in intel['analysis']:
            if condition == intel['enemy_code'] * 2:
               code = intel['analysis'].index(condition)
               return self.get_empty_square(intel['options'], code)
        return False

    def take_fork_chance(self, intel):
        if intel['board'] == [1,10,0, 0,1,0, 0,0,10]:
            return 6
        return False
