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
        take_6a = [1,10,0, 0,1,0, 0,0,10]
        take_6b = [10,0,0, 0,1,10, 0,0,1]
        take_8a = [0,10,1, 0,1,0, 10,0,0]
        take_8b = [0,0,10, 10,1,0, 1,0,0]
        if intel['board'] == take_6a or intel['board'] == take_6b:
            return 6
        elif intel['board'] == take_8a or intel['board'] == take_8b:
            return 8
        return False

    def avoid_fork(self, intel):
        return False
