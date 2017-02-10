import unittest
from Scenery.cli_display import *
from OnStage.game_table import *

class Helper(object):
     def get_methods(self, obj):
         return [i for i in dir(obj) if callable(getattr(obj, i))]

class TerminalInterfaceTestCase(unittest.TestCase):

    def setUp(self):
        self.table_top = TableTop()
        self.ui = TerminalInterface(self.table_top)
        self.helper = Helper()
        self.methodList = self.helper.get_methods(self.ui)
        self.start_message = '\nWelcome to XOX, \na Noughts and Crosses Game you can never win \nno matter how hard you try.\n\nType 1 to go first and not win, or \nType 2 to go second and not win.'
        self.error_message = 'That\'s not a legal move, human. Try again.'
        self.tie_message = '\n\x1b[90m 1 \x1b[0m|\x1b[90m 2 \x1b[0m|\x1b[90m 3 \x1b[0m\n---+---+---\n\x1b[90m 4 \x1b[0m|\x1b[90m 5 \x1b[0m|\x1b[90m 6 \x1b[0m\n---+---+---\n\x1b[90m 7 \x1b[0m|\x1b[90m 8 \x1b[0m|\x1b[90m 9 \x1b[0m\n\nYour moves were practically non-incompetent. \nThe game is a draw.\n'
        self.win_message = '\n\x1b[90m 1 \x1b[0m|\x1b[90m 2 \x1b[0m|\x1b[90m 3 \x1b[0m\n---+---+---\n\x1b[90m 4 \x1b[0m|\x1b[90m 5 \x1b[0m|\x1b[90m 6 \x1b[0m\n---+---+---\n\x1b[90m 7 \x1b[0m|\x1b[90m 8 \x1b[0m|\x1b[90m 9 \x1b[0m\n\nWhat?! You Won? Impossible!\nOpen an issue at https://github.com/IanDCarroll/xox/issues/new \nso it can be corrected immediately.\n'

    def test_terminalinterface_is_a_class(self):
        self.assertIsInstance(self.ui, TerminalInterface)

    def test_terminalinterface_has_an_ask_human_method(self):
        self.assertTrue('ask_human' in self.methodList)

    def test_terminalinterface_has_a_refresh_method(self):
        self.assertTrue('refresh' in self.methodList)

    def test_display_renders_accurate_displays(self):
        test_start = self.ui.display()
        self.assertEqual(test_start, self.start_message)
        self.assertEqual(self.table_top.start_of_game, False)

        self.table_top.error = True
        test_error = self.ui.display()
        self.assertEqual(test_error, self.error_message)
        self.assertEqual(self.table_top.error, False)

        self.table_top.tie = True
        test_tie = self.ui.display()
        self.assertEqual(test_tie, self.tie_message)
        self.table_top.tie = False

        self.table_top.win = True
        test_win = self.ui.display()
        self.assertEqual(test_win, self.win_message)
        self.table_top.win = False
