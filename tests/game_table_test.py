import nose.tools
from source.game_table import * 



def test_game_board_returns_a_2Dlist():
    table = TableTop()
    test = all(isinstance(row, list) for row in table.board)
    assert test ==  True

def test_game_board_initial_state():
    table = TableTop()
    expected = [[0,0,0],[0,0,0],[0,0,0]]
    assert table.board == expected

def test_game_board_can_be_changed():
    table = TableTop()
    expected = [[0,0,1],[0,0,0],[0,0,0]]
    table.board = expected
    assert table.board == expected 
