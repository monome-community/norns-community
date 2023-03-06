---
title: compass
description: asynchronous looper built around the concept of a command sequencer
published: true
date: 2021-03-30T16:29:36.629Z
tags: sequencers, grid, arc, delays + loopers
editor: markdown
dateCreated: 2021-03-29T20:14:17.042Z
---

![compass.png](/community/olivier/compass.png)

Compass’ sequencer moves through commands of your choosing that trigger different functions. Use commands to, for example:

- manipulate the sequence’s clock or jump to a random step
- randomly change the location of your loop within the buffers
- alter the rate, direction and position of each record/playback head

Compass’ audio buffers and its sequencer each have their own sense of time in order to facilitate experimentation. Interesting effects and textures can be created by recording into loops long and short, randomizing commands on the fly, modifying the sequence length, etc. Midi-mapping additional parameters allows for more gestural control.

As of v3.0, Compass can be controlled via grid, which opens it up to many new performance possibilities. Commands and buffers can be controlled by hand, and all of your gestures can be captured by pattern recorders to build evolving sequences of layered sound.

![1c3148501994b511661d7cda54d3b121d6211b63.jpeg](/community/olivier/compass/1c3148501994b511661d7cda54d3b121d6211b63.jpeg)

## manual
[compass-manual.glitch.me](https://compass-manual.glitch.me/)

## requirements
[200424](https://llllllll.co/t/norns-update-200424/31644)

## installation
Get it via maiden's project manager, or via [github](https://github.com/oliviercreurer/compass) or [direct download](https://github.com/oliviercreurer/compass/archive/master.zip)

## contributions
@GoneCaving for arc support!

## changelog

>[3.1](https://llllllll.co/t/compass-3-1/25192/235?u=olivier) -- support for the new global clocking system + (slightly) reworked key/encoder layout. 

>[3.0](https://llllllll.co/t/compass-3-0/25192/172?u=olivier) -- __Major__ update: grid control, pattern recorders, and command exclusions!

>[2.2](https://llllllll.co/t/compass/25192/159?u=olivier) -- Redesigned recording behavior + new params organization + arc fix.

>[2.1](https://llllllll.co/t/compass/25192/142?u=olivier) -- Redesigned loop behavior + record command + bit reduction.

> [2.0.1](https://llllllll.co/t/compass/25192/121?u=olivier) -- Configurable base metro speed.

> [2.0.0](https://llllllll.co/t/compass/25192/81?u=olivier) -- Introduces crow support.