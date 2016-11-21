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

def test_check_for_winner_can_do_so():
    false_board = [1,10,1,0,10,0,1,0,10]
    edge_board = [1,1,10,10,10,1,1,10,1]
    center_board = [1,10,1,0,10,0,1,10,0]
    diagonal_board = [1,10,1,10,1,0,1,0,10]
    cross_board = [1,0,1,10,10,10,0,0,1]
    false_ref = Referee(false_board, 'P1', 'P2')
    edge_ref = Referee(edge_board, 'P1', 'P2')
    center_ref = Referee(center_board, 'P1', 'P2')
    diagonal_ref = Referee(diagonal_board, 'P1', 'P2')
    cross_ref = Referee(cross_board, 'P1', 'P2')
    assert false_ref.check_for_winner() == False 
    assert edge_ref.check_for_winner() == True
    assert center_ref.check_for_winner() == True
    assert diagonal_ref.check_for_winner() == True
    assert cross_ref.check_for_winner() == True
