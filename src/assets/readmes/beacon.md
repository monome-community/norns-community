# beacon
***
beacon is a norns script for sample mangling by entering commands using a computer keyboard.

#### Requirements
- [x] norns
- [x] a USB computer keyboard
- [x] some samples


## Quick Start
*(AKA just tell me how to make some noise)*

Make sure your keyboard is connected to your norns and start the script

Enter the following pressing enter at the end of each line

```
load audio/tehn/whirl1.aif 1
voice 1 1
play 1
```
These comands will **load** a sample into the first of two buffers, set the first **voice** of six to use that first buffer and then **play** the first voice.

You can use the up and down arrows to move through the history of commands you have entered. Press the up arrow once and press enter to hear the sample again.

The **help** command will list all available commands.
A command followed by *help* will give help about that command e.g.
```
load help
```
Commands that require a *voice* parameter will generally give the current settings by entering the command with just the voice number e.g.
```
every 1
```
Commands that don't require a voice parameter will generally give the current setting by just entering the command with no parameters e.g.
```
bpm
```

## Commands
Parameters in \< \> are required, those in ( ) are optional.

[bpm \<bpm\> (s)](#bpm)

[load \<file\> (b#) (s)](#load)

[rec \<v#\>](#rec)

[voice \<v#\> \<b#\>](#voice)

[level \<v#\> \<l\>](#level)

[*pan \<v#\> \<p\>*](#pan)

[range \<v#\> \<s\> \<e\>](#range)

[rate \<v#\> \<r1\> (r2) (p)](#rate)

[rate_slew \<v#\> \<s\>](#rate_slew)

[play \<v#\>](#play)

[stop \<v#\>](#stop)

[loop \<v#\>](#loop)

[every \<v#\> \<x\> \<b/s\> (n%)](#every)

[euc \<v#\> \<p\> \<s\> (o)](#euc)

[rhy \<v#\> \<r\>](#rhy)

[filter \<v#\> \<off/hp/lp/bp\> \<f\> (q)](#filter)

[lfo \<l#\> \<v#\> \<p\> \<f\> (a)](#lfo)

[delay \<off/fb\>](#delay)

[delay_voice \<v#\> \<a\>](#delay_voice)

Use the UP and DOWN arrow keys to scroll through command history.

Use LEFT, RIGHT, HOME and END to move around the current command line.

Use ESC to clear the current command line.

Press an F key to store the current command text to that key. Press an F key on an empty line to recall stored text.

Multiple commands can be entered on a single line separated with a semicolon (e.g. rate 1;every 1 2 b)

### bpm
*bpm \<bpm\> (s)*

Sets the norns clock tempo to the specified value.

Optionally set the number of seconds to change the tempo over.

Enter the command without a tempo to see the current tempo.
```
bpm 120
bpm 80 15
```

### load
*load \<file\> (b#) (s)*

Loads the specified file into a buffer (1 or 2).

If no buffer number is specified the file is loaded as stereo - left channel to buffer 1 and right channel to buffer 2.

If a buffer is specified, the start point in the buffer (in seconds) to load the sample into can be specified. This allows multiple samples to be loaded into a buffer to be used in different voices e.g. a kick drum in buffer 1 at 0 seconds assigned to voice 1 and a snare in buffer 1 and 5 seconds assigned to voice 2. Loading a sample into a buffer will clear everything in the buffer after the start point.

Use the TAB key to auto-complete the file path.
```
load audio/tehn/whirl1.aif 1
load audio/common/606/606-SD.wav 1 5
```

### rec
*rec \<v#\>*

Toggles recording for the specified voice's buffer from the audio input.

Recording starts at the voice start point and the voice end point is changed to the end of the recording when recording is stopped.

*note:* if other voices are using the same area of the buffer it will be overwritten for them too and they will start playing the recording.
```
rec 1
```

### voice
*voice \<v#\> \<b#\>*

Sets the specified voice (1 to 6) to use the specified buffer (1 or 2).

Enter with just a voice to view the current buffer for that voice.
```
voice 5 2
```

### level
*level \<v#\> \<l\>*

Sets the amplitude for the specified voice (1 to 6).

Enter with just a voice to view the current level for that voice.
```
level 1 0.5
```

### pan
*pan \<v#\> \<p\>*

Pan the specified voice from -1.0 (full left) to 1.0 (full right)

Enter with just a voice to view the current pan for that voice.
```
pan 1 -0.5
```

### range
*range \<v#\> \<s\> \<e\>*

Sets the start and end point (in seconds) of the buffer to use for the specified voice.

Enter with just a voice to view the current range for that voice.
```
range 1 1.25 2
```

### rate
*rate \<v#\> \<r\> (r2) (p)*

Set the rate to play the specified voice (1.0 is default speed, 2.0 is twice speed etc).

Enter a min and max rate to play at a random rate between the two. 

Enter a comma separated list of rates (e.g. 1,1.2,2) followed by a pattern (up/dn/rnd) to play a sequence.

You can also specify rates as a [sequins](https://monome.org/docs/crow/reference/#sequins) sequence (without and spaces).

Specify a negative rate to play backwards.

Enter with just a voice to view the current rate for that voice.
```
rate 1 2
rate 1 0.8 1.5
rate 1 0.5,1,1.5 rnd
rate 1 -2,-2.4,-2.6 dn
rate 1 s{1,2,3}
rate 1 s{1,2,s{3,4}}
```

### rate_slew
*rate_slew \<v#\> \<s\>*

Set the slew time (in seconds) when changing the rate of the specified voice.
```
rate_slew 1 2
```

### play
*play \<v#\>*

Plays the specified voice as a one off.
```
play 1
```

### stop
*stop \<v#\>*

Stops playing the specified voice
```
stop 1
```

### loop
*loop \<v#\>*

Loop play the specified voice
```
loop 1
```

### every
*every \<v#\> \<x\> \<b/s\> (n%)*

Play the specified voice every *x* beats (b) or seconds (s).

The optional n parameter specified the chance of the sound playing.
```
every 1 1 b
every 1 10 s
every 1 4 b 75%
```
Enter with just a voice to view the current every for that voice.

### euc
*euc \<v#\> \<p\> \<s\> (o)*

Generates a euclidean rhythm of *p* pulses in *s* steps with an optional *o* offset for use in conjunction with *every* for the specified voice.

When *every* would normally play the voice, the current step of the euc sequence in checked and if set, the voice plays.

Enter with just a voice to view the current euc settings for that voice.
```
euc 1 5 8
euc 2 12 16 2
```

### rhy
*rhy \<v#\> \<r\>*

As an alterntive to euc, specify a sequence as a list of zeros and ones.

When *every* would normally play the voice, the current step of the sequence in checked and if set, the voice plays.

Enter with just a voice to view the current rhy settings for that voice.
```
rhy 1 1,1,0,1
```

### filter
*filter \<v#\> \<off/hp/lp/bp\> \<f\> (q)*

Sets the filter to the specified voice to off, high pass (hp), low pass (lp) or band pass (bp) at the specified frequency with an optional Q factor.
```
filter 1 lp 15000
filter 3 bp 2000 1
filter 6 off 
```

### lfo
*lfo \<l#\> \<v#\> \<p\> \<f\> (a)*

Applies an lfo (l#) to a parameter (p) on a voice (v#) at the specified frequency (f) with an optional amount (a).

Parameters are:
- filter - current value +/- 5000
- pan - current value +/- 1
- rate - current value +/- 1
- level - current value +/- 1

An amount of 1 gives the full range specified above, an amount of 0.5 would give half of the range.

```
lfo 1 3 level 2
lfo 2 5 pan 4 0.5
```

### delay
*delay \<off/fb\>*

Uses the 6th voice as a delay effect with the specified amount of feedback (fb).

When enabled some commands cannot be used with voice 6 (e.g. range, every, euc) but others can (e.g rate, filter, level, lfo).

```
delay 0.75
delay off
```

### delay_voice
*delay_voice \<v#\> \<a\>*

Specifies the amount (a) of voice (v#) to send to the delay effect.

Enter with just a voice to view the current settings for that voice.

```
delay_voice 1 0.5
```