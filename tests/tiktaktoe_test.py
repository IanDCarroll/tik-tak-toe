import nose.tools
from source import * 



def test_game_board_returns_a_list():
    board = Game_Board()
    board_right_now = getattr(board, 'current_board')
    test = all(isinstance(row, list) for row in board_right_now)
    assert test ==  True
