class Display():
    
    def __init__(self):
        self.start = "Welcome"
        self.draw = "Draw"
        self.computer = "Computer Wins"
        self.human = "You Win"
        self.next_move = "What is your next move?"
        self.bad_move = "That is not a legal move."

    def show(self, text):
        print text

    def render_board(self, board):
        for i in range(0, len(board)):
            if board[i] == 0:
                board[i] = " "
            elif board[i] == 1:
                board[i] = "X"
            elif board[i] == 10:
                board[i] = "O"
        return str(board)
