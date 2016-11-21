import nose.tools
from source.referee_highchair import *

def test_referee_is_an_object():
    referee = Referee()
    assert isinstance(referee, object) == True

def test_check_for_draw_can_do_so():
    referee = Referee()
    false_board = [1,10,1,0,10,0,1,0,10]
    true_board = [1,1,10,10,10,1,1,10,1]
    assert referee.check_for_draw() == False 
    assert referee.check_for_draw() == True

