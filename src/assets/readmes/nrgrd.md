Nørgård
------

v0.1.1

**A small library to generate Nørgård infinity sequences for [Norns](https://monome.org/norns).**

Thank you to [Ezra Buchla](https://llllllll.co/t/composition-toolkit-blog-generative-techniques/35657/9) for his lua Nørgård algorithm and [Lawton Hall](https://llllllll.co/u/_greathorned) for his Nørgård [SuperCollider algorithms](https://www.lawtonhall.com/blog/2019/9/9/per-nrgrds-infinity-series).


---

## Install

You can install this library and demos via Maiden. Be sure to refresh the `Community` lists, and look for `nørgård`.

Otherwise, if you're a developer, pull down the library from [Github](https://github.com/frederickk/noergaard) and checkout the API below.


---

## Usage

Look at the demos to see how the library can be used. The library itself is [`lib/noergaard.lua`](./lib/noergaard.lua) just add that file to your scripts folder, wherever you chose (I prefer `lib/`). Then add the following to your script.

```lua
local noergaard = include("path/to/noergaard")
```

---

## Demos

Along with the library are 3 demos showing how to use the library.

### **noergaard-simple**

Generates Nørgård infinity series and played using the PolyPerc engine. There are no controls, it just starts and goes on... infinitely

![screenshot of noergaard-simple](./.assets/noergaard-simple.png)


### **noergaard-sequencer**

A fairly simple sequencer that plays infinity sequence — uses PolyPerc engine and also outputs Midi notes (to device 1).

![screenshot of noergaard-sequencer](./.assets/noergaard-sequencer.png)

| Page | Controller | Description                                                  | Values                |
| ---- | ---------- | ------------------------------------------------------------ | --------------------- |
| All  | E1         | Change page                                                  |                       |
|      |            |                                                              |                       |
| 1    | E2         | BPM                                                          | 20 - 300              |
| 1    | E3         | note length                                                  | 1/256 - 4             |
|      |            |                                                              |                       |
| 2    | E2         | Midi root                                                    | C-2 - C8              |
| 2    | E3         | Scale type (see [norns/musicutil.lua](https://github.com/monome/norns/blob/main/lua/lib/musicutil.lua#L12) for full list); 0 = scale determined naturally by algorithm | 0 - 46 |
|      |            |                                                              |                       |
| 3    | E2         | Step                                                         | 1 – 12                |
| 3    | E3         | Sequence length; 0 = maximum (or 480)                        | 0 - 320               |
|      |            |                                                              |                       |
| 4    | E2         | Loop at length                                               | true (1) or false (0) |
| 4    | E3         | Increment                                                    | 1 - 8                 |



### **noergaard-chords**

Generate chords from infinity series intervals — uses PolyPerc engine and also outputs Midi notes (to device 1). Thanks to [Devine Lu Linvega](https://github.com/neauoire/monitor) for the keyboard.

![screenshot of noergaard-chords](./.assets/noergaard-chords.png)

| Page | Controller | Description                                                  | Values                |
| ---- | ---------- | ------------------------------------------------------------ | --------------------- |
| All  | E1         | Change page                                                  |                       |
|      |            |                                                              |                       |
| 1    | E2         | BPM                                                          | 20 - 300              |
| 1    | E3         | note length                                                  | 1/256 - 4             |
|      |            |                                                              |                       |
| 2    | E2         | Midi root                                                    | C-2 - C8              |
| 2    | E3         | Chord type (see [norns/musicutil.lua](https://github.com/monome/norns/blob/main/lua/lib/musicutil.lua#L60) for full list); 0 = build chord from sequence notes using amount determined by `Chord length` | 0 - 26 |
|      |            |                                                              |                       |
| 3    | E2         | Step                                                         | 1 – 12                |
| 3    | E3         | Sequence length; 0 = maximum (or 480)                        | 0 - 320               |
|      |            |                                                              |                       |
| 4    | E2         | Loop at length                                               | true (1) or false (0) |
| 4    | E3         | Chord length; only applies when `Chord type` is set to `Noergaard` | 2 - 9                 |


---

## API

`Noergaard.compute(t, step)`

Nørgård algorithm to compute intervals. Thank you @zebra!
https://llllllll.co/t/35657/9

**Parameters**

`t` a table containing at least 2 values

`step` (optional, default=1) new interval step

**Returns**

nothing; new value is appended to the table in-place


<hr style="border-style: dotted;">

`Noergaard.integer(index)`

Returns integer in infinity series by index.
https://www.lawtonhall.com/blog/2019/9/9/per-nrgrds-infinity-series

**Parameters**

`index` index of infinity series to calculate 

**Returns**

Nørgård number


<hr style="border-style: dotted;">

`Noergaard.compute_subset(start_index, end_index)`

Populates intervals table with Nørgård integers within a given range.
https://www.lawtonhall.com/blog/2019/9/9/per-nrgrds-infinity-series

**Parameters**

`start_index` starting index of infinity series

`end_index` ending index of infinity series


<hr style="border-style: dotted;">

`Noergaard.step()`

Adds interval to table, based on "start" and "step" params.


<hr style="border-style: dotted;">

`Noergaard.get_step()`

Gets step increment.

**Returns**

Step interval


<hr style="border-style: dotted;">

`Noergaard.get_interval(index)`

Gets interval.

**Parameters**

`index` (optional) interval index; no index returns last added interval

**Returns**

Interval


<hr style="border-style: dotted;">

`Noergaard.get_midi_note(index)`

Gets Midi note number.

**Parameters**

`index` (optional) note index; no index returns last added note

**Returns**

Midi note number


<hr style="border-style: dotted;">

`Noergaard.get_midi_note_scale(scale_type, index)`

Gets Midi note number, snapped to given scale.

**Parameters**

`scale_type` String defining scale type (eg, "major", "aeolian" or "neapolitan major"), see "musicutil" class for full list.

`index` (optional) note index; no index returns last added note

**Returns**

Midi note number


<hr style="border-style: dotted;">

`Noergaard.get_midi_root()`

Gets Midi root note as name + octave e.g. "C4".

**Returns**

Midi root note


<hr style="border-style: dotted;">

`Noergaard.get_note_name(index)`

Gets Midi note name e.g. "C".

**Parameters**

`index` (optional) note index; no index returns last added note

**Returns**

Midi note name


<hr style="border-style: dotted;">

`Noergaard.get_note_freq(index)`

Gets note as frequency name e.g. C4 => "261.63".

**Parameters**

`index` (optional) note index; no index returns last added note

**Returns**

Note frequency 


<hr style="border-style: dotted;">

`Noergaard.get_note_freq_scale(scale_type, index)`

Gets note as frequency name e.g. C4 => "261.63", mapped to given scale

**Parameters**

`scale_type` String defining scale type (eg, "major", "aeolian" or "neapolitan major"), see "musicutil" class for full list.

`index` (optional) note index; no index returns last added note

**Returns**

Note frequency 


<hr style="border-style: dotted;">

`Noergaard.set_octave(index)`

Sets octave to lock Midi notes to.

**Parameters**

`index` (optional) Midi octave value -2 to 8; no index sets octave to "Natural".


<hr style="border-style: dotted;">

`Noergaard.get_octave()`

Gets octave as string.

**Returns**

Octave value



---

## Params

`params:set("noergaard_start", num)` 

Sets seed starting value, setting/changing this will reset the interval values table; default = 0

`params:get("noergaard_start")`

Returns seed starting value

**Range**

0 – 12


<hr style="border-style: dotted;">

`params:set("noergaard_step", num)`

Sets seed step value, setting/changing this will reset the interval values table; default = 1 

`params:get("noergaard_step")`

Returns seed step value

**Range**

1 – 12


<hr style="border-style: dotted;">

`params:set("noergaard_midi_root", num)`

Sets root (starting) note for all Midi subsequent notes.

`params:get("noergaard_midi_root")`

Returns Midi root (starting) note as number

**Range**

0 – 128


<hr style="border-style: dotted;">

`params:set("noergaard_octave", num)`

Sets octave for notes returned any value above 0 locks the returned notes to that octave; default = 0 (or Natural)

`params:get("noergaard_octave")`

**Range**

- 0: Natural, i.e. what the algorithm would naturally generate
- 1: -2
- 2: -1
- 3: 0
- 4: 1
- 5: 2
- 6: 3
- 7: 4
- 8: 5
- 9: 6
- 10: 7
- 11: 8


<hr style="border-style: dotted;">

`params:set("noergaard_len", num)`

Sets a specific maximum number for intervals, a value of 0 means no defined length, but the maximum is 480; default = 0

`params:get("noergaard_len")`

**Range**

0 – 480


---

## References

- [Per Nørgård](https://en.wikipedia.org/wiki/Per_N%C3%B8rg%C3%A5rd)
- [A guide to Per Nørgård's music](https://www.theguardian.com/music/tomserviceblog/2012/jul/30/per-norgard-contemporary-music-guide)
- [Per Nørgård's infinity sequence](https://www.youtube.com/watch?v=Q_FGImH1RWE)
- [Composition Toolkit Blog - Generative Techniques](https://llllllll.co/t/composition-toolkit-blog-generative-techniques/)
- [Per Nørgård's Infinity Series](https://www.lawtonhall.com/blog/2019/9/9/per-nrgrds-infinity-series)
