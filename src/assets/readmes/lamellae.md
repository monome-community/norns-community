# Lamellae
![A screenshot of the script in norns](./doc/cover.png)

A music box inspired generative instrument for Norns.
Create randomised patterns of controllable length and note density, which can be played by turning an encoder, in the spirit of hand wound music boxes. Alternatively let the pattern automatically play at a set rate.

### Requirements
- Norns
- Midi out (optional)

### Install

In Maiden via the project manager,

Or via the REPL with
```
;install https://github.com/Not-A-Creative/lamellae
```

### Controls

- KEY2: Start/Stop automatic playing
- KEY3: Regenerate the pattern
- ENC2: Play Speed
- ENC3: Turn Clockwise to play

Other functions controllable from the params menu:

- Scale quantisation and length
- Total length of the pattern (in screen widths)
- Number of events in the pattern
- Engine controls (PolyPerc)
- Midi Out options

### Interface

The screen displays a number of rectangles to the left, representing the 'lamella' or 'tongues' of a music box. Each corresponds to an individual note in the assigned scale. The number of which can be changed from the params menu.

The bulk of the screen is taken up with the pattern of notes, each triggering the engine when passing a tongue. Movement of the pattern from left to right is controlled by turning ENC3 or can be set running at a constant rate with KEY2.

The pattern loops back to the starting point at the tongues after reaching a specified distance, measured in widths of the display area (which can be changed in the params menu).

The pattern is generated completely randomly, with a total number of events that can again be set in the params. NOTE: There is not protection against multiple events holding the same coordinates. This is intentional for code simplicity and as it adds some extra variation in the way patterns may generate and individual note volume.

The pattern is regenerated if any of the key or pattern params are altered.

### Engine

The script uses Poly Perc with the associated engine options accessable in the params. The engine can also be turned off, if needed from the params.

By default the settings are; Amp = 0.8, Cutoff = 800 Hz, Pan = 0, Pulse Width = 0.5, Release = 1.5 s

Other engines may be used, but would require editing of the params setup.
