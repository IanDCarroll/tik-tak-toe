import unittest
from source.announcer_2_chair import *

class Helper(object):
     def get_methods(self, obj):
         return [i for i in dir(obj) if callable(getattr(obj, i))]


class AnnouncerTestCase(unittest.TestCase):

    def setUp(self):
        self.announcer = Announcer()
        self.helper = Helper()
        self.methodList = self.helper.get_methods(self.announcer)

    def test_announcer_is_a_class(self):
        self.assertIsInstance(self.announcer, Announcer)

    def test_announcer_has_a_show_method(self):
        pass

    def test_announcer_has_an_ask_human_method(self):
        pass
