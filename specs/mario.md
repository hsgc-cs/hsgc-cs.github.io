# Mario

HSGC, Intro to Computer Science — September 19, 2014

Start with your walking and costumes SNAP project.

## Abstract

Create your own _Mario_-style game in SNAP.

First appearing as "Jumpman" in the original Donkey Kong arcade game, Mario quickly moved on to start his own 30-year franchise. There have been sports, racing, puzzle, and RPG Mario games, but the core of his talents are in platforming. In this project, we will be making a platformer! [Wikipedia][1]

## Specifications

1. The game starts when the **green flag** is pressed; it will be playable entirely in presentation mode.
2. Create a sprite that appears to be standing on the ground.
3. **Move** the sprite left or right by pressing [left] or [right] keys.
4. Switch the sprite's **costume**, dependent on what its doing.  
    * ★☆☆ standing, moving  
    * ★★☆ standing, moving, jump  
    * ★★★ standing, moving (cycle), jump
5. **Jump** by pressing [space]
    * ★☆☆☆☆ **Teleport up:** go to (x, ground + 100) while holding [space]
    * ★★☆☆☆ **Timed:** go to (x, ground + 100) by pressing [space]. 1 second later, return to (x, ground)
    * ★★★☆☆ **Glide:** glide to (x, ground + 100), glide back down to (x, ground)
    * ★★★★☆ **Include velocity:** go to (x + velocity, ground + 100) by pressing [space]. 1 second later, return to (x, ground)
    * ★★★★★ **Gravity:** simulate it
6. Goomba (mushroom): enemy movement
    * ★☆ **Moves** back and forth along ground forever. Stays on the screen.  
    * ★★ Pursues Mario.
7. Goomba collision
    * ★☆ The game ends when Mario **touches** a Goomba.
    * ★★ Mario can jump on top of the enemy to get 10 points and make the mushroom. **Touching** its side is still a game over.
8. Place three coins at _y = ground + 100_. When Mario **touches** a coin he gets 4 points and the coin disappears.
9. **Show** the score.

Start with your walking and costumes SNAP project.

Don't forget your resetting blocks.

## Extra Credit

Congratulations, you've made your own Mario game! Add in some DLC for your fans.

a. Maybe present some stars from above as extra credit??


[1]: http://en.wikipedia.org/wiki/Mario_(franchise)
