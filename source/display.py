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
        print str(board)
        return str(board)
