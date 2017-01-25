import unittest
from BackStage.referee_chair import *
from BackStage.judge_pit import*
from Scenery.announcer_chair import *
from Scenery.carpenter_shop import *
from OnStage.player_chair import *
from OnStage.game_table import *

class MuteAnnouncer(Announcer):
    def show(self, statement):
        return statement

class DummyHuman(Player):
    name = 'human'
        
class DummyComp(Player):
    name = 'computer'

class DummyTable(TableTop):
    def __init__(self):
        self.board = [0,0,0, 0,0,0, 0,0,0]
        self.noughts = 10
        self.crosses = 1
        self.player1 = DummyHuman(self.crosses)
        self.player2 = DummyComp(self.noughts)
        self.whos_turn = self.player1

    def give_computer_the_first_move(self):
        self.player1 = DummyComp(self.crosses)
        self.player2 = DummyHuman(self.noughts)
        self.whos_turn = self.player1

class DummyRef(Referee):
    def __init__(self, board_object):
        self.table_top = board_object
        self.judge = Judge(self.table_top)
        self.ui = MuteAnnouncer()
        self.carpenter = Carpenter()
        self.moves_taken = 0
    

class RefereeTestCase(unittest.TestCase):

    def setUp(self):
        self.table_top = DummyTable()
        self.ref = DummyRef(self.table_top)
        self.announcer = MuteAnnouncer()
        self.carpenter = Carpenter()
        self.first_move_board = [1,0,0, 0,0,0, 0,0,0]
        self.won_board = [1,10,1, 10,1,10, 1,0,0] 

    def test_referee_ties_when_all_squares_taken_no_winner(self):
        self.ref.moves_taken = 9
        self.assertEqual(self.ref.facilitate_turns(), 'tie')

    def test_referee_returns_win_even_if_all_squares_taken(self):
        self.ref.table_top.board = self.won_board
        self.ref.table_top.give_next_player_a_go() # sim sideEffect
        self.assertEqual(self.ref.facilitate_turns(), 'human')

    def test_referee_switches_players_when_it_takes_a_turn(self):
        self.ref.take_a_turn()
        test_yields = self.ref.table_top.whos_turn
        self.assertEqual(test_yields, self.ref.table_top.player2)

    def test_referee_moves_taken_plus_1_when_it_takes_a_turn(self):
        self.ref.take_a_turn()
        self.assertEqual(self.ref.moves_taken, 1)

    def test_referee_changes_the_board_when_it_takes_a_turn(self):
        self.ref.take_a_turn()
        test_yields = self.ref.table_top.board
        self.assertEqual(test_yields, self.first_move_board)

    def test_show_board_shows_the_board(self):
        board = self.carpenter.render_board(self.table_top.board)
        expected = self.announcer.show(board)
        test_yields = self.ref.show_board()
        self.assertEqual(test_yields, expected)
