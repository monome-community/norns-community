---
title: Superbrain
description: a five track sequencer with various sequencer engines per track
published: true
date: 2021-10-10T12:04:31.690Z
tags: sequencers, grid, midi
editor: markdown
dateCreated: 2021-05-09T06:44:22.908Z
---

## screenshots

![screenshot1](https://llllllll.co/uploads/default/original/3X/f/9/f93408dd147d3e2a57e58691222edb48fdef2a1f.png)

![screenshot2](https://llllllll.co/uploads/default/original/3X/3/2/327c0b5792e5efb995f5874bb5fbecf7a65f938a.png)


## description

SuperBrain is a five track sequencer with configureable sequencer engines per track. Each track can send note information to external gear via midi or to the internal sc engine. Notes can be send in mono, poly, or in fork mode. 64 presets can be stored and loaded.

This script was born out of the necessity to control hardware gear via a central interface. SuperBrain combines "structured midi recording" with "generative sequencing" possibilities.

The script itself is based on my personal workflow as well as on the direct inspiration and indirect influence from this wonderful community with its creative spirit.
Hence it contains scaled down variations of community scripts such as [meadowphysics](https://llllllll.co/t/meadowphysics-norns/21185), classic approaches such as step sequencers and midi loopers each with their own twist.

## Requirements

Launchpad X
(monome grid, not supported yet)

### Setup Norns
1. in `SYSTEM > DEVICES > MIDI` select `Launchpad X 2` in device slot nr. 1 (make sure to select `... X 2` since this is used for the programmers's mode)
2. the devices in slots 2-5 are referred later to as *usb devices*, select any usb midi device which you want to later control from the script

## Documentation

The documentation will use the following short notation for grid interaction:
\*: click
\**: double click
\_: hold
\*_: click followed with hold

[M]: main engine area (x:1-8; y:1-4)
[K]: main keyboard area (x:1-8; y:5-8)
[S]: side area (x:9; y:1-8) == Launchpad side row
[T]: top area (x:10; y:1-8) == Launchpad top row

Thus, the notation **_ [K] \*\* [M]** reads: *hold button in keyboard area, then double click in main area*
For both [S] and [T] adding a number notes the specific button in the area. **\* [S1]** reads: *click first (y=1) button in the side area (x=9)*

### Main Architecture
The grid is devided in three main parts: (1) top row = global functions, (2) upper half = sequencer engine, (3) lower half = isomorphic keyboard.

[comment]:![MAIN|690x493,50%](upload://1W93crhZojuh4PzUC8Hxrnm2PK7.png)

The top row of the Launchpad is used for global functions:
\* [T1]: play all tracks
\* [T2]: stop all tracks

\_ [T3] * [M]: select preset slot
\_ [T3] _ [M]: save to preset slot

\* [T4-8]: select track
\_ [T4-8]: edit track options (sequencer engine, midi target, usb device, midi mode, midi channel)
\** [T4-8]: reset sequencer engine of track

[comment]:![SETTINGS|690x493,50%](upload://jEVTpcl6V7ODEdxAErwzqH0jsH8.png)

[comment]:![KEYBOARD|690x492,50%](upload://d15NNZ4XrpFtCImGy9yblJ48RfK.png)

### Sequencer Engines
#### Quantum#Physics
is a scaled down version of the famous meadowphysics script. This version offers 4 "rhizomatic cascading counters". Rules and ranges are not implemented.

\* [M]: start counter from or jump to value
\** [M]: stop counter

\* [S]: start or stop counter

\_ [S]: set speed and resets for counter
\_ [S] \* [K]: set note

#### Graph^Theory
is a graph sequencer with 4 playheads. The 32 vertices are connected via individual edges. In the default configuration the vertices form a traditional 32 step sequencer, meaning each vertex is only connected to the next vertex. If a vertex contains multiple edges, the playhead follows a random edge.

\** [M]: clear notes in vertex
\_ [M] * [M]: set/remove edge
\_ [M] * [K]: add/remove note
\_ [K] * [M]: add/remove notes

\* [S]: de/activate playhead
\_ [S] * [M]: playhead jump to vertex
\_ [S] _ [M]: set reset vertex

\*_ [S1]: playhead speeds

#### Time~Waver
is a 4 loop midi looper with time filtering. The midi notes are recorded to a fixed 16th note quantization and the loop length can be quantized to the multiple of a chosen value or to the note quantization. Each note stores its order of appearance which can be used to filter early or last added notes (called time frame). This allows to temporarily filter, e.g., early overdubs or to define a time window through which notes are pushed when new notes are added.

\* [M]: start empty loop and set length to multiple (x) of the loop quantization value
\* [S]: start/stop empty loop or arm existing loop
\** [S]: clear loop

\_ [S1]: show time frame per loop
\_ [S2]: show loop quantization


## install

from maiden type
`;install https://github.com/BeatRossmy/SuperBrain`

## links

- [view on llllllll](https://llllllll.co/t/superbrain-multi-engine-midi-sequencer)
- [view on github](https://github.com/BeatRossmy/SuperBrain)
{.links-list}

## demos

<iframe title="vimeo-player" src="https://player.vimeo.com/video/546873594" width="560" height="315" frameborder="0" allowfullscreen></iframe>