class Player(object):
    def move(self, board):
        board[4] = "spam"
        return board

class Human(Player):
    def move(self, board):
        square = raw_input("Which square do you choose? ")
        board[square] = 10
        return board

class Computer(Player):
    def move(self, board):
        for i in range(0, len(board)):
            if 0 in board[i]:
                for j in range(0, len(board[i])):
                    if board[i][j] == 0:
                       board[i][j] = 1
                       break
                break
        return board
                   
