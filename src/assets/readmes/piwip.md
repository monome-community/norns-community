## piwip

a sampler that works in realtime.

![screenshot](.github/piwip.gif)

my goal here was to make a sampler that plays back samples of an instrument while playing an instrument. that way, i can have a "autotune" for my bad trumpet playing - e.g. turning off the monitor and sequencing with the notes i'm trying to play. 

future directions:

- add crow support
- fix bugs

### Requirements

- midi input (optional)
- audio input
- norns

### Documentation

- K2 arms recording
- K3 forces recording
- K1+K2 toggles monitor
- E1 activates presets
- E2/E3 trims sample


**quick start:** 

- *sampling*: plug in midi keyboard and audio source. turn E1 to "sampler". press K2 to arm or K3 to directly record. then play audio. now you can play it back on your midi source.
- *random harmony*: turn E1 to "follower". change `harmonizer -> probability` to `100%`. change the scale and root note to your preference. then press K2 to arm and play a sound through the input.


there are a number of customizable parameters in the global menu. currently there are two presets (E1 toggles):

- "sampler": generic sampler. record once and then midi notes are shifted by a constant amount (relative to middle c).
- "follower": sample in realtime. playing midi during recording will try to play notes near the leading edge, using a realtime pitch-detector to correctly pitch shift.

i'm sure there are other interesting combos. here is a quick rundown of some parameters:

- `recording->rec thresh`: lower to more easily trigger recording when armed
- `recording->silence to stop`: recording after armed stops after this much silence
- `playback->min recorded`: is the amount recorded before note playback is possible
- `playback->playback reference`: determines how pitch adjustment works
- `playback->live follow`: starts notes behind the latest sample
- `playback->keep armed`: re-arms recording if recorded stops
- `playback->only play during rec`: sequenced notes only emit during recording
- `playback->midi during rec`: use to disable midi during recording
- `playback->notes start at 0`: start notes at 0 or from where they last were


## demo 

<p align="center"><a href="https://www.instagram.com/p/CFla2iJh9zC/"><img src="https://user-images.githubusercontent.com/6550035/94328978-fed24c80-ff6b-11ea-8a8f-3b2c6f5c9e91.png" alt="Demo of playing" width=80%></a></p>

## my other norns scripts

- [barcode](https://github.com/schollz/barcode): replays a buffer six times, at different levels & pans & rates & positions, modulated by lfos on every parameter.
- [blndr](https://github.com/schollz/blndr): a quantized delay with time morphing
- [clcks](https://github.com/schollz/clcks): a tempo-locked repeater
- [oooooo](https://github.com/schollz/oooooo): digital tape loops

## license 

mit 


