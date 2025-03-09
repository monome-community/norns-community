## rebound: a kinetic sequencer

### about

rebound is a kinetic sequencer for norns 2.0.

Spawn orbs that bounce endlessly from left to right, top to bottom, and back
again. Each orb has its own velocity, direction, and note value. These values
may be adjusted individually or as a group. When an orb hits the top or bottom
its note plays. When an orb hits the left or right its note plays an octave
down or up, respectively.

Notes are quantised to the current scale and tempo, both of which may be set
through the parameters menu. rebound will send midi notes, should a midi output
device be attached, and may also slave to an external clock, should one be
present.

### install

This version of rebound is for norns 2.0. To install it, ssh into your norns,
and clone this repository into the dust directory:

  $ cd dust
  $ git clone https://github.com/nf/rebound.git

