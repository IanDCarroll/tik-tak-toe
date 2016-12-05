class Scriptographer(object):

    def __init__(self):
        self.start = "Welcome to XOX, a Noughts and Crosses Game"
        self.select = "Type 1 to go first, or 2 to go second."
        self.tie = "The game is a draw."
        self.computer = "The Computer wins the game."
        self.human = "You Win!"
        self.question = "Which square do you choose?"
        self.bad_move = "Sorry, that's not a legal move. Try again."
        self.prompt = "> "

        self.nought = "\033[34m O \033[0m"
        self.cross = "\033[91m X \033[0m"
        self.before_num = "\033[30m "
        self.after_num = " \033[0m"
        self.plank = '---'
        self.corner = '+'
        self.wall = '|'
