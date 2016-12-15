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
        self.bd_x = [0,0,0, 0,1,0, 0,0,0]
        self.bd_o = [1,0,0, 0,10,0, 0,0,0]
        self.bdnw = [10,0,0, 0,1,0, 0,0,0]
        self.bdse = [0,0,0, 0,1,0, 0,0,10]
        self.bdne = [0,0,10, 0,1,0, 0,0,0]
        self.bdsw = [0,0,0, 0,1,0, 10,0,0]
        self.optnw = [  1,2,3,  5,6,7,8]
        self.optse = [0,1,2,3,  5,6,7  ]
        self.optne = [0,1,  3,  5,6,7,8]
        self.optsw = [0,1,2,3,  5,  7,8]
        self.ana_x = [0,1,0,0,1,0,1,1]
        self.ana_o = [0,10,0,0,10,0,11,10]
        self.ananw = [10,1,0,10,1,0,11,1]
        self.anase = [0,1,10,0,1,10,11,1]
        self.anane = [10,1,0,0,1,10,1,11]
        self.anasw = [0,1,10,10,1,0,1,11]

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
        dic_x = { 'board': self.bd_x, 'analysis': self.ana_x,
                  'marker_code': 1, 'options': self.optnw }
        dic_o = { 'board': self.bd_o, 'analysis': self.ana_o,
                  'marker_code': 1, 'options': self.optnw }
        dicnw = { 'board': self.bdnw, 'analysis': self.ananw,
                  'marker_code': 1, 'options': self.optnw }
        dicse = { 'board': self.bdse, 'analysis': self.anase, 
                  'marker_code': 1, 'options': self.optse }
        dicne = { 'board': self.bdne, 'analysis': self.anane,
                  'marker_code': 1, 'options': self.optne }
        dicsw = { 'board': self.bdsw, 'analysis': self.anasw,
                  'marker_code': 1, 'options': self.optsw }
        test_x = self.cortex.take_catty_corner(dic_x)
        test_o = self.cortex.take_catty_corner(dic_o)
        testnw = self.cortex.take_catty_corner(dicnw)
        testse = self.cortex.take_catty_corner(dicse)
        testne = self.cortex.take_catty_corner(dicne)
        testsw = self.cortex.take_catty_corner(dicsw)
        self.assertEqual(test_x, False)
        self.assertEqual(test_o, False)
        self.assertEqual(testnw, 8)
        self.assertEqual(testse, 0)
        self.assertEqual(testne, 6)
        self.assertEqual(testsw, 2)

    def test_take_the_center_takes_the_center(self):
        dic0 = {'options': self.opt0}
        dic5 = {'options': self.opt5}
        test_aye = self.cortex.take_the_center(dic0)
        test_ney = self.cortex.take_the_center(dic5)
        self.assertEqual(test_aye, 4)
        self.assertEqual(test_ney, False)
