from player_chair import Player

class Computer(Player):

    name = 'computer'

    def choose(self, board):
        options = self.get_legal_moves(board)
        win_chance = self.take_win_chances(board)
        center = self.take_the_center(options)
        catty_corner = self.take_catty_corner(options, board)
        if win_chance:
             return win_chance
        elif center:
             return center
        elif catty_corner:
             return catty_corner
        return self.make_default_choice(options)

    def take_win_chances(self, board):
        analysis = self.scan_board(board)
        return False

    def take_the_center(self, options):
        if 4 in options:
            return 4
        return False

    def take_catty_corner(self, options, board):
        if board[4] == self.marker_code:
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

    def make_default_choice(self, options):
        priorities = [0,2,6,8]
        for priority in priorities:
            if priority in options:
               return priority
        return options[0]
