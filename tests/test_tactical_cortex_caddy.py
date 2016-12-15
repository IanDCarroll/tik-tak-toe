import unittest
from OnStage.tactical_cortex_caddy import *

class TacticalCortexTestCase(unittest.TestCase):

    def setUp(self):
        self.cortex = TacticalCortex()
        self.ana_f = [0,0,0,0,0,0,0,0]
        self.ana_0 = [2,0,0,0,0,0,0,0]
        self.ana_1 = [0,2,0,0,0,0,0,0]
        self.ana_2 = [0,0,2,0,0,0,0,0]
        self.ana_3 = [0,0,0,2,0,0,0,0]
        self.ana_4 = [0,0,0,0,2,0,0,0]
        self.ana_5 = [0,0,0,0,0,2,0,0]
        self.ana_6 = [0,0,0,0,0,0,2,0]
        self.ana_7 = [0,0,0,0,0,0,0,2]
        self.opt_f = [0,1,2, 3,4,5, 6,7,8]
        self.row_0 = [0,1,   3,4,5, 6,7,8]
        self.row_1 = [0,1,2,   4,5, 6,7,8]
        self.row_2 = [0,1,2, 3,4,5, 6,  8]
        self.col_3 = [0,1,2, 3,4,5,  ,7, ]
        self.col_4 = [0,  2, 3,4,5, 6,7,8]
        self.col_5 = [0,1,2, 3,4,   6,7,8]
        self.diag6 = [  1,2, 3,4,5, 6,7,8]
        self.diag7 = [0,1,2, 3,4,5,   7,8]

    def test_take_win_chance(self):
        dic_f = { 'analysis': self.ana_f,'options': self.opt_f,
                  'marker_code': 1 }
        dic_0 = { 'analysis': self.ana_0,'options': self.row_0,
                  'marker_code': 1 }
        dic_1 = { 'analysis': self.ana_1,'options': self.row_1,
                  'marker_code': 1 }
        dic_2 = { 'analysis': self.ana_2,'options': self.row_2,
                  'marker_code': 1 }
        dic_3 = { 'analysis': self.ana_3,'options': self.row_3,
                  'marker_code': 1 }
        dic_4 = { 'analysis': self.ana_4,'options': self.row_4,
                  'marker_code': 1 }
        dic_5 = { 'analysis': self.ana_5,'options': self.row_5,
                  'marker_code': 1 }
        dic_6 = { 'analysis': self.ana_6,'options': self.row_6,
                  'marker_code': 1 }
        dic_7 = { 'analysis': self.ana_7,'options': self.row_7,
                  'marker_code': 1 }

    def test_avoid_losing(self):
        dic_f = { 'analysis': self.ana_f,'options': self.opt_f,
                  'enemy_code': 1 }
        dic_0 = { 'analysis': self.ana_0,'options': self.row_0,
                  'enemy_code': 1 }
        dic_1 = { 'analysis': self.ana_1,'options': self.row_1,
                  'enemy_code': 1 }
        dic_2 = { 'analysis': self.ana_2,'options': self.row_2,
                  'enemy_code': 1 }
        dic_3 = { 'analysis': self.ana_3,'options': self.row_3,
                  'enemy_code': 1 }
        dic_4 = { 'analysis': self.ana_4,'options': self.row_4,
                  'enemy_code': 1 }
        dic_5 = { 'analysis': self.ana_5,'options': self.row_5,
                  'enemy_code': 1 }
        dic_6 = { 'analysis': self.ana_6,'options': self.row_6,
                  'enemy_code': 1 }
        dic_7 = { 'analysis': self.ana_7,'options': self.row_7,
                  'enemy_code': 1 }
