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
Raw_Input()<----Human(Player)<-----     Rules File
                     |             |      ^
                     |             |      |
   Player(object)<---               ---Referee------->Display
                     |             |      |             |
                     |             |      v             |
Algorithm<---Computer(Player)<----      Game Board<-----
    |                                     ^
    |                                     |
     -------------------------------------
```
