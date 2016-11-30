from referee_chair import Referee
from game_table import TableTop

def play_xox():
    tabletop = TableTop()
    ref = Referee(tabletop)
    ref.start_game()

if __name__ == "__main__":
    play_xox()
