---
title: seaflex
description: training app for earthsea
published: true
date: 2021-10-10T01:38:26.625Z
tags: grid, utilities
editor: markdown
dateCreated: 2021-10-10T01:04:53.694Z
---

[discussion thread](https://llllllll.co/t/seaflex/23209)

note: if you get errors when trying to load the script, you probably need to install "we" from maiden, which this app depends on.

practice tool for earthsea. learn to play chords on an earthsea-style grid layout. there is a gamified version built in where you can go for a high score based on speed and accuracy.

the app tries to be mostly self-documenting with instructions on the norns display. Options for scale, scale guides, voicing complexity, as well as two-handed vs one-handed play are available in the params page.

At any time you can toggle between light and dark modes. Chord shapes are displayed in light mode only. In light mode, to advance chords all the lit keys must be pressed. Whereas in dark mode any voicing of the chord or chords displayed on screen will be accepted, meaning if all the keys (and no others) belonging to those chords are pressed, anywhere on the keyboard (any octave), the chords will advance.

The norns encoders don’t do anything except modify a few parameters of the PolySub engine.

Some code has been copied over from the earthsea implementation shipped with norns 2.0.

If you’d like to add your own scales, chords, or voicings, it’s as simple as changing a few constants at the top of seaflex.lua

## requirements
norns
grid

## future development
i have no plans for future developments at the moment, but feel free to submit pull requests or report issues on the discussion thread.