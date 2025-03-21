# tetra
**tetra** is a script for monome norns and grid.

Use the grid to create and interact with sound objects called tetras.  
Each tetra makes a sound that can be played manually or sequentially.  
Sequences are created from groups of adjacent tetras.

## Tetras

Tetras are formed on the grid by four adjacent keys, excluding diagonals.  
There are 7 possible shapes (think tetris): I, O, T, L, J, S, Z.  
Some shapes have two or four possible orientations.  

### Playing tetras
When a tetra is completed, it starts to act as a single button on the grid: pressing any one of its keys  
will activate it and trigger a sound. The sound is determined by the shape of the tetra.  
This script uses the [n.b. voice library](https://llllllll.co/t/n-b-et-al-v0-1/60374), and each shape can
be associated with any installed n.b. voice.  
The initial note played by the tetra is chosen randomly from the scale specified in the PARAMETERS>>EDIT menu.  

### Adjusting tetras
There are several possible adjustments to the sound of a tetra: note, length, volume, ratchet and iteration,  
which can be changed by selecting a tetra and turning the encoders or pressing the buttons on the norns.  
The length, ratchet and iteration only take effect when the tetra is played in a sequence (see Groups, below).  
The last tetra to be pressed will remain selected.  
If a tetra is held while turning the encoders, the sound will be previewed with each turn of the encoder.  

### Moving and deleting tetras
To move a tetra, press and hold a key on it, and then press another key at the destination.  
Tetras can not overlap, or go outside the bounds of the grid.  
Any lit keys, which are not part of a tetra, will also prevent a tetra from moving to that position.  

To delete a tetra, press and hold **three** of its keys.  
To delete all tetras, press and hold any two diagonally opposite corner-keys on the grid.  

## Groups

A group is created when two or more tetras are adjacent to each other by at least one key.  
Tetras in a group are played sequentially, in the order they were added to the group.  
The last tetra to be added will play after all the other tetras in the group.  
If a tetra adjoins two or more exisiting sequences, the sequences are merged into one.  
If deleting or moving a tetra splits a group, new groups are created from the remaining tetras.  

The rate at which the sequence is played can be adjusted from the parameters clock menu.  
Pressing both keys on the norns simultaneously will stop/start group sequences playing.  
 
### Ratchets, iterations and rests
The ratchet and iteration values of a tetra are displayed on the screen when a tetra is selected,  
in the form "play (ratchet) times every (iteration) loops".  
For example, a ratchet of 2 and an interation of 3 will play the tetra twice every 3 loops.  
The default maximum value for ratchets and interations is 4, but this can be changed from the parameters menu.

Turning the length parameter fully counter-clockwise turns the note into a _rest_.
Rests can be particularly useful to allow long monophonic notes to play out in a sequence without being cut off.  


## Requirements

- monome norns or norns shield
- monome grid or compatible device (any size should work,
but have only been tested with 128 grid)
- [n.b. voices](https://llllllll.co/t/n-b-et-al-v0-1/60374/155)  

## Installation

1. Install via maiden from the project manager, or manually by running 
    ;install https://github.com/nvillar/tetra

2. [Install one or more n.b. voices](https://llllllll.co/t/n-b-et-al-v0-1/60374/155)  
Enable each voice in SYSTEM>>MODS and restart. The [emplaitress](https://github.com/sixolet/emplaitress) and [polyperc](https://github.com/dstroud/nb_polyperc) voices  
are recommended as a starting point. MIDI is supported by n.b. out of the box.  

3. Go to the parameters menu and select the voice for each tetra shape. Two PSET files
are included with the script, which can be loaded from the PARAMETERS>>PSET menu (make sure you have installed and enabled the necessary voices first):    
    - polyemp: uses the [emplaitress](https://github.com/sixolet/emplaitress) and [polyperc](https://github.com/dstroud/nb_polyperc) voices  
    - mannequins: uses the [emplaitress](https://github.com/sixolet/emplaitress), [crow](https://github.com/sixolet/nb_crow), [just friends](https://github.com/sixolet/nb_jf), and [W/Syn](https://github.com/sixolet/nb_wsyn) voices

## Thank you

Thank you the monome community, especially @tehn, @dndrks for the study material,  
@tyleretters for the nornsilerplate, and @sixolet for the n.b. voice library.





