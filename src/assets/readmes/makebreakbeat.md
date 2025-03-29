# makebreakbeat

make break beats.

![img](https://user-images.githubusercontent.com/6550035/156637615-a0363244-2186-4604-b75f-4c1936982e24.png)

this script is a wrapper for [another script I wrote](https://github.com/schollz/dnb.lua/) that generates breakbeats from a drum sample. I made this to learn more about [sox](http://sox.sourceforge.net/) and [aubio](https://aubio.org/) as all the audio is generated with those tools.

# Requirements

- norns

# Documentation

- press K2 to generate beat
- press K3 to toggle playing
- use any E to change sample

to "break" a beat, this script first determines the tempo of the input file. it then determines onsets based on the tempo (minimum distance being sixteenth notes) and splits the input file into slices by onset markers. it then takes each slice and manipulates the slice with effects with some probability. the manipulated slice is then appended to an audio file at a position quantized to the desired tempo (set by norns clock). all the effect probabilities are available to modify in the parameters.

- [deviation](https://github.com/schollz/makebreakbeat/blob/a81972cd0b642a5efa309b46867e8bc090bb4957/lib/dnb.lua#L546-L548): probability of deviating from base pattern (0-100%)
- [reverse](https://github.com/schollz/makebreakbeat/blob/a81972cd0b642a5efa309b46867e8bc090bb4957/lib/dnb.lua#L611): probability of reversing (0-100%)
- [stutter](https://github.com/schollz/makebreakbeat/blob/a81972cd0b642a5efa309b46867e8bc090bb4957/lib/dnb.lua#L292-L330): probability of stutter (with random volume/pitch ramps) (0-100%)
- [pitch](https://github.com/schollz/makebreakbeat/blob/a81972cd0b642a5efa309b46867e8bc090bb4957/lib/dnb.lua#L595): probability of pitch up (0-100%)
- [trunc](https://github.com/schollz/makebreakbeat/blob/a81972cd0b642a5efa309b46867e8bc090bb4957/lib/dnb.lua#L333-L346): probability of truncation (0-100%)
- [half](https://github.com/schollz/makebreakbeat/blob/a81972cd0b642a5efa309b46867e8bc090bb4957/lib/dnb.lua#L603): probability of slow down (0-100%)
- [reverb](https://github.com/schollz/makebreakbeat/blob/a81972cd0b642a5efa309b46867e8bc090bb4957/lib/dnb.lua#L655): probability of adding reverb tail to kick/snare (0-100%)
- [stretch](https://github.com/schollz/makebreakbeat/blob/a81972cd0b642a5efa309b46867e8bc090bb4957/lib/dnb.lua#L281-L290): probability of stretching audio (0-100%)
- [kick](https://github.com/schollz/makebreakbeat/blob/a81972cd0b642a5efa309b46867e8bc090bb4957/lib/dnb.lua#L577): probability of snapping a kick to down beat (0-100%)
- [snare](https://github.com/schollz/makebreakbeat/blob/a81972cd0b642a5efa309b46867e8bc090bb4957/lib/dnb.lua#L586): probability of snapping a snare to down beat (0-100%)
- kick db:  volume of added kick in dB (-96-0 dB)
- snare db:  volume of added snare in dB (-96-0 dB))

all the resulting audio files are automatically put into the `~/dust/audio/makebreakbeat` folder.

## notes

this script generates beats *slowly*. to get around this I suggest generating short beats (8-16 beats) continuously (beats continue to play when generating).

# Install

install with

```
;install https://github.com/schollz/makebreakbeat
```

once you start the script for the first time it will install `aubio` and `sox` (~5 MB total).
