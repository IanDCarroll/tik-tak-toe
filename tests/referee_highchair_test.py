import nose.tools
from source.referee_highchair import *

def test_referee_is_an_object():
    referee = Referee('fake_board','fake_P1', 'fake_p2')
    assert isinstance(referee, object) == True

def test_check_for_draw_can_do_so():
    false_board = [1,10,1,0,10,0,1,0,10]
    true_board = [1,1,10,10,10,1,1,10,1]
    false_ref = Referee(false_board, 'P1', 'P2')
    true_ref = Referee(true_board, 'P1', 'P2')
    assert false_ref.check_for_draw() == False 
    assert true_ref.check_for_draw() == True

