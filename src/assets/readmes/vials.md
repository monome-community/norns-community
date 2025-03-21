# vials

## a sequencer for norns

each track features 4 slots containing decimal values between 0 and 255. a decimal is converted to its binary representation and played in a sequence of binary where 1 sends a trigger and 0 denotes a break. a track can be muted, has its own probability and divisions, each sequence can be rotated along its binary string. the sequencer is enhanced for performance using a grid, can be externally clocked and outputs midi.


## home

the first view is the main interface
on this page

- ENC 1 changes BPM 
- ENC 2 changes track
- ENC 3 changes value

- KEY 1 takes you to PARAMS
- hold KEY 1 to start the sequencer
- while playing, hold KEY 1 for SEQ ALT
- SEQ ALT + KEY 2 resets the sequence
- SEQ ALT + KEY 3 stops the sequence

- KEY 2 changes slot on selected track
- KEY 2 + KEY 3 mutes the track

- hold KEY 2 for TRACK ALT
- TRACK ALT + KEY 2 rotates track sequence
- TRACK ALT + ENC 2 changes track division
- TRACK ALT + ENC 3 changes track probability

- hold KEY 3 + ENC 3 to load pattern

each track is configured to output midi and trigger a sample. see the PARAMETERS menu for configuration.

## grid

grid expands the performability of vials, allowing looping and editing sequence values in both binary and decimals. performance controls such as sample triggers, mutes, reverb and delay controls and randomisation are also exposed on grid level. reverb and delay effects have their own view, found by holding the reverb and delay view keys which then allow for fx control with the norns encoders.

![alt text](assets/grid_interface.jpg "grid interface")
* **A** - trigger samples
* **B** - mute track
* **C** - track reverb send switch (-60.0db : 0db)
* **D** - kill all reverb sends
* **E** - change track
* **F** - change selected slot
* **G** - loop slot
* **H** - param view
* **I** - decimal number pad to input decimals
* **J** - hold to add more decimals to same slot (ie, 2 to 1 = 12)
* **K** - shift track sequences
* **L** - rotate forward or backwards track sequence
* **M** - reset all sequences to start position
* **N** - start / stop
* **O** - reverb controls left to right
    - reverb level switch (-60.0db : 0db)
    - random short reverb
    - random mid reverb
    - random long reverb
    - reverb view 
      - enc 1 - reverb level
      - enc 2 - reverb room size
      - enc 3 - reverb damp
* **P** - echo controls left to right
    - echo send mute
    - echo edit view
      - enc 1 - echo level
      - enc 2 - rate
      - enc 3 - feedback
    - randomise echo
    - kill echo
* **Q** - binary input, tap for 1, tap twice for 0
* **R** - trim binary sequence at index
* **S** - hold to access load/save 
* **T** - load pattern
* **U** - save pattern

## saving / loading
on start vials loads a session of 15 patterns from memory
within the session patterns can be saved and loaded
the session is saved to disk when stopped
note the current pattern must be saved to the session to be recalled.

## vague ideas for the future
* fills
* swing 
* accents
