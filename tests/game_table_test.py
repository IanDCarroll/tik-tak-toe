import nose.tools
from source.game_table import * 



def test_that_board_returns_a_2D_list():
    table_top = TableTop()
    test = all(isinstance(row, list) for row in table_top.board)
    assert test ==  True

def test_the_boards_initial_state():
    table_top = TableTop()
    expected = [[0,0,0],[0,0,0],[0,0,0]]
    assert table_top.board == expected

def test_that_board_can_be_changed():
    table_top = TableTop()
    expected = [[0,0,1],[0,0,0],[0,0,0]]
    table_top.board = expected
    assert table_top.board == expected 
