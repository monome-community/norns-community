## plonky

> plonk (/plɒŋk/) - to play a musical instrument, usually not very well but often loudly
> - Cambride Dictionary


https://vimeo.com/520650445


plonky is a keyboard and sequencer. i made it to be able to play [mx.samples](https://llllllll.co/t/mx-samples/41400) directly from the grid. the grid layout (and name) is inspired by the [plinky synth](https://www.plinkysynth.com/), i.e. it is a 8x8 layout with notes spaced out between columns by a specified interval (default is C-major scale spaced out by fifths).


### Requirements

- norns
- grid

### Documentation

use the grid to play an engine. by default the engine is "PolyPerc", but if you install [mx.samples](https://llllllll.co/t/mx-samples/41400) you can also play that by switching "`PLONKY > engine"` via parameters.

**voices:** use E1 to change voices. each 8x8 section of the grid is a voice. you can play notes in that voice by pressing pads. the notes correspond to a C-major scale, where each column is a fifth apart. use the menu `PLONKY` to change parameters. while in a menu you can press a note to change to that voice.

**arps:** you can do arps by turning E2 or E3 to the right. in "arp" mode you can press multiple keys and have them play. in "arp+latch" mode the last keys you pressed will play. in "arp+latch only" mode keys you press will change the arp but no play when you press (useful for seamless arps). change the speed using the "`PLONKY > division`" parameter in the menu.

**patterns:** you can record patterns by pressing K1+K2 (for right voice press K1+K3). press a note (or multiple) and it will become a new step in the pattern. you can hold out a step by holding the notes and pressing K2 (for right voice press K3). you can add a rest by releasing notes and pressing K2 (for right voice press K3). erase steps with E2 (for right voice use E3). when done recording press K1+K2 (for right voice press K3). to play a pattern press K2 (for right voice press K3).

**crow + jf:** each voice sends one note to crow at 1v/octave. jf is available if you [change this line of code](https://github.com/schollz/plonky/blob/main/lib/plonky.lua#L28). these are untested so idk if they work.

**midigrid:** check the instructions in the code in the `plonky/lib/plonky.lua` file, search for "midigrid".

### Install

https://github.com/schollz/plonky

from maiden:

```
;install https://github.com/schollz/plonky
```

