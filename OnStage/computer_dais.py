from player_chair import Player

class Computer(Player):

    name = 'computer'

    def choose(self, board):
        center = self.take_the_center(board)
        catty_corner = self.take_catty_corner(board)
        if center:
             return center
        elif catty_corner:
             return catty_corner
        return self.make_default_choice(board)

    def take_the_center(self, board):
        options = self.get_legal_moves(board)
        if 4 in options:
            return 4
        return False

    def take_catty_corner(self, board):
        options = self.get_legal_moves(board)
        analysis = self.scan_board(board)
        if analysis[6] == 11:
            if 0 in options:
               return 0
            return 8
        elif analysis[7] == 11:
            if 2 in options:
               return 2
            return 6
        return False

    def make_default_choice(self, board):
        options = self.get_legal_moves(board)
        priorities = [0,2,6,8]
        for priority in priorities:
            if priority in options:
               return priority
        return options[0]
