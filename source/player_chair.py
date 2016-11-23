class Player(object):

    def get_legal_moves(self, board):
        legal_moves = []
        for i in range(0, len(board)):
            if board[i] == 0:
                legal_moves.append(i)
        return legal_moves

class Human(Player):

    id = 'human'

    def move(self, board):
        square = raw_input("Which square do you choose? ")
        self.check_if_legit(square, board)
        board[square] = 10
        return board

    def check_conscience(self, number, board):
        if number not in self.get_legal_moves(board):
            self.move(board)
            

class Computer(Player):

    id = 'computer'

    # will play a perfect game for board size 2x2 or smaller!
    def move(self, board):
        options = self.get_legal_moves(board)
        board[options[0]] = 1
        return board
                   
