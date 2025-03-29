# Tidbit

Use Just Friends or a MIDI device as a 'melodic' granular synth.

![tidbit](doc/tidbit.png)

See a video of Tidbit in action, using JF:
https://vimeo.com/668942592/96eb5f63ae

Discussion on the llllllll.co forum: https://llllllll.co/t/tidbit

# What is Tidbit?
Tidbit uses either Norns, Crow and JF (or W/) or MIDI to create granular notes - addressing the device in a very rapid way as to use the absolute most of JFs six voices or a MIDI device to create everything from rich sound beds to short scrapy percussive sounds. It applies the long history of granular synthesis to the six voices of Just Friends or a MIDI device, starting from Democritus' atom theory all the way to Curtis Roads' writings on Microsound and beyond.

You curate four sets of five notes, or- randomise them in the PARAMS menu. Now, you can modulate the sound parameters on JF, skipping through different note-sets with E3 and divisions with E2. On MIDI devices Tidbit relies on voice stealing.

See another short demo from an earlier version a while back [here](https://vimeo.com/663336524/55a05fcd1f).

# Installation
 1. Install via maiden or clone/download the repo to `dust/code`.
 2. Restart norns.
 3. Start Tidbit!

# Requirements
Norns and either Crow and Just Friends, or a MIDI device.
Optional: W/

# Todo
* randomisation of wsyn params per grain would be cool
* A working internal engine so it does not need anything external
* a more beautiful visualisation (seems broken rn?)
* amplitudes should start at 1 (or at least half of them per chord)
* check the range of the notes (seemed to be able to go lower first when it was still numerical)
* dynamic amount of notes/note sets?
make a “spread” param that can detune every note by a random amount
* set Crow inputs to determine noteset/division!
* make a “slow ambient mode”, in which I maybe read out ‘cycle’ state, or can trigger with K3 or something. Slow moving partial-mode ish. Have to think this through.

# Contribute
PR's welcome!