---
title: tetrabobo
description: triangle wave organ with variable slope for norns & shbobo shnth
published: true
date: 2022-12-20T01:25:42.826Z
tags: synths
editor: markdown
dateCreated: 2022-12-14T20:42:29.920Z
---

## screenshot

![tetrabobo.png](/community/william-hazard/tetrabobo.png)


## description

triangle wave organ with variable slope for norns & [shbobo](https://ciat-lonbarde.net/shbobo/index.html) [shnth](https://llllllll.co/t/shbobo-shnth-patches-and-appreciation/7385)

*note: requires the [shnth library](https://llllllll.co/t/norns-shnth-library/33238) for norns, which can be found [here](https://github.com/cfdrake/shnth)*

In the tradition of [@Justmat](/authors/justmat)’s wonderful [otis](https://norns.community/authors/justmat/otis), this is a very loose adaptation of Peter Blasser’s [Ciat-Lonbarde](https://ciat-lonbarde.net/ciat-lonbarde/index.html) [Tetrax Organ](https://ciat-lonbarde.net/ciat-lonbarde/tetrax/index.html). The principle is the same: 4 wooden bars each elicit a triangle wave with variable slope when touched. The rise and fall times can be changed independently of one another (for those more familiar with the world of Eurorack, you might think of this as something like a Maths or other voltage-controlled envelope generator running at audio rate), to shift between saw, triangle, and ramp shapes but also to determine overall pitch. Each bar also has its own independent pitch control, whose value is added to the master rise and master fall time values to determine the pitch of the oscillator expressed by that particular bar. Bars are numbered 0-3 (not 1-4).

Additionally, there is chaos. When chaos is increased (in either a positive or negative direction), modulation is gradually increased from one oscillator to the next in a circular pattern (read: FM). It gets noisy. You can control all of these parameters either from the parameters menu, with midi-mapping (for example, if you wanted to recreate the experience of pitch sliders on the Tetrax Organ, you could map bar pitches to sliders on a [16n](https://llllllll.co/t/16n-is-a-bank-of-faders-release-thread/18620) faderbank or similar device), or with norns’s knobs and encoders. K1 increases the resolution of all 3 norns encoders 10x, for fine tuning of their associated parameters (for example: to fine-tune the pitch of bar 0, hold K1, hold K2, and turn E2).

As with the Tetrax Organ, all of the above-mentioned parameters are available for modulation. On norns, they can be modulated with LFOs, which can be set up in the parameters menu. Also in keeping with the Tetrax Organ, output is in stereo, with the stereo position determined by the s-curve of the shnth’s bars.

*With thanks to [@alanza](/authors/alanza), who provided invaluable help and guidance throughout every stage of this script’s development, especially with regard to the [SuperCollider](https://supercollider.github.io/) engine*

## demonstration

<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1391254177&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>

## requirements
- [norns](https://monome.org/docs/norns/) or [norns shield](https://github.com/monome/norns-shield) (with shnth library installed)
- shnth

## Documentation
*note: you will need to restart norns after installing this script, in order for the synth engine to install*

E1: master chaos (circular FM)
E2: master rise time
E3: master fall time

K1: hold for fine tuning
K2: alt behavior for E2 & E3
K3: alt behavior for E2 & E3

K2 + E2: bar 0 time (pitch)
K2 + E3: bar 1 time (pitch)
K3 + E2: bar 2 time (pitch)
K3 + E3: bar 3 time (pitch)

master rise + master fall + bar time = pitch

shnth minors halve the time of their corresponding bars

shnth majors double the time of their corresponding bars

chaos, master rise, master fall, and each bar’s time can be modulated with LFOs in the params menu

## install

from maiden type
`;install https://github.com/williamthazard/TetraBobo`

## links

- [view on llllllll](https://llllllll.co/t/tetrabobo/60112)
- [view on github](https://github.com/williamthazard/TetraBobo)
{.links-list}
