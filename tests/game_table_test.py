import nose.tools
from source.game_table import * 

def test_that_board_returns_a_list():
    table_top = TableTop()
    test = isinstance(table_top.board, list)
    assert test ==  True

def test_the_boards_initial_state():
    table_top = TableTop()
    expected = [0,0,0,0,0,0,0,0,0]
    assert table_top.board == expected

def test_that_board_can_be_changed():
    table_top = TableTop()
    expected = [0,0,1,0,0,0,0,0,0]
    table_top.board = expected
    assert table_top.board == expected

def test_get_board_size_3():
    mock_3x3 = [0,0,0, 0,0,0, 0,0,0]
    table_top = TableTop()
    assert table_top.get_board_size(mock_3x3) == 3

def test_get_board_size_4():
    mock_4x4 = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
    table_top = TableTop()
    assert table_top.get_board_size(mock_4x4) == 4
