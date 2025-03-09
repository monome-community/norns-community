---
layout: project
title: ortf
permalink: /ortf
cover: ortf.png
raw_name: ortf
sanitized_name: ortf
project_url: https://github.com/felart/ORTF
description: Sort of Radio music clone where each audio file in tape folder is a station
discussion_url: https://llllllll.co/t/ortf/39694
documentation_url: 
tags:
 - utility
 - sampler
 - midi
authors:
 - felart
redirect_from:
 - /en/authors/felart/ortf
 - /authors/felart/ortf
---
# O R T F
Sort of Radio music clone
each station is an audio file

The idea is to treat your tape folder as a radio and navigate into it

![GitHub Logo](https://raw.githubusercontent.com/felart/ORTF/HEAD/ortf.png)

Change samples rep in params
(default is tape)

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
