import unittest
from source.carpenter_shop import *

class CarpenterTestCase(unittest.TestCase):

    def setUp(self):
        self.carpenter = Carpenter()
        self.mock_board = [1,10,1, 0,10,0, 1,0,10]
        self.rendered_board = '''
\033[91m X \033[0m|\033[34m O \033[0m|\033[91m X \033[0m
---+---+---
\033[30m 4 \033[0m|\033[34m O \033[0m|\033[30m 6 \033[0m
---+---+---
\033[91m X \033[0m|\033[30m 8 \033[0m|\033[34m O \033[0m
'''

    def test_rendered_board_is_rendered_well(self):
        pass

    def test_number_square_numbers_square(self):
        pass

    def test_stringify_board_stringifies_the_board(self):
        pass

    def test_construct_board_builds_the_board(self):
        pass

    def test_assemble_rack_builds_a_rack(self):
        pass

    def test_assemble_rows_builds_a_list_of_rows(self):
        pass

    def test_build_proto_row_builds_a_list_of_row_bits(self):
        pass
