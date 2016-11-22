import nose.tools
from source.announcer_chair import *

def test_display_start_of_game():
    announcer = Announcer()
    test = announcer.start
    assert test == "Welcome"

def test_display_game_over_tie():
    announcer = Announcer()
    test = announcer.tie
    assert test == "Draw"

def test_display_game_over_computer_wins():
    announcer = Announcer()
    test = announcer.computer
    assert test == "Computer Wins"

def test_display_game_over_human_wins():
    announcer = Announcer()
    test = announcer.human
    assert test == "You Win"

def test_display_current_board():
    announcer = Announcer()
    mock_board = [1,10,1, 0,10,0, 1,0,10]
    test = announcer.render_board(mock_board)
    expected = """
 X | O | X 
---+---+---
   | O |   
---+---+---
 X |   | O 
"""
    assert test == expected

def test_display_ask_for_human_input():
    announcer = Announcer()
    test = announcer.next_move
    assert test == "What is your next move?"

def test_display_human_made_illegal_move():
    announcer = Announcer()
    test = announcer.bad_move
    assert test == "That is not a legal move."
