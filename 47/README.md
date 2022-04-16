# JETPACK-JOYRIDE - "Terminal-based version"

## About :-
```
Jetpack Joyride is a 2011 side-scrolling endless runner action video game created by Halfbrick Studios. The game features the same protagonist from Monster Dash, Barry Steakfries, who the player controls as he steals a jet pack from a top-secret laboratory. The game has been met with very favorable reviews, and has won numerous awards. 
It exhibits Object-Oriented Programming concepts like encapsulation, inheritance, abstraction and polymorphism.
```
## Pre-requisites :-
```
In order to play this game, python3 should be installed on your system and colorama,mpg123(terminal based mp3 player) should be installed. Step to install are given for linux.
```
### Installation [For linux] :-
```
foo@bar:~$ sudo apt-get update
foo@bar:~$ sudo apt-get install mpg123
foo@bar:~$ sudo apt-get install python3
foo@bar:~$ pip3 install colorama
```

## Instructions To Play 

* Run the following command to start the game.

    ```
    foo@bar:~$ python3 Game.py
    ```

* Use 'w', 'a' and 'd' to control player.

* Use 'Space' to fire bullets.

* Use 'p' to activate shield around player.

* Use 't' to transform it's shape

* Use 'q' to quit

## About this game
```
Din is a mandalorian living in the post-empire era. He is one of the last remaining members of his clan in the galaxy and is currently on a mission for the Guild. He needs to rescue The Child, who strikingly resembles Master Yoda, a legendary Jedi grandmaster. But there are lots of obstacles in his way, trying to prevent Din from saving Baby Yoda. Din is wearing classic mandalorian armour and has a jetpack as well as a blaster with unlimited bullets. We’ve got to help him fight his way through and rescue Baby Yoda.
This game consists of one level. You will see that this game is quite a replica of the original game. You win when you defeat the **Boss enemy**. Rest of the details are stated below explicitly for each element of the game.
The game is a classic combination of Jurassic park(movie series),Jetpack Joyride that is why I named it "Jurassic Jet".
```

### Mandolian

* He is the main player of the game.

* Has 5 lives.

* Has 100 seconds to complete the game.

* Can fire bullets.

### Scenery

* background keeps changing

* It contains clouds, obstacles, coins

### Coins
* Comes randomly at any point 

* Player score increases on collecting it

### Beams

* There are three types of beams :-
1) Horizontal beam
2) Vertical beam
3) Diagonal beam

* comes randomly at any point

* Mandolian loses a life on colliding with a beam

* Can be destroyed by a bullet fired by Mandolian

#### Magnet

* Comes randomly at any point

* Constantly attracts Mandolian towards it, if it is in certain range

* Can't be destroyed

* Touching it will drain all your lives at once

### Boss_enemy

* Comes at end of the game

* It is the Hardest enemy to defeat

* Fires iceballs that follow the mando, but can be destroyed by bullets or any other entity on the screen

* Adjust its position in accordance with Mandolian's y-coordinate

* Has 10 lives

* Once Mandolian defeats him, game is over

### Iceball

* Fired by Boss_enemy

* Follows the mandalorian

* Mandolian loses a life on colliding with a iceball

* Are fired at every 2 seconds

### Shield

* Used to shield Mandolian from obstacles and iceballs

* refills at every 10 seconds

* Once occupied, it lasts for 5 seconds

* Can be activated by pressing 'p'

* Mandos shape changes on its activation

### Speed_booster

* Comes randomly at any point 

* Game speed,mando's speed of moving around increases on collecting it

* Once occupied, it lasts for 5 seconds

### Color 

* Different colors are given to different components of the game

### Score 

* Increases on destroying beams, collecting coins and killing the BOSS ENENMY

### Start Screen

* Tells the controls to its user

### End Screen

* Tells the player about his/her score

* Different screen wrt loss or a win

* Tells the cause of death in case of a loss
