# hpns
hpns - selected randomness step sequencer
(heavily based on parc: https://github.com/monome-community/parc)

requires - norns, grid, crow

200520

---------

hpnsansible - selected randomness step sequencer

200530

requires grid, norns, crow and ansible (in teletype expander mode)

controls
norns
enc 1 - scrolls top bar (notes, divs', octaves, play
 for notes, divs', octaves:
  enc 2 - scroll to parameter
  enc 3 - set selected parameter
 for play:
  enc 2 - set global bpm
  enc 3 - clockwise to play, anti to stop
 key 2 or 3 (any page) - switch grid view from tracks to global

grid
 top row:
  1 to 4 - track selection (each track has the below options)
  9 to 12 - notes, divs', octaves, mutes

 notes, divs', octaves pages
  press any non top-row to toggle selection
 mutes
  1 option, per column. percentage chance of a mute,
  from top to bottom; per division trigger
  0%, 25%, 50%, 75%, 100%

norns  screen columns represent tracks 1 to 4, from the left.
each column parameter matches the corresponding grid row (+1).
for example top left note (on norns) is track 1,  row 2 toggle option (on grid).
bottom right is track 4, row 8 toggle. and so on).

global grid page
 rows 1 to 4
  play head and loop brackets, per track
  single press to jump playhead
  double press to set loop points
 rows 5 to 8
  rate, per track.
  defaults a 'normal rate' for 4/4
  left mostly halves rate
  right mostly doubles it
  (change globalrates table to suit. might make this parameter changeable in the future)

outputs
 ansible - trigger and cv match track number
 crow - either trigger on beat one only, or
             trigger every step (not division)
             regardless of step mute.
             selectable per track, via params.
