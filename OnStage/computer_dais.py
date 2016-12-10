from player_chair import Player

class Computer(Player):

    name = 'computer'

    def choose(self, board):
        center = self.take_the_center(board)
        if center:
             return center
        return self.make_default_choice(board)

    def take_the_center(self, board):
        options = self.get_legal_moves(board)
        if 4 in options:
            return 4
        return False

    def make_default_choice(self, board):
        options = self.get_legal_moves(board)
        priorities = [0,2,6,8]
        for priority in priorities:
            if priority in options:
               return priority
        return options[0]
