class Player(object):

    def get_legal_moves(self, board):
        legal_moves = []
        for i in range(0, len(board)):
            if board[i] != 1 and board[i] != 10:
                legal_moves.append(i)
        return legal_moves

class Human(Player):

    id = 'human'

    def move(self, board):
        choice = int(raw_input("Which square do you choose? "))-1
        self.check_conscience(choice, board)
        board[choice] = 10
        return board

    def check_conscience(self, choice, board):
        if choice not in self.get_legal_moves(board):
            self.move(board)
            

class Computer(Player):

    id = 'computer'

    # will play a perfect game for board size 2x2 or smaller!
    def move(self, board):
        options = self.get_legal_moves(board)
        print "Computer chooses square", options[0]
        board[options[0]] = 1
        return board
                   
