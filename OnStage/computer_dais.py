from player_chair import Player
from strategic_cortex_caddy import *
from tactical_cortex_caddy import *

class Computer(Player):

    name = 'computer'
    strat = StrategicCortex()
    tac = TacticalCortex()

    def choose(self, board):
        priority_list = self.ask_cortecies(board)
        for priority in priority_list:
            if priority is not False:
	        return priority

    def ask_cortecies(self, board):
        intel = self.get_intelligence(board)       
        p1 = self.tac.take_win_chance(intel)
        p2 = self.tac.avoid_losing(intel)
        p3 = self.strat.take_the_center(intel)
        p4 = self.strat.take_catty_corner(intel)
        p5 = self.strat.make_default_choice(intel)
        priority_list = [p1, p2, p3, p4, p5]
        return priority_list

    def get_intelligence(self, board):
        intel = { 'board': board, 
                  'options': self.get_legal_moves(board),
                  'analysis': self.scan_board(board),
                  'marker_code': self.marker_code, 
                  'enemy_code': self.get_enemy_code() }
        return intel
