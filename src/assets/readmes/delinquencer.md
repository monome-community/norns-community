<img src="https://github.com/kevinlindley/delinquencer-support/blob/main/DelinquencerTitle.png" width="544">

# delinquencer
A "sequencer" module for Norns but with a mind of its own.

## Requirements
* Norns

#### Optional 
* A Synth of your choice connected via MIDI

## Background
The Delinquencer is my second ever script for the Norns and I wanted to create a sequencer that allowed a music producer to have fun exploring, mangling and generally being inspired by finding sweet spots in a 64 grid of notes. Essentially, the Delinquencer starts out as a simple 64 grid sequencer but then allows you to experiment quickly.

**So it’s the Delinquencer feature complete?**

> Well probably not, I’m sure its missing a feature you think will be vital, but I’ve had to draw the line under the Delinquencer project otherwise it would never see the light of day outside of my Norns Shield.

**So what makes the Delinquencer something you should try?
After all it’s not like the world needs yet another sequencer?**

> Entering notes into a 64 grid and playing them back is usually the end state for most sequencers but for the Delinquencer that’s the starting point. It’s the ability to mangle and alter over time the playback of these notes that makes the Delinquencer different to many other sequencers.

**So is Delinquencer a MIDI sequencer?**

> Well yes, but I also dabbled in SuperCollider and ended up producing a new sound engine. I only added it so I could just have a simple sound during development of the Delinquencer. Trouble is, that took on a life of its own. It’s still simplistic but then this was meant to be a sequencer project not a synth-engine project, but it’s fun to play with.

## Mini Manual
Warning: This mini manual is just a list of navigation commands and parameter descriptuions, its providd as an *aide-mémoire* and is not a replacement for the full Delinquencer manual and its walkthroughs.

<img src="https://github.com/kevinlindley/delinquencer-support/blob/main/DelinqunecerRunningOnNorns450.png" width="250" height="250">

### Theory of operation
Fundamentally the Delinquencer script turns your Norns into a 1 to 64 notes / cells / steps  sequencer that allows you to set the note pitch, length, velocity and probability. You can change the BPM, time divisions The Delinquencer play both sound through its own limited PolySaw engine and/or send MIDI instructions to a connected synth (its intended purpose).

Delinquencer also allows you to change the direction of sequence note play, forward, back, up, down etc., as well as some more interesting ways (spiral, snake, frog, blocks etc.). It also has some note presets to get the 64 grid filled in quickly (to get you exploring rather than laboriously entering notes manually). Delinquencer allows you to transpose the whole grid of 64 notes and quantise the notes to a specific music scale.
If you do want to enter notes manually you can still set the individual pitch, length, probability for each of the 64 steps/cells.

*So far nothing new I hear you say ….. but …..*

Delinquencer allows you to set each cell/step to one of the following four states: On, Rest, Skip and Control. The On, Rest and Skip states are all standard, but where things get interesting is setting a notes state to “Control”. Now you have just handed over control of that cell/step to the Delinquencer. The Delinquencer now decides what happens based on the other settings you make.

The PatterMaker screen makes it easy for you to assign the state to the 64 steps and which cells/steps you are going to give the Delinquencer control over.
So once the Delinquencer has some notes to play with, the fun starts. On the Delinquencer menu page you will see that the 64 grid of notes are displayed and 8 modulation indicators run along the bottom and on the right. The modulation indicators have one of two settings, either On (lit) or Off (un-lit). If the intersecting cell/step at an “On” modifier in a column and row modifiers are both On.

###Navigation and finding your way around
The Delinquencer application consists of four screens: Sequencer, Note Entry, PatterMaker and Delinquencer. You can access these by pressing the [K2] button on your Norns. The four screens loop around as you continue to press the [K2] button, see the Figure below:

<img src="https://github.com/kevinlindley/delinquencer-support/blob/main/MenuNavigation.png">

### Screen 1 - Sequencer
#### Navigation Controls
* Encoder 1 - Change BPM
* Encoder 2 - Menu Item Selection
* Encoder 3 - Menu Item Value
* Key 1 - System Menu
* Key 1*- Reset if Held
* Key 2 - Next Menu
* Key 3 - Stop/Start
#### Settings
* BPM       - Beats per Minute
* Division  - Divs per Beat
* Loop      - Looping Type
* Scale     - Quantised Scale
* Transpose - Transposition
* Preset    - Patches
### Screen 2 - Note Entry
#### Navigation Controls
* Encoder 1 - Sequencer Cell Position Selection
* Encoder 2 - Menu Item Selection
* Encoder 3 - Menu Item Value
* Key 1 - System Menu
* Key 2 - Next Menu
* Key 3 - Toggle Current Cell
#### Settings
* Note      :  Cell Note Pitch
* Velocity : Cell Note Velocity
* Length : Cell Note Length
* Cell State : On/Off/Rst/Skp
* Probability: 0-100%
* Len Notes  : Set all Note Lengths
### Screen 4 - PatternMaker
#### Navigation Controls
* Encoder 1 - Change BPM
* Encoder 2 - Menu Item Selection
* Encoder 3 - Menu Item Value
* Key 1 - System Menu
* Key 2 - Next Menu
* Key 3 - Stop/Start
#### Settings
* Pattern  - Mod Pattern
* Neutron  - On/Off/Rst/Skp/Ctl
* Proton   - On/Off/Rst/Skp/Ctl
* Mutation - 0-100%
### Screen 4 - Delinquencer
#### Settings
* Encoder 1 - Select Modifier
* Encoder 2 - Menu Item Selection
* Encoder 3 - Menu Item Value
* Key 1 - System Menu
* Key 2 - Next Menu
* Key 3 - Stop/Start
#### Settings
* X-Pat  - Column Pattern
* X-Loop - Column Change Freq
* Y-Pat  - Row Pattern
* Y-Loop - Row Change Freq
* State  - Modifier Setting
* Preset - Presets to try
## Installation
1. From maiden:
```;install https://github.com/kevinlindley/delinquencer```
2. Power Off and On to install the new Engine provided.

## Bugs Fix - Release 2.1.0
* Splashscreen bug cause by incorrect path fixed, thanks to Mace Ojala for reporting the bug and the fix :-).

## Bugs Fix - Release 2.2.0
* Fixed bug, you can now use all of the MIDI devices and not just 2 to send sequences out to external MIDI devices.
* Also changed the code so it shows which MIDI device the Delinquencer is connected to which is more useful than just the Device ID.
