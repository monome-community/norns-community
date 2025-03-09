# delar

*always looping*

*sample player*

*delar == parts*

This script will slice any sample into 128 slices and loop all activated slices sequentially. A way of freeing yourself and your samples from typical sequencer timing.

[![Demo](https://img.youtube.com/vi/f790xR9Q2Q8/hqdefault.jpg)](https://www.youtube.com/embed/f790xR9Q2Q8)

## Requirements

norns
grid (optional)


## Documentation

### Loading Samples:

Load your sample from the params menu. Make sure that your sample is long enough. The engine won’t play if your sample is too short because a short sample / 128 slices can potentially cause performance issues.

### Navigating and Activating Slices:

Use `E3` to select a slice.
Press `K3` to activate the selected slice.

### Playback Control:

Press `K2` to start or stop playback.

### Adjusting Slice Values:

Use `E1` to navigate to the second page.
Use `E2` to select a value and `E3` to adjust it for the selected slice.
Pressing `K3` resets all values for the current slice to their defaults.

### Global Offset Value:

Navigate to the third page using `E1`.
Set a global offset value for all slices.
The value ranges from -100 to 100, with 0 indicating no offset.
Pressing `K3` resets all offset values to 0.

### Rotating Slice Values:

On the first page, use `E2` to rotate all slice values to the neighbouring slice in the encoder's direction.

### Auto-Rotation:

Hold `K1` and press `K2` on the first page to initiate auto-rotation.
Auto-rotation speed is controlled by the `CLOCK`.

### Pattern Change:

Hold `K1` and turn `E3` on the first page to adjust the pattern.

### Values

`atk`: Attack phase

`len`: Length

`lvl`: Level

`rate`: Playback rate in octaves

`rFreq`: Speed of random panning

`rStart`: Amount of random start position

`rEnd`: Sets if rStart also should set a random end position (true = always, false = never, numbers = probability to be true)

`rPan`: Amount of random panning

`rel`: Release phase

`loop`: Preserve slice length when rate changes (true = always, false = never, numbers = probability)

## Download

install via maiden:

`;install https://github.com/filipforsstrom/delar`

or download via GitHub:
https://github.com/filipforsstrom/delar

## Thanks

[graymazes](https://llllllll.co/u/graymazes/summary) for initial design of the engine.
