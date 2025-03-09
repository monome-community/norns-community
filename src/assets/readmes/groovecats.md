# groovecats 
is a weird cat sequencer thing. 

many cats can exist in a two dimensional space.

cats spit furballs at rhythmic intervals.

the furballs can bounce and collide with each other. 

different types of physics events can trigger different types of bangs. 

play, explore, meow.

![groovecats.png](https://norns.community/community/quixotic7/groovecats.png)

https://www.youtube.com/watch?v=ip6Ou3-8g_s

**new grid update!**
https://www.youtube.com/watch?v=RlfxUO4MQcQ

## requirements

* **norns**
* [**TheBangs**](https://llllllll.co/t/38865/) - for cool sounds

## optional

* **128 grid** - very highly recommended
* **external midi devices** - expand your sound pool!

## features
* a unique physics based sequencer
* 7 different cats
* 4 internal synths
* 7 different synth engines provided by the [bangs engine](https://llllllll.co/t/38865)
* time synced delay

## grid features
* use the toolbar in collumn 16 to change between grid pages
* move around your cats or enjoy a lightshow in the "Petting zoo" page
* sequence bounces with an awake style sequencer in the "Meowquencer" page
* change bang sound sources for "launch", "bounce", and "collision" physics events, launch probability, and launch sync rates in the "Cat Config" page
* adjust every parameter of the synths using grid faders in the "Synths" page
	* click a key on a fader to jump to a value, hold a key to smoothly fade to a value
* quickly save and load projects on the "File IO" page
* every grid action shows an on-screen message so it's easy to figure out

## norns doc

* **key 1** shift

* **hold key 1, press key 2** toggles playback
* **hold key 1, press key 3** randomizes everything

* **hold key 1, enc 1** rotate cat
* **hold key 1, enc 2** adjust auto rotation speed

* **enc 1** select cat

* **enc 2, enc 2** move cat

* **key 2** toggle cat on or off

* **key3** edit params for selected cat

* **params** here you can save / load your project, and change settings for the 4 internal synths, the delay and the 16 midi outs. 

## grid doc

* **playback [x: 16, y: 1]** - toggle playback
* **cat selection [x: 8-15, y: 1]** - found in a couple pages. click to select a cat, double click to turn a cat on or off, hold for more settings
* **petting zoo [x: 16, y: 2]** - cats are bright. click to select, click elsewhere to move. 
* **meowquencer [x: 16, y: 3]** - awake style sequencer on the left half.
	* x: 9, y: 8 - randomize the pattern
	* x: 10, y: 8 - shuffle the notes in the pattern
	* x: 9-15, y: 7 - change the octave
* **cat config [x: 16, y: 4]** 
	* x: 1 - 3, y: 1 - change between settings for "launch", "bounce", and "collision" physics events. 
	* x: 1, y: 3 - disable synth bangs for current mode
	* x: 1 - 4, y: 3 - synth selection for current mode
  * x: 1, y: 4 - disable midi bangs for current mode
  * x: 1 - 8, y: 4 - 5 - midi selection for current mode
  * right side, x: 9 - 15, y: 2 - 7 - change launch sync rate for every cat
  * bottom, x: 1 - 15, y: 8 - change the launch probability for currently selected cat
* **synths [x: 16, y: 5]**
	* x: 1 - 4, y: 1 - select which synth to edit
	* x: 6 - 13, y: 1 - change the synth algorithm
  * each row, y : 2 - 8 is a fader. click fader key to jump to a value, hold key to smoothly fade to a value
  * row 2 - amp
  * row 3 - pan
  * row 4 - mod1
  * row 5 - mod2
  * row 6 - cuttoff
  * row 7 - attack
  * row 8 - release
* **randomize [x: 16, y: 7]** - use to randomize the current page. double click to randomize the selected cat or synth, long hold to randomize all cats or synths. 
* **file io [x: 16 y: 8]** - use the two keys in the top left to change between save and load mode. press the other grid keys to save or load. this can be done during playback for fun & profit.

## cat personalities
each cat can have a different personality:
* **lively** - constantly spits furballs are a rhythmic rate
* **bipolar** - toggles on or off when hit by a furball. if on, spits furballs at a rhythmic rate, if off, does nothing
* **sleepy** - only spits furballs when hit by one, spends the rest of the time sleeping. when activated he/she meows loudly by spitting out 4 furballs in cardinal directions

## installation

**on maiden:**

```lua
;install https://github.com/Quixotic7/groovecats.git
;install https://github.com/catfact/thebangs.git
```

**on norns:**
system > reset then launch groovecats

## faq
**why?**
- I like making sequencers and I like cats.

**will there be grid 64 support?**
- maybe basic support for the petting zoo. 

## version notes
**v1.3.2**

- Added autoshuffle feature that automatically shuffles notes when the playhead is 1 on a launch event. 
- Added new cat personality, Ninja, that does not launch furballs, but still sends launch events.

**v1.3.1**

- added randomization features. shift[key 1] + key 2 to randomize all. grid[x: 16, y: 7] to randomize page. see updated documentation for details. 

**v1.2.1**

- bug fix, app would crash if velMin was greater than velMax

**v1.2**

- added further grid support with ability to change synth params and cat params from the grid. 
- added the ability to save and load projects.
- updated the UI a bit.

**v1.1** 
- added more support for the grid. Use the grid to select cats, toggle them on and off, move them, and view a lightshow.

**v1.0**
- initial release

[view on llllllll](https://llllllll.co/t/groovecats/)
[view on norns.community](https://norns.community/en/authors/quixotic7/groovecats)