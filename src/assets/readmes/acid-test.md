# acid test

generative acid basslines.

![acid-test](https://github.com/schollz/acid-test/raw/main/img/acid-test2.png)



lately I've been listening to acid house music and thinking about markov chains. previously I used markov chains to make a [jazz piano accompaniment](https://github.com/schollz/pianoai). it seemed to me that acid house basslines might be amenable to applying stateless logic for generating believable sequences. whether this results in "believable" acid music is up to you, but worth it for me to give it a try.

https://vimeo.com/670308126

this script started off as a literal "test" to do A/B explorations on different meta-parameters of the markov chains, but its too slow to sample parameter space by listening. so instead, I decided that the markov chains might be intuitive enough to edit directly, and I added controls to edit each individual markov chain. the output can be sent to midi, crow, or the builtin engine. the builtin engine is forked from [bernhard](https://sccode.org/bernhard)'s [sc code](https://sccode.org/1-5d8) which itself is forked from [by_otophilia's code](https://www.scribd.com/document/424490809/Acid-Otophilia) for a 303 emulator in SuperCollider.



## Requirements

- norns
- midi (optional)
- crow (optional)

## Documentation

### quick start

simply use K2 to generate/modify sequences.

- K2 modifies current sequence
- K3 toggles start/stop

you can have sequences modify themselves and evolve by changing the parameter `PARAMS > sequences > evolve`.

each time you generate/modify a sequence it will increase the number of modifications it makes (with a refractory period). each time you modify a sequence, it also creates a saved sequence which you can recall:

- K1+E1 selects saved sequence
- K1+K3 loads saved sequence

you can also manually edit notes in the sequence

- E2 selects a note
- E3 changes a note

### editing markov chains

sequences are generated based on the transition probabilities in the markov chains. you can edit these properties to create your own style of generative acid basslines.

to enter the markov-chain editing mode hit K1+K2. all controls are as follows:

- K1+K2 toggles markov chain editing mode
- E1 selects markov chain
- E2 selects transition
- E3 changes transition probability


this next part assumes a basic understanding of a markov chain. pretty much all you need to know can be learned by reading [these examples](https://en.wikipedia.org/wiki/Markov_chain#Examples). feel free to ask questions.

the generation of each step in a sequence is determined based on the states of 9 markov chains. the states of the markov chains change based on only the previous state (i.e. "memoryless"). each step in a sequence has similar properties to the 303 sequencer in that it has three parameters: a note, a slide toggle, and an accent toggle. each step in the sequence has these three parameters determined based on the state of a markov chain and discussed in detail below.

the transitions between the states of the markov chain are under your control. use E1 to select an markov chain property and use E2 to select a transition in that property. then use E3 to modify the probability of that transition. **the brighter the transition arrow, the higher the probability**. the combination of these 9 markov chains are then combined to generate the sequence.

#### accent

transitions between "no" and "yes". when the state of this markov chain is 'yes', then the velocity will be increased slightly for that note.

![accent](https://github.com/schollz/acid-test/raw/main/img/accent.png)

#### slide

transitions between "no" and "yes". when the state of this markov chain is 'yes', the portamento will be increased. for midi devices you can set the portamento cc in the `PARAMS > midi` section. for crow/engine output, the portamento is applied automatically through slew in the pitch.

![slide](https://github.com/schollz/acid-test/raw/main/img/slide.png)

#### bass or lead

in designing this sequencer I felt that I had to separate between "bass" and "lead" notes in the bassline - though technically the whole thing is a bassline, the "bass" notes typically being an octave below. I felt that acid basslines get part of the signature sound by oscillating between two intertwined melodies that are loosely mirrored across an octave. so there are separate markov chains for the "bass" and "lead", which are combined using this "bass or lead" property.

this property transitions between "bass" and "lead". the generator actually generates twice as many notes as requested - i.e. one entire set of bass notes and one entire set of lead notes. but will only select either based on the state of this property.

![bassorlead](https://github.com/schollz/acid-test/raw/main/img/bassorlead.png)

#### bass / lead coef+mult


the bass and lead parts each use two properties to generate a single note. the starting note of each sequence is the "base note" defined in the parameters. the base note is then increased by `coef x mult` at each step in the sequence where `coef` and `mult` are determined by the current state in both of those markov chains. for example, if the `coef` state is `2` and the `mult` is `-1` then the sequence will transition `-2` notes *in the scale*. the scale can be defined in the parameters.


![bassorlead](https://github.com/schollz/acid-test/raw/main/img/basscoef.png)

![bassorlead](https://github.com/schollz/acid-test/raw/main/img/bassmult.png)


the lead coef+mult works the same way as the bass coef+mult, but only affects the lead notes.

![bassorlead](https://github.com/schollz/acid-test/raw/main/img/leadcoef.png)

![bassorlead](https://github.com/schollz/acid-test/raw/main/img/leadmult.png)

#### bass / lead note

the legato of the note will be determined by the "bass note"  property (for bass notes) or the "lead note" property (for lead notes). if the state is "rest" then no note will be played, and any current note will be stopped. if the state is "new" then the current note will be stopped and a new note will be played. if the state is "hold" and the new note is the same as the last note, then there will be no gate, it will simply continue the note. if the new note is not the same and there is a slide, then portamento will be applied.

![bassnote](https://github.com/schollz/acid-test/raw/main/img/bassnote.png)

![leadnote](https://github.com/schollz/acid-test/raw/main/img/leadnote.png)

### crow

crow is supported. output 1 is pitch which will be slewed according to slides. output 2 is the gate (0-5v).

### midi

midi out can be selected in the parameters. you can also select the cc value for portamento (if your synthesizer allows it) as well as up to three LFOs that will be sent to the midi device via cc's (e.g. for filter / resonance / etc).

### saving/loading

save and load via the PSETs. saving and loading should save all the sequences that you've accumulated over time (i.e. saves are "collections" of all evolved sequences).

## Install

install using with

```
;install https://github.com/schollz/acid-test
```

