import unittest
from Training.cortex_3x3_caddy import *

class Cortex3x3TestCase(unittest.TestCase):

    def setUp(self):
        self.cortex = Cortex_3x3()
        self.intel = { 'board': [10,10,0, 1,1,0, 10,0,1],
                       'options': [2,5,7], 
                       'analysis': [20,2,11, 21,11,1, 12,11],
                       'marker_code': 1,
                       'enemy_code': 10 }
        self.priorities = [5,2,False,False,False,2,2]


    def test_get_priority_list_returns_a_priority_list(self):
        test_yields = self.cortex.get_priority_list(self.intel)
        self.assertEqual(test_yields, self.priorities)

    def test_direct_move_returns_a_direction(self):
        test_yields = self.cortex.direct_move(self.intel)
        self.assertEqual(test_yields, 5)
