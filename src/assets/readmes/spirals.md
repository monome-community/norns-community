
## spirals

A circular sequencer for monome norns

![image](https://github.com/user-attachments/assets/8b146764-113e-49c6-a13b-545855d16984)

Notes of the selected scale are spread around a circle. Points are drawn by rotating a set amount from the last point while moving outwards slightly and notes are triggered depending on where they land. Patterns repeat and change over time.

If you find any interesting patterns or have ideas of how this can be expanded then let me know!

### Requirements

norns
MIDI (optional)
mx.samples (optional)
grid (optional)

### Documentation

E1 change current spiral
K2 play / stop current spiral
K3 toggle options
  -> E2 change option
  -> E3 change value
K1 + K2 toggle lock sequence to the last X number of notes
K1 + K3 toggle scale overlay

### grid
spirals supports grid or midigrid to enable you to change current spiral, start/stop the current spiral and lock/unlock the current spiral.

![image](https://github.com/user-attachments/assets/8bc86ca6-5a88-4671-97ed-a351c1f291af)


on the bottom row the left 4 pads change the current spiral, the right most pad starts or stops the current spiral and one in from the right locks and unlocks the current spiral.

the top 6 rows fill up as notes play - the bottom right most lit pad is the most recent note. 

press two pads to lock the current spiral to loop between those notes.

https://youtu.be/5-2XTOoBuU0

### Changelog
20210206:
- Added options screen
- Added ability to lock the sequence to the last X number of notes
- Added ability to change root note with a midi input device
- Added ability to overlay the available notes
- When resetting the pattern, don't reset the angle to 0, continue from the last angle

20210208:
- Added chord mode for midi and audio output
- Minor bug fixes and display improvements

20210210:
- Added lfo for rotation parameter

20210217:
- Added support for multiple spirals! Currently 4 with just the first one playing by default. Some changes to buttons to allow play/stop. There's a good chance I broke something moving everything around so let me know if you find anything.

20210220:
- If you have mx.samples installed it can now be used as the audio engine. Change the audio engine parameter and then select an instrument for each spiral. Make sure mx.samples is up to date before using it. If you don't have it installed, restart after installing to ensure everything goes smoothly. Massive thanks to @infinitedigits for the library and help.

20210221:
- Added fractional step divisions (.5, .25, .125) for notes every other beat, 4 beats or 8 beats
- Added rests - set the number of rests and they are spread around the circle in a euclidean style
- Fixed midi note off

20210226:
- Added icons to show if currently spiral is playing or stopped and if it is locked

20210420:
- Don't enable mx.samples if there are no instruments available

20211003:
- Added grid support

### Download

https://github.com/tomwaters/spirals
