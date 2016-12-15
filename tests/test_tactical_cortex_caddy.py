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
        dic_f = { 'analysis': ,'options': ,'marker_code':}
        dic_0 = { 'analysis': ,'options': ,'marker_code':}
        dic_1 = { 'analysis': ,'options': ,'marker_code':}
        dic_2 = { 'analysis': ,'options': ,'marker_code':}
        dic_3 = { 'analysis': ,'options': ,'marker_code':}
        dic_4 = { 'analysis': ,'options': ,'marker_code':}
        dic_5 = { 'analysis': ,'options': ,'marker_code':}
        dic_6 = { 'analysis': ,'options': ,'marker_code':}
        dic_7 = { 'analysis': ,'options': ,'marker_code':}
  

    def test_avoid_losing(self):
        dic_f = { 'analysis': ,'options': ,'marker_code':}
        dic_0 = { 'analysis': ,'options': ,'marker_code':}
        dic_1 = { 'analysis': ,'options': ,'marker_code':}
        dic_2 = { 'analysis': ,'options': ,'marker_code':}
        dic_3 = { 'analysis': ,'options': ,'marker_code':}
        dic_4 = { 'analysis': ,'options': ,'marker_code':}
        dic_5 = { 'analysis': ,'options': ,'marker_code':}
        dic_6 = { 'analysis': ,'options': ,'marker_code':}
        dic_7 = { 'analysis': ,'options': ,'marker_code':}
