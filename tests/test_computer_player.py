import unittest
from OnStage.player_chair import Computer
from OnStage.game_table import *
from Scenery.cli_display import *


class MuteComputer(Computer):
      def __init__(self, marker_code):
          self.marker_code = marker_code

class ComputerTestCase(unittest.TestCase):

    def setUp(self):
        self.hal = MuteComputer(1)
        self.holly = MuteComputer(10)
        self.table_top = TableTop()
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

    def test_computer_chooses_to_win(self):
        self.table_top.board = self.win_chance
        test_yields = self.hal.move(self.table_top)
        self.assertEqual(test_yields, self.win)

    def test_computer_doesnt_let_you_win(self):
        self.table_top.board = self.loose_chance
        test_yields = self.hal.move(self.table_top)      
        self.assertEqual(test_yields, self.dont_loose)

    def test_computer_forks(self):
        self.table_top.board = self.fork_chance
        test_yields = self.hal.move(self.table_top)
        self.assertEqual(test_yields, self.forked)

    def test_computer_does_not_allow_itself_to_be_forked(self):
        self.table_top.board = self.lose_fork_1
        test_1_yields = self.holly.move(self.table_top)
        self.assertEqual(test_1_yields, self.unforked_1)
        self.table_top.board = self.lose_fork_2
        test_2_yields = self.holly.move(self.table_top)
        self.assertEqual(test_2_yields, self.unforked_2)

    def test_computer_prefers_the_center_to_all_else(self):
        self.table_top.board = self.empty_board
        test_yields = self.hal.move(self.table_top)
        self.assertEqual(test_yields, self.fill_center)
        self.table_top.board = self.hollow_board
        test_yields = self.hal.move(self.table_top)
        self.assertEqual(test_yields, self.fill_hollows)

    def test_computer_prefers_oposite_corner_to_other_corners(self):
        self.table_top.board = self.NE_corner
        test_yields = self.hal.move(self.table_top)
        self.assertEqual(test_yields, self.catty_corner)

    def test_computer_prefers_corners_to_edges(self):
        self.table_top.board = self.center_board
        test_yields = self.hal.move(self.table_top)
        self.assertEqual(test_yields, self.fill_corners)

    def test_computer_will_choose_edges_as_a_last_resort(self):
        self.table_top.board = self.diagon_board
        test_yields = self.hal.move(self.table_top)
        self.assertEqual(test_yields, self.fill_whatevs)

    def test_computer_can_get_intelligence_for_cortecies(self):
        test_yields = self.hal.get_intelligence(self.empty_board)
        self.assertEqual(test_yields['board'], self.empty_board)
        self.assertEqual(test_yields['options'], self.all_open)
        self.assertEqual(test_yields['analysis'], self.all_zero)
        self.assertEqual(test_yields['marker_code'], 1)
        self.assertEqual(test_yields['enemy_code'], 10)
