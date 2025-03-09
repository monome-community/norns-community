---
title: supertonic
description: an introspective drum machine.
published: true
date: 2021-05-31T18:06:19.309Z
tags: generative, drums
editor: markdown
dateCreated: 2021-05-31T17:38:27.648Z
---

# supertonic

![supertonic.png](/community/infinitedigits/supertonic.png)

an introspective drum machine that looks into itself and produces rhythm from its own self-examination.

https://vimeo.com/557258118

### introspection

this drum machine introspects by looking at any of the current drum patterns and generating a new drum pattern based specifically on that pattern and which instruments they are (e.g. a snare rhythm based on the kick pattern).

these generative rhythms are accomplished using [Google's "variational autoencoder"](https://github.com/magenta/magenta/tree/master/magenta/models/music_vae) for drum performances. [their blog post](https://magenta.tensorflow.org/groovae) explains it best (and [their paper](https://arxiv.org/pdf/1803.05428.pdf) explains it better), but essentially they had professional drummers play an electronic drum-set for 12+ hours which was later used to feed a special kind of neural network. I used their model from this network and sampled it randomly to produce "new" groups of drum rhythms (>~1,000,000 of them). then I created probability distributions from calculating bayesian probabilities from each instrument to each other instrument, within each rhythm grouping. this probability table can then generate a snare drum pattern based on a kick drum pattern, or generate a hihat pattern based on a snare drum pattern, etc. etc.


### sounds

the sounds for this drum machine come from a new engine which I call "supertonic" because it is a as-close-as-I-can port of the [microtonic VST by SonicCharge](https://soniccharge.com/microtonic). 

the act of porting is not straightforward and the experience itself was a motivation for this script - it helped me to learn how to use SuperCollider as I tried to match up sounds between the VST and SuperCollider using my ear. I learned there is a lot of beautiful magic in microtonic that makes it sounds wonderful, and I doubt I got half of the magic that's in the actual VST (so this is by no means a replacement). looking at the resulting engine you might notice some weird equations that are supposed to be approximating the magic behavior in the true microtonic. this script also includes a standalone SuperCollider drum machine to use with this engine (and conversion scripts to convert microtonic patches).

here is a [demo comparing microtonic and this engine](https://www.instagram.com/p/CPghuJUB2Of/?utm_source=ig_web_copy_link).

### drummer in a box

in the end, this script is a little drum machine in a box and also a new drum machine engine for norns, a little like @21echoes's [cyrene](https://norns.community/authors/21echoes/cyrene), @pangrus's [hachi](https://norns.community/authors/pangrus/hachi), or @justmat's [foulplay](https://norns.community/authors/justmat/foulplay). 

for me personally, this script is an experiment. to try to answer the question: what is it like to perform with an AI generated rhythm section (i.e. paralleling [what its like to play with a AI generated piano](https://github.com/schollz/pianoai))? is it good? surprisingly so, sometimes.

### Requirements

- norns

### Documentation

all the parameters for the engine are in the `PARAM` menu, as well as preset loading.

on the main screen:

- K2 starts/stops
- K3 toggles hit 
- E2 changes track (current is bright)
- E3 changes position in track

this script automatically detects all midi keyboards and will start/stop based on midi start/stop events.

you can hold K3 and move E2 to lay down a lot of beats.

**introspection** 

introspection requires downloading a prior table (~100 mb, not included in repo) and `sqlite3`. both of these can be installed by running this command in maiden:

```
os.execute("sudo apt install -y sqlite3; mkdir -p /home/we/dust/data/supertonic/; curl -L --progress-bar https://github.com/schollz/supertonic/releases/download/v1_ai/drum_ai_patterns.db > /home/we/dust/data/supertonic/drum_ai_patterns.db")
```

- hold K1, then press K3 to generate a new pattern based on the highlighted pattern
- hold K1 and turn E2 to change the highlighted pattern (basis of the generation)
- hold K1 and press K2 to generate beats 17-32 based on beats 1-16 for current instrument

**using your own microtonic presets**

if you have microtonic you can easily use your own microtonic preset. simply copy your microtonic preset file (something like `<name>.mtpreset`) and and save it into the `/home/we/dust/data/supertonic/presets` directory. then, you can then load these presets via the `PARAM > SUPERTONIC > preset` menu.

**converting microtonic presets for use with SuperCollider**

you can also use the engine directly with SuperCollider. the engine file is synced with a SuperCollider script, `lib/supertonic.scd`. an example drumset is in `lib/supertonic_drumset.scd`. you can easily get a SuperCollider file with your microtonic presets by running this lua script:

```
lua ~/dust/code/supertonic/lib/mtpreset2sc.lua /location/to/your/<name>.mtpreset ~/dust/data/supertonic/default.preset > presets.sc
```

**known bugs**

the supertonic engine is pretty cpu-intensive, so if you have 4-5 instruments all doing fast patterns (or fast tempo) you will hit cpu walls and hear crunching. any ideas to improve cpu usage are welcome :)

the pattern generation (k1+k3 or k1+k2) runs asynchronously but I've noticed that sometimes it might cause a little latency when using it while performing (generating patterns while playing).

if you aren't seeing any new randomly generate patterns when pressing K1+K3/K2, it could be that the pattern that you're using as a basis doesn't exist in the database (and therefore won't produce any new patterns).

**thanks**

the ex-dash patterning functions are from @license from the collaborative [song](https://github.com/northern-information/song/) project. the flying confetti is from @eigen's brilliant [pico-8 wrapper](https://llllllll.co/t/p8-pico-8-wrapper-lib/37947). also thanks @dan_derks, out little discussion helped me figure out the beginnings of this thing. finally, big big thanks to @midouest who shared their microtonic supercollider project which showed me some tricks I had missed and also showed me I was on the right track (because our implementations had a lot of parallels).

### Download

install via maiden or

```
;install https://github.com/schollz/supertonic
```

make sure to restart after installing because it includes a new engine.

https://github.com/schollz/supertonic

