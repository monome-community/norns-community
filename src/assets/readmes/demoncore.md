# demoncore
A very simple noise module for Norns but with a mind of its own.

## Requirements
* Norns

## Background
I wanted to create a simple Norns project in order to learn Lua and 
SuperCollider. Inspiration came from watching the 1989 film "Fat Man and Little Boy".
(https://www.youtube.com/watch?v=AQ0P7R9CfCY)

I wanted to create a similar sound to that created when scientists 
were experimenting with a spherical plutonium core, blocks of graphite 
and a screwdriver! as part of the Manhattan Project.

The core was involved in two incidents at the Los Alamos Laboratory 
in 1945 and 1946, resulting in the acute radiation poisoning and 
subsequent deaths of scientists Harry Daghlian and Louis Slotin. 
After these incidents the spherical plutonium core was referred to 
as the "Demon Core".
## Manual
![alt text](https://github.com/kevinlindley/DemonCore/blob/55c5bdccfdd51665a203fefc01973fa4af2d7787/DemonCoreSmall.png "Demon Core running on a Norns Shield")
### Page 1 -  Core  (Noise)
* Encoder 1 - Volume
* Encoder 2 - Criticality  (density)
* Encoder 3 - Mix
* Key 2 - Menu Page 2
* Key 3 - Alive / Sleeping (rnd)
### Page 2 - Shield (LP Filter)
* Encoder 1 - Volume    
* Encoder 2 - Frequency 
* Encoder 3 - Cuttoff    
* Key 2 - Menu Page 3
* Key 3 - Alive / Sleeping (rnd)
### Page 3 - Lab (Reverb)
* Encoder 1 - Volume
* Encoder 2 - Room Size
* Encoder 3 - Dmaping
* Key 2 - Menu Page 1
* Key 3 - Alive / Sleeping (rnd)
## Notes on Use
The Norns script comprises of three menus that can be accessed
by pressing the K2 button.
Each menu allows you to adjust the volume control for 
convenience.

The first menu page also allows you to change the Criticality
(density) of the noise and the Blocks (mix) which affects the
reverb Wet/Dry mix. 
The second menu page allows you to adjust the filter of the
noise sound from both frequency and resonance amount.
The third menu allows you to change the room size and damping
of the reverb. Changes here affect the Dry/Wet mix on menu 1.

Finally the K3 button toggles between the Core being "Alive"
or "Sleeping". If toggled to the "Alive" setting the script
will slowly randomise the settings.
You can still interact with the core when in this mode and it's 
useful for finding new noise sounds, when the Demon Core finds 
a noise sound you like, click on the K3 button and take over.
## Installation
1. From maiden:
```;install https://github.com/kevinlindley/demoncore```
2. Power Off and On to install the new Engine.
