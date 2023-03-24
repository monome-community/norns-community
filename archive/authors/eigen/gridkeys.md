---
title: gridkeys
description: mod to use grid as a midi keyboard
published: true
date: 2021-10-26T17:30:38.276Z
tags: grid, mods, crow, midi, jf
editor: markdown
dateCreated: 2021-10-10T20:05:57.148Z
---

## description

![grids.jpg|690x461, 75%](/community/eigen/grids.jpg)

mod to use grid as midi keyboard anywhere.

can send midi message towards currently running script (`in`), external hadware (`out`) or both at the same time (`in+out`).


## usage

when no script is loaded, auto-activates in `out` mode. the target device can be selected in the params menu (`MOD - GRIDKEYS > MIDI OUT device`).

will auto-activate in `in` mode for scripts that don't natively use grid. it can anyway be toggled on/off via param menu (`MOD - GRIDKEYS > gridkeys active`).

in `in` mode, notes will be sent to the input of the `virtual` midi device, which you certainly would have to activate in `SYSTEM > DEVICES > MIDI`.


### gotchas

in `in` mode, playing grid will only take effect if current script listens to the `virtual` midi device.

in `out` mode, playing grid will only take effect if target device is other than `none` and `virtual`.


## install

from maiden type
`;install https://github.com/p3r7/gridkeys`


## links

- [view on llllllll](https://llllllll.co/t/gridkeys-mod/49431/2)
- [view on github](https://github.com/p3r7/gridkeys)
{.links-list}