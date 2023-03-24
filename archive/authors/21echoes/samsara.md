---
title: samsara
description: a minimalist looper
published: true
date: 2021-12-23T17:47:38.175Z
tags: delays + loopers
editor: markdown
dateCreated: 2021-03-22T17:15:34.454Z
---

> **samsara** /səmˈsärə/
> the cycle of death and rebirth to which life in the material world is bound

Samsara is a minimalist looper that, given enough time, reaches nirvana.

![samsara.png](/community/21echoes/samsara.png)

Inspired by [Dakim](https://www.youtube.com/watch?v=AmQ7AMnooj0), Samsara invites you to slowly layer in new material as old material fades away. Toggle recording on and off easily while the loop plays, or use one-shot record mode to precisely record a single phrase. The loop duration is set in terms of tempo & beats, making it simple to integrate into other musical contexts (it uses norns' clock system, so you can use MIDI clock & transport messages, Ableton Link, or Crow). Tap tempo is also available via K2+K3, and a click track is available via K2+e3.

You can also easily extend the loop. Say you have an awesome 1-bar drum pattern, and now you want to add harmonic content. Your harmonic phrase is probably longer than that one bar, so just hold K1 and tap K2 to double to two bars, and then again to double to four bars. Now you can layer a 4-bar harmonic phrase on top of that original 1-bar drum loop and keep everything moving.

## Requirements
* norns (update to software version 200424 or later)
* Audio in (stereo or mono, select via params menu)

## Documentation
* E1: Number of beats
* Hold K2+turn E1: Tempo
* E2: Loop preserve rate
* E3: Record mode (loop/one-shot)
* Hold K2+turn E3: click track (on/off)
* K2: Start/pause playback
* K3: Arm/disarm recording
* Hold K2+tap K3: Tap tempo
* Hold K1+tap K2: Double buffer
* Hold K1+tap K3: Clear buffer

## Roadmap
* Param-ify recording and playing (so they can be MIDI-mapped)
* threshold-triggered recording
* Work on "double buffer" not introducing discontinuities (see https://github.com/monome/norns/issues/1151)
* "Extend mode"
  * While recording, keep extending the loop by the original loop length, until "stop recording" is hit (and then it'll stop recording at next multiple-of-original-length). Kinda like "double buffer", but useful when you don't know how long your new phrase is gonna be
* loop wav viewer (with tempo indicators?)
* Varispeed
* Multi-mode filter
* Loop window slide, loop endpoint move

## Download
Latest version: v1.1.0 (8a0d38b)
Install by visiting http://norns.local/maiden when your norns is on WiFi and typing
```
;install https://github.com/21echoes/samsara.git
```
into the command entry box at the bottom of the screen.

Also available as a [direct download](https://github.com/21echoes/samsara/archive/master.zip). Unzip it, rename the folder to just "samsara", and put the whole folder onto your norns inside the `/home/we/dust/code` folder

Github: https://github.com/21echoes/samsara

## discussion
For feature requests and bug reports, discuss [over on lines](https://llllllll.co/t/34095)