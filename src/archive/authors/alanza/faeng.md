---
title: faeng
description: faeng is a sequencer
published: true
date: 2022-09-27T19:47:51.316Z
tags: sequencers, grid, arc, norns
editor: markdown
dateCreated: 2022-08-22T01:16:43.573Z
---

# faeng
faeng is a sequencer.
inspired by kria. 
powered by timber. 
connect a grid and take wing.

My brother pointed out to me the other day that my live music was lacking in drums and bass.
Since drums and bass combine to form a genre I quite like, I was chagrined;
indeed, my modular rack, while capable of many things, 
struggles to produce a rhythm section along with a lead.
Faeng represents an attempt to remedy that for myself; I hope you might enjoy it too.
("Why do you do synths the hard way?" asks my brother)
Faeng gives timber wings to soar alongside its inspiration, kria.

Many thanks to @markeats for timber, 
@tehn and everyone who has contributed to kria,
@Galapagoose and @tyleretters for sequins and lattice,
and to all of you for being part of such an inspiring community.

Now is the time for me (and you!) to use faeng, 
to find bugs and figure out what it wants to be.

### Requirements

norns.
grid.


### Documentation

Plug in a grid.
To load a folder of samples 
(into the active track's bank) 
press K3 on the landing page;
otherwise, scroll to page 1 with E1 and press K3 on `Load` to load individually.
K1+E1 scrolls the active sample; there are 64 per track, 
although only the first 49 are playable (sorry)

To change the active track, 
press one of the first four lighted buttons on the bottom row of the grid.
Four tracks.
To change the displayed page,
press one of the next five buttons
(note to kria afficionados, no "alt" pages—yet).
The pages are 
`Triggers`, 
`Sample Fine / Note`, 
`Sample Coarse / Octave`, 
`Velocity` 
and `Ratchet`.
The slashed pages have varying behavior
depending on whether the corresponding track is set to `multisample` or `repitch`.
`Multisample` is like a drummer: one arm or leg can make multiple sounds,
but only one at a time, so triggers in the same row will "cut" each other.
`Repitch` is like a bassist: one core sound (selected with K1+E1),
but can play a mean melody.
On the `Triggers` page, all four tracks are visible,
but on the others, only the active track is displayed.
Try it: press some grid keys and hear your samples played back.

`Velocity` is maybe what you expect,
but `Ratchet` has some fun in store:
pressing above the current maximum ratchet value will turn on new "bits"
which can be turned on and off individually;
turn off the last bit to reset the behavior of the step.

There are three mods:
`Loop`,
`Division`
and `Probability`,
which correspond to the next group of three on the nav bar.
Each changes the interaction and will flash while active,
and can be deactivated by pressing the same button again.

`Loop` allows you to move and resize a track's loop
(like kria, each of faeng's pages has an individual loop length).
To move, press a key to move the start of the row to that x-coordinate.
To resize, press the left and right ends of the new loop at the same time—
but release the right side first;
releasing the left side first will set the loop length to one.

`Division` shows the clock divider for the current track's selected page.
The default division is 16th notes,
and in general setting the division row to coordinate x will result in a division of x/16.
(Like kria, each page for each track has its own division.)

`Probability` shows the likelihood that a given step will update the behavior of the track.
Each page for each track has its own set of probabilities.

Faeng is powered by sequins.
Hold a step for a second and two things will happen:
the grid UI will change,
and the active track button will begin to dance.
You've entered `SubSequins` mode.
On the triggers page, the `SubSequins` row is row 6,
while on other pages, the `SubSequins` UI takes up the full page.
Resize the `SubSequins` by using the same gesture as the `Loop` mod,
then enter data.
Each time the step you originally selected is reached,
its `SubSequins` will advance, multiplying the variations one track can create.
To leave `SubSequins` mode, press the flashing `Track` button.
You'll see that the step you created a `SubSequins` for
will dance to show you the values you entered—
the dancing may not line up perfectly with what you hear.

Finally, the last key on the nav bar is the `Patterns` page.
Press a pattern to switch to it;
press and hold to copy the current pattern to it.
Switching patterns and back is a good way to bring your loops back into phase.
Faeng also has kria's `Metasequencer`, 
which can create a metapattern of up to 64 patterns,
each with its own length,
set by row 7.
Activate the `Metasequencer` while on the Patterns page
by holding the `Patterns` page key
and pressing in row 7.
In the `Metasequencer`,
row 2 is a clock divider for row 7.
Rows 3 through 6 are the 64 'steps' of the `Metasequencer`;
press one to select it or press two as in the `Loop` mod
to resize the sequence.
With a step selected, press a pattern to store it as that step's data.
Don't be alarmed:
the other page views follow the currently active pattern as set by the `Metasequencer`,
so the view may change over time.
To exit the `Metasequencer`,
repeat the gesture that you used to enter it.

### Install

```
;install https://github.com/ryleelyman/faeng
```