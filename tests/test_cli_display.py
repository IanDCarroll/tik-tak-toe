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

    def test_terminalinterface_is_a_class(self):
        self.assertIsInstance(self.ui, TerminalInterface)

    def test_terminalinterface_has_an_ask_human_method(self):
        self.assertTrue('ask_human' in self.methodList)

    def test_terminalinterface_has_a_refresh_method(self):
        self.assertTrue('refresh' in self.methodList)

    def test_display_renders_accurate_displays(self):
        test_start = self.ui.display()
        self.assertEqual(test_start, self.start_message)
