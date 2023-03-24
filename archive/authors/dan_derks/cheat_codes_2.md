---
title: cheat codes 2
description: a sample playground
published: true
date: 2021-08-03T07:53:04.204Z
tags: delays + loopers, sequencers, grid, arc, midi, samplers, jf
editor: markdown
dateCreated: 2021-04-02T12:49:04.083Z
---

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/484816462?byline=0&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

by [`@dan_derks`](/authors/dan_derks)

## requirements

### norns OS
norns `210301` or later

### compatible hardware + software
- monome grid (64 or 128, all editions -- 256 works too, just half-used)
- monome arc (made for 4-encoder)
- OP-Z ([setup notes](https://github.com/dndrks/cheat_codes_2#op-z-setup-notes))
- Midi Fighter Twister: [cc-mft.mfs](https://llllllll.co/uploads/short-url/so1QoxfHVWn29a4YNkybdVEIQgi.mfs) 
- Launchpad, Push 2, or other device supported by [midigrid](https://llllllll.co/t/midigrid-use-launchpads-and-other-midi-grid-controllers-with-norns/42336)
- TouchOSC for the cheat codes 2 [template](https://llllllll.co/t/cheat-codes-2-rev-210714-lts2/38414/924) (many thanks to `@carlosunch` for helping update the cheat codes 1 template and keeping this part of the project alive!)
- any device which sends midi
- max for live: [cc-osc.amxd](https://llllllll.co/uploads/short-url/cckkpyWjH3ywfaHfYzOmV27GS3m.amxd) 
- crow
- Just Friends

## documentation + learning

there are a number of ways into learning cheat codes!

### text
- [PDF of primary docs](https://github.com/dndrks/cheat-codes-docs/raw/main/assets/images/pdf/cheat_codes_2.pdf) 50 pages of guidance and tricks!
- [inverted pdf of primary docs](https://llllllll.co/t/cheat-codes-2-rev-210315-small-fix/38414/115) printer-friendly!
- [inverted pdf of 64 grid layout](https://llllllll.co/t/cheat-codes-2-rev-210315-small-fix/38414/574) essential for `midigrid` use!
{.links-list}

### video
- [an introductory on-demand video course](https://musichackspace.org/events/getting-started-with-cheat-codes-2-a-sample-playground-for-monome-norns-live-session/) via Music Hackspace
- [an extended techniques on-demand video course](https://musichackspace.org/events/going-further-with-cheat-codes-2-a-sample-playground-for-norns-live-session/) via Music Hackspace
- [Ways I Use Cheat Codes; Patterns and timing](https://www.youtube.com/watch?v=5P0vzHSHA0I) demonstration by duelling ants
- [Ways I Use Cheat Codes, Part 2 Delays](https://www.youtube.com/watch?v=kz2Uyhy9HMM) demonstration by duelling ants
{.links-list}

## captures

supplemental video material released alongside updates

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/519262102?byline=0&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/509308873?byline=0&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/494198104?byline=1&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/503912517?byline=0&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

## changelog

## Tabs {.tabset}

### patch 210315

- rnd's weren’t restoring correctly when a collection was reloaded. now they are!

### patch 210307

#### CPU optimization + 64/midigrid live rec fix

- refined the waveform redraw during live recording to reduce CPU by about 10% when recording
- fixed an errant 64-grid live recording issue

### rev 210303

#### threshold live input recording + general improvements

added:

- threshold recording (ty @infinitedigits for code examples in oooooo and for the nice params reveal mechanism in the latest norns update)
- on 64-sized grids (monome or midigrid), switching banks will switch views of applicable on-screen menus (ty @cuberoo for mentioning this during the workshop)
- groundwork for speed dial (more coming)

fixed:

- ghost clicks getting into the live buffer upon script startup
MIDI CC messages could be sent to devices which weren’t meant to listen (ty @bc3 for report!)
- pattern recording now shows bars instead of distro (ty @SPIKE for suggestion!)
- arp refresh built into the arp clear function to avoid needing to go through menus to restart if the arp clock dies

### rev 210227

#### macros, transport, midigrid, midi config, w/synth, even more

too much to describe, see [lines](https://llllllll.co/t/cheat-codes-2-rev-210315-small-fix/38414/380)

### rev 201222

#### MIDI notes + Just Friends voices
**added**:

- MIDI note output!
- Just Friends voice output!
- a TON of mappable MIDI triggers + mods in params!
- random recording probability per live segment
- feedback % per live segment

**fixed**:

- control pads from either a single external MIDI channel or multiple external MIDI channels (previously was only multiple) -- this fixes issues related to Launchpad + Midi Fighter button-boxes. thank you for debugging help @leolodreamland + @fourhoarder 
- arps other than `fwd` now restart correctly after being paused! thank you for the report, @sno!
- live segment recording behaves more predictably when using random triggering (oxymoron, I know, but previous behavior was buggy)

[more here](https://llllllll.co/t/cheat-codes-2-rev-201222-midi-notes-just-friends-voices/38414/230)

### patch 201203
- lowercase alt can perform focus hold (ty @bloc + @888m)
- if MFT doesn't have a port, ignore it until one is assigned (ty @mattlowery)

### patch 201129
- restored OP-Z encoder control over parameters

### rev 201128

#### 64 grid compatibility

**additions**:

- 64 grid support (see PARAMS > GRID): main performance and delay pages! more controls to come.
- 1-shot Live rec latency offset: if you're recording into cheat codes from another computer's DAW, you'll likely see some latency in 1-shot mode. this is expected, so the `latency offset` parameter allows you to compensate for this in 10ms increments, up to 1 second. ymmv, but an easy way to determine a good value to is record in 1-shot mode without this compensation and see how many 0.01s increments it takes to align an auto-chopped pad to the start of the recorded sample. match the latency compensation to this number of increments and you'll be set for the rest of the session!
- brought back `manual control` parameters for folks wishing to map a static slider to current pad's start/end points
- laid the foundation for a `#` submenu to the `[loops]` menu, not accessible in this update tho :)

**fixes**:

- arc window parameter now calculate correctly
- Live rec behaviors (loop or 1-shot) are unique per Live segment
- changing rec loop encoder resolution snaps all segments to appropriate values
- auto-slice zilchmo gesture now checks for pads' segment assignment and auto-chops pads appropriately to the segment's start and end points (previously, was just checking with the current rec focus start/end points)
- more fluid buffer jumping

### patch 201119

**arc**  
- arc LEDs now scale appropriately across all buffers (thank you @swhic!)
- arc movements now update waveform
- arc pattern recorder can switch between foci
  - E2 on timing > arc patterns > loop(w) switches between loop(w), loop(s), and loop(e)
- arc pattern playback can have variable rate
  - after recording an arc pattern, hold K1 on timing > arc patterns to reveal pattern playback rate
  - use E3 while holding K1 to adjust playback rate (1/10th speed to 10x)

**grid**
- 1x works on all pads in non-focus mode
- focus hold unlocks crow pad toggle
  - bright key next to zilchmo 3 when in focus hold mode
  - determines whether a pad execution should send a pulse out of the crow output, if timing > pad pattern > crow pulse is set to `pads`)
- fixed some local alt issues (thank you @bloc!)

## thank you

- @tyleretters for helping me build the yet-to-be-released docs website (more on this soon) and talking through life every few weeks
- @mbutz for establishing such clear methods of grid docs, which served as the backbone to the PDF above
- @DuellingAnts, @glia, @CarlosUnch, @yoyosandshoes, @zanderraymond, @MatthewAshmore, @Quasi, @andrew, @ypxkap, @PaulFe, @Olivier, @edison, @pfig, @noiserock, and everybody else who tested, contributed feedback, gave encouragement, and shared artifacts while this script was coming together, falling apart, stalling out, ramping up, and finally released. each of you has a fingerprint on this thing. i’m so thankful for your time + warmth.
- @tehn + @zebra for initiating norns, developing softcut, and building the patterns of musical inquiry and creative code that have inspired so so so many artists to build, deconstruct, and share. i am deeply grateful for each of your work. you’ve improved + impacted my life so much :revolving_hearts: for those who are able, please [buy a few coffees for ezra](https://www.buymeacoffee.com/catfact). cheat codes wouldn’t exist without softcut, which ezra built.

![cheat_codes_2.png](/community/dan_derks/cheat_codes_2.png)