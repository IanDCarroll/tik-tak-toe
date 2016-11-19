import nose.tools
from source.player_chair import *

def test_that_player_can_make_a_move():
    philip = Player()
    mock_board = [1,10,1,10,0,0,1,0,10]
    test = philip.move(mock_board)
    assert test == [1,10,1,10,"spam",0,1,0,10]

def test_that_computer_player_can_make_a_move():
    spamBot9000 = Computer()
    mock_board = [1,10,1,0,10,0,1,0,10]
    test = spamBot9000.move(mock_board)
    assert test == [1,10,1,1,10,0,1,0,10]
