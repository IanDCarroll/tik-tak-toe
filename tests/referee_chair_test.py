import nose.tools
from source.referee_chair import *

def test_referee_is_an_object():
    referee = Referee('fake_board','fake_P1', 'fake_p2')
    assert isinstance(referee, object) == True

def test_check_for_draw_returns_true():
    true_board = [1,1,10,10,10,1,1,10,1]
    true_ref = Referee(true_board, 'P1', 'P2')
    assert true_ref.check_for_draw() == True

def test_check_for_draw_returns_false():
    false_board = [1,10,1,0,10,0,1,0,10]
    false_ref = Referee(false_board, 'P1', 'P2')
    assert false_ref.check_for_draw() == False 

def test_check_for_winner_returns_false():
    false_board = [1,10,1,0,10,0,1,0,10]
    false_ref = Referee(false_board, 'P1', 'P2')
    assert false_ref.check_for_winner() == False 

def test_check_for_winner_does_edges():
    edge_board = [1,10,1,1,10,0,1,0,10]
    edge_ref = Referee(edge_board, 'P1', 'P2')
    assert edge_ref.check_for_winner() == True

def test_check_for_winner_does_columns():
    column_board = [1,10,1,0,10,0,1,10,0]
    column_ref = Referee(column_board, 'P1', 'P2')
    assert column_ref.check_for_winner() == True

def test_check_for_winner_does_rows():
    row_board = [1,0,1,10,10,10,0,0,1]
    row_ref = Referee(row_board, 'P1', 'P2')
    assert row_ref.check_for_winner() == True

def test_check_for_winner_does_diagonals():
    diagonal_board = [1,10,1,10,1,0,1,0,10]
    diagonal_ref = Referee(diagonal_board, 'P1', 'P2')
    assert diagonal_ref.check_for_winner() == True
