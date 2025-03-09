<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/1-1-0-start.png" />

# krill

a [Lorenz system](https://en.wikipedia.org/wiki/Lorenz_system) sequencer and mod matrix running @okyeron's UGen linux port of Mutable Instruments Rings for monome norns.

## requirements

* norns (required)
* crow, W/, Just Friends, midi (optional)
* audio input to excite the MIRings engine (optional)

## installation

the install process requires three steps to properly install:

1. open maiden and below the "matron" tab, enter:

    `;install https://github.com/jaseknighter/krill`

2. in the same "matron" tab install the MIRings UGen with this command:

```
os.execute("wget -T 180 -q -P /tmp/ https://github.com/okyeron/mi-UGens/raw/master/linux-norns-binaries/mi-UGens-linux-v.03.tar && tar -xvf /tmp/mi-UGens-linux-v.03.tar -C /tmp && cp -r /tmp/mi-UGens-linux-v.03/* /home/we/.local/share/SuperCollider/Extensions/ && rm -r /tmp/mi-UGens-linux-v.03 && rm -r /tmp/mi-UGens-linux-v.03.tar")
```
   

note: you may skip step 2 above if you previously installed the MIRings UGen with either @okyeron's [MI-UGens for Norns](https://llllllll.co/t/mi-ugens-for-norns/31781) or the resonator pedal that is part of @21echoes' [Pedalboard](https://llllllll.co/t/pedalboard-chainable-fx-for-norns/31119).

3. restart your norns.

  
## about the script
the idea for the script and its name came from @mattallison and is inspired by [Todd Barton's Krell patch](https://vimeo.com/48382205). this script's use of a chaotic Lorenz system algorithm differentiates it from the classic Krell patch. in theory at least, using chaos instead of randomness produces patterns that reside in a space between the random and the predictable. 

## krill studies for beginner scripters
i have created a [study](krill_study1.md) to accomany the krill script. the study includes notes and simple code that can be run in maiden's matron REPL. it relates to a problem (one of many) i had to solve while putting this script together. i hope it is informative and useful for folks interested in learning more about coding on the norns platform.


## credits

bunches and bunchs of credit are due to Matt Allison and SPIKE the Percussionist. i am deeply grateful to the two of them for working with me over many hours and days testing and discussing the script. 

additional thanks and credits go out to:

* @helen for very patiently working with me to get the installation instructions working
* @whimsicalraps for publishing a Lorenz algorithm in Lua as part of the [crow bowery](https://github.com/monome/bowery/blob/3dd5c520c6ea401db5e1b01e0bddae396da4ed53/Lorenz.lua)
* @okyeron for creating a linux version of Volker Bohm's (@geplanteobsoleszenz) SuperCollider port of the MI modules
* @geplanteobsoleszenz for porting the MI modules to SuperCollider
* @pichenettes for creating the MI Rings module for eurorack
* @midouest for developing a [really splendid SuperCollider envelope](https://llllllll.co/t/supercollider-tips-q-a/3185/371) that captures rise and fall as individual events
* @justmat for creating lua lfo's which i borrowed from his [otis script](https://github.com/justmat/otis)
* @tyleretters for creating the lattice module and porting @whimsicalraps's sequins module to norns


## caution!!!
the mod matrix built into the krill script allows any parameter to modulate any other parameter. unexpected results may result (e.g. when modulating the compressor's gain settings), so please proceed with care and caution when using this feature.

## documentation

### views
the krill script has two basic views:

* sequencer view
* mod matrix view

use k1+e1 to navigate between views.

### sequencer
<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/1-2-0-start_w_grid.png" width="500" />
the sequencer view is divided into three UI sections (from left to right):

1. controls 
2. Lorenz system visualization
3. Lorenz x/y and lfos

#### encoder and key controls
e1/e2/e3 are used to navigate the controls section. 

all of the UI controls found in the sequencer view are also found in the main norns params menu (PARAMETERS>EDIT).

when changing numerical values, k2+e3 can be used to change values faster by a factor of 10.

**notes on the grid overlay** 
- when the script is first loaded, just the second and third UI sections are visible. when an encoder is turned, the first section becomes temporarily visible, along with a grid overlaying the Lorenz system visualization. 

to make the grid overlay and UI controls section always visible after the script has been loaded, there is a PARAMETER called `grid display` in the main norns params menu (PARAMETERS>EDIT) that can be set to `always show`. 

alternatively, to make grid overlay and UI controls section always visible every time the script is loaded, open the */lib/globals.lua* file and change the value of the `UI_DISPLAY_DEFAULT` variable to `3`.

#### sequencer menus
<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/1-2-1-menus.png" width="500" />

five menus are available from the sequencer view:

* *seq* (sequencer controls)
* *scr* (Lorenz system visualization controls)
* *lrz* (Lorenz system algorithm controls)
* *lfo* (lfo controls)
* *eng* (MI Rings SuperCollider engine controls)

use e1 to switch between sequencer menus. 

#### *seq* (sequencer controls)
<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/1-2-2-menus-seq.png" width="500" />

  the notes generated by the krill script are based on the underlying Lorenz system algorithm. notes are selected by visualizing the algorithm and overlaying a grid on top of the visualization. 
  
  the grid is subdivided by note/octave to determine pitch, which is sent to the internal krill SuperCollider engine and/or the other supported outputs (midi, crow, Just Friends, and W/).

  there are two sequencer modes: *krell* and *vuja de*

  by default, when the script first loads, the *vuja de* sequencer is running.

- *krell* sequencer

  the krell sequencer is modelled after Todd Barton's Krell script. the vuja de sequencer is modelled after MI Marbles eurorack module. new notes are generated in the krell mode based on the rise and fall of an envelope built into the krell script's SuperCollider engine.

  when the krell sequencer is active, seven parameters are accessible from the main UI's *seq* menu:

  1. *seq mode* (sequencing mode): switch between the two sequencing modes
  2. *env sclr* (envelope scalar): scale the rise and fall time of the SuperCollider engine's envelope proportionally
  3. *rise(ms)* (rise time): envelope rise time
  4. *fall (ms)* (fall time): envelope fall time
  5. *env level* (envelope level): envelope amplitude
  6. *env shp* (envelope shape): envelope shape (smaller values create pluckier envelopes)
  7. *num octs* (# octaves): the number of octaves available to sequence

- *vuja de* sequencer

  the vuja de sequencer is structured as a set of patterns (up to six) built using the norns [lattice](https://monome.org/docs/norns/reference/lib/lattice) and [sequins](https://monome.org/docs/norns/reference/lib/sequins) modules. 

  when the vuja de sequencer is active the seven parameters listed above are accessible from the main UI's *seq* menu. 

  in addition to the seven parameters listed above, there are three additional controls on the main UI's *seq* menu specific to the vuja de sequencer: 

  8. *loop len* (loop length): the length of each pattern (1-8 steps)
  9. *vuja_de_prob* (vuja de probability): the probability that a new note will be selected for the active step
  10. *vjd div[1-6]* (vuja de pattern divisions): sets a default division of the 1-6 enabled patterns. by default each pattern has the same set of default divisions: 1,1/2,1/4,1/8,1/16,1/32,1/64

      note: the default divisions (*vjd div[1-6]*) can be modified for each of the 6 available patterns by editing a variable found in `/lib/globals.lua` called `VJD_PAT_DEFAULT_DIVS`. custom divisions may also be set while the script is running (see *division patterns* in the **sequencer param listing** below)

  - **other sequencer params**

    additional sequencer params may be found in the main norns PARAMETERS>EDIT menu: 

    ***SCALES+NOTES* section**: param settings related to scale, quantization, and number of octaves. this section of the params menu also displays the active note of the sequencer 

    ***VUJA DE* section**:  *vjd num divs* *: sets the number of active patterns (1-6)

    ****div pat assignments* sub-menu***:  the outputs available to the script (krill SuperCollider engine, midi, crow, W/, and Just Friends) may be assigned to up to two of the vuja de division patterns. 

    *** *division pattern[1-6]* sub-menu ***
    * *vjd divX*: same as the *vjd div[1-6]* referenced above
    * *vjd div numX*: sets a custom numerator for the pattern's division
    * *vjd div denX*: sets a custom denominator for the pattern's division
    * *vjd jitterX*: sets a positive or negative jitter to the pattern division
    * *vjd oct offset*: offsets the octave of the notes played by this pattern
  
    *** *rthm patterns[1-6]* sub-menu ***
    each pattern contains three rhythms that are defined as 8-step cellular automata patterns

     * *active rthm patX*: sets which of the three rhythm patterns are active
     * *vjd rthm stepX*: change the step size of the rhythm patterns from default 1 to 8
     * *vjd rthm patX-X*: sets the 3 rhythms to one of 256 patterns
     * *vjd rthm activeX*: indicates whether the selected rhythm is active. note, this "read only" param will only indicate a selected rhythm is active if the sequence mode (*seq mode*) is set to *vuja de*.

##### *scr* (Lorenz system visualization controls)
<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/1-2-3-menus-scr.png" width="500" />

  the *scr* (screen) sub-menu's params control how the Lorenz system is displayed, which effects sequence generation:

- *x/y input***
  the Lorenz system algorithm outputs three values: *first*, *second* and *third*. the *x input* and *y input* params are used to assign two of the three Lorenz system output values to x/y coordinates and visualize the algorithm. changing the x input and y input assignments will change the shape of the visualization.

  as mentioned above, a grid is placed on top of the Lorenz system visualization which is subdivided by note and octave to set the pitch each time the sequencer plays a note.

- ***x/y offset***
  the *x offset* and *y offset* params move the Lorenz system visualization horizontally and vertically relative to the note/octave grid. this changes the pitches generated by the krill and vija de sequencers. setting these parameters to lower values will tend to lower the pitch of the notes and setting them to higher values will tend to increase the pitch of the notes.

- ***x/y scale***
  *x scale* and *y scale* changes the width and height of the Lorenz system visualization. 

  an increase to the x scale will tend to generate pitches across more notes and a decrease will tend to generate pitches of across fewer notes.

  an increase to the y scale will tend to generate pitches across more octaves and a decrease will tend to generate pitches of across fewer octaves.

  the *scr* params described above are found in the main norns PARAMETERS>EDIT menu under the *LORENZ* menu separator in the *Lorenz view* sub-menu.

- **Lorenz x/y output**
  controls for sending Lorenz x/y values to crow and midi are found in the main norns PARAMETERS>EDIT menu under the *MODULATION* menu separator in the *Lorenz x/y outputs* sub-menu. 


##### *lrz* (Lorenz system algorithm controls)
  the *lrz* (Lorenz system algorithm) sub-menu's params set a number of the Lorenz system's parameters, effecting how it behaves and gets displayed, which subsequently effects sequence generation. 

  the *lz speed* param changes how fast the algorithm changes. the other params will effect the algorthm in other ways that i don't really understand well enough to describe, but they are worth exploring and are generally "safe" to use (unlike some of the other params mentioned below).

- **additional *lrz* (Lorenz algorithm) params**
  the *lrz* params described above are found in the main norns PARAMETERS>EDIT menu under the *LORENZ* menu separator in the *Lorenz params* sub-menu.

  there are additional params related to the Lorenz system algorithm in the *Lorenz params* and *Lorenz weights* sub-menus. these additional paramschange a variety of settings for the Lorenz system algorithm. 

  *USE CAUTION* when changing the params in these two sub-menus as unexpected results may occur that sometimes cause the Lorenz system algorithm visualization to disappear and when this happens the sequencer tends to stop playing, requiring a restart of the script. 

##### *lfo* (lfo controls)
<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/1-2-5-menus-lfo.png" width="500" />
  the *lfo* sub-menu's params control two lfos:

  * *lfo*: turns the lfo on and off
  * *shape*: sets the lfo to a sine shape, a square shape, or a Sample and Hold random value generator
  * *depth*: scales the values generated by the lfo
  * *offset*: offsets the values generatored by the lfo
  * *freq*: sets the speed of the lfo

- **additional *lfo* params**
  the *lfo* params described above are found in the main norns PARAMETERS>EDIT menu under the *MODULATION* menu separator along with parameters to set how lfo values are sent to crow and midi.

  the crow parameters in this sub-menu set slew and params to scale the lfos output values to a min and max voltage.

  the midi parameters in this sub-menu set the cc and channel values to be used with the lfo as well as turn the midi version of the lfo on and off.

  finally, the read-only *lfo value* param displays the current value of the lfo.

##### *eng* (MI Rings SuperCollider engine controls)
<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/1-2-6-menus-eng.png" width="500" />
  the *eng* sub-menu's params control the settings for the MI Rings SuperCollider engine:

  * mode controls
    * *egg mode*: setting egg mode to 1 enables the Rings easter egg, inspired by the Roland RS-09 and disasterpeace
    * *eng mode*: sets the resonator model to one of 6 modes: 
      ** *res*: resonator
      ** *sstr*: sympathetic string
      ** *mstr*: modulated/inharmonic string
      ** *fm*: 2-op fm voice
      ** *sstrq*: sympathetic string quantized
      ** *strr*: string and reverb
    * *eng mode* (egg mode): sets the 'model' to one of 6 modes: 
      ** *for*: formant
      ** *chor*: chorus
      ** *rev*: reverb
      ** *for2*: formant 2
      ** *ens*: ensemble
      ** *rev2*: chorus 2
      * *trig type*: sets excitation signal to *internal* or *external.* if set to external, an audio signal is required from the norns audio input jack(s)
  * slew controls
    * *freq slew*: sets a slew value for the pitch of notes played by the SuperCollider engine
    * *fslw enbl* (frequency slew enable): enables/disables frequency slew
  * model controls
    * *pos* (position): specifies the position where the model's structure is excited
    * *str* (structure base): with the modal and non-linear string models, controls the inharmonicity of the spectrum (which directly impacts the perceived “material”); with the sympathetic strings model, controls the intervals between strings.
    * *str rng*: sets a range that the value of the structure base param above will modulate around 
    * *brt* (brightness base): specifies the brightness and richness of the spectrum
    * *brt rng*: sets a range that the value of the brightness base param above will modulate around
    * *dmp* (damping): controls the damping rate of the sound, from 100ms to 10s
    * *dmp rng*: sets a range that the value of the damping base param above will modulate around. 
    * *poly* (polyphony): number of simultaneous voices (1 -- 4) - this also influences the number of partials generated per voice. more voices mean less partials.

    the *eng* params described above are also found in the main norns PARAMETERS>EDIT menu in the *rings* sub-menu. 

    the above parameter descriptions are copied with gratitude from @geplanteobsoleszenz SuperCollider help documentation.

### mod matrix
<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/2-1-0.png" width="500" />
the mod matrix allows any parameter to be used to modulate any other parameter. 

the mod matrix UI is divided into four sections:

a. menu name<br>
b. control parameters<br>
c. input output labels and values<br>
d. patchpoints<br>

#### encoder and key controls
use k1+e1 to switch to the mod matrix view.

when changing numerical values, k2+e3 can be used to change values faster by a factor of 10.

#### data management
mod matrix settings are saved at the end of each krill session. multiple mod matrix configurations can also be saved. see the *DATA MANAGEMENT* section below for additional details.

#### mod matrix menus
<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/2-1-1-start.png" width="500" />

the mod matrix has 5 menus:

* *row/col* (patchpoint navigator)
* *in/out* (input/output selection)
* *pp opt* (patchpoint options)
* *crow* (crow output settings)
* *midi* (midi output settings)

use e1 to switch between mod matrix menus.

#### *row/col* (patchpoint navigator)
<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/2-2-1-row-col.png" width="500" />
  e2/e3 navigates the patchpoint matrix. on all mod matrix screens, k1+e2 and k1+e3 are used to navigate the patchpoint matrix.
  
  the patchpoint circles indicate the state of each patchpoint:
  * dimly lit:  disabled
  * with a dot in the middle: the patchpoint is selected for editing
  * brightly lit: patchpoint is enabled
  * left half of circle filled: an input is defined for the patchpoint
  * right half of circle filled: an output is defined for the patchpoint
  *  circle completely filled: an input and output is defined for the patchpoint 
  
#### *in/out* (input/output selection)
<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/2-2-2-in-out.png" width="500" />

  e2/e3 selects the inputs/outputs for the selected row/column of the matrix.

  k1+e2 and k+e3 display parameter folders names for fast navigation between the various sections found in the main norns params menu (PARAMETERS>EDIT).

  matrix rows (a-d) represent inputs. matrix columns (1-7) represent outputs.

  changing a patchpoint's input or output will disable all the patchpoints in the selected row/column.
  
  a value with carrots at the front and end (e.g. "<<Lorenz view>>") indicates a param sub-menu.

  a value with dashes at the front and end (e.g. "--LORENZ--") indicates a param separator.

  the input and output for the row/column of the selected patchpoint can be cleared by pressing k2 + k3.

#### *pp opt* (patchpoint options)
<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/2-2-3-pp-opt.png" width="500" />

  the patchpoint options menu updates three controls for the selected patchpoint:

  * *enbl* (enable): enables modulation of the output by the input (assuming they have been set for the selected patchpoint)
  * *lvl* (level) the value of the patchpoint output is multiplied by the lvl value. setting lvl to 0 is the same as setting the patchpoint's enbl value to off.
  * *lvlr* (level range): adds a positive or negative random value between 0 and the lvlr value. if lvlr is set to 0, nothing will be added.

  e2 selects the patchpoint option controls. e3 updates them.
  

#### *crow* (crow output settings)
<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/2-2-4-crow.png" width="500" />

  there are three crow controls for the selected patchpoint:

  * *enbl* (crow enable): sends the patchpont's modulation to crow
  * *out* (crow out): selects which crow output to send voltages for the selected patchpoint
  * *slew* (crow slew): tells crow to slew the voltages it sends for the selected patchpoint

  e2 selects the crow output controls. e3 updates them.
 
#### *midi* (midi output settings)
<img src="https://raw.githubusercontent.com/jaseknighter/krill/main/images/2-2-5-midi.png" width="500" />

  there are three midi controls for the selected patchpoint:

  * *enbl* (midi enable): sends the patchpont's modulation to midi
  * *cc* (midi cc): sets which cc to use to send midi messages for the selected patchpoint
  * *ch* (midi channel): sets the midi channel to use to send midi messages for the selected patchpoint

  note: to send mod matrix outputs to midi, a midi out device needs to be set in the midi sub-menu of the main norns parameters menu (PARAMETERS>EDIT). 

  e2 selects the midi output controls. e3 updates them.

## misc parameters
### read only params
a number of parameters have are listed beneath a "read only" separatator. these are intended to be used as inputs by the mod matrix. 

### inputs/outputs 
settings for midi, crow, jf, and w/ are avaiable in the params menu.
  

### DATA MANAGEMENT
the *krill data* sub-menu at the end of the PARAMETERS menu has all the options for saving, loading, deleting mod matrix settings. saving/loading mod matrix settings also saves/loads the script's parameters.


there is a variable in the `globals.lua` file called `AUTOSAVE_DEFAULT`. setting this variable to `2` means autosave is on by default. setting it to `1` means autosave is off by default.


## feature roadmap
* fix issues with functionality, documentation, and usability 
* set vuja de loop length and probability separately for each pattern
* publish the mod matrix as a mod that other scripts can use

