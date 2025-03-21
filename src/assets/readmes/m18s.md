## m18s

### a sequencer for norns based on the RYK M-185

m18s is a two voice sequencer.  each voice is 8 steps, and each step is made up of 1-8 stages.

stages trigger notes based on the particular stage gate mode.  these can be:
- “off”: don’t trigger any gates during the step
- “single”: only trigger a gate for the first stage of the step
- “all”: trigger a gate for every stage of the step
- “every2”: trigger a gate every other stage
- “every3”: trigger a gate every 3rd stage
- “every4”: trigger a gate every 4th stage
- “random”: 50% chance you trigger a gate for each stage
- “long”: gate should go high on stage 1 and low on the last stage. If the step is 1 stage long, just do a standard gate pulse

in the current version of m18s, you can change the sequence by randomizing the stages, stage gate modes, and note (specified by the scale in the params menu).  in the future these will be able to be set within the norns interface.

you can download and run m18s from the maiden package manager or by cloning/downloading this repo and moving to dust/code.  it currently uses the PolySub engine to generate sound found in the we standard community library that norns is packaged with.

### crow standalone version:

this started as a script built for crow, but because it was not very fun to use (and the size of the script caused some weirdness with some people's crows), I decided to port to norns.  I've moved the original script to the lib/crow_standalone/

to run this:
- clone or download this repo
- install druid (`pip3 install monome-druid`)
- open a new shell, cd to `<repo_location>/lib/crow_standalone`, and run `druid` 
- type `r m18s.lua` to run the script

see https://llllllll.co/t/m18s-updating-somehow-the-post-accidentally-published-early/32068 for documentation and to share anything you make with m18s or any feature requests you have, I'd love to hear it!
