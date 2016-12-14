import unittest
from OnStage.strategic_cortex_caddy import *

class StrategicCortextTestCase(unittest.TestCase):

    def setUp(self):
        self.cortex = StrategicCortex()
        self.opt0 = [0,1,2,3,4,5,6,7,8]
        self.opt2 = [  1,2,3,4,5,6,7,8]
        self.opt6 = [  1,  3,4,5,6,7,8]
        self.opt8 = [  1,  3,4,5,  7,8]
        self.opt1 = [  1,  3,4,5,  7  ]
        self.opt3 = [      3,4,5,  7  ]
        self.opt4 = [        4,5,  7  ]
        self.opt5 = [          5,  7  ]
        self.opt7 = [              7  ]
        self.board_0 = [0,0,0, 0,1,0, 0,0,0]
        self.x = 1
        self.o = 10
        self.optnw = [4,8]
        self.optse = [0,4]
        self.optne = [2,4]
        self.optsw = [4,6]
        self.ananw = [0,0,0,0,0,0,11,0]
        self.anase = [0,0,0,0,0,0,11,0]
        self.anane = [0,0,0,0,0,0,0,11]
        self.anasw = [0,0,0,0,0,0,0,11]

    def test_make_default_choice_chooses_the_right_order(self):
        dic0 = {'options': self.opt0}
        dic1 = {'options': self.opt1}
        dic2 = {'options': self.opt2}
        dic3 = {'options': self.opt3}
        dic4 = {'options': self.opt4}
        dic5 = {'options': self.opt5}
        dic6 = {'options': self.opt6}
        dic7 = {'options': self.opt7}
        dic8 = {'options': self.opt8}
        test_0 = self.cortex.make_default_choice(dic0)
        test_1 = self.cortex.make_default_choice(dic1)
        test_2 = self.cortex.make_default_choice(dic2)
        test_3 = self.cortex.make_default_choice(dic3)
        test_4 = self.cortex.make_default_choice(dic4)
        test_5 = self.cortex.make_default_choice(dic5)
        test_6 = self.cortex.make_default_choice(dic6)
        test_7 = self.cortex.make_default_choice(dic7)
        test_8 = self.cortex.make_default_choice(dic8)
        self.assertEqual(test_0, 0)
        self.assertEqual(test_1, 1)
        self.assertEqual(test_2, 2)
        self.assertEqual(test_3, 3)
        self.assertEqual(test_4, 4)
        self.assertEqual(test_5, 5)
        self.assertEqual(test_6, 6)
        self.assertEqual(test_7, 7)
        self.assertEqual(test_8, 8)

    def test_take_catty_corner_does_appropriately(self):
        

    def test_take_the_center_takes_the_center(self):
        dic0 = {'options': self.opt0}
        dic5 = {'options': self.opt5}
        test_aye = self.cortex.take_the_center(dic0)
        test_ney = self.cortex.take_the_center(dic5)
        self.assertEqual(test_aye, 4)
        self.assertEqual(test_ney, False)
