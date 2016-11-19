import nose.tools
from source.player_chair import *

class Mock(object):
    def __init__(self):
        self.board = [1,10,1,10,0,0,1,0,10]

def test_that_player_can_make_a_move():
    mock = Mock()
    philip = Player()
    test = philip.move(mock.board)
    assert test == [1,10,1,10,"spam",0,1,0,10]

def test_that_player_can_only_make_legal_moves():
    mock = Mock()
    philip = Player()
    test = philip.get_legal_moves(mock.board)
    assert test == [4,5,7]

def test_that_computer_player_can_make_a_move():
    mock = Mock()
    spamBot9000 = Computer()
    test = spamBot9000.move(mock.board)
    assert test == [1,10,1,1,10,0,1,0,10]
