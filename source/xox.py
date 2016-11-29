from referee_chair import Referee
from player_chair import *
from game_table import TableTop

def play_xox():
    tabletop = TableTop()
    player1 = Human()
    player2 = Computer()
    ref = Referee(tabletop, player1, player2)
    ref.start_game()

if __name__ == "__main__":
    play_xox()
