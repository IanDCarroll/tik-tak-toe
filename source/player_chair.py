class Player(object):

    def get_legal_moves(self, board):
        legal_moves = []
        for i in range(0, len(board)):
            if board[i] != 1 and board[i] != 10:
                legal_moves.append(i)
        return legal_moves

class Human(Player):

    name = 'human'

    def move(self, board):
        choice = self.choose() - 1
        if self.check_conscience(choice, board):
            self.move(board)
        else: 
            board[choice] = 10
        return board

    def choose(self):
        return int(raw_input("Which square do you choose? "))

    def check_conscience(self, choice, board):
        if choice not in self.get_legal_moves(board):
            return True
            

class Computer(Player):

    name = 'computer'

    # will play a perfect game for board size 2x2 or smaller!
    def move(self, board):
        options = self.get_legal_moves(board)
        board[options[0]] = 1
        return board
                   
