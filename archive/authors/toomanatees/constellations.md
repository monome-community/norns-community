---
title: constellations
description: scan the stars; make music! an interactive sequencer for Norns, Crow, JF, and midi.
published: true
date: 2022-03-15T17:14:52.298Z
tags: sequencers, crow, midi, generative
editor: markdown
dateCreated: 2022-03-15T17:11:25.620Z
---

## screenshots

![constellations.png](/community/toomanatees/constellations.png)

## description

scan the stars; make music! an interactive sequencer for Norns, Crow, JF, and midi.

## install

from maiden type
`;install https://github.com/timothy-taylor/constellations`

## links

- [view on llllllll](https://l.llllllll.co/constellations)
- [view on github](https://github.com/timothy-taylor/constellations)
{.links-list}

## getting started

to start making music just __press [key3] and use encoders 2 & 3 to tag some stars__.

if you like your little sequence __press [key3] again to lock it__ and just watch the stars pass by, otherwise constellations can make some comically long sequences with ease. __Clear your sequence with [key2]__.

A star’s location on the Y axis determines the note value (bottom of the screen is low notes, top of the screen is high notes). A star’s size determines the release time and crow’s bipolar cv. A star’s brightness determines the amplitude and crow’s unipolar cv.

### controls

* [key 1] hold for ALT
* [key 2] clears the sequence
* [key 3] locks/unlocks the sequence
* [enc 1] time division to the Norns master clock
* [enc 2] crosshair Y axis
* [enc 3] crosshair X axis
* ALT + [enc1] probability
* ALT + [enc2] star density
* ALT + [enc3] star size
* ALT + [key2] sequence shift
* ALT + [key3] sequence pop

### output, sequencer params, engine params are located in the parameter menu (again thanks to awake & tehn)
* [engine, crow, jf, midi] outputs are all available
* [scale, root, probability, max sequence length, and overwrite logic] are available under ‘sequencer params’
* all notable engine params are available

### crow:
* [input2] unipolar (0-5v) control over Y axis
* [output1] 1 volt per octave
* [output2] clock pulse
* [output3] unipolar cv (0-5v)
* [output4] bipolar cv (-5-5v)