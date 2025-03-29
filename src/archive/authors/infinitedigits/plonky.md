---
title: plonky
description: a grid-based keyboard and sequencer
published: true
date: 2021-04-04T17:17:46.144Z
tags: sequencers, grid, keyboard
editor: markdown
dateCreated: 2021-03-28T19:06:14.977Z
---

## plonky

> plonk (/plɒŋk/) - to play a musical instrument, usually not very well but often loudly
> - Cambride Dictionary

![plonky.png](/community/infinitedigits/plonky.png)

https://vimeo.com/520650445

plonky is a keyboard and sequencer. i made it to be able to play [mx.samples](https://llllllll.co/t/mx-samples/41400) directly from the grid. the grid layout (and name) is inspired by the [plinky synth](https://www.plinkysynth.com/), i.e. it is a 8x8 layout with notes spaced out between columns by a specified interval (default is C-major scale spaced out by fifths).


### Requirements

- norns
- grid (optional)

### Documentation

use the grid to play an engine. by default the engine is "PolyPerc", but if you install [mx.samples](https://llllllll.co/t/mx-samples/41400) you can also play that by switching "`PLONKY > engine"` via parameters.

each 8x8 section of the grid is a voice (1 voice for 64-grid, 2 voices for 128-grid). you can play notes in that voice by pressing pads. the notes correspond to a C-major scale, where each column is a fifth apart (all adjustable in menu).

**arps:** you can do arps by turning E2 or E3 to the right. in "arp" mode you can press multiple keys and have them play. in "arp+latch" mode the last keys you pressed will play. change the speed using the "`PLONKY > division`" parameter in the menu.

**patterns:** you can record patterns by pressing K1+K2 (for voice 2 press K1+K3). press a note (or multiple) and it will become a new step in the pattern. you can hold out a step by holding the notes and pressing K2 (for voice 2 press K3). you can add a rest by releasing notes and pressing K2 (for voice 2 press K3). when done recording press K1+K2 (for voice 2 press K3). to play a pattern press K2 (for voice 2 press K3).

**midi keyboard support**: every voice now has a "midi-in" which you can assign to it a midi keyboard for input. the midi-in keyboards only work if the voice is selected (i.e. only two work at a time). _note_: its important to note that the midi keyboard support is basically allowing to use a midi keyboard as a input into *plonky* - emphasis on plonky. meaning, plonky doesn't accept notes from a midi keyboard that aren't in the plonky grid area (even if there is no grid attached). so if you have a C major scale plugged in, plonky will only respond to the white keys on your keyboard. also, a grid only lets you play two voices at once, so similarly plonky will only respond to two midi keyboards at the same time (you can switch voices to switch which keyboards are used if they are assigned across each voice). I realize these are weird limitations, but its the only way I can see forward to keep the grid-based plonky and the now keyboard-based plonky in unison.


### Install

https://github.com/schollz/plonky

from maiden:

```
;install https://github.com/schollz/plonky
```