# XOX
An unbeatable game of noughts and crosses (AKA tic-tac-toe)

### Name origin story:

it was originally called tik-tak-toe, which was supposed to be a little like <a href="https://www.youtube.com/watch?v=Kl7f2ytS7Vw">rikki-tikki-tavi</a>, a favorite cartoon when I was small, based on a short story by Rudyard Kipling. However it just looked like I didn't know how to spell.

So the new name is xox. Named after one of the first computer games, OXO by Sandy Douglas at Cabridge University in 1952. I felt it was appropriate because this is my first attempt at something of this scale. I could have instead called it "Bertie the Bot" after "Bertie the Brain", the first Noughts and Crosses computer game in Canada (1950), with a bit of Harry Potter thrown in. But xox is easier to spell.

### Things it does:

This is a simple command line noughts and crosses game.

 - You are a human, much like John Henry
 - Your opponent will be a machine, much like a Steam-Powered Drill
 - Your opponent will never lose, and will always play perfectly.(feature to be added)
 - Finally, you can feel what it's like to rage against the machine and never win!(feature to be added)

### How to play:

 1. Clone this repository (Or just copy the contents of the `source` folder into an empty one of your own)
 2. On the command line, cd into the directory the source files are in.
 3. $`python xox.py`

### How to test:

 1. Clone this repository
 2. On the command line, cd into the `xox` directory
 3. $`nosetests`

### The Process:

want to see how I am spelling your noughts-and-crosses-playing doom?

Watch my progress on the <a href="https://github.com/IanDCarroll/GoScrumYourself">GoScrumYourself</a> repo!

### Notes on making the code clean:

this sprint will focus first on making the code clean and free from repeated statements. There are probably a lot of them.

I could probably somehow abstract all of the scanning loops the Computer, Referee, and Announcer do into a single parent class.

Though, the thought of having the Referee and the Computer Player inheriting the same code smacks of unfairness for the Human. And the idea of having the Computer Player inherit from two classes seems abhorrent. I might be able to turn the Player class into a Being class and have all actors inherit from it. If that was the case, then it wouldn't seem quite as unfair. Or for that matter have Facilitator and Player inherit from a root class. That would make for a nice tree structure.

Also that Referee is doing an aweful lot, and her file is getting rather long with it. I should probably give her `check_for_winner` method and create a Judge class to do that job.

And the final play file does some things that Referee does as well. I want to put all of the `start_game()` code together in a single entity with responsibility for that.

I spent a lot of time crafting a story from the code so I could keep it in my mind, but that story may be holding me back from optimizing the code now. It's a price to pay, but I wanted a very nice handle from which to grok the code, and I was willing to make sacrifices to do it. Now it might be time to start rewriting that story.

I was definitely focused squarely on the cleanness of individual functions last iteration. I'll need to go through and identify any code I duplicated unwittingly. It also might be sneekily baked into functions that appear different. So that's something to look out for.

I'll also be seeing about refactoring the test cases. There's certainly a lot of duplication happening there. Also, I think I'd like to invest some time trying to refactor the tests for unittest instead of nose. It's the batteries included testing framework, and so I really should master the use of it.

Finally I need to consider a lesson I learned from coding arduinos with johnny-five. Annoying.js was exceptionally unclean. It had to be in order to annoy on as many levels as possible. It had many separate variables that were in no way related. It must have had eight different places in the code that needed to be tweaked if we wished to annoy in a different manner. But when we unannoyed it, every one of those variables was derrived from a single tempo. It was beautiful, easy to change, and did not require open-heart surgery to use. If there is one philosphy I should fall back on, it's subject the entire system to a single tempo. So I will work on unannoying this code.

### Notes on an evil algorithm:

A few notes on your ultimate destruction. Just something to let you know I'm thinking about you... 

The algorithm could be unbeatable if it is able to:

 1. __Win:__ Check if there is an opportunity to win next move.
 2. __Don't let you win:__ If none, then check to see if it can keep you from winning next move.
 3. __Fork for the win.__ If none, find a way to set itelf up for a win in two moves by creating a "fork" so no matter what you do next, it still wins.
 4. __Don't let you fork for the win.__ If none, prevent you from making said "fork". Don't let you fork.
  - by distracting you with an emergency elsewhere on the board.
  - by occupying the one spot you need to make a fork.
 5. Otherwise, take the center square.
 6. If the center is taken, and the opponent has taken a corner, take the opposite corner from you.
 7. If the center square is taken, take a corner square.
 8. If the center and all the corner squares are taken, take whatever remains. (sides are undesirable)

These strategies should work regardless of whether it plays first or second.

__On the other hand,__ there may be another way to do it by using a series of 48 board states to test against, and returning the propper response to each. That is how the <a href="http://constructingmodernknowledge.com/wp-content/uploads/2013/03/TinkerToy-Computer-Dewdney-article.pdf">tinkertoy tic-tac-toe</a> worked. Reproducing that in software would not be too hard, though could be less elegant than another method.

__On the third hand,__ There may be a CS way to go about this. I am only vaguely aware of this, but noughts and crosses is a game tree that can be searched using a minimax method with unlimited depth. The trick is that perfect games end in a tie, how would you go about finding the optimal way to tie? That's heavy on theory, and I have not the foggiest clue right now of how to turn that into actual code. More research required for that...

## Suggestions?

Have ideas about how I can better defeat you with this program? Is there a bug you'd like to report? A duplication you see? A feature to request? Or is the readme unclear? (I'm afraid I cannot accept any PRs beside my own because reasons.) But otherwise, all comments and help are welcome! <a href="https://github.com/IanDCarroll/tik-tak-toe/issues/new">Open up an issue!</a> :smile:
