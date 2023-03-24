---
title: norniths
description: 
published: true
date: 2021-09-29T16:01:53.835Z
tags: sequencers, generative
editor: markdown
dateCreated: 2021-09-29T10:52:51.712Z
---

## description

This started as ‘I wonder what Crow’s First would sound like on Norns’, and then playing around with the ghosts.lua script from the p8 lib.

Hacked up conglomeration of code from:

Crow’s First script by @Galapagoose
Graphics from a tweetcart, adapted to Norns by @eigen
Uses the P8 library from @eigen
Engine is PolyPerc plus attack, plus some other code from awake from @tehn

## description

e1 - span
– hard stereo pan to mono

e2 - velocity
– clock bpm

e1 + e2 - divides steps for notes, but does not change the ‘screen clock’

e3 - diversity
– this is a simulation of input 2 for Crow, center (default) has little note diversity, the farther you travel away from center in each direction should yield more diversity
– the number of norniths increases/decreases with note diversity
– clockwise from center is one scale (black floating dots), counter clockwise is a different scale (grey floating dots)

k2 - clarity (each clarity setting has a unique animation)
– changes attack type:
—1 - percussive
—2 (default) - wavering between percussive and slight attack
—3 - long attack/smear

k3 - inspiration
–Crow pulls the ‘seed’ from the unique ID of the device, on Norns I used the current time in milliseconds as the seed. You can reseed at anytime with k3.
– reseeding changes both the notes and the rhythm

## known issues
been awhile since I've worked on this script and there have been some changes to the clock system in norns... seems like e2/bpm is not actually changing tempo. 

## install

from maiden type
`;install https://github.com/hypnogogue/norniths.git`

Then restart since it adds a new engine

## links

- [view on llllllll](https://llllllll.co/t/norniths-crows-first-for-norns/40856)
- [view on github](https://github.com/hypnogogue/norniths)
{.links-list}