---
title: lamination
description: substitution sequencer
published: true
date: 2022-10-31T20:47:28.205Z
tags: synths, sequencers, crow, norns
editor: markdown
dateCreated: 2022-09-27T19:51:27.526Z
---

# lamination
a substitution sequencer

![lamination.png](/community/alanza/lamination.png)

![img_8692be086d4e-1.jpeg](/community/alanza/img_8692be086d4e-1.jpeg)

lamination is based on a certain kind of discrete dynamical system wherein letters in a finite alphabet are replaced with strings of letters in that alphabet. Pictured is one such dynamical system: here the “alphabet” is just the letters `a` and `b`, and the rules generating the dynamical system are `a -> b` and `b -> ba`. Repeatedly performing substitutions according to these rules starting with the string “`a`” yields (in this case) a string that grows exponentially and has certain self-similarity properties but never truly repeats itself. (Certainly substitution rules that don’t produce this behaviour are possible.)

lamination presents you with three dynamical systems that together control the PolyPerc engine (would be easy to change engines, and not too difficult to add other outputs), one each for note, octave and repeats. Tweak the rules to explore the space of possible dynamical systems!

lamination is named for a concept in the study of outer automorphisms of free groups (inspired by a similar concept for mapping classes of surface homeomorphisms), namely that of an attracting lamination. Dynamical systems similar to the one described above describe automorphisms of a free group, and in this situation, repeatedly applying the rules creates a string that converges to a “leaf” of an attracting lamination. lamination is perhaps ill-named because it is possible to produce sequences that don’t fit the model of an attracting lamination, but it seems more interesting as a script for this failing.

NB – lamination in many situations will eventually crash when it attempts to create a longer string than Lua allows you to. Fortunately it should take a while for this to happen.

## Requirements

norns, grid (optional)

## Documentation

`E1` scrolls the current page.
`E2` scrolls in current page, and E3 edits when applicable
`K2` on size resets
`K3` on rule opens it for editing

## Install

`;install https://github.com/ryleelyman/lamination`

v0.1