import unittest
from OnStage.computer_dais import *

class ComputerTestCase(unittest.TestCase):

    def setUp(self):
        self.hal = Computer(1)
        self.holly = Computer(10)
        self.win_chance = [10,10,0, 0,0,0, 0,1,1]
        self.loose_chance = [10,0,1, 0,1,0, 10,0,0]
        self.fork_chance = [1,10,0, 0,1,0, 0,0,10]
        self.lose_fork_1 = [1,0,0, 0,10,0, 0,0,1]
        self.lose_fork_2 = [0,0,1, 0,10,0, 1,0,0]
        self.empty_board = [0,0,0, 0,0,0, 0,0,0]
        self.hollow_board = [1,10,0, 0,0,0, 10,1,0]
        self.NE_corner = [0,0,10, 0,1,0, 0,0,0]
        self.center_board = [10,0,0, 1,1,10, 10,0,1]
        self.diagon_board = [10,0,1, 1,1,10, 10,0,1]

        self.win = [10,10,0, 0,0,0, 1,1,1]
        self.dont_loose = [10,0,1, 1,1,0, 10,0,0]
        self.forked = [1,10,0, 0,1,0, 1,0,10]
        self.unforked_1 = [1,10,0, 0,10,0, 0,0,1]
        self.unforked_2 = [0,10,1, 0,10,0, 1,0,0]
        self.no_win_chance = [10,0,0, 0,1,0, 0,0,0]
        self.fill_center = [0,0,0, 0,1,0, 0,0,0]
        self.fill_hollows = [1,10,0, 0,1,0, 10,1,0]
        self.catty_corner = [0,0,10, 0,1,0, 1,0,0]
        self.fill_corners = [10,0,1, 1,1,10, 10,0,1]
        self.fill_whatevs = [10,1,1, 1,1,10, 10,0,1]

        self.all_open = [0,1,2,3,4,5,6,7,8]
        self.all_zero = [0,0,0,0,0,0,0,0]

        self.ask_board = [10,10,0, 1,1,0, 10,0,1]
        self.intel = [5,2,False,False,False,2,2]

    def test_computer_chooses_to_win(self):
        test_yields = self.hal.move(self.win_chance)
        self.assertEqual(test_yields, self.win)

    def test_computer_doesnt_let_you_win(self):
        test_yields = self.hal.move(self.loose_chance)
        self.assertEqual(test_yields, self.dont_loose)

    def test_computer_forks(self):
        test_yields = self.hal.move(self.fork_chance)
        self.assertEqual(test_yields, self.forked)

    def test_computer_does_not_allow_itself_to_be_forked(self):
        test_1_yields = self.holly.move(self.lose_fork_1)
        test_2_yields = self.holly.move(self.lose_fork_2)
        self.assertEqual(test_1_yields, self.unforked_1)
        self.assertEqual(test_2_yields, self.unforked_2)

    def test_computer_prefers_the_center_to_all_else(self):
        test_yields = self.hal.move(self.empty_board)
        self.assertEqual(test_yields, self.fill_center)
        test_yields = self.hal.move(self.hollow_board)
        self.assertEqual(test_yields, self.fill_hollows)

    def test_computer_prefers_oposite_corner_to_other_corners(self):
        test_yields = self.hal.move(self.NE_corner)
        self.assertEqual(test_yields, self.catty_corner)

    def test_computer_prefers_corners_to_edges(self):
        test_yields = self.hal.move(self.center_board)
        self.assertEqual(test_yields, self.fill_corners)

    def test_computer_will_choose_edges_as_a_last_resort(self):
        test_yields = self.hal.move(self.diagon_board)
        self.assertEqual(test_yields, self.fill_whatevs)

    def test_computer_can_get_intelligence_for_cortecies(self):
        test_yields = self.hal.get_intelligence(self.empty_board)
        self.assertEqual(test_yields['board'], self.empty_board)
        self.assertEqual(test_yields['options'], self.all_open)
        self.assertEqual(test_yields['analysis'], self.all_zero)
        self.assertEqual(test_yields['marker_code'], 1)
        self.assertEqual(test_yields['enemy_code'], 10)

    def test_ask_cortecies_returns_a_priority_list(self):
        test_yields = self.hal.ask_cortecies(self.ask_board)
        self.assertEqual(test_yields, self.intel)

    def test_choose_returns_a_choice(self):
        test_yields = self.hal.choose(self.ask_board)
        self.assertEqual(test_yields, 5)
