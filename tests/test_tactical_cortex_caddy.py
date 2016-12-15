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

    def test_take_win_chance(self):
        pass

    def test_avoid_losing(self):
        pass
