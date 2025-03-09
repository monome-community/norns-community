# pit orchisstra  
the game of snake  
a group of snakes is a pit  
live loooong and prosper  

[![pit orchisstra tutorial](https://github.com/entzmingerc/pit-orchisstra/blob/main/pittutorial.png)](https://www.youtube.com/watch?v=NpIjsqzu0Q0)

Click the image above for a tutorial. For more discussion, see the thread on [lines](https://llllllll.co/t/pit-orchisstra/66521).    

This is a sequencer script inspired by the game of snake. Each snake can turn left or right and only steps one square forward. Poke the grid or press K2 to use Food View to place food onto the grid. If the snake eats a food, a note will be played depending on the location on the grid the food was in and the length of the snake will increase. If a snake runs into itself or any other snake, the snake will die and respawn at the minimum length. However, each of these rules can be changed. The maximum length, whether or not a snake can die, whether or not a food spawns, how many snakes, and so on can all be changed to get different behaviors. There are 4 behaviors the snakes can take on as well, none, random, wander, and sequence. Depending on the behavior, snakes can automatically seek out food, or keep wandering forward indefinitely. Combining different snake behaviors and game rules generates a variety of musical sequences. See [this playlist](https://www.youtube.com/watch?v=NpIjsqzu0Q0&list=PLvUVlqry7k40gZtUj0rqv4FkUx6IMi0Ue) for a tutorial and many examples of how this script can be used.  

There are no prerequisites other than a monome norns. This script supports [nb](https://llllllll.co/t/n-b-et-al-v0-1/60374) which you can use to download and install diffrent nb voices to use with the snakes if you get tired of using the built-in rudiments synthesizer. This script supports typing keyboard controls and monome grid controls.  

# NORNS CONTROLS  
__selected snake__:  
E1: select snake  
E2: speed  
E3: turn snake  
K2: toggle food view / snake view  
K3: cycle snake behaviors  

__food view__:  
E2: ← down, → up  
E3: ← left, → right  
K3: place/destroy food  
if two player mode is on  
E2 turns next snake (+1)  

__slithering behaviors__:  
1 none: turn with ENC3 only  
2 random: random snake turn (whimsy)  
3 wander: turn towards closest food  
4 sequence: seek food in order placed  

# GRID CONTROLS  
poke the grid to place/destroy food!  

# KEYBOARD CONTROLS  
__select snake, select view__:  
1   select snake 1  
2   select snake 2  
3   select snake 3  
4   select snake 4  
TAB   toggle food view / snake view  

__selected snake controls__:  
Q   toggle slithering (TURN ON/OFF THE SNAKE)  
W   increase speed  
A   turn left  
S   decrease speed  
D   turn right  
SPACE   cycle snake behaviors  
E   toggle immortality  
R   toggle quantize  
F   decrease whimsy  
G   increase whimsy  
SHIFT + W   increase snake transpose  
SHIFT + A   decrease max length (kill snake to decrease length)  
SHIFT + S   decrease snake transpose  
SHIFT + D   increase max length  
U    toggle randomSpawn  
I    decrease spawnY (move up)  
J    decrease spawnX (move left)  
K    increase spawnY (move down)  
L    increase spawnX (move right)  

__food view__:  
W   move up  
A   move left  
S   move down  
D   move right  
SPACE   place food  
cursor spawns inside the top left square initially  
other snake controls remain the same in food view  

__global__:  
8   toggle food spawn  
9   toggle food immortality  
0   toggle strict food order  
BACKSPACE   clear food grid  
Z   decrement noteRowOffset (-1)  
X   increment noteRowOffset (+1)  
C   decrement scale (-1)  
V   increment scale (+1)  
/   toggle two player mode  

# GAMEPAD CONTROLS  
__selected snake controls__:  
←   turn left  
→   turn right  
↑   increase speed  
↓   decrease speed  
A   toggle food view / snake view  
B   cycle snake behaviors  
SELECT   cycle selected snake  
START    toggle slithering (TURN ON/OFF THE SNAKE)  

__food view__:  
↑   move up  
←   move left  
→   move right  
↓   move down  
A   toggle food view / snake view  
B   place/destroy food  
SELECT   cycle selected snake  
START    toggle slithering (TURN ON/OFF THE SNAKE)  

# SNAKE PARAMETERS:  
| Parameter | Description |
| --- | --- |
| nb snake 1-4 | select the nb voice for the snake |
| Internal ON/OFF | turn ON/OFF the internal synth engine |
| selected snake | selects snake 1, 2, 3, or 4 <br> only shows parameters of the selected snake |
| slithering | 0 removes snake, 1 spawns snake |
| behavior | defines the movement of the snake (see more details below) |
| speed | 1-70, syncs to norns clock tempo |
| immortal | 0 can be killed, 1 all hail immortal snek |
| max length | 1 - 128, default 10 |
| whimsy | 0-10, 0-100% chance to flip a coin to turn left or right |
| transpose | midi note offset for nb voices |
| quantize | 0/1, controls if note is quantized to scale of the grid |
| spawnX | respawn x-coordinate |
| spawnY | respawn y-coordinate |
| randomSpawn | 0 uses respawn coordinates <br> 1 (default) respawns the snake in a random location |
| [rudiments](https://github.com/cfdrake/rudiments) | [rudiments](https://github.com/cfdrake/rudiments) |
| osc shape | 0 sine, 1 square|
| osc freq | ...this isn't used <br> the pitch is controlled by snake transpose, note row offset, and scale |
| env decay | 0.05 - 1 sec, both pitch and amplitude envelope decay time |
| env sweep | 0 - 2000, envelope modulation depth |
| lfo freq | 1 - 10000 Hz, lfo frequency |
| lfo shape | 0 sine, 1 square |
| lfo sweep | 0 - 2000, lfo modulation depth |

we're using [rudiments](https://github.com/cfdrake/rudiments) for internal synth engine  

# FOOD PARAMETERS  
| Parameter | Description |
| --- | --- |
| food spawn | 0/1, spawns new food if food is eaten |
| food immortal | 0/1, deletes/keeps food if food is eaten |
| strict food order | 0: append any eaten food to the end of foodOrder <br>1: append only destination food to the end of foodOrder  |
| clear food grid | (TRIGGER) clear all food and foodOrder |  
| two player mode | changes ENC2 to turn the next snake <br> if snake 1 is selected, it snake+1, which is snake 2 | 
| note row offset | transpose offset per row of the grid <br> if this is 5, then if a pad is note 3, the next pad down is 3+5 |
| scale | 1 Ionian, 2 Dorian, 3 Phrygian, 4 Lydian, 5 Mixolydian, 6 Aeolian, 7 Locrian |

# SNAKE BEHAVIORS  
This controls how the snake behaves.  
For each behavior, you can always turn the snake with ENC3.  
Snakes preserve their direction and behavior upon death.  

### 1 None!
Snake moves forward, turn left or right with ENC3.  
Useful for actually playing the game Snake.  
Useful for predictable, repeating patterns of snake movement.  
Useful for drum machine style sequencing with each snake as a different percussion instrument and the foods as triggers.  

### 2 Whimsical  
Snake turns randomly!  
Whimsy controls the percentage chance to flip a coin to turn left or turn right.   
Whimsy at 0 (0%) means it always steps forward  
Whimsy at 3 (30%) means each step there's a 30% chance to flip a coin (turn left, turn right)  
Whimsy at 10 (100%) means each step it flips a coin to turn left or turn right  
Turn up speed & whimsy and watch them wiggle!  

### 3 Wander  
Snake turns towards the food closest to it that it can "see".  
Each square, the snake looks left, forward, and right in a straight line. This sight wraps through the boundaries of the grid.  
If it sees food in its sight line, it turns in the direction of closest food  
Slightly unpredictable in a complex environment of many snakes and foods.  
Results in emergent stabilizing paths and loops with immortal food.  
Pseudorandom pathing with foodSpawn on.  
    
### 4 Sequence  
Snake seeks out food in order. This is the "smartest" snake mode.  
When you place a food, it tracks the order of foods placed.  
For example, placing down 3 foods will give an order 1, 2, 3.  
The snake will go to food 1 first, eat it, then go to 2.  
Use the options "food immortal", "food spawn", "strict food order" to get different slithering paths.  

If food 2 is eaten on the way to food 1, it is removed from the order, 1, 3.  
If "food immortal" is ON, then any food eaten is not deleted and moved to the end of the food sequence.  
If food 2 is eaten on the way to food 1, it is removed from the order, and moved to the end 1, 3, 2.  
If "strict food order" is ON, only the head of food sequence (food 1 in this case) is moved to the end if eaten.  

There is only one food sequence shared among the 4 snakes.  
If snake 1 gets to the food before snake 2 does, then they'll both turn towards the next food in the sequence.  
All snake behaviors affect food sequence, so sometimes repeating sequences can get broken up with high whimy snaking.  

This is a pretty wiggling style.  
I had a vision of placing my hand on the grid and watching a snake slither around my fingertips.  
This was the attempt to realize that daydream.  
Try placing immortal foods one at a time and build up a melody.  
Placing one immortal food results in the snake to spiral around the food in a 3x3 clover pattern.  
Placing two foods will get the snake to loop back and forth.  
Placing a few foods nearby might make a repeating melody.  
And so on.  

behavior 4, slithering up, deciding how to turn:  
1 1 2 2 2 2 2 2 2 3 3 3 3 1 1 1  
1 1 1 2 2 2 2 2 3 3 3 3 3 1 1 1  
1 1 1 1 2 2 2 3 3 3 3 3 3 1 1 1  
1 1 1 1 1 H 3 3 3 3 3 3 3 1 1 1  
1 1 1 1 1 1 3 3 3 3 3 3 3 1 1 1  
1 1 1 1 1 1 3 3 3 3 3 3 3 1 1 1  
1 1 1 1 1 1 3 3 3 3 3 3 3 1 1 1  
1 2 2 2 2 2 2 2 2 2 3 3 3 1 1 1  
