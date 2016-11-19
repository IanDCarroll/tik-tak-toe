class Player(object):
    def move(self, board):
        board[1][1] = 1
        return board

class Human(Player):
    def move(self, board):
        row = raw_input("Which row do you choose? ")
        col = raw_input("Which column do you choose? ")
        board[row][col] = 10
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
        print board
        return board
                   
