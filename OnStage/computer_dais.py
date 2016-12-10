from player_chair import Player

class Computer(Player):

    name = 'computer'

    def choose(self, board):
        return self.make_default_choice(board)

    def make_default_choice(self, board):
        options = self.get_legal_moves(board)
        priorities = [4,0,2,6,8]
        for priority in priorities:
            if priority in options:
               return priority
        return options[0]
