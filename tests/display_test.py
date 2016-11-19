import nose.tools
from source.display import *

def test_display_start_of_game():
    display = Display()
    test = display.start
    assert test == "Welcome"

def test_display_game_over_draw():
    display = Display()
    test = display.draw
    assert test == "Draw"

def test_display_game_over_computer_wins():
    display = Display()
    test = display.computer
    assert test == "Computer Wins"

def test_display_game_over_human_wins():
    display = Display()
    test = display.human
    assert test == "You Win"

def test_display_current_board():
    display = Display()
    mock_board = [1,10,1,0,10,0,1,0,10]
    test = display.render_board(mock_board)
    expected = """
 X | O | X 
---+---+---
   | O |  
---+---+---
 X |   | O 
"""
    assert test == expected

def test_display_ask_for_human_input():
    display = Display()
    test = display.next_move
    assert test == "What is your next move?"

def test_display_human_made_illegal_move():
    display = Display()
    test = display.bad_move
    assert test == "That is not a legal move."
