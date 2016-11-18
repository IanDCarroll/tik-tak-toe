# tik-tak-toe
An unbeatable game of tic-tac-toe

### Things it should do:
a simple Tic-Tac-Toe program. At the very least this program should:

- allow for a human player
- play against a computer player
- have some user interface (text is fine)
- never lose and win whenever possible

### Architecture:

```
                                    Rules File
                                        ^
Raw_Input()<----Human(Player)<-----     |  GameOver checker
                     |             |    |   ^
                     |             |    |   |
   Player(object)<---               ---Referee------->Display
                     |             |      |             |
                     |             |      v             |
Algorithm<---Computer(Player)<----      Game Board<-----
    |                                     ^
    |                                     |
     -------------------------------------
```

### Functions:

The game Board does one thing. It returns the state of the board.

the player does one thing. It makes a change to the state of the board.
    the computer player calls an algorythm to change the board
    the human player calls raw_input() to change the board

The referee does one thing. It modulates the turns of the game.

The gameOver Checker does one thing. It checks if the game is over or not.

The Rules File does one thing. It supplies the rules to the Referee.

The Display does one thing. It displays the state of the Game Board.
