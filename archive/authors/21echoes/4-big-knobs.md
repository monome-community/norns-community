---
title: 4 Big Knobs
description: simple controls for crow's outputs
published: true
date: 2021-04-09T16:37:43.145Z
tags: crow, arc, utilities, midi
editor: markdown
dateCreated: 2021-03-22T17:19:27.185Z
---

Simple tool for sending control voltages out of a Crow connected to Norns. Intended for use with Arc, where each Arc encoder controls the voltage sent from the corresponding Crow output. Works without Arc, too! Also has a Quantized mode and a Snapshot mode for interpolating between two different states

## UI
![4-big-knobs.png](/community/21echoes/4-big-knobs.png)
* 4 dials showing current voltage values
* Ships with helper text on by default, showing what each encoder and button does. Turn off in params menu, once you know how it works!

## Controls
### Arc (optional)
* Each encoder is mapped to the corresponding dial on screen

### Norns
* E1 changes which dials are focused
* E2 & E3 are mapped to the highlighted dials on screen

### Snapshot mode
* Switch modes via Params menu. Defaults to Snapshot mode if launched with an Arc connected
* K2 & K3 save current state to one of two snapshot banks
* E1 interpolates between the two snapshots
* If you change a dial while interpolating, an intermediary snapshot is taken.
  * Now as you turn E1, you are interpolating between 3 snapshots: snapshot 1 at the leftmost extreme, snapshot 2 at the rightmost extreme, and your intermediary snapshot in between them (located wherever the interpolation was when you changed the dial)
  * The intermediary snapshot is reset whenever you take a new real snapshot

### Quantize mode
* Switch modes via Params menu
* E2 & E3 select scale root and scale type
* K2: Toggle between continuous quantization and on-demand quantization
* K3: Quantize now!
* Set slew timing for quantization in the Params > Quantization menu

### Additional Parameters (in Params menu)
* Crow Outputs
  * Minimum and Maximum voltage per output
  * Slew time per output
  * Customize dial -> Crow output mapping
  * Direct control over dial values (can be used for MIDI mapping if you'd like a different control surface)
* Crow Inputs
  * Each Crow input can exert influence over all the Crow outputs via Attenuation or Offset (or None)
  * Defaults to None
* MIDI Out
  * Each dial can send MIDI out, either as CCs or Notes
  * Customize which MIDI device and channel is used
  * Customize which CC# is sent, along with minimum and maximum CC values
* Misc
  * If you have a Norns shield, you can switch top left and right text to match where your E1 is
  * You can turn off the helper text once you understand how it works

## Requirements
* norns (200712 or later)
* crow (2.0.0 or later)
* arc optional, but encouraged
  * use a MIDI device for input in place of an arc by going into the params menu, clicking “map”, scrolling to “crow outputs”, scroll to “1_volt” and the other 4 options, and map each of them to a different control on the MIDI device

## Roadmap
### Quantization mode improvements
* More scales (whole volts, 10TET, more?)}

## Download
Latest version: v1.0.0 (2c4267c)
Available in the Maiden Library

Or, install via the Maiden command line: visiting http://norns.local/maiden when your norns is on WiFi and type
```
;install https://github.com/21echoes/4-big-knobs.git
```
into the command entry box at the bottom of the screen.

Also available as a [direct download](https://github.com/21echoes/4-big-knobs/archive/main.zip). Unzip it, rename the folder to just “4-big-knobs”, and put the whole folder onto your norns inside the `/home/we/dust/code` folder

github: https://github.com/21echoes/4-big-knobs

## discussion
For feature requests and bug reports, discuss [over on lines](https://llllllll.co/t/42190)