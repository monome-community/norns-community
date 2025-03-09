---
title: automs70
description: Automate up to nine knobs of the MS-70 CDR multieffect
published: true
date: 2021-06-14T08:51:10.431Z
tags: utilities, midi
editor: markdown
dateCreated: 2021-04-16T09:57:41.785Z
---

## screenshots
![automs70.png](/community/pangrus/automs70.png)
## description

This script allows to automate up to nine parameters of the ZOOM MS-70 CDR multieffect. For each knob you can set the minimum and maximum value. The value will change using linear interpolation between randomly chosen values in the selected range, with a BPM related speed.

## Documentation

Connect the MS-70 CDR to the norns and set it as the midi first device.
Use the encoder 1 to select one of the nine controllers.
The encoder 2 sets the minimum value and encoder 3 sets the maximum value that will be sent to the MS-70 CDR.
Pressing key 2 you can select the effect and knob destination.
Use key 3 to randomize min/max values.
Automs70 can be also used to generate nine MIDI control change commands: define in the norns parameters menu the destination CC number and relative midi channel.


## install

from maiden type: `;install https://github.com/pangrus/automs70`
or install via the maiden project manager

## links

- [lines forum](https://llllllll.co/t/automs70/39686)
- [github](https://github.com/pangrus/automs70)
{.links-list}
