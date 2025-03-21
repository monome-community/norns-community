# cc-canvas

Fifteen grid-controllable MIDI CC messages with slewing and snapshot recall.  
This project runs on both norns and seamstress.  
Requires monome zero / 256, though script can be edited to accommodate any dimensions.

Each column is a fader, which can be assigned a target MIDI device, channel, CC number and CC value -- see the system parameters menu for these settings.

Each key in each fader column (1-15) sets CC value directly -- 127 at top, 7 at bottom, reselect current value to zero-out.  

`PARAMETERS > morph` will increment the CC value of every slider by a random value between -10 and 10.

snapshots @ `(16, 1-14)`
- hold to capture current values as snapshot
- press stored snapshot to recall stored values

ALT key @ `(16, 16)`
- hold to show slew times
- while holding, hold stored snapshot to delete snapshot

ALL key @ `(16, 15)`
- hold and press a value to set all channels to that value
  - this works on the CC values and slew times pages
- while holding, press stored snapshot to jump all values to that snapshot without slewing
- while holding, `PARAMETERS > morph` will jump to new morphed value without slewing
