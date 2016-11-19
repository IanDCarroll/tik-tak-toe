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
    assert test == "Human Wins"

def test_display_current_board():
    pass

def test_display_computers_last_move():
    pass

def test_display_ask_for_human_input():
    pass

def test_display_human_made_illegal_move():
    pass
