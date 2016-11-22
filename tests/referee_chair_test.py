import nose.tools
from source.referee_chair import *
from source.game_table import * 

def test_referee_is_an_object():
    referee = Referee('fake_board','fake_P1', 'fake_p2')
    assert isinstance(referee, object) == True

def test_check_for_draw_returns_true():
    true_top = TableTop()
    true_top.board = [1,1,10, 10,10,1, 1,10,1]
    true_ref = Referee(true_top, 'P1', 'P2')
    assert true_ref.check_for_tie() == True

def test_check_for_draw_returns_false():
    false_top = TableTop()
    false_top.board = [1,10,1, 0,10,0, 1,0,10]
    false_ref = Referee(false_top, 'P1', 'P2')
    assert false_ref.check_for_tie() == False 

def test_check_for_winner_returns_false():
    false_top = TableTop()
    false_top.board = [1,10,1, 0,10,0, 1,0,10]
    false_ref = Referee(false_top, 'P1', 'P2')
    assert false_ref.check_for_winner() == False 

def test_check_for_winner_does_edges():
    edge_top = TableTop()
    edge_top.board = [1,10,1, 1,10,0, 1,0,10]
    edge_ref = Referee(edge_top, 'P1', 'P2')
    assert edge_ref.check_for_winner() == True

def test_check_for_winner_does_columns():
    column_top = TableTop()
    column_top.board = [1,10,1, 0,10,0, 1,10,0]
    column_ref = Referee(column_top, 'P1', 'P2')
    assert column_ref.check_for_winner() == True

def test_check_for_winner_does_rows():
    row_top = TableTop()
    row_top.board = [1,0,1, 10,10,10 ,0,0,1]
    row_ref = Referee(row_top, 'P1', 'P2')
    assert row_ref.check_for_winner() == True

def test_check_for_winner_does_diagonals():
    diagonal_top = TableTop()
    diagonal_top.board = [1,10,1, 10,1,0, 1,0,10]
    diagonal_ref = Referee(diagonal_top, 'P1', 'P2')
    assert diagonal_ref.check_for_winner() == True

def test_get_board_size_3():
    mock_3x3 = TableTop()
    mock_3x3.board = [0,0,0, 0,0,0, 0,0,0]
    referee = Referee(mock_3x3, 'p1', 'p2')
    assert referee.get_board_size(mock_3x3.board) == 3

def test_get_board_size_4():
    mock_4x4 = TableTop()
    mock_4x4.board = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
    referee = Referee(mock_4x4, 'p1', 'p2')
    assert referee.get_board_size(mock_4x4.board) == 4


