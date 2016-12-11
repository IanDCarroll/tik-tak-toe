from player_chair import Player

class Computer(Player):

    name = 'computer'

    def choose(self, board):
        options = self.get_legal_moves(board)
        win_chance = self.take_win_chances(options, board)
        lose_chance = self.avoid_losing(options, board)
        center = self.take_the_center(options)
        catty_corner = self.take_catty_corner(options, board)
        if win_chance:
             return win_chance
        elif lose_chance:
             return lose_chance
        elif center:
             return center
        elif catty_corner:
             return catty_corner
        return self.make_default_choice(options)

    def take_win_chances(self, options, board):
        analysis = self.scan_board(board)
        for condition in analysis:
            if condition == self.marker_code * 2:
               code = analysis.index(condition)
               return self.parse_analysis(options, code)
        return False

    def avoid_losing(self, options, board):
        enemy_code = 10
        if self.marker_code == 10:
            enemy_code = 1
        analysis = self.scan_board(board)
        for condition in analysis:
            if condition == enemy_code * 2:
               code = analysis.index(condition)
               return self.parse_analysis(options, code)
        return False


    def take_the_center(self, options):
        if 4 in options:
            return 4
        return False

    def take_catty_corner(self, options, board):
        if board[4] == self.marker_code:
            analysis = self.scan_board(board)
            if analysis[6] == 11:
                return self.parse_analysis(options, 6)
            elif analysis[7] == 11:
                return self.parse_analysis(options, 7)
        return False

    def make_default_choice(self, options):
        priorities = [0,2,6,8]
        for priority in priorities:
            if priority in options:
               return priority
        return options[0]

    def parse_analysis(self, options, code):
        if code == 0:
           if 0 in options:
              return 0
           elif 1 in options:
              return 1
           return 2
        elif code == 1:
           if 3 in options:
              return 3
           elif 4 in options:
              return 4
           return 5
        elif code == 2:
           if 6 in options:
              return 6
           elif 7 in options:
              return 7
           return 8
        elif code == 3:
           if 0 in options:
              return 0
           elif 3 in options:
              return 3
           return 6
        elif code == 4:
           if 1 in options:
              return 1
           elif 4 in options:
              return 4
           return 7
        elif code == 5:
           if 2 in options:
              return 2
           elif 5 in options:
              return 5
           return 8
        elif code == 6:
           if 0 in options:
              return 0
           elif 4 in options:
              return 4
           return 8
        elif code == 7:
           if 2 in options:
              return 2
           elif 4 in options:
              return 4
           return 6
