from player_chair import Player

class Computer(Player):

    name = 'computer'

    def choose(self, board):
        return self.make_default_choice(board)

    def make_default_choice(self, board):
        options = self.get_legal_moves(board)
        if 4 in options:
            return 4
        elif number in options % 2 == 0:
            return number
        else:
            return options[0]
