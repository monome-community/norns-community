---
title: drone zone 
description: first steps with supercollider and norns
published: true
date: 2021-03-21T21:08:31.354Z
tags: 
editor: markdown
dateCreated: 2021-03-21T01:58:52.663Z
---

# tone to drone in 60 seconds (a dronecaster tutorial)

the following is a tutorial to quickly get into supercollider and make a contribution to [dronecaster](https://llllllll.co/t/dronecaster/34737). i wrote this as reference for a future [norns study group meetup](https://llllllll.co/t/discord-norns-study-group/14233/35). 

## before you begin 

in this tutorial I will help you create your first drone in supercollider and add it to [dronecaster](https://llllllll.co/t/dronecaster/34737). before starting, make sure you have supercollider and plugins (if you want). also, if you'd like, you can get a github account to make the addition to the dronecaster script!

- [install supercollider](https://supercollider.github.io/download)
- [install supercollider plugins](https://supercollider.github.io/sc3-plugins/) (optional, but recommended) 
- [get access to norns from computer](https://monome.org/docs/norns/wifi-files/#transfer)
- [get a github account](https://github.com)

if you have these basic things installed, you are good to go. everything else will be explained (including how to use supercollider, how to use git, etc.). however, if you are wanting to make a contribution i'm assuming you are okay using a terminal.

## [supercollider tutorial] five steps to get in the drone zone

okay, we'll start with supercollider. we'll go from tone to drone in just five steps. we are going to make the drone called "Gristle", a primal sawtooth drone:

<audio preload="metadata" controls="">
    <source src="https://llllllll.co/uploads/default/original/3X/c/7/c7485797a851549ce9cda46f0706a14e74c5ed40.wav">
</audio>
  
### 1. the tone

first open supercollider and "boot the server" by selecting `Server -> Boot Server` from the menu. 

now paste the following code as the starting drone. this drone is simply a C2 sine wave (C2 = 65.41 hz). 

```supercollider
(
x = SynthDef("basic",
{
	arg hz=65.41, amp=0.5, amplag=0.02,hzlag=0.02;
	var amp_,hz_,sig;
	amp_ = Lag.ar(K2A.ar(amp),amplag);
	hz_ = Lag.ar(K2A.ar(hz),hzlag);

	// << the drone zone >>
	sig = SinOsc.ar(
			freq:hz_,
			mul:amp_,
	);
	// << end drone zone >>

	sig = Splay.ar(sig);
	Out.ar(0,sig); // this line is not needed for adding to dronecaster
}
).play;
)
```


<audio preload="metadata" controls="">
    <source src="https://llllllll.co/uploads/default/original/3X/e/5/e5e995d15e5603e022a5eaf1c6473cf013ae20f9.wav">
</audio>
  

the actual drone code is found in "`<< the drone zone >>`", the rest is code that is useful for integrating into norns. you need not worry about that. for now, we'll work with only the code in "`<< the drone zone >>`".

to run this code, click your cursor anywhere in the code and press `Ctl+<enter>`. this runs all the code between the first and last parentheses. you should hear a very low sound (maybe use headphones to hear it!).

to stop it just press `Ctl+<period>`.

another cool trick is that you can change things while its playing, for instance we can change the frequency and volume (use `Ctl+Enter` to run each line).

```
x.set("hz",65.41*2); // up can octave
x.set("amp",0.01); // volume down
```

the reason this works is that we defined the drone into the `x` variable and defined arguments (see the line "`arg hz=65.41, amp=0.5;`").

### 2. add overtones

now lets make it less boring with overtones. overtones are multiples of fundamental at lower volumes. when dealing with multiple anything, its useful to make an "array". you can define all sorts of arrays in supercollider, for example here's an array of powers of 2:

```supercollider
Array.fill(3,{arg i; 2**i}).postln
// -> [ 1.0, 2.0, 4.0 ]
```

we can use that array as the frequency in the `SinOsc` oscillator so it will automatically make 3 oscillators, each frequency doubled. we can multiply that array by the fundamental to scale the frequencies.

```supercollider
(
x = SynthDef("basic_w_overtones",
{
	arg hz=65.41, amp=0.5, amplag=0.02,hzlag=0.02;
	var amp_,hz_,sig;
	amp_ = Lag.ar(K2A.ar(amp),amplag);
	hz_ = Lag.ar(K2A.ar(hz),hzlag);

	// << the drone zone >>
	sig = Mix.ar(
		SinOsc.ar(
			freq:hz_*Array.fill(3,{arg i; 2**i}),
			mul:amp_*Array.fill(3,{arg i;(1/2)**i}),
		)
	);
	// << end drone zone >>

	sig = Splay.ar(sig);
	Out.ar(0,sig); // this line is not needed for adding to dronecaster
}
).play;
)
```

<audio preload="metadata" controls="">
    <source src="https://llllllll.co/uploads/default/original/3X/d/2/d25f4a45ddba5c5e4a2630a58535035a99f517d9.wav">
</audio>

similarly, i added in a array for the volume (`mul`) which scales each oscillator. also i wrapped the `SinOsc` inside `Mix.ar` which simply "mixes" the signals by adding them up so that you get a single signal.

### 3. different oscillators!

Sine waves are nice, but there are lots of different oscillators we can use. we can swap out `SinOsc` (sine wave) for `VarSaw` (sawtooth), `SinOscFB` (sine w/ feedback), `Pulse`, or many others. here i've opted for the saw wave:

```supercollider
(
x = SynthDef("basic_w_overtones_varsaw",
{
	arg hz=65.41, amp=0.5, amplag=0.02,hzlag=0.02;
	var amp_,hz_,sig;
	amp_ = Lag.ar(K2A.ar(amp),amplag);
	hz_ = Lag.ar(K2A.ar(hz),hzlag);

	// << the drone zone >>
	sig = Mix.ar(
		VarSaw.ar(
			freq:hz_*Array.fill(3,{arg i; 2**i}),
			mul:amp_*Array.fill(3,{arg i;(1/2)**i}),
		)
	);
	// << end drone zone >>

	sig = Splay.ar(sig);
	Out.ar(0,sig); // this line is not needed for adding to dronecaster
}
).play;
)
```

<audio preload="metadata" controls="">
    <source src="https://llllllll.co/uploads/default/original/3X/7/c/7cb8a878498fa2995d1804bdcd52a8c374bb2344.wav">
</audio>


try other oscillators! see what happens.

### 4. add modulation

modulation will bring in organic wavering to the drone. there are many ways to do this, but my favorite is to use a randomly oscillating sine wave with a long period.

we can get randomness by using the `LFnoise`:

```supercollider
{LFNoise0.kr(10)}.plot(1)
```

![lfnoise1|402x332](https://llllllll.co/uploads/default/original/3X/7/5/75142f84692281128a8c0d5600e99d946b4ea898.png) 

then we can make a sine wave which uses that stepped noise as its frequency:

```supercollider
{SinOsc.kr(LFNoise0.kr(2)*4)}.plot(4)
```

![sin-lfnoise|402x332](https://llllllll.co/uploads/default/original/3X/5/e/5eeab15a7391b4dac849a15f54dd0df240d1300f.png) 

the sine wave naturally has values between -1 and 1, so we might need to change that. its easy to change to any range you want with `LinLin`. here i can change it to 0-100:

```supercollider
{LinLin.kr(SinOsc.kr(LFNoise0.kr(1)),-1,1,0,100)}.plot(4)
```

great, now throw those into the drone to modulate the frequencies of the oscillators by a fraction of the frequency:

```supercollider
(
x = SynthDef("basic_w_overtones_varsaw_modulation",
{
	arg hz=65.41, amp=0.5, amplag=0.02,hzlag=0.02;
	var amp_,hz_,sig;
	amp_ = Lag.ar(K2A.ar(amp),amplag);
	hz_ = Lag.ar(K2A.ar(hz),hzlag);

	// << the drone zone >>
	sig = Mix.ar(
		VarSaw.ar(
			freq:hz_*Array.fill(3,{arg i;
					2**i *
					LinLin.kr(SinOsc.kr(LFNoise0.kr(1)),-1,1,0.99,1.01)
			}),
			mul:amp_*Array.fill(3,{arg i;(1/2)**i}),
		)
	);
	// << end drone zone >>

	sig = Splay.ar(sig);
	Out.ar(0,sig); // this line is not needed for adding to dronecaster
}
).play;
)
```

<audio preload="metadata" controls="">
    <source src="https://llllllll.co/uploads/default/original/3X/4/7/47011a30bb07b001188fb48d5b8b263c1e5e9d07.wav">
</audio>


sounding good, but we can get better with one more step.

### 5. add filter + effects

filters and effects go a long way. there are lots of filters available: `BPF` (band pass), `LPF` (low pass), `MoogFF` (Moog VCF), `HPF` (high pass), to name a few. there are also some nice effects available like `FreeVerb` and `Greyhole` (extensions needed for latter). lets add these in.

here's i've added a band-pass filter modulated by the mouse and a Greyhole delay modulated by the mouse.

```supercollider
(
x = SynthDef("basic_w_overtones_varsaw_modulation_filtereffects",
{
	arg hz=65.41, amp=0.5, amplag=0.02,hzlag=0.02;
	var amp_,hz_,sig;
	amp_ = Lag.ar(K2A.ar(amp),amplag);
	hz_ = Lag.ar(K2A.ar(hz),hzlag);

	// << the drone zone >>
	sig = Mix.ar(
			VarSaw.ar(
			freq:hz_*Array.fill(3,{arg i;
					2**i *
					LinLin.kr(SinOsc.kr(LFNoise0.kr(1)),-1,1,0.99,1.01)
			}),
			mul:amp_*Array.fill(3,{arg i;(1/2)**i}),
		)
	);
	sig = BPF.ar(sig,
			MouseX.kr(80,2000)
	);
	sig = Greyhole.ar(sig,delayTime:MouseY.kr(0.1,0.4));
	// << end drone zone >>

	sig = Splay.ar(sig);
	Out.ar(0,sig); // this line is not needed for adding to dronecaster
}
).play;
)
```

<audio preload="metadata" controls="">
    <source src="https://llllllll.co/uploads/default/original/3X/c/7/c7485797a851549ce9cda46f0706a14e74c5ed40.wav">
</audio>


another trick when adding something is to use your mouse to play with parameters. we can do that here. simply change one of the parameters to `MouseX.kr` or `MouseY.kr` and moving your mouse will change that parameter.

you have entered the *drone zone*! 

in the next part of the tutorial we can add this drone to dronecaster.

---

## [norns] adding a drone to dronecaster

now we will take the drone and add it to dronecaster/

### fork dronecaster

lets first start by *forking* dronecaster and *cloning* it to our norns.

goto  the dronecaster webpage: https://github.com/northern-information/dronecaster

click the fork button. that's it! now you have a copy of dronecaster you can create or destroy as you wish.

now ssh into your norns (click [here](https://monome.org/docs/norns/wifi-files/#ssh) for help with that). from here we will need to use a terminal. 

to put your copy of dronecaster on your norns, first remove a previous copy by typing into the terminal:

```
rm -rf ~/dust/code/dronecaster
```

now clone your copy using (making sure to change with your user github name):

```
git clone https://github.com/<your github user name>/dronecaster ~/dust/code/dronecaster
```

### add your drone

now you can edit the dronecaster code. the easiest way to do this is to mount the norns files on your computer and edit them as you would normally. click [here](https://monome.org/docs/norns/wifi-files/#transfer) for instructions on how to get your Mac or Windows computer to open up the norns drive.

once you have the norns drive on your computer, goto the `dust/code/dronecaster` folder. from here, goto the `engines -> drones` folder. now make a new drone - a file called `<your name>.scd`. open up that file and paste the following:


```
// @yourname
// your drone name
// how does your drone describe itself

{
    arg hz=440, amp=0.02, amplag=0.02, hzlag=0.01;
    var amp_, hz_, sig;
    amp_ = Lag.ar(K2A.ar(amp), amplag);
    hz_ = Lag.ar(K2A.ar(hz), hzlag);

    // << the drone zone >>
    // replace with your drone zone!
    // << end drone zone >>

}
```

replace the part in the middle with your "`<< the drone zone >>`" code.

make sure to not use `MouseX` or `MouseY` when putting your drone in, as the norns doesn't (yet) have mouse support.

to listen to your drone, just load up dronecaster and use E1 to find your drone. cast away!

### push the drone

lets share your drone! the following instructions will take you through the steps to send your drone code back to the original repository so that everyone can share in the glory of your drone.

back in the terminal, go to the dronecaster repositor.

```
cd ~/dust/code/dronecaster
```

now add the new drone to the `git` repository and commit it.

```
git add .
git commit -am "added <your drone name>"
git push
```

great, now you've uploaded your new code to the Github cloud. to finish up the share, goto your code's website: `https://github.com/<yourname>/dronecaster`. click "Pull request" and then on the next page click "Create pull request".

that's it! give it time for Tyler to merge it.

now that you know this, *what drone will you make?*