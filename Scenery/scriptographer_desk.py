from Training.observer_abilities import *

class Scriptographer(Observer):

    start = """
Welcome to XOX, 
a Noughts and Crosses Game you can never win 
no matter how hard you try.
"""
    select = """Type 1 to go first and not win, or 
Type 2 to go second and not win."""
    tie = """Your moves were practically non-incompetent. 
The game is a draw.
"""
    computer = """The computer has deftly exploited 
your pathetic human weaknesses and won the game.
"""
    human = """What?! You Won? Impossible!
Open an issue at https://github.com/IanDCarroll/xox/issues/new 
so it can be corrected immediately.
"""
    question = "Which square do you choose before your inevitable failure to win?"
    pre_choice = "The computer chooses square "
    post_choice = ", a perfect move."
    bad_move = "That's not a legal move, human. Try again."
    strike_3 = """Look, if you're not going to take this seriously, I'm out.
"""
    prompt = "> "

    nought = "\033[34m O \033[0m"
    cross = "\033[91m X \033[0m"
    pre_num = "\033[90m "
    post_num = " \033[0m"
    plank = '---'
    corner = '+'
    wall = '|'
    new_line = '\n'
