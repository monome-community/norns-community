---
title: bakeneko
description: a haunted drummer companion
published: true
date: 2021-10-18T20:20:54.460Z
tags: sequencers, drums, eduscript
editor: markdown
dateCreated: 2021-03-21T14:39:36.772Z
---

## screenshots

![bakeneko.png](/community/northern-information/bakeneko.png)

## description


the main goal of this script is to help non-developers get comfortable with editing code! the script is relatively short, hackable, and (hopefully) understandable. it uses simple lua patterns and clear variable names.

musically, bakeneko has six tracks. each track contains a simple sequence that causes samples to play. bakeneko uses the norns system clock, so you can sync it with other gear.

open up `bakeneko.lua` in maiden and you can change all sorts of attributes. after editing, save, and re-run the script. here are some global attributes:

```
start_playing_on_boot = true, -- start playing as soon as you launch the script?
default_bpm = 120, -- change with e2 while running
default_level = 100, -- how loud is the whole thing
sample_directory = "/home/we/dust/audio/common/808",  -- change to whatever directory you want
```
and each track attribute can either be set to "random" a particular value:

```
track_1_on = true, -- toggle the sample on and off
track_1_level = 100, -- max level of this sample
track_1_density = 50, -- percentage representing how dense the notes are
track_1_period  = 1/4, -- periods can be anything (i think)
track_1_length = 16, -- how many periods before looping back to 1?
track_1_sample = "808-BD.wav", -- specifcy a sample name
track_1_pattern = "x---x---x---x---", -- draw a pattern with "x" and "-"

track_2_on = "random", -- ...or spin the wheel with "randoms"
track_2_level = "random",
track_2_density = "random",
track_2_period = "random",
track_2_length = "random",
track_2_sample = "random",
track_2_pattern = "random",
```

finally, you can get a taste of "live coding" with the **matron** tab in http://norns.local/maiden. while bakeneko is playing:

```
tracks[1].on = false -- turn off track one
tracks[2].level = 25 -- sets track two's level to 25%
bpm = 100 -- change the bpm
tracks[4].current_step = 1 -- set track four's current step back to 1
toggle() -- start / stop
```


## install

from maiden type
`;install https://github.com/northern-information/bakeneko`

## links

- [view on llllllll](https://l.llllllll.co/bakeneko)
- [view on github](https://github.com/northern-information/bakeneko)
{.links-list}