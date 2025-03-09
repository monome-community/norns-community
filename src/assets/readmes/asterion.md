# Asterion
An inscrutable adventure game as a percussive drone sequencer

Asterion is an unconventional musical instrument. It's a noisy corridor simulator with gloom modulation, a sequencer programmed a move at a time by exploring a randomly generated maze. Past steps dog your heels as your actions play back upon you. It's a paean to [Jorge Luis Borges](https://en.wikipedia.org/wiki/The_House_of_Asterion). Maybe it's even an art project.

"All the parts of the house are repeated many times, any place is another place."

## Use
Each floor of the labyrinth is generated at random with a couple of simple rules for distributing keys and locks.

Use arrow keys or `W, A, S, D` to navigate. Collect keys with `SPACE` or `ENTER`. Unlock doors with the same.

Every locked door has a matching key, and every floor has a final door that descends to the next level. Repeat ad nauseum. Loops, however, are finite. Each step advances the loop and records a new step at that index with audio characteristics defined by the situation of the room and the player's inventory. The Number of steps in the loop and the depth of events at each step are determined by the app params. The default is a loop of 16 steps with each step having a maximum event depth of 4 events. The result is like overdubbing, where each step recorded proceeds along the loop and then wraps around, but rather than overwriting the original step, a new event is added (up to the maximum allowed). Over the max, the next step records to the first index at the step and the original is lost.

While events are recorded in a breadth-based loop, playback is depth-first. At each step in the playback loop, which begins advancing when the splash screen is dismissed, all available modulation events within that loop step are played before advancing to the next step. 1:1, 1:2, 1:3, 2:1, 2:2, 3:1, and so on.

Adjust the `Drone Base` note, `Loop Length`, and `Max Step Depth`, along with various `Asterion (Engine)` characteristics in the params menu. Note that in the `Asterion (Engine)` params, only `amplitude`, `hz` and `noise amplitude` will stay where you put them due to the nature of the script.

In addition to the sequenced drone, programmed by exploring the labyrinth, you can play accent notes in scale from the drone base using your (typing) keyboard's number keys. These will play the ten notes in the `scale` of your selection from the `Asterion` parameter group. You may also adjust the fixed `velocity` of accent notes played. Note that `attack`, `decay`, `sustain` and `release` within the `Asterion (Engine)` params apply exclusively to the Accent feature in this script and have not effect on the drone.

Parameter adjustments and accent notes are not recorded to the loop. Only events from gameplay are sequenced.

A word of WARNING: Care has been take to tame the drone, but it has some intimidating qualities that should be explored at moderate volumes as you begin to wander the labyrinth. I moved from testing it on a regular stereo speaker to a bass amp and nearly had a heart attack.

Run the following in maiden to install:
`;install https://github.com/cachilders/asterion.git`

You will need to restart (possibly twice) for the Asterion engine to be compiled by norns.

## Acknowledgements
Asterion splash typeface is adapted from [Rosarivo](https://fonts.google.com/specimen/Rosarivo/about). Environments and graphical elements were built in [Crocotile](http://www.crocotile3d.com) and [Aseprite](https://www.aseprite.org). Everything else was [reading the manual](https://monome.org/docs/norns/engine-study-2/#engine-lib), [watching tutorials](https://youtu.be/ntL8QDOhhL8?si=0lnKQxBFNbMhZilt), gaining confidence from [a workshop](https://musichackspace.org/product/tone-to-drone-introduction-to-supercollider-for-monome-norns/), and trial and error. Oh, also the initial game portion of development was done in [seamstress](https://llllllll.co/t/seamstress-is-a-lua-scripting-environment-for-musical-communication/64556).