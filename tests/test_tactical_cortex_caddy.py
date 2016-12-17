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

        self.opt_f = [ 0,1,2,
                       3,4,5,
                       6,7,8 ]

        self.row_0 = [     2,
                       3,4,5, 
                       6,7,8 ]

        self.row_1 = [ 0,1,2,
                           5,
                       6,7,8 ]

        self.row_2 = [ 0,1,2,
                       3,4,5,
                         7   ]

        self.col_3 = [   1,2,
                       3,4,5,
                         7,8 ]

        self.col_4 = [ 0,1,2,
                       3,  5, 
                       6,  8 ]

        self.col_5 = [ 0,1,  
                       3,4,   
                       6,7,8 ]

        self.diag6 = [ 0,1,2,
                       3,  5,
                       6,7,  ]

        self.diag7 = [ 0,1,  
                       3,  5,
                       6,7,8 ]

        self.expected = [False, 2,5,7, 3,1,8, 0,6]

    def test_take_win_chance(self):
        dic_f = { 'analysis': self.ana_f,'options': self.opt_f,
                  'marker_code': 1 }
        dic_0 = { 'analysis': self.ana_0,'options': self.row_0,
                  'marker_code': 1 }
        dic_1 = { 'analysis': self.ana_1,'options': self.row_1,
                  'marker_code': 1 }
        dic_2 = { 'analysis': self.ana_2,'options': self.row_2,
                  'marker_code': 1 }
        dic_3 = { 'analysis': self.ana_3,'options': self.col_3,
                  'marker_code': 1 }
        dic_4 = { 'analysis': self.ana_4,'options': self.col_4,
                  'marker_code': 1 }
        dic_5 = { 'analysis': self.ana_5,'options': self.col_5,
                  'marker_code': 1 }
        dic_6 = { 'analysis': self.ana_6,'options': self.diag6,
                  'marker_code': 1 }
        dic_7 = { 'analysis': self.ana_7,'options': self.diag7,
                  'marker_code': 1 }
        tf = self.cortex.take_win_chance(dic_f)
        t0 = self.cortex.take_win_chance(dic_0)
        t1 = self.cortex.take_win_chance(dic_1)
        t2 = self.cortex.take_win_chance(dic_2)
        t3 = self.cortex.take_win_chance(dic_3)
        t4 = self.cortex.take_win_chance(dic_4)
        t5 = self.cortex.take_win_chance(dic_5)
        t6 = self.cortex.take_win_chance(dic_6)
        t7 = self.cortex.take_win_chance(dic_7)
        test_yields = [tf, t0,t1,t2, t3,t4,t5, t6,t7]
        self.assertEqual(test_yields, self.expected)

    def test_avoid_losing(self):
        dic_f = { 'analysis': self.ana_f,'options': self.opt_f,
                  'enemy_code': 1 }
        dic_0 = { 'analysis': self.ana_0,'options': self.row_0,
                  'enemy_code': 1 }
        dic_1 = { 'analysis': self.ana_1,'options': self.row_1,
                  'enemy_code': 1 }
        dic_2 = { 'analysis': self.ana_2,'options': self.row_2,
                  'enemy_code': 1 }
        dic_3 = { 'analysis': self.ana_3,'options': self.col_3,
                  'enemy_code': 1 }
        dic_4 = { 'analysis': self.ana_4,'options': self.col_4,
                  'enemy_code': 1 }
        dic_5 = { 'analysis': self.ana_5,'options': self.col_5,
                  'enemy_code': 1 }
        dic_6 = { 'analysis': self.ana_6,'options': self.diag6,
                  'enemy_code': 1 }
        dic_7 = { 'analysis': self.ana_7,'options': self.diag7,
                  'enemy_code': 1 }
        tf = self.cortex.avoid_losing(dic_f)
        t0 = self.cortex.avoid_losing(dic_0)
        t1 = self.cortex.avoid_losing(dic_1)
        t2 = self.cortex.avoid_losing(dic_2)
        t3 = self.cortex.avoid_losing(dic_3)
        t4 = self.cortex.avoid_losing(dic_4)
        t5 = self.cortex.avoid_losing(dic_5)
        t6 = self.cortex.avoid_losing(dic_6)
        t7 = self.cortex.avoid_losing(dic_7)
        test_yields = [tf, t0,t1,t2, t3,t4,t5, t6,t7]
        self.assertEqual(test_yields, self.expected)

    def test_take_fork_chance(self):
        pass

    def test_avoid_fork(self):
        pass
