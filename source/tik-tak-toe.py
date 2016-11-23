from referee_chair import Referee
from player_chair import *
from game_table import TableTop

def computer_goes_first():
    tabletop = TableTop()
    player1 = Computer()
    player2 = Human()
    ref = Referee(tabletop, player1, player2)
    ref.start_game()

def human_goes_first():
    tabletop = TableTop()
    player1 = Computer()
    player2 = Human()
    ref = Referee(tabletop, player1, player2)
    ref.start_game()

def choose_your_destiny():
    select = raw_input("Type 1 to go first, 2 to go second: ")
    if select == '1':
       human_goes_first()
    elif select == '2':
       computer_goes_first()
    else:
        print "I'm sorry, that is not a valid response."
        choose_your_destiny()

def tik_tak_toe_time():
    print "Tik-Tak-Toe Time!"
    choose_your_destiny()



if __name__ == "__main__":
    tik_tak_toe_time()
