import unittest
from Scenery.cli_display import *

class Helper(object):
     def get_methods(self, obj):
         return [i for i in dir(obj) if callable(getattr(obj, i))]

class AnnouncerTestCase(unittest.TestCase):

    def setUp(self):
        self.ui = TerminalInterface("fake_board_object")
        self.helper = Helper()
        self.methodList = self.helper.get_methods(self.ui)

    def test_announcer_is_a_class(self):
        self.assertIsInstance(self.ui, TerminalInterface)

    def test_announcer_has_a_show_method(self):
        self.assertTrue('show' in self.methodList)

    def test_announcer_has_an_ask_human_method(self):
        self.assertTrue('ask_human' in self.methodList)
