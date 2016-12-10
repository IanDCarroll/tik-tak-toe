from player_chair import Player

class Computer(Player):

    name = 'computer'

    def choose(self, board):
        return self.make_default_choice(board)

    def make_default_choice(self, board):
        options = self.get_legal_moves(board)
        if 4 in options:
            return 4
        if 0 in options:
            return 0
        if 2 in options:
            return 2
        if 6 in options:
            return 6
        if 8 in options:
            return 8
        else:
            return options[0]
