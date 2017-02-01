import unittest
from BackStage.stage_manager_booth import *
from BackStage.referee_chair import *
from BackStage.emcee_podium import *
from Scenery.cli_display import *
from OnStage.player_chair import *
from OnStage.game_table import *

class MuteUI(TerminalInterface):
    def show(self, statement):
        return statement
    def refresh(self):
        return self.display()
    def ask_human(self):
        return '1'

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
        self.start_of_game = True
        self.tie = False
        self.win = False
        self.error = False
        self.exit = False

    def give_computer_the_first_move(self):
        self.player1 = DummyComp(self.crosses)
        self.player2 = DummyHuman(self.noughts)
        self.whos_turn = self.player1

class DummyRef(Referee):
    def __init__(self, board_object, user_interface):
        self.table_top = board_object
        self.judge = Judge(self.table_top)
        self.ui = user_interface
        self.moves_taken = 0

class DummyMC(Emcee):
    def __init__(self, board, user_interface):
        self.table_top = board
        self.ui = user_interface

    def ask_human(self):
        return '1'

class DummySM(StageManager):
    def __init__(self):
        self.table_top = DummyTable()
        self.ui = MuteUI(self.table_top)
        self.mc = DummyMC(self.table_top, self.ui)
        self.ref = DummyRef(self.table_top, self.ui)

class StageManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.stage_manager = DummySM()
        self.ui = MuteUI("fake_board_object")

    def test_stage_manager_can_call_the_show(self):
        game_yields = self.stage_manager.play_game()
        expected = '\n\x1b[91m X \x1b[0m|\x1b[34m O \x1b[0m|\x1b[91m X \x1b[0m\n---+---+---\n\x1b[34m O \x1b[0m|\x1b[91m X \x1b[0m|\x1b[34m O \x1b[0m\n---+---+---\n\x1b[91m X \x1b[0m|\x1b[90m 8 \x1b[0m|\x1b[90m 9 \x1b[0m\n\nWhat?! You Won? Impossible!\nOpen an issue at https://github.com/IanDCarroll/xox/issues/new \nso it can be corrected immediately.\n'
        self.assertEqual(game_yields, expected)
