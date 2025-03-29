---
title: oomph
description: put a little oomph into it.
published: true
date: 2022-06-10T13:19:59.758Z
tags: synths, sequencers, grid, drums
editor: markdown
dateCreated: 2022-06-10T13:19:55.740Z
---

# oomph

![oomph.png](/community/infinitedigits/oomph.png)


https://vimeo.com/718961010

oomph is sequencer with multiple built-in synth and sample voices. 

this script combines some previously contributed projects with additions. it currently encompasses:

- a monophonic synthesizer w/ 16-step sequencer (from [acid-test](https://github.com/schollz/acid-test) w/ better accenting dynamics)
- a sample loop player with customizable effects (from [amen](https://github.com/schollz/amen))
- a sample-based chord sequencer (from [synthy](https://github.com/schollz/synthy) and the unreleased [mx.samples2](https://github.com/schollz/mx.samples2))
- a [plaits module](https://mutable-instruments.net/modules/plaits/) (from [mi-ugens](https://github.com/v7b1/mi-UGens))
- a tape emulator (from [portedplugins]()/[tapedeck](https://github.com/schollz/tapedeck))

following guidance from @sixolet I worked out a way to make almost every parameter modulateable through internal ramps/lfos.

## Requirements

- norns
- midi controller (optional)
- grid (optional)

## Documentation

most of the usage can be found in the parameters - you can directly edit parameters or use a midi controller to map devices for easy manipulation. there are also LFOs for nearly every parameter accessible through the "MOD" menus. 

## monophonic synth 

the main screen allows you to sequence the monophonic synth. the sequencer ui is based off the [TB-303 pattern chart](https://www.peff.com/synthesizers/) ([pdf](https://www.peff.com/synthesizers/roland/tb303/Tb303Chart2.pdf)).

- K2 changes a parameter
- K3 stops/starts 
- E1 changes pattern
- E2/E3 navigate the individual parameters

the parameters are set out in columns, where each column is one of the sixteen steps of the sequence. 

the first row is the note in the C major scale (this scale is transposed in parameters but still displays as the C major scale.

the second row allows you to modify the accidentals of each note (b = flat, and # = sharp).

the third row allows you to change the octave of each note - M for minus octave (-1) and P for plus octave (+1).

the fourth row allows you to add an accent or slide. "O" does an accent (i.e. provides **O**mph) and "F" provides a slide (i.e. the note **F**loats...).

the fifth row can change the articulation of the sequence. the "@" denotes a gate, the "o" is a rest" and a "-" after a gate provides a legato. the actual strength of a legato is controlled in teh parameters by the "sustain" parameter.

### audio input

audio input is re-routed through norns into the tape emulator. because of this, instead of using the "MONITOR" control in the audio mixer, you should instead use the "INPUT LEVEL" control in the parameters menu.

### sample looper

the sample looper attempts to sync to the tempo by changing playback speed and resetting to the beginning at the beginning of the 16 step sequencer (can be controlled by a probability in the parametrs). the script tries to determine bpm from the filename if there is a "bpmX" in the name (i.e. `mysample-bpm120-1.wav` => 120 bpm). if there is no bpm available then the script figures out the bpm by a "best guess" approach by assuming that the loop is quantized to the nearest beat and checking to see which bpm allocates the most even number of beats. 


there are some hard coded triggerable effects in the parameters menu and its possible to add your own since every parameter in the sample looper can be modulated using a variety of functions (sine, ramps, etc) - all you do is make a function that you want toggled ([like this](https://github.com/schollz/oomph/blob/main/lib/Amen.lua#L194-L196)) and then add the name of that function [to this array](https://github.com/schollz/oomph/blob/main/lib/Amen.lua#L34).

if you need a script to create quantized loops - checkout [amen](https://llllllll.co/t/amen).

### grid

grid is simply an alternative interface for the main norns screen - it is totally optional.

the first five rows edit the parameters of the monophonic synth. the sixth row can be used to change patterns. the sixth row also allows chaining patterns by holding down one pattern key and pressing another *while playing*. the sixth row also allows copying patterns by holding down one pattern key and pressing another *while not playing*.


## todos

- lfos: make more chaotic
- midi: give tracks midi out
- midi: allow midi in (for plaits)
- rpi3: possible cpu spikes?
- grid: light-up special parameters
- grid: recall patterns on double tap
- grid: clear sequenced patterns
- sound: distortion fx

## known bugs

- (cosmetic bug) if you goto a "MOD" and toggle one, and you go to the non-MOD page and change the parameter it will automatically turn off the toggle *but the toggle won't appeared to be turned off in the menu* until you exit the menu and come back into the menu.
- (ux bug) MOD lfos are set according to the current tempo, if you change tempos the MOD lfos will stay with periods from the previous tempo
- (ux bug) the sample looper may not work fully with mono sound files, try to use stereo files


## install

*oomph* will need 100mb of disk space (95 mb for wav files and 5 mb for SuperCollider files).

there are three steps to install.

**first** open maiden and run the following:

```
;install https://github.com/schollz/oomph
```

**secondly**, keep maiden open and run the following line to make sure everything is copasetic:

```lua
dofile("/home/we/dust/code/oomph/lib/update.lua")
```

**thirdly**, you need to restart your norns. now you can run `oomph` without issues.

## update

to update the script just run the following in maiden:

```lua
dofile("/home/we/dust/code/oomph/lib/update.lua")
```
