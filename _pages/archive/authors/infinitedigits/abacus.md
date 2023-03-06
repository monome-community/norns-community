---
title: abacus
description: sequence rows of beats with samples
published: true
date: 2021-03-28T18:10:15.796Z
tags: sequencers
editor: markdown
dateCreated: 2021-03-28T18:10:13.120Z
---

## abacus

sequence rows of beats with samples.

![abacus.png](/community/infinitedigits/abacus.png)

demo:

https://www.instagram.com/p/CHEyfpZB0YZ/

tutorial:

https://vimeo.com/474676681

this norns script creates sequences of samples from a tape. you can load any tape and splice it into up to 26 samples (named a-z). samples can then be patterned into 16-subdivided measures. patterns can then be chained together.

this script was a hard one to make because at a certain point i kept getting caught up playing with for hours instead of making it "user friendly." let me know if you find things to improve!

this script builds off others. it is inspired a lot from ideas in [glitchlets](https://llllllll.co/t/glitchlets) (no realtime here) and a lot of code ideas from @mattbiddulph's exquisite [beets](https://llllllll.co/t/beets-1-0/30069) (initially i forked beets but i didn't want to ruin the code with my hacks). also inspiration from the po-33. and, it is inspired by @csboling's beautiful waveform renderings in the latest update.

future directions:

- fix all the 🐛🐛🐛
- add individual parameters for samples
- add play trigger
- ?? requests

### Requirements

- norns (version 201023+)


### Documentation

any mode

- K1+E1 changes mode

sample mode

- E1 changes sample
- E2/E3 change splice position
- K1+K3 starts/stops chain
- K2 zooms
- K3 plays sample

pattern mode

- E1 changes pattern
- E2 selects sample
- E3 positions sample
- K2 patterns
- K3 plays sample
- K1+K2 erases position
- K1+K3 plays pattern

chain mode

- E2 positions
- E3 selects pattern
- K2/K3 does effects

### Download

https://github.com/schollz/abacus