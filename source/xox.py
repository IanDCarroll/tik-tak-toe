from referee_chair import Referee
from player_chair import *
from game_table import TableTop

def play_xox():
    tabletop = TableTop()
    ref = Referee(tabletop)
    ref.start_game()

if __name__ == "__main__":
    play_xox()
