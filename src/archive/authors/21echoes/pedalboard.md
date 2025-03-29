---
title: pedalboard
description: a broad collection of chainable stereo effects
published: true
date: 2021-05-25T04:08:18.267Z
tags: audio fx, crow, arc
editor: markdown
dateCreated: 2021-03-02T19:02:12.894Z
---

![board.png](/community/21echoes/pedalboard.png)
![pedal.png](/community/21echoes/pedal.png)
![modmatrix.png](/community/21echoes/modmatrix.png)

## Pedals
* Delay
* Reverb
* Overdrive
* Chorus
* Tremolo
* Distortion
* Flanger
* Phaser
* Compressor
* Sustain
* Bitcrusher
* Wavefolder
* Ring Modulator
* Pitch-shifter
* Sub-boost
* Vibrato
* Auto-wah
* Lo-Fi
* Resonator, based on Mutable Instruments Rings
* Granular, based on Mutable Instruments Clouds
* Amp simulator
* Equalizer
* Tuner


## Documentation

### UI & Controls
* E1 always changes page

### Page 1: Board
* Left-to-right list of slots for pedals
* E2 changes focused slot
* E3 changes pedal in focused slot (including "no pedal")
* E3 doesn't take effect til K3 confirms
* Last slot is always "add new" (using K3 to confirm) (until you reach the max of 4 pedals)
* K2 jumps to pedal page
* K2 + E2 re-orders pedals
* K2 + E3 changes wet/dry for focused pedal
* K2 + K3 toggles bypass for focused pedal
* If you hold K2 while adding a pedal via K3 then the pedal will be bypassed by default

### Last Page: Mod Matrix
* First few sections are high-level controls for the Envelope Follower and 3 LFOs
* After that, there's a "mod matrix" section, where each modulator can control the active pedals' settings
  * Left 3 columns are the 3 LFOs, then the right-most column is the Envelope Follower
* E2 scrolls through the rows
* E3 changes the focused value
* K2 moves left, K3 moves right (when in the "mod matrix" section)

### Other Pages: the Pedals
* UI is custom per pedal, but typically shows a dial or two at a time, controlled by E2 & E3
* Each pedal has dials specific to its effect
* K2 cycles left thru dial pairs, moving left a section or looping at the left edge
* K3 cycles right thru dial pairs, moving right a section or looping at the right edge
* Every pedal has the following dials as its last 4:
  * Bypass
  * Wet/dry mix
  * In gain
  * Out gain
* On pedals with tap-tempo (Delay and Tremolo), hold K2 and tap K3 for tap tempo

### Arc (optional)
* Choose "Follow" or "Fixed" in the params menu, under "Arc". Defaults to "Follow"
* "Follow" mode
  * On The Board, each arc encoder controls wet/dry
  * On Pedal Pages, arc encoders 1, 2, and 3 change dial values and arc encoder 4 changes wet/dry
  * On the Mod Matrix page, arc encoders change what they control depending on which row you are on
    * In the LFOs and Envelope Follower "meta" sections, each encoder controls a different "meta" control
    * In the detailed Mod Matrix grid, the four encoders control the four columns of the focused row
* "Fixed" mode
  * Use the params page to choose which params are controlled by which arc encoder
  
### Crow (optional)
* Use the params page to choose which params are controlled by which crow input
* also has settings for minimum and maximum input voltage


## Roadmap
* Better Pedals!
  * Multi-tap and Varispeed delays
  * Spring and Plate reverbs
  * EQ shelves can be filters instead, and an additional peak EQ
  * Continued iteration on how the dials alter the effect
    * Covering musical ranges with multiple sweet spots, while also offering interesting extremes
* Clock-synced LFOs in the Mod Matrix
* Delay's BPM and Beat Division should be mod-matrix-able

## Requirements
* norns (200328 or later)
* Audio input (stereo, or mono via the left input and a parameter change in the menu)
* Reset after installs and updates (this is a new Engine)

## Acknowledgements
Thanks to @zebra, @carltesta, @mimetaur, and @jah for the SuperCollider help and inspiration. Double thanks to @mimetaur for [arcify](https://llllllll.co/t/arcify/22133). Thanks to @Justmat for [hnds](https://github.com/justmat/otis/blob/master/lib/hnds.lua). Thanks to @okyeron and @geplanteobsoleszenz (and, of course, the wonderful Émilie Gillet) for the Resonator and Granular pedals.

## Download
Latest version: v2.2.2 (0323837)
Install by visiting http://norns.local/maiden when your norns is on WiFi and typing
```
;install https://github.com/21echoes/pedalboard.git
```
into the command entry box at the bottom of the screen. If this is your first time installing Pedalboard, make sure to tell norns to sleep once the install has completed, then it should work after you boot it up again.

Also available as a [direct download](https://github.com/21echoes/pedalboard/archive/master.zip). Unzip it, rename the folder to just “pedalboard”, and put the whole folder onto your norns inside the `/home/we/dust/code` folder. As with the normal install process, if this is your first time installing Pedalboard, make sure to tell norns to sleep once the install has completed, then it should work after you boot it up again.

github: https://github.com/21echoes/pedalboard

## discussion
For feature requests and bug reports, discuss [over on lines](https://llllllll.co/t/31119)

