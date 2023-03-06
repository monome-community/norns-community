---
title: spirals
description: a spiral sequencer
published: true
date: 2021-10-03T17:51:08.131Z
tags: sequencers, generative, midi, grid, midigrid
editor: markdown
dateCreated: 2021-04-10T18:25:18.964Z
---

## screenshots

![spirals.png](/community/tomw/spirals.png)

![spirals2.png](/community/tomw/spirals2.png)

## description

Notes of the selected scale are spread around a circle. Points are drawn by rotating a set amount from the last point while moving outwards slightly and notes are triggered depending on where they land.

up to 4 spirals can play at the same time. each spiral can be set to output midi or audio using the PolyPerc engine or [mx.samples](/authors/infinitedigits/mx-samples) if installed.

![anim.gif](/community/tomw/anim.gif)

## install

from maiden type
`;install https://github.com/tomwaters/spirals`

## documentation

### controls

E1 change current spiral
K2 play / stop current spiral
K3 toggle options
→ E2 change option
→ E3 change value
K1 + K2 toggle lock sequence to the last X number of notes
K1 + K3 toggle scale overlay (when options are hidden)

### options

changes to the options apply to just the current selected spiral

![anim_settings.gif](/community/tomw/anim_settings.gif)

#### rotation
how far around the circle to move each step

#### lfo
an lfo can be used to alter the rotation amount. the lfo amount setting controls how much the rotation will be altered - with an lfo amount of 1.0, the lfo will move between -1 and 1 and add that value to the rotation. 

#### lock steps
when the spiral is locked (k1 + k2), the last few steps of the sequence will be repeated. the lock steps setting controls how steps will be repeated. hint - the lock steps setting can be changed while the sequence is locked.

#### play mode
a spiral can play notes or chords. in chord mode, the 3rd and 5th are added.

#### step div
spirals play according to the norns clock. step div controls how many steps play per beat. when set to 2, 2 steps play per beat, when set to 0.5 a step plays every 2 beats.

#### rests
the rests setting inserts rests into the circle of notes giving the possibility of not playing a note on a step

### parameters
additional settings which you are less likely to want to change so frequently are available in the parameters. overall settings for the polyperc and mx.samples engines are available as well as per spiral settings for the in-app settings plus:
* output (audio/midi)
* mx.samples instrument
* midi out device and channel
* midi in device and channel (to set root note)
* note length
* velocity (for midi and mx.samples)

### grid
spirals supports grid or midigrid to enable you to change current spiral, start/stop the current spiral and lock/unlock the current spiral.

![spirals_grid.png](/community/tomw/spirals_grid.png)
on the bottom row the left 4 pads change the current spiral, the right most pad starts or stops the current spiral and one in from the right locks and unlocks the current spiral.

the top 6 rows fill up as notes play - the bottom right most lit pad is the most recent note. 

press two pads to lock the current spiral to loop between those notes.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-2XTOoBuU0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## links

- [view on llllllll](https://llllllll.co/t/spirals/)
- [view on github](https://github.com/tomwaters/spirals)
{.links-list}

