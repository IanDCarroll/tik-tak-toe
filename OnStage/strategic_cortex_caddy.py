from parser_abilities import *

class StrategicCortex(Parser):

    def take_the_center(self, intel):
        if 4 in intel['options']:
            return 4
        return False

    def take_catty_corner(self, intel):
        center = intel['board'][4]
        NWSE_diag = intel['analysis'][6]
        NESW_diag = intel['analysis'][7]
        if center == intel['marker_code']:
            if NWSE_diag == 11:
                return self.get_empty_square(intel['options'], 6)
            elif NESW_diag == 11:
                return self.get_empty_square(intel['options'], 7)
        return False

    def make_default_choice(self, intel):
        priorities = [0,2,6,8]
        for priority in priorities:
            if priority in intel['options']:
               return priority
        return intel['options'][0]
