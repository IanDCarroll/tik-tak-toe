import nose.tools
from source.game_board import * 



def test_game_board_returns_a_2Dlist():
    board = Game_Board()
    test = all(isinstance(row, list) for row in board.current_board)
    assert test ==  True

def test_game_board_initial_state():
    board = Game_Board()
    expected = [[0,0,0],[0,0,0],[0,0,0]]
    assert board.current_board == expected

def test_game_board_can_be_changed():
    board = Game_Board()
    expected = [[0,0,1],[0,0,0],[0,0,0]]
    board.current_board = expected
    assert board.current_board == expected 
