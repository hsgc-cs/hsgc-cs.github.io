# Project 2, Pong

HSGC, Intro to Computer Science — November, 2014

## Abstract

Created in 1972 by Atari incorporated, Pong is one of the earliest video games.  The game simulates a very simple table-tennis match involving two players. A ball (a moving pixel) moves back and forth across the screen horizontally and paddles (vertical bars) can hit the ball back and forth.

[https://www.youtube.com/watch?v=5uuxFhUc8tg](https://www.youtube.com/watch?v=5uuxFhUc8tg)

## Deadline

End of class Wednesday, November 26, 2014.

## Specifications

### Variables

* You will display each player’s score and the number of remaining balls
* Each player’s score will start at 0
* Number of balls remaining will start at 3
* The score for each player should increment every time the ball crosses the plane of the paddle (a goal for the opposing player)
* Number of balls remaining will decrement every time a new ball is put in play

### Ball Sprite

* You need to decide how your ball will move when it first starts in the game.
    * Where is its location?
    * What direction does it face?
    * How does it start to move?
    * How does this initialization get triggered? 
* You need to decide what happens to your ball when it touches a paddle.  You must implement this as a function (a command block).  You should name this block BounceOffPaddle
    * One suggestion: Each time your ball sprite touches a paddle, it will reverse its direction and you will add a random change in the direction by turning between -15 and 15 degrees from the reversed direction
    * Note: If you just reverse the direction of the ball, you will still be touching the paddle so you may need to move off of it a bit.
* You need to make it so that the ball sprite bounces off the top and bottom parts of the playing field.

### Player Paddle Sprite

* Your paddle sprite will move within a single x position close to the right side of the stage.  
* Your paddle will be controlled by the up and down buttons on the keyboard.

### Computer Paddle Sprite

* The computer paddle sprite will move within a single x position close to the left side of the stage.  
* You need to decide how the paddle will move automatically.
    * The computer paddle should track the ball when it comes within a close range
* That paddle will return the ball for the computer by moving with the ball.

### When you miss

* You need to decide how a new ball is brought into the game.
    * You need to think about the smooth play transition between missing the ball and starting a new round of play.
* If all balls have been used, you should declare “Game Over”
    * There should be an option to either a) play again or b) quit.

### How to win

* You need to decide how a player wins the game
    * You need to think about a smooth transition in the game mechanics between making the final point and declaring the winner

## Additional extensions

Once you complete the above, you can extend your program.  Some suggestions:

* Instead of a random bounce, turn the ball based on where in the paddle it hit (Hint – by comparing center positions).  This means that you can straighten out the ball’s path to make it easier, or make the ball bounce at a higher angle when it hits near the edge of the paddle to make it more difficult.
* Increment the ball speed after every 5 times the ball hits your paddle instead of incrementally 
* Alter the computer-controlled paddle so that it can miss the ball
* Make the second paddle be controlled by a second human player

## Grading Criteria

The list of what we will use to grade your projects, and what we are looking for, is below.  Please review your project before submitting it to be sure you meet all of the specifications.  If you have any questions on whether you meet a requirement, **please ask us**.

| Requirement | Possible Points |
| --- | --- |
| Variables are initialized as specified | 10 |
| Ball is properly initialized at start of game and after each miss | 10 |
| The score increments 1 every time the ball touches the human player’s paddle | 5 |
| The remaining balls decrement by one every time one is generated | 5 |
| Ball bounce off the paddles is implemented as a function/block as specified above. | 20 |
| The ball bounces off the top and bottom of the stage | 10 |
| When either player’s score reaches 2, the winner is declared | 5 |
| When balls run out, Game Over is announced | 5 |
| The player paddle sprite moves with the up and down direction buttons and the computer paddle moves with the ball | 10 |
| Good programming skill: Program is repeatable and initializes state correctly | 10 |
| Ball bounces smoothly, overall program runs smoothly | 10 |
| _Extra Credit: Ball bounces based on where it hits the paddle_ | _10_ |
| _Extra Credit: The computer paddle can (optionally) be controlled by a second player._ | _10_ |
| _Extra Credit: Make your own extension_ | _0-10_ |
| **Total points** | **100** |
