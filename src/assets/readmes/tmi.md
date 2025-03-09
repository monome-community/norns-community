## tmi

*textual music instructions / tiny midi interface / too much information*

https://vimeo.com/503866942

*tmi* is a norns library for composing and sequencing devices with text, ported to norns from [a version i previously wrote](https://github.com/schollz/miti). its basically a norns tracker, but unlike other norns trackers with wonderful visuals and features (e.g. [yggdrasil](https://llllllll.co/t/yggdrasil), [orca](https://llllllll.co/t/orca)), *tmi* has few features and basically no visual interface. however, the one feature that *tmi* does have is that **tmi can be used within any other norns script** so with a few lines of code+text you can sequence multiple external devices (notes and ccs) from your favorite norns script.

*tmi* music tracks are written in text files (more on that below). when *tmi* is added to a script, these files can be loaded via the `PARAMETERS > TMI` screen in the parameters menu. once loaded, any changes to files are hot-loaded so you could do live-coding (if you have a computer handy).

this script finalizes a trilogy of norns scripts i've been writing that can be imported into other norns scripts. my goals was to take a existing sample-based script be able to *also*...

- ...have command-mapping to single buttons (via [middy](https://llllllll.co/t/middy))
- ...be compatible with a grid-based drum machine (via [kolor](https://llllllll.co/t/kolor))
- ...be able to do midi sequencing (via [tmi](https://llllllll.co/t/tmi))

the importable scripts above work in a multitude of scripts ([barcode](https://llllllll.co/t/barcode), [oooooo](https://llllllll.co/t/oooooo), [cranes](https://llllllll.co/t/cranes), [otis](https://llllllll.co/t/otis), to name a few) but might not work with all (especially if the host script already uses midi or something).

### Requirements

- norns
- external midi device

### Documentation

#### Install

first install in maiden with 

```
;install https://github.com/schollz/tmi
```

then edit an existing script. in the existing script add these lines of code somewhere (preferable near the top) of the script:

```lua
if util.file_exists(_path.code.."tmi") then 
  tmi=include("tmi/lib/tmi")
  m=tmi:new()
end
```

if you want *tmi* to play a certain file on a certain instrument right away, you can add these two lines:

```lua
-- change "op-1" to the instrument your using
m:load("op-1","/home/we/dust/data/tmi/somefile",1)
m:toggle_play()
```

now open the script and goto the parameters menu: `PARAMETERS > TMI`. make sure you have your midi device plugged in before you start, otherwise `TMI` menu will not be available. now you can load *tmi* files into any connected midi instrument (up to 4 tracks per instrument).

### Making *tmi* files

*tmi* works with text files with textual musical notation - either notes, chords, rests, or sustains. by default these files are found in the `~/data/dust/tmi` directory. you need to make these files yourself using maiden or another text editor.

rules for these files:

- one line is one measure, and is subdivided according to how many things are in it. example: "`C . . .`" plays a C-major chord on beat 1 and rests for 3 beats
- chords start with an uppercase letter, inversions allowed with "`/`" and octaves allowed with "`;`". examples: "`Cmin`", "`F#min/A;4`", or "`Db;5`")
- notes start with a lower case letter, with optional octave number, separated by commas. examples: "`e5`", or  "`f4,a,c`"
- the "`-`" character sustains the last entry
- the "`*`" character re-plays the last entry
- the "`.`" character is a rest
- multiple sequences can be in one file with each below a line specifying "`pattern X`" where you fill in "`X`"
- if multiple sequences are in one file, chain them with "`chain X Y`"
- comments are specified by "`#`"
- pairs of *numbers* are interpreted as cc number and cc value respectively, example: "`24,99`"

by default *tmi* uses a meter of 4, but this can be changed at startup using `m = tmi:new{meter=X}`.

### examples of *tmi* files

the following are valid *tmi* files. 

this one plays four chords:

```
# a four chord song
C
G/B
Am/C
F/C
```

this one alternates between holding out a C-major7 chord and an arpeggio:

```
# switch between playing a chord for two measures 
# and an arpeggio of the chord

chain a b 

pattern a 
Cmaj7
-

pattern b
c4 e g b c e g b
c6 b g e c b g e
```

modulate two ccs (74 and 24) periodically:

```
74,100,24,40 74,99,24,40 74,99,24,42 74,99,24,45 
74,98,24,48 74,97,24,53 74,96,24,58 74,95,24,64 
74,94,24,69 74,92,24,75 74,91,24,81 74,89,24,86 
74,87,24,91 74,85,24,94 74,83,24,97 74,81,24,99 
```

this last example is actually generated from a lua script. though you can certainly type out the numbers you want, you can also generate your own cc lfo patterns on any number of ccs, just open `~/dust/code/tmi/lib/cc_lfo.lua` and edit it and then run:

```
> lua ~/dust/code/tmi/lib/cc_lfo.lua > ~/dust/data/tmi/your_ccs
```