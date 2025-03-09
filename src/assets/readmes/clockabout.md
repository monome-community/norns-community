# Clockabout

A non-linear MIDI clock for monome norns - why should
swing be the only non-linear time pattern?

![Cover image](screenshot.png)

The current version is 0.9.0.


## How to use it

In the norns PARAMS menu select which MIDI device the script will send its
clock signal to. Select a single device, or use the submenu to choose
multiple devices.

- E1: Select pattern.
- E2: Change BPM.
- E3: Pattern-specific param.
- K1+E3: Second pattern param (for some patterns only).
- K3: Start/stop the clock.

The PARAMS menu also allows you to change how many beats the pattern
lasts for.

If you like the script, you may also want to run it as a mod. See further
below.


## Installation

In maiden, use
```
;install https://github.com/niksilver/clockabout
```


## General notes

A MIDI start/stop message is sent when, and only when, the clock starts and stops
(K3, or via the PARAMETERS > EDIT menu).
Just changing which MIDI device receives the clock
will route (or stop routing) the clock messages to that device,
but won't send a MIDI start/stop message.

The script will load the last saved PSET on startup. So if you save your
setup then you can continue with that as soon as you start the script next time.

The on-screen graph may or may not mean what you think it means.
The x-axis is standard time and the y-axis is pattern time. A more shallow
line means the pulses are more compressed, so occur closer together. A steeper
line means the pulses are more spread out, so occur further apart.

Beats sync on the first clock pulse of the pattern.
For example, consider a random pattern of length one beat, at 60 BPM. This will
send 24 pulses per second (because MIDI clocks must send 24 pulses per beat,
and 60 BPM means one beat per second).
Those pulses will be spaced irregularly, but the first of those 24 pulses
will always be 1 second apart. As a more complicated example,
consider a pattern also at 60 BPM, but with length 4 beats. This will still
send 24 pulses per second, and there will be 96 pulses across the whole pattern
(96 = 4 * 24). And we can (only) rely on that fact that the first of these
96 pulses will always be 4 seconds apart.

It's about 3/1000 of a second out each beat. Internally, some processing
between pulses takes a bit of time and adds this delay. This means that when
we said above that an example pattern's first pulse was 1 second apart,
it's really about 1.003 seconds on average. I hope that's not too important
to most people.

The pattern is not entirely smooth. The on-screen graph might
look like a curve, but internally that curve is broken into six linear
segments and pulses are sent according to that. I am assuming that the
difference will be inaudible... or at least excusable.


# Running as a mod

Once installed, you can enable this as a mod.
See the [documentation on
installing and enabling mods](https://monome.org/docs/norns/mods/).
Then you can run
a norns script and send Clockabout MIDI pulses to external devices.

You can also route those MIDI pulses back into the norns, so that your
script responds to the non-linear clock. Set this up using the
PARAMETERS > EDIT > CLOCK menu to receive MIDI clock input.
But note that to do this you
do need an external device - Clockabout sends MIDI pulses out, and
cannot control norns' own internal clock directly.

When it is enabled as a mod things are slightly different, as follows...

The mod attaches itself to any script that starts up. It puts its
parameters in the usual PARAMETERS > EDIT menu, and they will appear before
the script's own parameters. So you'll need to scroll down to see those
script parameters.

The mod does not use the Clockabout graphical input. Instead, you'll need
to adjust its parameters via the PARAMETERS > EDIT menu.

If you do want to use Clockabout's graphical input then you can also
run it as a script. Of course, in this case you can't run another norns
script.

As usual in norns, you can save and load a script's parameters via the
PARAMETERS > PSET menu. If you save a script's parameters with
Clockabout enabled as a mod, then you will save Clockabout's parameters,
too. Then you can load them next time for that script and the Clockabout
mod. But note that parameters are saved per script; you can't save
the mod's parameters alone. However, since you can run Clockabout as
a script, even with the mod enabled, then you can save the Clockabout
script's parameters and load them back when you run the script again.

If a script runs without any Clockabout parameters being loaded from
a PSET, then
Clockabout's clock will not start by default. This is different
to running Clockabout as script (with or without the mod), when its
default is to start its clock as soon as it loads.

Internally, Clockabout uses two of norns' own metronomes, and there is
a limited number of these. So it's possible that a script will take
all the available metronomes, leaving none for Clockabout. If this
happens then there will be a warning message in the matron log and
Clockabout will stop its clock. You can toggle it back on in the usual
way. Of course, when you do this there may or may not be metronomes
available again.


## Development and testing

To run the tests just execute

```
lua lib/test_clockabout.lua
```
or
```
make test
```

The tests are in the `lib` directory so that they don't show up in norns'
SELECT menu.


## Thank you!

Thanks to all those who have contributed to the metro module -
@tehn, @okyeron, @scazan, @catfact -
and to the norns codebase and documentation generally.
