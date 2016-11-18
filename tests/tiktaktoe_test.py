import nose.tools
from source.game_board import * 



def test_game_board_returns_a_2Dlist():
    board = Game_Board()
    board_right_now = getattr(board, 'current_board')
    test = all(isinstance(row, list) for row in board_right_now)
    assert test ==  True

def test_game_board_initial_state():
    board = Game_Board()
    test = getattr(board, 'current_board')
    expected = [[0,0,0],[0,0,0],[0,0,0]]
    assert test == expected
