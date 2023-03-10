---
title: Gridstep
description: polyphonic, isomorphic grid keyboard sample sequencer
published: true
date: 2021-08-11T13:46:19.615Z
tags: sequencers, grid, midi
editor: markdown
dateCreated: 2021-03-30T17:07:56.810Z
---

**gridstep** is a polyphonic, **isomorphic** grid keyboard sequencer for **monome norns** + **grid** using the **timber** engine. 

https://www.instagram.com/p/CH_JGvhh5JG/

![gridstep.png](/community/quixotic7/gridstep.png)

![gridstep-grid.png](/community/quixotic7/gridstep-grid.png)

## requirements

* **norns**
* **grid** - note input and sequencing
* **timber** - for internal sounds. install from maiden

## optional

* **external midi devices** - for getting more sounds than just Molly The Poly

## features

* The grid can be played in an isomorphic layout that is either chromatic or in-scale. 
* It can sequence up to 16 tracks. 
* 16 sounds can be loaded into the Timber engine. 
* Sequences are stored as grid positions rather than notes and can be recorded from the grid input or programmed in.
* Each track can send it's notes to the internal sound engine (Molly The Poly) or to any midi channel or device. 
* Each track can have up to 16 patterns that can be quickly changed individually or as scenes.
* Each pattern can have up to 16 bars and the length of a bar can be set between 1 step to 16 steps. By mixing up bar lengths, you can create interesting polyrhythms! 
* Each step can have trigger conditions to create dynamic patterns!
* Each step can have a different velocities and note lengths.
* Each step can be offset +- 12 substeps or 16 substeps if the pattern is in triplet mode.
* The entire project can be saved and projects can be loaded during playback.

## documentation

documentation for **gridstep** can be found [here](https://github.com/Quixotic7/gridstep/blob/master/doc/README.md).

<iframe width="560" height="315" src="https://www.youtube.com/embed/RaOxDwYcZiQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## download

in maiden or https://github.com/Quixotic7/gridstep

## installation

Use the community catalog in Maiden

Or use norns.fetch in Maiden

```lua
norns.fetch("https://github.com/Quixotic7/gridstep.git")
```

system > reset then launch gridstep



to update

```lua
os.execute("rm -rf ~/dust/code/gridstep")
norns.fetch("https://github.com/Quixotic7/gridstep.git")
```

## changelog

**1.3.3** - Added feature to send midi program change or note when changing the pattern for midi tracks. To configure, select a pattern from the pattern launch grid view, then find the pattern page on the norns screen. Set the "Launch Event" to "Disabled", "Prog Change", or "Send Note". The value can be between 0-127 and determines the note or prog change midi message that is sent. Midi Channel can also be set. The midi event will be sent whenever you press a key in the pattern launch grid view to select a new pattern. https://www.youtube.com/watch?v=DlUwQmZqUnM

**1.3.1** - Added Timber UI! Select sample by changing track. If track's sound source is set to kit, select the sample by pressing a grid key. Loading a folder of samples for a kit now sets all samples to one-shot unless "loop" is in the name of the sample. 

**1.2.4** - Experimental support added for loading kits. Go to kit page, select "load kit" using  K3, then select a sample, the entire folder will be loaded and the active track's sound source will change to kit. Use the new layout mode to map all the sounds across the grid. Samples can be adjusted in params menu, kit samples start at 16 and sample 16 maps to kit sample 1/C0, sample 17 kit sample 2/C#, etc...

**v1.2.3** - Added beat synced delay based on halfsecond from awake.

**v1.2.1** - Changed the sound engine to Timber. No UI yet, use the params menu to change sounds. There are 16 sound slots which are currently mapped to a track's midi channel parameter. 

**v1.1.1** - Bug fix to prevent too many of the same note from triggering at once which can crash Molly The Poly

**v1.1.0** - Added support for 64 / 8x8 grids. 

- works mostly the same as for 128 grids. 
- in 64 grid mode, keys 7 and 8 on the toolbar(y = 8) can be used to select steps 1-8 or steps 9-16 for editing. 
- use key 3 to round robin through the grid pages: play, pattern launch, sequence. 
- cut, copy, and paste have been moved to keys 4,5,6
- in grid play and grid sequence keys 7 and 8 on row 7 can be used to scroll up and down
- in grid pattern launch mode use shift + 5 and 6 to scroll the pattern view up and down. 
- All the shortcuts for the 128 mode are unchanged. 

**v1.0.1** - fixed bug that could occur when changing the number of bars in a pattern.

**v1.0.1** - initial release

- [view on llllllll](https://llllllll.co/t/38559)
- [view on github](https://github.com/Quixotic7/gridstep)
{.links-list}