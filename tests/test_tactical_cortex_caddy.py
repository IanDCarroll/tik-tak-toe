import unittest
from Training.tactical_3x3_lobe_slot import *

class Tactical3x3LobeTestCase(unittest.TestCase):

    def setUp(self):
        self.lobe = TacticalLobe()
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

        self.empty_board = { 'board': [0,0,0, 0,0,0, 0,0,0], 
                             'analysis': [0,0,0, 0,0,0, 0,0] }
        self.fork_with_6a = { 'board': [1,10,0, 0,1,0, 0,0,10] }
        self.fork_with_6b = { 'board': [10,0,0, 0,1,10, 0,0,1] }
        self.fork_with_8a = { 'board': [0,10,1, 0,1,0, 10,0,0] }
        self.fork_with_8b = { 'board': [0,0,10, 10,1,0, 1,0,0] }
        self.avoid_fork_1 = { 'analysis': [1,10,1, 1,10,1, 12,10] }
        self.avoid_fork_2 = { 'analysis': [1,10,1, 1,10,1, 10,12] }

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
        tf = self.lobe.take_win_chance(dic_f)
        t0 = self.lobe.take_win_chance(dic_0)
        t1 = self.lobe.take_win_chance(dic_1)
        t2 = self.lobe.take_win_chance(dic_2)
        t3 = self.lobe.take_win_chance(dic_3)
        t4 = self.lobe.take_win_chance(dic_4)
        t5 = self.lobe.take_win_chance(dic_5)
        t6 = self.lobe.take_win_chance(dic_6)
        t7 = self.lobe.take_win_chance(dic_7)
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
        tf = self.lobe.avoid_losing(dic_f)
        t0 = self.lobe.avoid_losing(dic_0)
        t1 = self.lobe.avoid_losing(dic_1)
        t2 = self.lobe.avoid_losing(dic_2)
        t3 = self.lobe.avoid_losing(dic_3)
        t4 = self.lobe.avoid_losing(dic_4)
        t5 = self.lobe.avoid_losing(dic_5)
        t6 = self.lobe.avoid_losing(dic_6)
        t7 = self.lobe.avoid_losing(dic_7)
        test_yields = [tf, t0,t1,t2, t3,t4,t5, t6,t7]
        self.assertEqual(test_yields, self.expected)

    def test_take_fork_chance(self):
        test_f = self.lobe.take_fork_chance(self.empty_board)
        test_6a = self.lobe.take_fork_chance(self.fork_with_6a)
        test_6b = self.lobe.take_fork_chance(self.fork_with_6b)
        test_8a = self.lobe.take_fork_chance(self.fork_with_8a)
        test_8b = self.lobe.take_fork_chance(self.fork_with_8b)
        self.assertEqual(test_f, False)
        self.assertEqual(test_6a, 6)
        self.assertEqual(test_6b, 6)
        self.assertEqual(test_8a, 8)
        self.assertEqual(test_8b, 8)

    def test_avoid_fork(self):
        test_f = self.lobe.avoid_fork(self.empty_board)
        test_1 = self.lobe.avoid_fork(self.avoid_fork_1)
        test_2 = self.lobe.avoid_fork(self.avoid_fork_2)
        self.assertEqual(test_f, False)
        self.assertEqual(test_1, 1)
        self.assertEqual(test_2, 1)
