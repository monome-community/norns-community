---
title: barcode
description: six-voice varispeed random looper
published: true
date: 2021-03-22T16:46:03.362Z
tags: delays + loopers
editor: markdown
dateCreated: 2021-03-22T16:42:41.640Z
---

## Barcode

![barcode.png](/community/infinitedigits/barcode.png)

loop a sound into six voices playing at different levels & pans & rates & positions, modulated by lfos on every parameter.


https://www.instagram.com/p/CDxUwsSh7oP/

inspired by [cranes](https://llllllll.co/t/cranes/21207) and the [cut and poll softcut study](https://github.com/monome/softcut-studies#3-cut-and-poll), i tried to take these ideas to the extreme. in *barcode* i wanted to utilize all six voices after recording into a buffer.

### Requirements

- norns
- audio input


### Documentation

- hold K1 to shift
- K2 to pauses LFOs
- K3 starts recording
- any key stops recording
- shift+K2 switches buffer
- shift+K3 clears
- E1 changes output/rec levels
- E2 dials through parameters
- E3 adjusts current parameter
- shift+E3 adjusts freq of lfo

after recording finishes, the corresponding buffer will be played on six different voices. 

each voice has six parameters: level, pan, rate, reverse, start point, and end point. each of these parameters is modulated by a randomly initialized lfo (that's 36 lfos!). at this point, the lfos cannot be modulated except by changing the code.

in the ui, the parameters of the voices are represented as six groups of five lines. each group of lines corresponds to one voice. the order of the five lines corresponds to the parameters:

1. level ( L )
2. pan ( P )
3. rate ( R )
4. direction ( D )
5. tape start/end points ( T )

you can bias the modulation for any parameter using E2 to move the corresponding line (a parameter for a voice) and then adjusting with E3. shift+E3 adjusts the frequency of the lfo for that parameter.

the line at the very top is for the overall level, which can be adjusted with E1. during recording, E1 adjusts the recording level.

_note_: the buffer max is 60 seconds. the loop end point is whatever end point you stop recording though.

### Download

download in maiden or via command:
```
;install https://github.com/schollz/barcode
```

https://github.com/schollz/barcode