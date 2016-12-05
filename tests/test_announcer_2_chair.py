import unittest
from source.announcer_2_chair import *

class AnnouncerTestCase(unittest.TestCase):

    def setUp(self):
        self.announcer = Announcer()
        self.methodList = [method for method in dir(self.announcer) if callable(getattr(self.announcer, method))]

    def test_announcer_is_a_class(self):
        self.assertIsInstance(self.announcer, Announcer)

    def test_announcer_has_a_show_method(self):
        pass

    def test_announcer_has_an_ask_human_method(self):
        pass
