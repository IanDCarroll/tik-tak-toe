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
        line1 = board[0] + ' ' + board[1] + ' ' + board[2]
        line2 = board[3] + ' ' + board[4] + ' ' + board[5]
        line3 = board[6] + ' ' + board[7] + ' ' + board[8]
        rendered_board = line1 + '\n' + line2 + '\n' + line3
        return rendered_board
