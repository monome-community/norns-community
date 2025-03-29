## Fugarc

"awake meets fugu" - a for the Norns (@popgoblin)

*Current release v1.0.2*

Fugarc is inspired by the fugu-script by @its_your_bedtime  and "Fugue-machine" for the iPad, but based on the Awake script by @tehn. Optimised for use with Crow, Arc, Grid with Ansible thru Crow and i2c.

Every function can be used without Grids, Arc or the Ansible. It will not make sense without the Crow connected to CV-responding gear though.

A pattern (between 1 and 16 steps wide) can be played as 4 different tracks.
Think of a track as a "playhead" you can direct to move through the steps with different speeds, different directions — or even randomly. You can also set each track to transpose the steps of patterns.

Pitch and trigger information for each track can be directed to crow and/or ansible outputs in the parameter section. You can also direct track outputs to (seperate) midi channels

Also available are options to direct clock-signals, extra LFO's and random voltages to crow outputs - available in the parameter-sections.

### Requirements:
- Crow

Optional: *Ansible, Arc, Grid, MIDI, TXo*

### Controls:
- **Grids** controls pattern

- **Arc** controls track 1 through 4 playback-modes. K1+Arc controls speed.

- **E1** changes modes:
	STEP/LOOP/TRACKS/OPTION

- **K1** held is alt *

#### STEP
- **E2/E3** move/change
- **K2**  *clear
#### LOOP
- **E2** loop length
#### TRACKS
- **E2** selects
- **E3** changes div *transpose
- **K2/K3** step thru  modes
#### OPTION
- *toggle
- **E2/E3** changes
