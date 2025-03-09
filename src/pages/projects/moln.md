---
layout: project
title: moln
permalink: /moln
cover: moln.png
raw_name: moln
sanitized_name: moln
project_url: https://github.com/antonhornquist/moln
description: polyphonic subtractive synthesizer
discussion_url: https://llllllll.co/t/moln/21111
documentation_url: 
tags:
 - synth
authors:
 - jah
redirect_from:
 - /en/authors/jah/moln
 - /authors/jah/moln
---
# Moln

Polyphonic subtractive synthesizer

## Features

- 2 square oscillators per voice with variable pulse width and pulse width modulation.
- Resonant lowpass filter
- ADSR envelope

## Operation

![screenshot](https://raw.githubusercontent.com/antonhornquist/moln/HEAD/screen.png)

- `ENC1` adjusts main output level.
- `ENC2` changes filter cutoff.
- `ENC3` changes filter resonance.
- `KEY2` momentary toggles fine parameter control.
- `KEY3` triggers a random note.
- `MIDI` device plays notes.
- `GRID` plays notes too.
- `ARC` changes filter cutoff (`ENC1`) and filter resonance (`ENC2`).

## Options

Parameters are available in the global parameters list:

- `Osc A Range` - -2..+2. Octave range.
- `Osc A Pulse Width` - 0..100%.
- `Osc B Range` - -2..+2. Octave range.
- `Osc B Pulse Width` - 0..100%.
- `Osc Detune` - 0...100%. Detunes the two oscillators.
- `PWM Rate` - 0..50Hz. Pulse Width Modulation rate.
- `PWM Depth` - 0...100%. Pulse Width Modulation depth.
- `Filter Frequency` - 10Hz...8kHz. Lowpass filter cutoff frequency.
- `Filter Resonance` - 0...100%. Lowpass filter cutoff resonance.
- `Env > Filter Frequency` - -100%...100%. Lowpass filter envelope modulation.
- `Env Attack` - ADSR envelope attack time.
- `Env Decay` - ADSR envelope decay time.
- `Env Sustain` - 0...100%. ADSR envelope sustain level.
- `Env Release` - ADSR envelope release time.

