# TimeParty

Delay/FX sequencer for monome norns/grid (crow optional)

---

TimeParty is a delay effect with 7 step sequencers that each modulate a different parameter of the feedback path.

Each sequencer has an independent loop length, clock division, and direction ("forward", "reverse", "random", or "drunk"), 
as well as a "shift" parameter which can be used to update the range of modulation values associated with the grid y positions.
For example, shift can be used to speed up the overall delay time, or fine tune the feedback amount.

* **Encoder 2** - change sequence/page
* **Encoder 3** - change sequencer parameter value
* **Key 3** - select new parameter value
* **Key 2** - freeze buffer

### Sequencers

1. _Time_  - delay time
2. _Rate_ - also delay time, but with pitch shifting effects. Rate modulation values are set to "perfect" musical intervals 
(1, 4 and 5) by default, which correspond with both more "musical" delay times and more consonant pitch shifting, 
but can also be changed to "major" or "minor" scale modes via the parameters menu.
3. _Feedback_ 
4. _Autopan_ - autopan rate. Available thanks to the [hnds](https://github.com/justmat/otis/blob/master/lib/hnds.lua) Lua LFO library from @justmat. Change LFO waveform and depth via the parameters menu.
5. _Reverb_ - Norns softcut reverb level
6. _FilterCut_ - Filter cutoff. Uses low pass by default, but can dial in band pass, high pass, and filter Q levels via 
the parameters menu.
7. _Position_ - the only sequencer that is off by default, since it can mess with more "normal" sounding delay effects. 
It can be fun to play with after freezing the buffer, or for more glitchy delay sounds.

### Crow

Crow inputs 1 and 2 are configurable via the parameters menu. Both accept triggers to toggle freezing or reversing the buffer. 

Input 2 can be set to "trigger step," which will cause the sequencer to advance steps on each incoming pulse. This will override your 
global clock source if it is set to "crow." Global clock will still sync the delay time, but will no longer advance the sequencer. This 
behavior enables you to advance the sequencer with an irregular clock, while still tempo syncing your delay to a master tempo. 
