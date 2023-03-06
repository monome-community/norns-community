---
title: Less concepts 3
description: cellular automata sequencer
published: true
date: 2021-05-20T12:50:20.567Z
tags: sequencers, crow, grid, midi, generative, jf
editor: markdown
dateCreated: 2021-03-28T15:53:54.497Z
---

## description

*less concepts is rooted in the idea that complexity is just a shit-ton of simplicity, chained together. at its core, less concepts holds 65,536 possible combinations of notes which can be gated, offset, and manipulated to create minimal sequences for improvisation. small changes to a single parameter can bring sweeping or subtle changes.*

*seek. think. discover.* - dan derks

less concepts 3 is a collaboration between [@dan_derks](/authors/dan_derks) + [@vicimity](/authors/vicimity)

## instructions

![lessconcepts3.png](/community/collabs/lessconcepts3.png)

### start

at first you are met by a constructive concept built from the seed 36 and rule 30. root note is C and the scale is major. the sequence is fed through the built in sound engine "passersby" and midi device 1 / channel 1.

- the combination of seeds and rules feed the sequencer with 8-bit numbers. this number is visualized by the eight squares top left on the screen / grid (in the screenshot above 11001111 = 207), a new number is seeded with every beat of the selected time signature. the two voices are individually triggered when they cross paths with the true value 1. the current 8-bit number (11001111 = 207) translates into a note by passing it through the limits for high / low and then transposed within the selected scale.

- navigate the main performance screen by scrolling with E1, changing values with E2 and E3. adding snapshots with K2 and randomizing selected values with K3.

- K3 takes on a different role when snapshots are selected (bottom left) or cycling sequencer direction / duration (bottom right). while snapshots are selected K3 will randomize all values (except time and duration). while direction / duration is selected K3 activates a ´destructive´mode, indicated by '*'. all changes to snapshots will be saved while in destructive mode. if you wish to delete a snapshot hold K2 and press K3, this results in the snapshot still playing but no snapshot is selected. you scroll through and select the snapshots with E2.


NEWS

- time: change time signature for the sequencer. 1/8 - 1/32 (more options available in params).
- a cycling sequencer that steps through saved snapshots and move when the indicated duration has passed. the cycling sequencer can move up '>', down '<' or random '~'.
- midi notes can trigger snapshots. select "midi -> snapshot root" and play away!

/ / / / / / / /

### **\~ r e f r a i n**

![2|614x307](https://llllllll.co/uploads/default/original/3X/c/c/cc73969b2b59583e0fdad265babbea4dd9dfcaf3.png) 

hold K1 to find the built in pitch, delay, micro looper.

NEWS

- buffers are now visible (top right)
- input mix (engine and adc) is editable on screen (prev. in params / adc is new)
- K2 toggles state for both buffers 'rec | play'

/ / / / / / / /

### **params -> edit**

![3|614x307](https://llllllll.co/uploads/default/original/3X/d/a/da5505f3e667d6b9f60e1a9e6ffa5139d8e66393.png) 

'load & save' 
- all values including params are now saved with a set.
- saves from pre 3.0 works, you need to move them from `dust\data\less_concepts` to `dust\data\less_concepts_3`. also saves with 0 presets/snapshots will not work (I think maybe they never did?)

'time, midi & outputs'
- select time range('legacy 1/8 - 1/32', 'slow 1/1 - 1/16' and 'full 2/1 - 1/32' (locked with snapshots)
- default length (cycle) 1x - 32x (cycle duration for new snapshots)
- midi (choose midi device and channels) turn midi/link transport on / off
- midi -> snapshots root (play your snapshots with a midi keyboard)
- outputs, choose outputs for voice 1 & 2.

'scaling & randomization'
- choose scale and global transpose
- set transpose randomization
- clamp the values for randomization with 'randomization limits'

\+ params for ~refrain, passersby and w/syn

### Grid operation
![less_concepts_grid|689x332](https://llllllll.co/uploads/default/optimized/3X/6/c/6ce522f225137587a0b7f0e3109b45b54f27064c_2_1378x664.png) 


## install

from maiden type
`;install https://github.com/linusschrab/less_concepts_3`

## links

- [view on llllllll](https://llllllll.co/t/less-concepts-3)
- [view on github](https://github.com/linusschrab/less_concepts_3)
{.links-list}