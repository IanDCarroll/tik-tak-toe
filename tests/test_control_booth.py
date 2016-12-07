import unittest
from source.BackStage.control_booth import *
from source.BackStage.referee_chair import *
from source.BackStage.judge_pit import*
from source.Scenery.announcer_chair import *
from source.Scenery.carpenter_shop import *
from source.Scenery.emcee_podium import *
from source.OnStage.player_chair import *
from source.OnStage.game_table import *

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
        self.carpenter = Carpenter()
        self.moves_taken = 0

class DummyMC(Emcee):
    def __init__(self, board):
        self.table_top = board
        self.announcer = MuteAnnouncer()

    def ask_human(self):
        return '1'

class DummySM(StageManager):
    def __init__(self):
        self.table_top = DummyTable()
        self.mc = DummyMC(self.table_top)
        self.ref = DummyRef(self.table_top)

class StageManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.stage_manager = DummySM()
        self.announcer = MuteAnnouncer()

    def test_stage_manager_can_call_the_show(self):
        game_yields = self.stage_manager.play_game()
        expected = self.announcer.human
        self.assertEqual(game_yields, expected)
