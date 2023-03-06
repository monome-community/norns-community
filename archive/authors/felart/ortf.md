---
title: ORTF
description: Sort of Radio music clone. Each station is an audio file.
published: true
date: 2021-10-26T13:09:14.729Z
tags: utilities, midi, samplers
editor: markdown
dateCreated: 2021-10-09T19:16:32.837Z
---

## ORTF

Sort of Radio music clone.
each station is an audio file.

The idea is to treat your tape folder as a radio and navigate into it

Change samples rep in params
(default is tape)

![ortf.png](/community/felart/ortf.png)

## Requirements
* norns
* samples in tape folder
* MIDI controller (optional)


## Documentation
* E1: radio station (sample)

#### Some lags may occur if you change too quicly (lots of softcut load/unload!)

* E2: scrobe in sample
* E3: rate (-4 to 4)

* K2: loop ponts : start / end / reset
* k3: jump to start

* ALT is K1
* K1 + E2: adjust loop start
* K1 + E3: adjust loop end
* K1 + K3: saved  loop in tape (rate=1 only)
 
## MIDI CC
* 9:sample
#### Some lags may occur if you change too quicly (lots of softcut load/unload!)

* 14:start
* 15:end
* 20:rate
* 21:position

## links

- [view on llllllll](https://llllllll.co/t/ortf/39694)
- [view on github](https://github.com/felart/ORTF)
{.links-list}

## demo

<iframe src="https://player.vimeo.com/video/494471477?h=d228f88d75" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>