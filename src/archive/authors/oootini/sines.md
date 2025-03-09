---
title: sines
description: A simple FM sine drone synth with 16 independant sine waves
published: true
date: 2021-12-13T18:20:19.179Z
tags: synths, midi, 16n
editor: markdown
dateCreated: 2021-08-26T06:57:13.219Z
---

# Sines

16 sines waves. each sine wave is FM modulated with configurable carrier - modulator FM index. Sample rate and bit depth can be changed for each voice.

![sines](https://github.com/aidanreilly/sines/raw/main/sines.png)

This is very much a personal learning exercise in how to develop for norns. I cobbled together bits and pieces from here and there. Inspired by everyone and everything on this forum, and beyond that, by the music of La Monte Young, Pauline Oliveros, Eliane Radigue, and Mika Vainio. There is no sequencer, no filters. It’s just simple waves playing and beating off each other.

## Installation

Ensure you are up to date with the latest norns OS. Visit http://norns.local/ in a browser, and install sines from the maiden project manager.

Then, `SYSTEM => RESET` on norns to pick up the new SuperCollider engine. Reboot for good measure.

## Play

Select a root note and scale from the norns parameters menu. 16 frequencies based on the selected scale are applied. You can also tune the sine waves by hand on norns. 

Controls:

* [E1] master volume
* [E2] select sine 1-16
* [E3] set sine amplitude
* [K1] exit to norns main menu
* [K2] + [E2] change note
* [K2] + [E3] detune
* [K3] + [E2] change envelope
* [K3] + [E3] change FM index
* [K1] + [E2] - change sample rate
* [K1] + [E3] - change bit depth
* [K2] + [K3] toggle voice pannning between 'middle' and odd numbered voices hard left, even numbered voices hard right. 

Saving a pset saves the note selection and midi mapping. The last saved pset is loaded when the app launches.

### Optional

Control individual sine amplitudes, envelopes, bit depth, sample rate, and FM index with a midi controller. Controls are mapped from the norns parameters page.

### squares, triangles, bandpass noise

You can install 3 variants of the app by pasting the below into Maiden. You will need to remap all controls for each variant. Instead of FM, Squares has a pulsewidth and filter control, Saws has a filter control. Bp_noise has a filter q control. Otherwise broadly similiar to Sines.

`;install https://github.com/aidanreilly/saws`

`;install https://github.com/aidanreilly/squares`

`;install https://github.com/aidanreilly/bp_noise`

### discuss

https://llllllll.co/t/sines/