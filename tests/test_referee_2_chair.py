import unittest
from source.referee_2_chair import *
from source.announcer_chair import *
from source.player_chair import *
from source.game_table import *
from source.judge_pit import*

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
        self.announcer = MuteAnnouncer()
        self.moves_taken = 0
    

class RefereeTestCase(unittest.TestCase):

    def setUp(self):
        self.table_top = TableTop()
        self.ref = DummyRef(self.table_top)
        self.announcer = MuteAnnouncer()

    def test_referee_ties_when_all_squares_taken_no_winner(self):
        pass

    def test_referee_returns_win_even_if_all_squares_taken(self):
        pass

    def test_referee_moves_taken_plus_1_when_it_takes_a_turn(self):
        pass

    def test_referee_changes_the_board_when_it_takes_a_turn(self):
        pass

    def test_show_board_shows_the_board(self):
        board = self.announcer.render_board(self.table_top.board)
        expected = self.announcer.show(board)
        test_yields = self.ref.show_board()
        self.assertEqual(test_yields, expected)
