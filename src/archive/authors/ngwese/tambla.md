---
title: tambla
description: semi-generative rhythmic arpeggiator with bendable playheads
published: true
date: 2021-10-07T03:50:28.111Z
tags: sequencers, grid, arc, midi
editor: markdown
dateCreated: 2021-04-02T01:25:26.719Z
---

# tambla

![](/community/ngwese/tambla.png)

[tambla](https://github.com/ngwese/tambla) is a semi-generative rhythmic arpeggiator with bendable playheads

## documentation

complete and up to date documentation lives [here](https://github.com/ngwese/tambla-docs/blob/main/README.md)

## overview

_tambla_ affords exploration of polyrhythms and syncopation. patterns consist of four
rows. rows have 2-16 triggers with velocity, duration, and chance values per
step. holding down a key generates notes at the given pitch
with the trigger pattern in the first (top most) row. each subsequent key held,
begins generation based on the trigger pattern in next lower row. note generation
starts from the current playhead position instead of the beginning of the row
ensuring the overall rhythmic structure is maintained unless note based sync it chosen.

the four playheads scanning each row are synchronized to a common clock.
individual rows can divide down the clock for linear phasing effects or bending the
clock or both. bend values < 1.0 result in the playhead progressing in a
logarithmic fashion (fast then slowing down) where as bend values > 1.0 result
in exponential progression (slow then speeding up).

## installation

_tambla_ can be intalled with any of the following methods

- via the project manager in [`maiden`](http://norns.local/maiden)
- by entering `;install https://github.com/ngwese/tambla` in the `maiden` repl
