---
title: initenere
description: 2-dimensional polyrythmic, random note sequencer.
published: true
date: 2021-03-28T16:16:48.898Z
tags: sequencers, crow, grid, midi
editor: markdown
dateCreated: 2021-03-21T16:55:44.753Z
---

## screenshot
![initenere-screen.png](/community/vicimity/initenere.png)

## description

/// Confining spaces of random seeds. ///

2-dimensional polyrythmic, random note sequencer for the Monome Norns.

![grid](https://llllllll.co/uploads/default/optimized/3X/3/0/308f7abfcf5733c8e26e6b415511742cce27d361_2_1380x672.jpeg)

### Documentation
At startup a random seed of 4x4 notes are generated, these can be re-seeded in params.

The screen has eight edit positions. Navigate with E1.

**Horizontally** 1-4 selects four separate rows of sequencers. These trigger notes and move in one of three ways. Edit with E2.
`>` forward
`<` backward
`~` random
`-` halt movement

E3 alters sequencer speed from /4 (slow) to 16x (fast).

K3 (hold) enables alt-edit.

`o -3 to 3` Sequenced notes octave offset (edit with K3+E2)
`x, 1, 2 and 5 o` Sequenced notes octave range (edit with K3+E3)

**Vertically** there are four sequencers with their own individual direction and speed (same instructions as above E2 = direction and E3 = time).

Parameters > Edit
**Load & Save** 
set 1-100 (including params)
**Midi, Crow & Outputs**
Choose midi settings and sequencer routings
Crow in 2 rising V change randomizes the note matrix
**Time Routings**
Route sequencer times
**Scale & Notes**
Choose scale and root note
Parameters for octave offsets and ranges.
Seed new random note matrix
**Molly the Poly**
**w/syn**
Edit synth stuff...

## install

from maiden type
`;install https://github.com/linusschrab/initenere`

## links

- [view on llllllll](https://llllllll.co/t/initenere/)
- [view on github](https://github.com/linusschrab/initenere)
{.links-list}