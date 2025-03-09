---
layout: project
title: zellen
permalink: /zellen
cover: zellen.png
raw_name: zellen
sanitized_name: zellen
project_url: https://github.com/sarweiler/zellen
description: game of life based sequencer
discussion_url: https://llllllll.co/t/zellen/21107
documentation_url: 
tags:
 - sequencer
 - grid
authors:
 - sbaio
redirect_from:
 - /en/authors/sbaio/zellen
 - /authors/sbaio/zellen
---
Zellen is currently not in active development, since I do not own a Norns anymore. If anyone wants to take over, feel free to fork the repository and create a new thread for it in the [lines library](https://llllllll.co/c/library/18). If you do so, send me a message on lines and I will happily link your new repository here and in the old [lines thread](https://llllllll.co/t/zellen/21107).


# zellen

A sequencer for Monome norns based on [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

## Usage

* Grid: enter/modify cell pattern
* KEY2: play/pause current generation (semi-manual mode), advance sequence (manual mode), play/pause sequence (automatic mode)
* KEY3: advance generation
* hold KEY1 and press KEY3: erase the board
* ENC1: set speed (bpm)
* ENC2: set play mode (see below)
* ENC3: set play direction (see below)
* hold KEY3 + ENC3: time jog

### Play Modes

Set the play mode with ENC2.
* reborn (default): Play a note for every cell that was born or reborn (= has exactly three neighbors), regardless of the previous state of the cell
* born: Play a note for every cell that was born (has exactly three neighbors and was not alive in the previous generation)
* ghost: Play a note for every cell that is dying(has less than two or more than three neighbors). Ghost notes can have a different pitch! (See the "ghost offset" setting in the parameters screen.)

### Play Direction

Set the play direction with ENC3.
* up: Cells on grid are played from top left (lowest note) to bottom right (highest note).
* down: Cells on grid are played from bottom right (highest note) to top left (lowest note).
* random: Cells are played in random order. The randomized order will be stable for a generation and will be re-randomized for every new generation.
* drunken up: Like up, but decides for each step randomly if it goes up or down.
* drunken down: Like down, but decides for each step randomly if it goes up or down.

### Sequencing modes
Set the sequencing mode in the parameters screen. Default is semi-automatic.
* manual: Press KEY2 to play the next step in the sequence for a single generation.
* semi-automatic: Plays the sequence for a single generation (and loops it if "loop seq in semi-auto mode" is enabled (default)).
* automatic: Like semi-automatic, but automatically calculates the next generation and plays it.

## Crow support

Zellen supports CV out via [Crow](https://monome.org/docs/crow/). Crow CV output can be configured in Norns's parameters menu.

Crow configuration for Zellen:
* Input 1: Clock
* Input 2: CV offset
* Output 1: CV
* Output 2: Trigger
* Output 3: CV 2
* Output 4: Clock

CV offset (input 2) can be set to pre or post quantization in the parameters menu.

CV 2 is, just like the main sequence, a CV derived from the current play position on the board. The CV can be calculated with these methods (configurable in the parameters menu):
* x/y (default)
* x%y
* x+y (same as the main sequence)

## Just Friends support (via ii)

Zellen supports playing notes on [Mannequins Just Friends](https://www.whimsicalraps.com/products/just-friends) via Crow and a ii connection. The note value can be determined with the same methods as the CV 2 value for Crow (configurable in the parameters menu).

## MIDI
Set the MIDI channel (default: 1), MIDI velocity (default: 100), and MIDI clock in the parameters screen.

## More Parameters
There is lots more to discover in the parameters screen, like root note, scale, and ghost offset.
