---
title: quence
description: A probabilistic 4-track sequencer for MIDI, Molly the Poly, and Crow
published: true
date: 2021-10-14T21:09:10.165Z
tags: midi, sequencers, crow, grid, generative
editor: markdown
dateCreated: 2021-10-14T01:27:03.396Z
---


`q*u*e*n*c*e`

## background
* Inspired by Turing Machine, Fugue Machine, and Physical (Norns Study 4)
* This sequencer was originally written in November of 2018, but had not been updated for Norns 2.0 compatibility
* [ground_state](https://llllllll.co/u/ground_state/summary) updated it to 2.0 in early 2020 and added audio output via Molly the Poly -> I'm Super grateful to this community member for updating the script, adding some new features and cleaning up my bad code
* [justmat](https://llllllll.co/u/Justmat/summary) also added the ability to output to Crow (Just Friends and CV) and helped us implement some new features
<br/>

## requirements

Grid, MIDI Interface required to output MIDI (optional), Crow (optional)
<br/>

## features

* Global tempo, tonic and scale
* There are 4 independent tracks of 1-16 steps
* Each MIDI track is sent to the channel equal to the track number
* Each track has a tempo modifier (1 is global bpm, 8 is global bpm divided by 8)
* Each track has a dispersion parameter (1 is a tight dispersion of notes, 10 is a very high dispersion of notes)
* Each track has a randomization parameter (1 is locked sequence, 8 is completely random)
* Each track has a rest frequency parameter (1 is no rests, 8 is no notes)
* Each track can be muted
* Each track can be copied and pasted into another track
* Each track can be transposed up or down a scale degree
* Each track can be shifted forward or backward one step
* Each track can be inverted or reversed
* All tracks can be locked or cleared simultaneously
* Tracks can be re-synced if tempo modification un-syncs them
<br/>

## documentation

* There are 5 pages in total, a settings page and 4 track pages
* After launching the script, the track page for Track One will be visible and the sequencer will be paused
* The bottom row is always the toolbar: pause, mutes for tracks 1-4, lock all, clear all, select tracks 1-4, and settings page
* The LED in the bottom right corner toggles between the current track page and the settings page
* The LED in the bottom left corner toggles the sequencer pause
* On the settings page, the eight buttons in rows 5-6, cols 13-16 are currently unassigned
* For now, pressing any of these LEDs will re-sync all sequences
* Hold Key 3 on the Norns to see the midi notes in the sequence for the current track
<br/>
![settings_page.png](/community/spunoza/settings_page.png)
<br/>
![track_page.png](/community/spunoza/track_page.png)
<br/>

## links

- [view on llllllll](https://llllllll.co/t/quence/29436)
- [view on github](https://github.com/millxing/QUENCE)
{.links-list}

<br/>

## demos

<iframe width="560" height="315" src="https://www.youtube.com/embed/w7hcWn9swu4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/ogu7FdoMybw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
