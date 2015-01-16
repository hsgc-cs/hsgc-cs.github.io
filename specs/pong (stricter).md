# Project 2, Pong

HSGC, Intro to Computer Science — November, 2014

## Abstract

Created in 1972 by Atari incorporated, Pong is one of the earliest video games.  The game simulates a very simple table-tennis match involving two players. A ball (a moving pixel) moves back and forth across the screen horizontally and paddles (vertical bars) can hit the ball back and forth.

[https://www.youtube.com/watch?v=5uuxFhUc8tg](https://www.youtube.com/watch?v=5uuxFhUc8tg)

## Specifications

### Variables

* Each player’s score and the number of remaining balls are displayed.

### Ball Sprite

* The beginning of a round

### Human Paddle Sprite

* Position
### Computer Paddle Sprite

* Position

### When you miss

* Cause

## Additional extensions

Once you complete the above, you can extend your program.  Some suggestions:

* Instead of a perfectly elastic reflection (the bounce), turn the ball based on where in the paddle it hit. (Hint: By comparing center positions of the ball and the paddle.) This means that you can straighten out the ball’s path to make it easier or make the ball bounce at a higher angle when it hits near the edge of the paddle to make it more difficult.

## Grading Criteria

The list of what we will use to grade your projects is summarized below. Please review your project before submitting it to be sure you meet all of the specifications. If you have any questions on whether you meet a requirement, **please ask us**.

| Requirement | Possible Points |
| --- | --- |
| Variables are initialized as specified. | 10 |
| The ball is properly initialized at start of game and after each miss. | 10 |
| When a player misses the ball, the score increments by 1. | 5 |
| The number of remaining balls decrements by 1 when a new ball is generated. | 5 |
| Ball bouncing off the paddle is implemented as a function/block and exactly as specified. | 20 |
| The ball bounces off the top and bottom of the stage. | 10 |
| When a player misses the last ball (the number of remaining balls is 0), “Game Over” and the winner is announced. | 5 |
| The human paddle sprite moves with the [up] and [down] direction keys; the computer paddle moves with the ball. | 10 |
| Good programming skill: Program is repeatable and initializes state correctly. | 10 |
| Ball bounces smoothly, overall program runs smoothly. | 10 |
| _Extra Credit: Ball bounces based on where it hits the paddle._ | _10_ |
| _Extra Credit: The computer paddle can (optionally) be controlled by a second player._ | _10_ |
| _Extra Credit: Make your own extension._ | _0-10_ |
| **Total points** | **100** |