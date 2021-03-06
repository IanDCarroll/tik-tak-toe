import unittest
from Scenery.carpenter_shop import *

class CarpenterTestCase(unittest.TestCase):

    def setUp(self):
        self.carpenter = Carpenter()
        self.mock_board = [1,10,1, 0,10,0, 1,0,10]
        self.square_4 = '\033[90m 5 \033[0m'
        self.stringy_board = ['\033[91m X \033[0m',
         '\033[34m O \033[0m','\033[91m X \033[0m',
         '\033[90m 4 \033[0m','\033[34m O \033[0m',
         '\033[90m 6 \033[0m','\033[91m X \033[0m',
         '\033[90m 8 \033[0m','\033[34m O \033[0m']
        self.rack = '\n---+---+---\n'
        self.proto_row = ['\033[90m 4 \033[0m',
                          '\033[34m O \033[0m',
                          '\033[90m 6 \033[0m']
        self.rows = [ 
'\033[91m X \033[0m|\033[34m O \033[0m|\033[91m X \033[0m',
'\033[90m 4 \033[0m|\033[34m O \033[0m|\033[90m 6 \033[0m',
'\033[91m X \033[0m|\033[90m 8 \033[0m|\033[34m O \033[0m']
        self.rendered_board = '''
\033[91m X \033[0m|\033[34m O \033[0m|\033[91m X \033[0m
---+---+---
\033[90m 4 \033[0m|\033[34m O \033[0m|\033[90m 6 \033[0m
---+---+---
\033[91m X \033[0m|\033[90m 8 \033[0m|\033[34m O \033[0m
'''

    def test_rendered_board_is_rendered_well(self):
        test_yields = self.carpenter.render_board(self.mock_board)
        self.assertEqual(test_yields, self.rendered_board)

    def test_number_square_numbers_square(self):
        test_yields = self.carpenter.number_square(4)
        self.assertEqual(test_yields, self.square_4)

    def test_stringify_board_stringifies_the_board(self):
        test = self.carpenter.stringify_board(self.mock_board)
        self.assertEqual(test, self.stringy_board)

    def test_construct_board_builds_the_board(self):
        test = self.carpenter.construct_board(self.stringy_board)
        self.assertEqual(test, self.rendered_board)

    def test_assemble_rack_builds_a_rack(self):
        test = self.carpenter.assemble_rack(self.stringy_board)
        self.assertEqual(test, self.rack)

    def test_assemble_rows_builds_a_list_of_rows(self):
        test = self.carpenter.assemble_rows(self.stringy_board)
        self.assertEqual(test, self.rows)

    def test_build_proto_row_builds_a_list_of_row_bits(self):
        test = self.carpenter.build_proto_row(self.stringy_board, 3)
        self.assertEqual(test, self.proto_row)
