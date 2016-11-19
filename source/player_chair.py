class Player(object):
    def move(self, board):
        board[1][1] = 1
        return board

class Human(Player):
    def move(self, board):
        row = raw_input("Which row do you choose? ")
        col = raw_input("Which column do you choose? ")
        board[row][col] = 1
        return board
