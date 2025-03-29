---
title: schicksalslied
description: a poetry sequencer
published: true
date: 2022-12-14T23:11:59.938Z
tags: synths, art, sequencers, crow, keyboard, jf, grid, generative, w/
editor: markdown
dateCreated: 2022-10-26T17:49:52.739Z
---

## screenshot

![schicksalslied.png](/community/williamhazard/schicksalslied.png)

“What is a poet? A poet is an unhappy being whose heart is torn by secret sufferings, but whose lips are so strangely formed that when the sighs and the cries escape them, they sound like beautiful music.”
-Søren Kierkegaard, *Either/Or*

with thanks to [@Justmat](/authors/justmat), whose crow talk script provided the foundation for this script’s UI, [@dan_derks](/authors/dan_derks) and [@jaseknighter](/authors/jaseknighter), whose [norns/habitus workshop](https://llllllll.co/t/norns-habitus-workshop-at-monome-sept-24-25-2022/57536) got me much more interested in scripting with [softcut](https://monome.org/docs/norns/softcut/) than I’d ever been before, [@infinitedigits](/authors/infinitedigits), whose [Tone to Drone](https://musichackspace.org/events/tone-to-drone-introduction-to-supercollider-for-monome-norns-live-session/) class helped me learn [SuperCollider](https://supercollider.github.io/), and [@alanza](/authors/alanza), who provided invaluable guidance and support throughout the process of this script’s creation, particularly with regard to the [grid](https://monome.org/docs/norns/grid-recipes/) concatenation features and incorporation of the [FormantTriPTR](https://github.com/ryleelyman/FormantTriPTR) SuperCollider UGen from [lamination](/authors/alanza/lamination)

## demonstration

<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1378475983&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>

## description

a poetry sequencer

*note: you will need to restart [norns](https://monome.org/docs/norns/) after installing this script, in order for the LiedMotor synth engine to install*

### Entering Text

Schicksalslied begins with a text field. You can input text into the field in two ways:

1) by attaching a keyboard to one of [norns](https://monome.org/docs/norns/studies/)'s usb ports and typing (20 characters max)
2) loading a .txt file into norns and importing it into schicksalslied using the "text file" feature in the params menu

For method 1, you can hit enter on your keyboard to send your line to schicksalslied. Each line you enter will be added to history. History items can be accessed by hitting the "up" arrow on your keyboard. The currently-selected history item will appear in the text field. Then you can hit enter again to make that line the active line.

History items can also be accessed with a grid. When a line is added to history, a square on the grid will be soft-lit. That square holds the line. You can access the line again by pressing that button. When the button is held down, the line it holds will be displayed in schicksalslied's text field. When the button is released, that line becomes the active line. It will not be re-entered into history. You can also combine lines with grid, by holding down multiple buttons and releasing them simultaneously. The lines will be combined in the order in which the buttons are pressed. Combined lines are not added to history.

For method 2, your imported .txt file will be broken up by line breaks. There is no character limit for lines entered in this way. Each line will be added to history and will get its own square on the grid. If your file exceeds 128 lines, only the first 128 lines will be available on the grid. But no line will be active by default. You'll need to select one. You can do this with a keyboard or a grid, using the methods described above. If you're looking for somewhere to store your .txt files on norns, there's a "text files" folder located within the "lib" folder for schicksalslied. There's one poem there already, to get you started.

### Turning Text into Music

Once you've entered your text, there are three ways to turn it into music. They can all be used simultaneously.

1) with the LiedMotor synth engine
2) with imported audio files
3) with [crow](https://monome.org/docs/crow/)

*LiedMotor*
Once you've got an active line, you can activate the LiedMotor engine by pressing K3. But by default, you won't hear any sound yet. You'll need to choose one or more voices. LiedMotor has six voices:

1) sinsin (an FM voice with a sine wave modulated by another sine wave)
2) tritri (an FM voice with two oscillators based on the Mannequins Mangrove module, patched "square to air")
3) ringer (a pinged resonant filter with variable decay)
4) trisin (an FM voice with a triangle wave modulated by a sine wave)
5) karplu (a karplus-strong-style physical modeling string synthesis voice)
6) resonz (a pinged resonant filter without variable decay)

You can activate each of these voices by turning up its "amp" parameter in the LiedMotor section of the parameters menu. Each of the voices interprets your text in its own way. You might think of them as a jazz combo "playing the changes." In this sense, a "chord" would correspond to a line. You can change between chords by entering more lines or choosing different lines from history using the "up" arrow or grid button presses.

You can also shape the timbre of each voice in the LiedMotor section of the parameters menu. There are a lot of parameters. MIDI mapping can be very helpful for managing them all. You can also modulate any of these parameters with LFOs, using the LFOs section of the parameters menu.

*Audio File*
You can import up to 3 audio files into schicksalslied using the “audio file” features in the params menu. Then you can start your files playing with K2. Schicksalslied will use norns’s softcut features to manipulate your audio files in ways that are determined by the text in the line you’ve entered. There are three manipulated-audio voices available. Each interprets your line to manipulate audio in its own way. You can load three different files or load one file into all 3 slots, to traverse different sections of a single recording. The three voices’ levels can be adjusted in the params menu.

*Crow*
You can activate crow features using K1. This works in essentially the same way as the [krähenlied](https://llllllll.co/t/krahenlied/59171) script for crow and [druid](https://monome.org/docs/crow/druid/). Documentation for krähenlied can be found [here](https://github.com/williamthazard/krahenlied/blob/main/README.md). As with krähenlied, the text you've entered will determine the following:

1) pitch (v/8) from crow outputs 1 & 3
2) slew time between pitches from outputs 1 & 3
3) AR envelope shapes from outputs 2 & 4
4) sequences for 6 [Just Friends](https://github.com/whimsicalraps/Mannequins-Technical-Maps/blob/master/just-friends/just-friends.md) synth voices
5) level for each note event on [Just Friends](https://github.com/whimsicalraps/Just-Friends/blob/main/Just-Type.md) in synthesis mode
6) repeats and divisions for Just Friends geode rhythms
7) quantization value for Just Friends in geode mode
8) virtual voltages to be sent to the run jack on Just Friends
9) playback speed and direction for [w/tape](https://www.whimsicalraps.com/products/wslash?variant=5936952049693)
10) creation, activation, and deactivation of loops on [w/tape](https://llllllll.co/t/mannequins-w-2-beta-testing/34091)
11) playhead position on w/tape
12) clock synch divisions for all of the above

Unlike krähenlied, schicksalsleid can also play w/syn’s 4 voices or a karplus-strong string synthesizer in w/del mode. W/syn’s “this” and “that” inputs will be set up to modulate its “ramp” and “curve” parameters, respectively, by default. Other timbral parameters can be shaped in the parameters menu. They can also be modulated with LFOs.

### A Note on Clock Divs

You'll notice that, in addition to the sections mentioned above, there is also a parameters menu section titled "Clock Divs." This allows you to choose the pace at which a given voice (engine, softcut, or crow) picks its notes from your line. For example, a bass player might not play notes as frequently as a saxophone player. Or they might play more! It's up to you.

Note that for the clock div settings, higher numbers mean longer (as in, longer pauses between notes), not faster.

## install

from maiden type
`;install https://github.com/williamthazard/schicksalslied`

## links

- [view on llllllll](https://llllllll.co/t/schicksalslied/59227)
- [view on github](https://github.com/williamthazard/schicksalslied)
{.links-list}
