---
title: o-o-o
description: an fm-based synthesizer and a sequencer that is played by connecting dots.
published: true
date: 2021-10-04T20:25:59.424Z
tags: synths, sequencers
editor: markdown
dateCreated: 2021-09-27T03:48:09.174Z
---

# o-o-o

o-o-o (pronounced *oh-dasho-dasho*) is a fm-based synthesizer and a sequencer that is played by connecting dots.

![o-o-o.png](/community/infinitedigits/o-o-o.png)

https://vimeo.com/615483324

## Requirements

- norns
- grid or midigrid (optional)


## Documentation

- E1 changes instrument
- E2/E3 changes position
- K3 adds connection
- K2 cancels connection
- K1 for help
- K1+K3 pauses/plays+saves on play
- K1+K2 loads current bank
- K1+E1 changes volume
- K1+E2 changes current bank
- K1+E3 adds random (cw) or removes last (ccw)

each dot represents a sound and has an underlying random euclidean rhythm to play that sound. the rhythm is randomly generated based on a seed (`PARAMS > seed`). the triggered sounds are all generated using an internal FM engine ("Odashodasho" engine). its possible to change the engine to [MxSamples](https://norns.community/en/authors/infinitedigits/mx-samples) in the parameters (`PARAMS > engine`)

a dot will trigger a sound if it is connected to another dot. a dot with zero incoming connections and at least one outgoing connections will trigger first. upon triggering, it will "arm" all outgoing connections. when a connection is armed, it will cause the connected dot to trigger the next time the rhythm of that dot hits a beat. connections curved up or curved left are going left to right, or down to up, respectively. connections curved down or curved right are going right to left or up to down, respectively.

there are gradients in the rows and columns. these are hard-coded in the script, but you can easily change the behavior through maiden. currently they are coded so that columns on the left typically trigger slower (except pads) and columns on the right trigger faster. rows on the bottom are lower notes and rows at the top are higher notes (except pads). pads are special - each dot actually represents two intervals, where the row specifies root and the column specifies the other two intervals.

the sounds, scales and root notes for each instrument can be changed in the parameters. you can also set each instrument to send to a midi device or to a crow device (one output for pitch, one for envelope). each instrument has 16 slots in a bank which you can save/load patches for individual instruments. the patch saves will include parameters for the instrument as well as connections in the networ. change banks for `k1+e2` and save a bank by pausing+starting a track (`k1+k3` twice) and load a bank using `k1+k2`.

the grid is optional and opens up some controls. the first 8 columns mirror the grid on the screen and connections can be made by pressing any two points. the first two rows of the second 8 columns (if using a 8x16 grid) save and recall patch saves - you can save a patch by holding for > 1 second and then releasing, and you can load a patch by quickly pressing and releasing. the other buttons on the grid are for scrolling through the instruments and toggling play:

<center>
<img src="https://user-images.githubusercontent.com/6550035/135916882-38887714-d413-4f28-96ee-92a9e42253e4.png">
</center>

simultaneous multitrack recording is available if you select `PARAMS > record each`. this will record all playing instruments into the `~/dust/audio/o-o-o/<date>` folder as `.flac` files. be careful though as this can add up in disk space quickly! the idea here is that you can record multiple instruments and then mix them / add effects to them individually in post.

if using the Odashodasho engine you can switch an instrument from the internal fm engine to a one-shot sample `PARAMS > <instrument> > sound`. then that sound will be triggered instead of the internal fm engine. 

this script wouldn't exist without  Eli Fieldsteel's [FM tutorials](https://github.com/elifieldsteel/SuperCollider-Tutorials/blob/4460e024800b6525e4223c6cce02d9643d0cfbe3/full%20video%20scripts/22_script.scd), which the internal engine is based. it also wouldn't exist without [goldeneye](https://llllllll.co/t/goldeneye) where @tyleretters first implemented this genius idea of creating a grid of random euclidean rhythms.

## Install

install with

```
;install https://github.com/schollz/o-o-o
```