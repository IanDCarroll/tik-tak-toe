from observer_abilities import *

class Announcer(Observer):
    
    def __init__(self):
        self.start = "Welcome to XOX, a Noughts and Crosses Game"
        self.select = "Type 1 to go first, or 2 to go second."
        self.tie = "The game is a draw."
        self.computer = "The Computer wins the game."
        self.human = "You Win!"
        self.question = "Which square do you choose?"
        self.bad_move = "Sorry, that's not a legal move. Try again."
        self.nought = " O \033[0m"
        self.cross = " X \033[0m"
        self.num1 = "\033[30m "
        self.num2 = " \033[0m"

    def show(self, text):
        print text

    def render_board(self, raw_board):
        stringified_board = self.stringify_board(raw_board)
        rendered_board = self.construct_board(stringified_board)
        return rendered_board
        
    def stringify_board(self, board):
        fresh_board = []
        for i in range(0, len(board)):
            if board[i] == 0:
                fresh_board.append(self.num1 + str(i+1)  + self.num2)
            elif board[i] == 1:
                fresh_board.append(self.cross)
            elif board[i] == 10:
                fresh_board.append(self.nought)
        return fresh_board

    def construct_board(self, board):
        rack = self.assemble_rack(board)
        rows = self.assemble_rows(board)
        constructed_board = '\n' + rack.join(rows) + '\n'
        return constructed_board

    def assemble_rack(self, board):
        board_size = self.get_board_size(board)
        corner = '+'
        shelves = []
        for i in range(0, board_size):
            shelves.append('---')
        rack = '\n' + corner.join(shelves) + '\n'
        return rack

    def assemble_rows(self, board):
        row_length = self.get_board_size(board)
        wall = '|'
        rows = []
        for i in range(0, len(board), row_length):
            completed_row = wall.join(self.build_proto_row(board, i))
            rows.append(completed_row)
        return rows

    def build_proto_row(self, board, start_of_row):
        row_length = self.get_board_size(board)
        end_of_row = start_of_row + row_length
        proto_row = []
        for i in range(start_of_row, end_of_row):
            proto_row.append(board[i])
        return proto_row
