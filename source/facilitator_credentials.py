from math import sqrt

class Facilitator(object):

    def scan_board(self, board):
        analyzed_list = []
        analyzed_list.extend(self.scan_rows(board))
        analyzed_list.extend(self.scan_cols(board))
        return analyzed_list

    def scan_rows(self, board):
        analyzed_rows = []
        board_size = self.get_board_size(board)
        start_index = 0
        for i in range(0, board_size):
            stop_index = start_index + board_size
            analyzed_row = 0
            for j in range(start_index, stop_index):
                analyzed_row += board[j]
            start_index += board_size
            analyzed_rows.append(analyzed_row)
        return analyzed_rows

    def scan_cols(self, board):
        analyzed_cols = []
        start_index = 0
        board_size = self.get_board_size(board)
        stop_index = len(board)
        for i in range(0, board_size):
            analyzed_col = 0
            for j in range(start_index, stop_index, board_size):
                analyzed_col += board[j]
            start_index += 1
            analyzed_cols.append(analyzed_col)
        return analyzed_cols

    def get_board_size(self, board):
        return int(sqrt(len(board))) 
