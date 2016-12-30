from strategic_3x3_lobe_slot import *
from tactical_3x3_lobe_slot import *

class Cortex_3x3(object):

    strat = StrategicLobe()
    tac = TacticalLobe()

    def direct_move(self, intel):
        priority_list = self.get_priority_list(intel)
        for priority in priority_list:
            if priority is not False:
	        return priority

    def get_priority_list(self, intel):       
        p1 = self.tac.take_win_chance(intel)
        p2 = self.tac.avoid_losing(intel)
        p3 = self.tac.take_fork_chance(intel)
        p4 = self.tac.avoid_fork(intel)
        p5 = self.strat.take_the_center(intel)
        p6 = self.strat.take_catty_corner(intel)
        p7 = self.strat.make_default_choice(intel)
        priority_list = [p1, p2, p3, p4, p5, p6, p7]
        return priority_list
