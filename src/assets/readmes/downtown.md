## downtown

become an architect of sound.

![Image](https://user-images.githubusercontent.com/6550035/103465225-7859a380-4cee-11eb-981d-bc571d9b152d.png)

https://vimeo.com/496475138

view downtown over the skyline. build skyscrapers or tear them down to change the sounds coming from the city. record and mix in your sounds into the city and even build your own towers.

all cities are alike and all cities are different. like cities, this script welcomes change. the towers are built from supercollider tweets - you can [easily find more](https://twitter.com/search?q=SinOsc%20(%23supercollider%20OR%20%23sc%20OR%20%23sctweet)&src=typed_query&f=live) and then [add it as a new tower in the city](https://github.com/schollz/infinitedigits/tree/master/1#new-towers).

### Requirements

- norns

### Documentation

- K2 changes sample
- K3 toggles recording
- E2 changes modulator
- E3 modulates

this script is meant as "playground" to add little supercollider things and interact with them through softcut loops. the three softcut loops record in stereo and their length is dependent on the norns internal tempo. they are set to 16 beats, but this can be changed [within the script](https://github.com/schollz/downtown/blob/228e087d3c298c2fef9077438173ce77687db969/downtown.lua#L22) (restart to apply changes).

the supercollider things are represented as towers, accessible through E2 and E3 (although you could certainly tie them to grid / controllers). the towers are modulations for supercollider scripts running in the norns engine.

#### new towers

the engine has a bunch of different free-running supercollider scripts. its easy to add your own. if you want to add one, you can follow these five steps to make your own.

1. in `Engine_Downtown.sc`, add a `  var <synthX;` [at the top](https://github.com/schollz/downtown/blob/228e087d3c298c2fef9077438173ce77687db969/lib/Engine_Downtown.sc#L20) after `Engine_Downtown : CroneEngine {`, where `X` is whatever you want.
2. in `Engine_Downtown.sc`, define the `synthX`, using something similar to this:

```
synthX = {
    arg amp=0.0, amplag=0.02, hz=440;
    var amp_, snd;
    amp_ = Lag.ar(K2A.ar(amp), amplag);

    // define your beautiful sound here
    snd = SinOsc(hz); // or anything!

    snd
}.play(target: context.xg);
```

3. in `Engine_Downtown.sc`, create a command definition that can be used from within lua. a simple one that each could have is amplitude to change the levels or change frequencies.

```
this.addCommand("ampX", "f", { arg msg;
    synthX.set(\amp, msg[1]);
});
this.addCommand("hzX", "f", { arg msg;
    synthX.set(\hz, msg[1]);
});
```

4. in `Engine_Downtown.sc`, add `synthX.free;` at the bottom of the code.
5. in `downtown.lua` [add a new modulator](https://github.com/schollz/downtown/blob/228e087d3c298c2fef9077438173ce77687db969/downtown.lua#L27) that references the command definitions:

```lua
modulators = {  
  {name="my sound",engine="ampX",min=0,max=0.5}, // add a line for each thing to modulate
  {name="my sound freq",engine="hzX",min=0,max=0.5}, 
  ...
```

6. that's it! there will now be a new tower in the city with each parameter for your sound.

## license 

mit 