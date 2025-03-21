# Norns REPL-LOOPER

> Anagogically integrated UI for Norns / Matron / Grid

<img src="https://github.com/awwaiid/repl-looper/raw/main/docs/logo.png" align="right" style="padding-left: 1em" />

Experimental performance and creative tool, mashing together several things that I like. REPL (Read-Eval-Print-Loop, a code execution console) for interactive code creating. Grid to have a tactile UI (maybe we'll throw in a midi pedal too). Dance between sound-generating code, recording commands, looping, slicing, mixing, generating tools and patterns on the fly, and maybe make some self-modifying loops.

<img src="https://github.com/awwaiid/repl-looper/raw/main/docs/20230318-norns-screenshot.png" width="40%" align="right" style="padding-left: 1em" />

Check out the [dev branch](https://github.com/awwaiid/repl-looper/tree/dev) and [dev branch development journal](https://github.com/awwaiid/repl-looper/tree/dev/journal.md) for ongoing development work. The `main` branch is the current "stable" (haha) version.

# Recent Releases
* v0.1 (2022-01-08) - Initial release, generally working!
* v0.2 (2022-01-17) - Multiple Mollies, per-loop amp/fade, `all` helper
* v0.3 (2022-02-06) - More loop utils, timing fixes, bug fixes
  * Generate key-off events
  * Fix Timber slicing
  * `loop:pan(-0.5)` to pan the whole loop
  * `loop:noLoop()` to stop looping
  * `loop:once()` to play once
  * `loop:align(other_loop)` to slide events into alignment
  * `loop:slice(s1)` now takes sample-variable instead of sample-variable-name
  * Fix `loop:split(other_loop)` to work more reliably and take a base-command
  * Fix `loop:merge(other_loop)` to keep relative timings (using the new `loop:align`)
  * Embedded Goldeneye - add pan, lowpass; fix rate
  * Lay out long loops on the grid by zooming-out (more steps-per-button)
  * Rename `ALL` to `all`
* v0.4 (2023-03-18) - On-norns UI, live sample recording, midi-pedal
  * New on-norns UI
  * New on-norns keyboard input
  * Using softcut, live record a sample and then slice it into a loop
  * Add the ability to select a current-loop and record via midi-pedal
  * If the current loop is loop-1, then stretch the BPM to match the sample at 16 steps
* v0.5 (2023-11-06) - Editor
  * Add cursor, arrow keys, home/end, and dynamic height to input editor
  * On-screen grid mirror
  * Abandon web UI
* v0.5.1 (2023-11-07) - Fix grid keypress

# Installation

Install directly from maiden or by running this in the maiden/matron console:

```lua
;install https://github.com/awwaiid/repl-looper
```

Then start `repl-looper` on the norns.

There are two primary ways to control `repl-looper` -- A USB keyboard and a Monome-Grid. The keyboard is for typing in live code that gets executed, the Grid for visualizing and sequencing events.

BONUS interface: A USB/Midi foot pedal! You can use this to select the current loop and start/stop recording!

# Basic Usage

The workflow is similar to maiden's REPL - you run Lua commands and see the results. Besides being on the norns directly, the other big thing you get is a tiny DSL, Domain Specific Language, which are some nice built in shortcuts for doing some loop manipulation.

Let's get started! First, verify that everything is running with some simple math, type in:

```lua
2+2
```

Which should output `2+2 -> 4` (give or take). You can see both the input and the result. While you can run any Lua commands you want, `repl-looper` comes with a built-in engine and a bunch of tools. The built-in engine is a mash-up of Timber, Goldeneye, and Molly the Poly, along with some lua wrappers. Try these commands:

```lua
-- Timber piano shortcut
p
p'c'
p'd'
p(68)

molly:note(60)
molly:randomize()
molly:note(62)
molly:stop()
```

Press `<tab>` for some completions. You can press `<up>` or `<down>` arrows to select previous commands or tab-completion choices. Press `<enter>` without any command to run the previous command again. You can use `<left>`, `<right>`, `<home>`, `<end>`, and `<backspace>` to do some light editing.

Next thing to play with is loops/sequences. There are 8 pre-defined 16-step loops, one for each row, put into variables `a` to `h`. Start by recording into loop `a`:

```lua
a:rec()
```

Loop `a` is now playing and recording! You can see the current step and steps with recorded events on the grid. Now run:

```
p'c'
```

Wait a bit, and then run:

```
p'd'
```

The loop is playing and will wrap back around at 16 steps and keep recording, so if you add more events they stack up on top of each other. Now try:

```
a:stop() -- this stops recording but keeps playing
a:stop() -- stop again to also stop playing
```

At this point press some of the grid buttons to trigger all the events recorded at that step immediately (this ignores their sub-step timing). Here are a few more things to try:

```
a:show() -- show the loop contents
a:play() -- start loop again
a:clear() -- erase loop contents
```

Now that you have the script running on norns and everything working, read through the [Usage Reference](#fullish-usage-reference) below and [Techniques](techniques.lua) to get more some ideas!

## The Grid

![repl-looper-grid](docs/repl-looper-grid.png)

The Grid visualizes the loops, their content, and their current status.

* Each row is a loop (`a`..`h`)
* Each step that has commands is lit up (dimly)
* Press a button to execute all the commands at that step
* You will see the command go into the REPL execution history exactly as if you had run it by hand
* The current step is lit up brightly
* When you are playing a loop (like `a:play()`) you will see the current step move across and then loop back around
* If you are recording one loop, like `a:rec()` and you press buttons on any loop those events are executed _and recorded!_
* So you can create an adhoc piano on loop `h`, start recording on loop `a`, and then jam the piano buttons
  * ```h:gen("p(`50+m`)")``` -- put a piano note on each step
  * You could also put some 808 stuff on a loop like ```g:gen(keys(s808))```
  * `a:rec()` -- start recording, jamming, looping!!!

# Resources

* [Techniques / Tutorial](techniques.md) to get some ideas!
* [Youtube video walk-through of the techniques](https://youtu.be/FPE5DOlScIY)
* [Development Journal / Changelog](journal.md) for a running log of experiments

# Fullish Usage Reference

## UI
* At the bottom is your input, above that are recent commands and completion suggestions
* `<left>`, `<right>`, `<home>`, `<end>`, and `<backspace>` to do some light editing
* Use `<up>` and `<down>` arrows to select commands and output from history
* Press `<enter>` to execute the most recent item from history (re-run command)
* Use `<tab>` to see what functions/methods are available (tab-complete)
* Simple functions with no parameters are automatically evaluated, so you use `p` instead of `p()`
* Common 808 samples are loaded under `s808.<tab>` and have shortcuts like `CP`

## Library and Live-Coding Helpers

There are a lot of pre-defined variables, functions, and objects to make live-coding with `repl-looper` convenient. These have been built organically based on usage, suggestions are welcome! In particular tab-complete-friendly prefixes for method names could be improved.

## Pre-defined variables/functions
* `a`..`h` -- loops, one per grid-row
  * `loops` is a table of all eight, so you can do `all(loops):amp(0, 10)` to fade everything at once
* `p` -- a Timber-based piano sample player
* `piano` -- the underlying piano sample (via Timber)
  * You can do things like `piano:reverse()`
* `molly` -- an instance of Molly, which wraps Molly The Poly
  * `molly2` ... `molly8` -- more pre-defined Mollys
  * `mollies` is a table of all eight, so you can do `all(mollies):stop()`
  * Tip: ```h:gen("molly:note(`60+m`)")``` will put one molly-note on each step for a playable synth!
* Pre-loaded 808 samples in `s808.*` with these shortcuts
  * `BD`, `BD`, `CH`, `CY`, `LC`, `MC`, `RS`, `BS`, `CL`, `HC`, `LT`, `MT`, `SD`, `CB`, `CP`, `HT`, `MA`, `OH`
  * Call with `CP` or `CP()` or `s808.CP:play()`
  * Modify with `s808.BS:amp(2)`
  * Tip: `h:gen(keys(s808))` will put one sample on each step for a playable drum kit!

## Loop

There are 8 pre-defined loops, `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h`. Each loops is assigned to a row on the grid. So `a` is on the first row and `h` is on the bottom row.

Here we use loop `a` as the example, but you could run these commands on any loop.

* `myloop = Loop.new()` -- Create a new Loop (I usually use `a`..`h` pre-defined loops instead)
* `a.current_step` -- current step (integer)
* `a:setLength(steps)` -- Set the number of steps (quarter-notes)
* `a:show()` -- Convert into a lua-style string and show it
* Control loop playback
  * `a:play()` -- Start playing and looping
  * `a:once()` -- Play once but do not loop
  * `a:stop()` -- Stop playing or recording
  * `a:noLoop()` -- Stop looping when we get to the end
  * `a:nextStep()` -- Increment the current step to the next step
  * `a:prevStep()` -- Decrement the current step to the previous step
  * `a:setStep(step)` -- Set the current step
* Modify or generate loop contents
  * `a:rec()` -- Start recording. Commands run in the REPL get recorded at the current time. You can also trigger commands by pressing grid buttons.
  * `a:clear()` -- Remove all events
  * `a:put(step, command)` -- Assign a command at a specific step
    * This is handy for building up a set of controls
  * `a:gen(code_string, condition, offset)` -- Generate events in a loop programmatically, with macro expansion. Very powerful!
    * `a:gen("CH")` -- puts the "CH" function on every step
    * `a:gen("CH", 1/2)` -- puts the "CH" on every half step
    * `a:gen("CH", 2, 3)` -- puts the "CH" on every other step starting with step 3
    * `a:gen("CH", { 1, 3, 4.5 })` -- puts the "CH" on the given steps (even fractional)
    * `a:gen({"BD","SD","CP"})` -- puts each one on each step
    * Macro expansion
      * Backticks are evaluated for each generated event
      * Within macros, you can use `n` for the one-based step/column and `m` for the zero-based step/colum
      * ```a:gen("p(`50+m`)")``` -- Generates `p(50)`, `p(51)`, `p(52)`, and so on filling up all 16 steps
      * ```a:gen("piano:filterFreq(`100 * n`)")``` -- Generates low-pass for 100 hz, 200 hz, 300 hz, etc
      * You can pass a second parameter to `gen` for grid button-release events. This way you can start playing a note on button-down and stop the note on button-release
      * Button release example: ```a:gen("molly:note(`60+m`)", "molly:offNote(`60+m`)")``` -- only for grid triggered events the "off" event will be executed on button release
  * `a:quantize()` -- Events are recorded at sub-steps by default; this immediately rounds them to the nearest step
  * `a:clone(other_loop)` -- Copy this loop onto another (empty the other out)
  * `a:merge(other_loop)` -- Merge other_loop into this one. New loop is the longest of the two
    * `other_loop` is cleared
  * `a:split(other_loop)` -- Split the current loop, putting some events into `other_loop` and keeping some
    * This works by looking at the text of the commands to judge similarity (edit-distance) to the first event-command in the loop. Events that are on-average similar to the first event are kept, events that are different are put into the other loop.
    * `a:split(other_loop, base_cmd)` -- You can pass in a base-command and it will try to keep things like that in the current loop
  * `a:slice(sample, step_offset, step_count, reverse)` -- Take a Goldeneye/Timber sample and slice it
    * This is effectively a complex generator of frame-offsets in the sample playback
    * If `reverse` is true then start from the end of the sample
  * `a:align(other_loop)` -- Slides events into alignment with another loop based on the current step of each; does not modify the loop otherwise
    * So if loop `a` and loop `b` are playing but their current-steps (playheads) are different, this will shift loop `a` events and current-step so that they are lined up
    * This is useful if you either recorded or played the loops visually out of sync, but you like they way they currently sound while they are playing and want to make them LOOK in-sync the way they sound
    * A fun thing to do is `all(loops):align(a)`
* Control loop dynamics
  * The whole output of a loop goes through its own Supercollider track for all of the bundled engines. The result is that you can modify the output of the whole loop at once
  * `a:amp(level)` -- Set the amp (0..1) for the whole loop; the included engine loops everything through the triggered loop!
    * `a:amp(level, lag_time)` -- Fade to the given volume over the given number of seconds
    * Example: `a:amp(0, 10)` will fade out the whole loop over 10 seconds
  * `a:pan(amount)` -- Pan the whole loop. Panning goes from -1 (left) to 1 (right), and 0 is center

## Engine wrappers

* `t1 = Timber.new("path/to/file.wav")` -- Timber wrapper (works with .ogg too!)
* `s1 = Sample.new("path/to/file.wav")` -- Goldeneye wrapper (works with .ogg too!)
* `m1 = Molly.new()` -- Molly the Poly wrapper (you can have several!)
  * Tip: `molly:randomize()` -- Randomize the synth params!
  * `molly` and `molly2..molly8` are pre-created for convenience
* Once you have an instance, use tab (ex `t1:<tab>`) to explore! There are wrapper methods that generally do what the engine does
  * Try this with the built-in `molly` sample by typing `molly:<tab>`
* You could of course use any engine you like! Only a few commands like `Loop:slice(...)` method depend on these wrappers. Otherwise this is arbitrary lua code getting sequenced

## BONUS: `all` object wrapper
* This function can be used on a table of objects and then call a given method on each of them
* `all(mollies):stop()` -- All the pre-created mollies are stored in `mollies`, this stops them all!
* `all(loops):amp(0, 10)` -- All the pre-created loops are stored in `loops`, this fades them all out!
* `all{a,b,c}:play()` -- Play all three loops, equivalent of `a:play();b:play();c:play()`
* `all{a,b,c}:play(1):amp(1, 10)` -- Chained command that both plays and fades-in the loops

# Development

I made a fancy script that rsyncs changes to the lua files when you save:

```sh
# Auto-push to norns
./util/watch-sync.sh
```

I also like to run VNC so that I can have it all on my laptop. I have a modified version of framebuffer-vncserver (the upstream one was causing weird screen glitches) which I run on the norns:

```
cd local/framebuffer-vncserver/build
./framebuffer-vncserver -k /dev/input/event0
```

And then locally the best client I found was the proprietary RealVNC client; it did the scaling without blur the best. I'm still not sure how to get rid of the local X cursor. Bleh.

```
vncviewer EnableToolbar=0 SecurityNotificationTimeout=0 ColorLevel=full SendPointerEvents=0 norns.local:5900
```

# Future Ideas

* Grid on screen
  * Show events
  * Click to do the same thing as the grid button press?
* Mash up editor and REPL
  * Like a notebook but worse
  * Let the code edit the code
  * Constant fzf-style autocomplete
  * LLM completions
* Loop Recording / Editing Modes
  * Step first: Pick a step and record an event
  * Event sequencing: Take an event and place (or edit) the location of the event
  * Edit mode where a button-press loads all (timed) events for editing
* Sync loops together better?
* Add visual half-loops (8 steps) for the grid
  * `a1`..`h1` to span columns 1..8
  * `a2`..`h2` to span columns 9..16

# Shout Outs!

* [Grégory Montigny for initial logo (CC-BY)](https://thenounproject.com/simpleicon/)
* eigen on norns-study-group discord for suggesting Lattice
* Everyone on [lines (llllllll.co)](https://llllllll.co) for being awesome
* [Hoelzro for lua-repl](https://github.com/hoelzro/lua-repl) from which I've adopted bits
* [Ensequence for js2lua (MIT, embedded)](https://github.com/Ensequence/js2lua)
* [markwheeler](https://github.com/markwheeler) for [Timber](https://github.com/markwheeler/timber) and [Molly The Poly](https://github.com/markwheeler/molly_the_poly) which I've embedded
* [Library of Congress Citizen DJ Project](https://citizen-dj.labs.loc.gov/), both inspirational and a source of samples I've been playing with
* [Infinite Digits](https://github.com/schollz) for this inspirational [Flash Crash Performance of Internorns](https://www.youtube.com/watch?v=bJTnfvg153M) and some help mashing in some samplers
