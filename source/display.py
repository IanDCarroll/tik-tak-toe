from math import sqrt

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

    def render_board(self, raw_board):
        stringified_board = self.stringify_board(raw_board)
        rendered_board = self.construct_board(stringified_board)
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

    def get_board_size(self, board):
        return int(sqrt(len(board))) 
