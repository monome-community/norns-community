## glaciers
Extreme sound stretcher and harmoniser.

https://vimeo.com/551661371
*(Demo uses four samples kindly provided by @tehn in the norns default image under `dust/audio/tehn` - whirl1, whirl2, mancini1 and mancini2)*

## Features
* Stretch audio samples to the extreme, until they are almost frozen in time
* Four separate audio buffers that can be manipulated
* Add multi-octave harmonisation
* Create movement and space with panning LFO
* Based on Paulstretch algorithm

This is my attempt to bring Paulstretch to the Norns platform. I’ve added multiple voices, harmonisation, and panning LFOs to help create multi layered dynamic textures.

This wouldn’t be possible without the amazing work of others.

Particular thanks to:

* @justmat for [otis](https://llllllll.co/t/otis/22149) and [pools](https://llllllll.co/t/pools/28320)
* @cfd90 for [twine](https://llllllll.co/t/twine-random-granulator/)
* @dan_derks for [cheat codes 2](https://llllllll.co/t/cheat-codes-2-rev-210315-small-fix/38414) and for making my first experience with monome super awesome
* [paulnasca](https://github.com/paulnasca/) for Paulstretch
* [jpdrecourt](https://sccode.org/jpdrecourt)  for the [supercollider port of paulstretch](https://sccode.org/1-5d6)
* @tehn @zebra and everyone else in the community for norns and all the knowledge, advice, and creativity that is shared on lines.

## Documentation

### navigation
**K1** (hold down) bring up the buffer (contextual) menu
**k2** (press) previous page/buffer action
**k3** (press) next page/buffer action

**e1** change voice
**e2** select parameter
**e3** change parameter value

### buffer - stopped state

![buffer1.png](https://raw.githubusercontent.com/dwtong/glaciers/main/assets/buffer1.png)

**k2** load a file from the norns audio directory
**k3** immediately start recording live input

### buffer - playing state

![buffer2.png](https://raw.githubusercontent.com/dwtong/glaciers/main/assets/buffer2.png)

**k2** clear buffer. stops currently playing file
**k3** immediately start recording live input

### buffer - recording state

![buffer3.png](https://raw.githubusercontent.com/dwtong/glaciers/main/assets/buffer3.png)

**k2** clear buffer. current recording will not be saved
**k3** save recording. new recording will then be stretched.

*recording is saved in glaciers audio directory.*
*when recording, buffer screen will stay open without having to hold k1.*

### sound

![sound.png](https://raw.githubusercontent.com/dwtong/glaciers/main/assets/sound.png)

*general sound parameters*

**volume** sets the level for the voice.
**stretch** is based on the playback rate. 1x stretch is 1x playback rate.
**harmonic oct** sets the octive for the harmonics. 1 will be one octave above.
**harmonic mix** controls how much of the harmonics vs original sound plays. 0 is all original, 1 is all harmonics.


### pan

![pan.png](https://raw.githubusercontent.com/dwtong/glaciers/main/assets/pan.png)

*move the sound through the stereo field*

**position** sets where the sound is in the stereo field.
**lfo spread** sets how far the sound will be moved by the lfo.
**lfo rate** controls how long it takes the pan lfo to complete a cycle.

### filter

![filter.png](https://raw.githubusercontent.com/dwtong/glaciers/main/assets/filter.png)

*a basic bandpass filter*

**freq** sets the centre frequency.
**width** sets the width of the filter from the centre freq, in octaves.

### global parameters
**gain offset** - offset the gain of all voices by up to +/-12db.

## Requirements
Norns

## Download
Install through the community catalogue on Maiden (don’t forget to refresh).
Be sure to restart to make sure Glacial Engine is loaded.

https://github.com/dwtong/glaciers
https://llllllll.co/t/glaciers/45117
