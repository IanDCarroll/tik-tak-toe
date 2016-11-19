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
        rendered_board = self.construct_board(self.stringify_board(board))
        return rendered_board
        
    def stringify_board(self, board):
        for i in range(0, len(board)):
            if board[i] == 0:
                board[i] = "   "
            elif board[i] == 1:
                board[i] = " X "
            elif board[i] == 10:
                board[i] = " O "
        return board

    def construct_board(self, board):
        from math import sqrt
        board_size = int(sqrt(len(board)))
        print "board_size: %", board_size

        corner = '+'
        shelves = []
        for i in range(0, board_size):
            shelves.append('---')
        rack = '\n' + corner.join(shelves) + '\n'

        wall = '|'
        rows = []
        for i in range(0, board_size):
            rows.append([])
            for j in range(0, board_size):
                rows[i].append(board.pop(0))
            working_row = rows[i]
            rows[i] = wall.join(working_row)
        grid = '\n' + rack.join(rows) + '\n'
        return grid

        
