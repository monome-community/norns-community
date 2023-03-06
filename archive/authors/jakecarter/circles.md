---
title: circles
description: move cursor; place circles; make music
published: true
date: 2022-11-22T00:41:29.556Z
tags: sequencers, crow
editor: markdown
dateCreated: 2021-11-06T22:34:44.485Z
---

## screenshots

![circles.png](/community/jakecarter/circles.png)

## description

The circles script allows you to move a cursor around on screen using *ENC 2* and *ENC 3*. Pressing *KEY 3* will place a new circle at the cursor point. *KEY 2* will remove the circle at the cursor point. Holding *KEY 1* will remove all circles after a confirmation step. *ENC 1* adjusts the cutoff frequency of the filter.

Placed circles will grow with each MIDI tick. This means that it will stay in beat with whatever else you have going on.

Circles will burst when they hit another circle or when the get *too big*. When they burst, they make sound. The sound they make depends on their *x*, *y* position on the screen and how big they are when they burst.

The pitch is determined by their *x* coordinate, with lower pitches on the left and higher pitches on the right.

The timbre is determined by their *y* coordinate, currently connected to PWM of the PolyPerc engine.

The size determins how long the sound will last. Larger circles will sound out for longer.

There are also a few parameters to adjust under the *KEY 1* parameters page. Play around with those.

## install

from maiden type
`;install https://github.com/jakecarter/circles`

## links

- [lines](https://llllllll.co/t/circles/22951)
- [github](https://github.com/jakecarter/circles)
{.links-list}

## demos

<iframe width="560" height="315" src="https://www.youtube.com/embed/t3IKu6pQcxM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### v1.6

This is a pretty major update under the hood. Because of that I took this as an opportunity to update some of the param IDs. This means that existing PSETs will probably result in unexpected behavior.

**Before updating, if you have any saved PSETs that you rely on, I'd encourage you to write down the settings so you can recreate them after updating.**

- Finally switched from using the old-school `beatclock` to the new hotness, `clock`.
- Added midi-in transport controls; circles will now start/stop when the midi leader starts and stops.
- MIDI out device shows name in params menu
- Updated order of `outputs` param list; This will probably cause issues with any existing PSETs
- Cleaned up params menu by grouping some params
- Added new "step division" param


### v1.5

- Added MIDI support. Choose midi device (1 - 4) and channel (1 - 16) in params.
- Added scale selection. Choose root note and mode in params.


### v1.4

- Added Crow + Just Friends support. Please make sure to update your crow and Norns to the latest firmware.


### v1.3

- Circles now supports the system saving/loading of params. See the PARAMETERS section of https://monome.org/docs/norns/ for more information.


### v1.2

- Added deterministic burst type option. This should allow for more loop like rhythms.


### v1.1

- Added crow support.

- Added params for output; audio or crow. If crow:
     - Output 1: Trigger
     - Output 2: Pitch
     - Output 3: Y Pos  (0 - 10V)
     - Output 4: Radius (0 - 10V)
 
- Added params for clock; midi or crow. Crow accepts clock on input 2. I would like this to be on input 1, but there is currently a bug with norns or crow mentioned here (https://llllllll.co/t/crow-help-norns/25863/10).
