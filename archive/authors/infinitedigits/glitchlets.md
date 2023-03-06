---
title: glitchlets
description: add glitching to everything
published: true
date: 2021-03-28T18:18:59.003Z
tags: audio fx
editor: markdown
dateCreated: 2021-03-28T18:18:56.528Z
---

## glitchlets

add glitching to anything/everything.

![glitchlets.png](/community/infinitedigits/glitchlets.png)

https://www.instagram.com/p/CGG1TPdhdCO/

*lets glitch with glitchlets.*     
                                                                                   
this script glitches incoming audio. everything is quantized to the global tempo so it stays somewhat in beat. this script is inspired by a [supercollider script glitching the "amen break"](https://sccode.org/1-1e) and a [recent track by John Frusciante](https://www.youtube.com/watch?v=1q8Yf-vlZg4).

there are five voices for glitching. each voice has individual volume, panning, gating, positions and probabilities. each voice contains a softcut loop with random tape modulations. each voice *also* emits a  supercollider engine that adds a wobbly resonant low pass filter to each glitch to get that 90's feel.

### Requirements

- audio input
- norns

### Documentation

**quickstart:** put music into line-in. set norns global tempo in `clock -> tempo` to tempo of music. open glitchlets and press K1+K2.

all five glitchlets can be consciously controlled via global params or quick menu. quick menu:

- first set clock->tempo then reload glitchlets
- K1+K2 does quick start
- hold K1 to turn off glitches
- K2 manually glitches
- K3 or K1+K3 switch glitchlet
- E1 switches parameters
- E2/E3 modulate parameters

*note:* make sure to restart norns the first time you install because it has a new supercollider engine that needs to be compiled.

### Download

v0.2.1 - https://github.com/schollz/glitchlets/releases/tag/v0.2.1

https://github.com/schollz/glitchlets