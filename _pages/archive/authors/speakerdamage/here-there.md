---
title: here/there
description: the sound begins here but you began there
published: true
date: 2021-08-22T15:21:11.259Z
tags: audio fx, synths, granulators
editor: markdown
dateCreated: 2021-08-22T15:21:07.954Z
---

## screenshots

![here-there.png](/community/speakerdamage/here-there.png)

(screen based on a concrete poem by Vagn Steen, 1969)

## description

as you begin inputting sound, norns listens and stores hz values in a table. at a certain point [20 values, for now], it outputs these unquantized values as sine waves (up to 32, for now) in a randomly generated stereo field with random parameters. there are currently two different ways it handles these voices - “chords”, with all changing at once at random intervals, or “drones”, with each voice entering at a random interval until all have been played, at which point value 1 is then brought back in with random parameters. at the same time, softcut is recording 30 second [for now] buffers in the left/right channels. when the buffer is full, stereo playheads begin to jump around to random positions connected to the [random] timing of the sine wave actions/mode. a granular buffer is added to the mix w/ random params concurrently with softcut. sines/softcut/granular levels can all be independently & quickly controlled via encoders.

## install

from maiden type
`;install https://github.com/speakerdamage/here-there`

## links

- [view on llllllll](https://llllllll.co/t/here-there/)
- [view on github](https://github.com/speakerdamage/here-there)
{.links-list}