---
title: libs & engines
description: reusable lua libs
published: true
date: 2022-06-04T23:23:05.919Z
tags: 
editor: markdown
dateCreated: 2021-05-17T17:17:56.243Z
---

## Softcut & Softcut-based libs

| library                        | code                                                       | description                         | provided by          | used by              |
| --                             | ---                                                        | ---                                 | ---                  | ---                  |
| [softcut][lib softcut lines]   | [lua][lib softcut gh lua], [undelying C][lib softcut gh C] | sample record & playback            | installed by default | sam, reels, piwip    |
| [cartographer][lib cartographer gh] | [lua][lib cartographer gh]                            | flexible buffer space managment     |                      | wrms, orgn                 |
| halfsecond                     | [lua][lib halfsecond gh]                                   | simple 1/2s delay                   | awake                | awake, vials, tambla |


## community Lua libs

| library                                | code                       | description                                                                      | provided by | used by                                            |
| ---                                    | ---                        | ---                                                                              | ---         | ---                                                |
| [passthrough][lib passthrough lines]   | [lua][lib passthrough gh]  | allows norns to pass through midi between connected devices                      | passthrough | passthrough, b-b-b-b-beat, beets, stjoernuithrott  |
| midi                                   | [lua][lib midi gh]         | helper to trig MIDI out                                                          | euclidigons | euclidigons                                        |
| midigrid                               | [lua][lib midigrid gh]     | use alternative midi grid hardware as a _grid_ (e.g. Novation Launchpad)         |             |                                                    |
| [middy][lib middy lines]               | [lua][lib middy gh]        | define midi mappings to specific controllers in your scripts, JSON configuration |             |                                                    |
| \_16n                                 | [lua][lib \_16n gh]     | easy integration of a 16n         |             |                                                    | sines, pirate-radio |     
| hnds                                   | [lua][lib hnds gh]         | LFOs to modulate app parameters                                                  | otis        | otis, pools, greyhole, pedalboard, timeparty |
| gridfader                              | [lua][lib gridfader gh]       | control parameters with faders drawn on grid | groovecats        | groovecats |
| [nest\_][lib nest_ gh]                 | [lua][lib nest_ gh]        | an experimental ui component library for screen, grid, or arc         |             | wrms, orgn                                               |
| [arcify][lib arcify lines]             | [lua][lib arcify gh]       | simple parameter binding to _arc_                                                |             | beets, compass                                     |
| [crowify][lib crowify lines]             | [lua][lib crowify gh]       | simple parameter binding to _crow_ inputs                                        |             | pedalboard                                  |
| [shnth][lib shnth lines]               | [lua][lib shnth gh]        | use the shbobo shnth as a controller                                             |             |                                                    |
| screencap                              | [lua][lib screencap gh]    | animated capture of the screen (into an animated png)                            |             |                                                    |
| [grid-capture][lib grid-capture lines] | [lua][lib grid-capture gh] | capture a _grid_ button press sequence as a gif                                  |             |                                                    |
| shape                                  | [lua][lib shape gh]        | draw shapes on screen                                                            | euclidigons | euclidigons                                        |
| noise                                  | [lua][lib noise gh]        | draw perlin Noise on screen                                                      |             |                                                    |
| [moreFilters][lib moreFilters lines]   | [lua][lib moreFilters gh]  | provides a moving, windowed RMS/standard deviation filter                        |             |                                                    |
| [3d][lib 3d lines]                     | [lua][lib 3d gh]           | 3D drawing lib                                                                   |             |                                                    |
| [p8][lib p8 lines]                     | [lua][lib p8 gh]           | pico-8 code adaptation layer                                                     |             |                                                    |
| pitfalls                               | [gh][app pitfalls src]     | compute microtonal intervals/scales/chords                                       | pitfalls    | pitfalls                                           |
| [namesizer][lib namesizer lines]       | [gh][lib namesizer gh]     | random (file) name generator                                                    |             |                                                    |
| [wobblewobble][lib wobblewobble lines]       | [gh][lib wobblewobble gh]     | chaotic LFO sources                                                    |             | wobblewobble                                             |
| scala      | [gh][lib scala gh]     | scala (microtonal language) parser                                                    |             | fretwork                                             |


## SuperCollider engines

To get the list of engines installed on your norns, type `tab.print(engine.names)` in the matron console in maiden.

| library                            | code                                                                         | description                                                                        | provided by                                | used by                                                         |
| --                                 | ---                                                                          | ---                                                                                | ---                                        | ---                                                             |
| ack                                | [lua wrapper][lib ack gh lua], [sclang][lib ack gh sc]                       | simple sample playback                                                             |                                            | step, ash/playfair, foulplay, takt, crash, vials, strides       |
| timber                             | [lua wrapper][lib timber gh lua], [sclang][lib timber gh sc]                 | advanced sample playback                                                           | [timber][app timber lines]                 | timber, orca                                                    |
| thunk                                | [sclang][lib thunk gh sc]                       | sample playback w/ 64 slots organized in tracks                                                     |                                            | thunk       |
| glut                               | [sclang][lib glut gh sc]                                                     | granular sample playback                                                           | [glut][app glut lines]                     | glut, mangl, uhf, langl                                         |
| [Thebangs][lib Thebangs lines]     | [sclang+lua wrapper][lib Thebangs gh]                                        | fork of PolyPerc w/ multiple synth algorythms & control over polyphony             |                                            | groovecats                                                      |
| PolyPerc                           | [sclang][lib PolyPerc gh sc]                                                 | simple polyphonic filtered decaying square wave                                    | installed by default                       | awake, meadowphysics, barycenter, zeelen, orbital, nono, tambla |
| PolySub                            | [sclang][lib PolySub gh sc]                                                  | multi-type oscillator with polyphonic modulation busses for polytimbral expression | installed by default                       | ash/earthsea                                                    |
| Gong                               | [sclang][lib Gong gh sc]                                                     | basic FM synth                                                                     | installed by default                       |                                                                 |
| TestSine                           | [sclang][lib TestSine gh sc]                                                 | a basic single mono sinewave                                                       | installed by default                       | there                                                           |
| thresher                           | [sclang][lib thresher gh sc]                                                 | live granular pricessing                                                           | [silos](/authors/justmat/silos)            | silos
| [R][lib R lines]                   | [sclang][lib R gh sc]                                                        | collection of engines that link together in a modular synth-style workflow         | installed by default                       | moln, torii                                                     |
| [mi-engines][lib mi-engines lines] | [lua+scland][lib mi-engines gh sc]                                           | port of Mutable Instruments rack modules                                           | [mi-eng/\*][app mi-eng lines]              | mi-eng/\*                                                       |
| molly_the_poly                     | [lua wrapper][lib molly_the_poly gh lua], [sclang][lib molly_the_poly gh sc] | analogue (substractive) synth                                                      | [molly_the_poly][app molly_the_poly lines] | molly_the_poly, arp_index, loom, quence, fugu                   |
| passersby                          | [lua wrapper][lib passersby gh lua], [sclang][lib passersby gh sc]           | westcoast-style synth                                                              | [passersby][app passersby lines]           | passersby, less_concepts, dunes                                 |
| [Dust2][lib Dust2 lines]           | [sclang][lib Dust2 gh sc]                                                    | impulses (ticks)                                                                   | [bgc_dust][app bgc_dust lines]             |                                                                 |
| PrimitiveString                    | [sclang][lib PrimitiveString gh sc]                                          |                                                                                    | [euclidigons][app euclidigons lines]       | euclidigons                                                     |



<!-- ========================================================================= -->



<!-- softcut libs -->
[lib softcut lines]: https://llllllll.co/t/norns-2-0-softcut/20550
[lib softcut gh lua]: https://github.com/monome/norns/blob/main/lua/core/softcut.lua
[lib softcut gh C]: https://github.com/monome/softcut-lib
[lib cartographer gh]: https://github.com/andr-ew/cartographer
[lib halfsecond gh]: https://github.com/tehn/awake/blob/master/lib/halfsecond.lua

<!-- lua libs -->
[lib arcify lines]: https://llllllll.co/t/arcify/22133
[lib arcify gh]: https://github.com/mimetaur/arcify
[lib arcify doc]: https://mimetaur.github.io/arcify/
[lib crowify lines]: https://llllllll.co/t/crowify-easily-map-crow-inputs-to-norns-params/45328/1
[lib crowify gh]: https://github.com/21echoes/crowify
[lib hnds gh]: https://github.com/justmat/otis/blob/master/lib/hnds.lua
[lib grid-capture lines]: https://llllllll.co/t/grid-capture/33158
[lib grid-capture gh]: https://github.com/tlubke/GridCapture
[lib screencap gh]: https://github.com/tlubke/capture
[lib nest_ gh]: https://github.com/andr-ew/nest_
[lib passthrough lines]: https://llllllll.co/t/passthrough/31156
[lib passthrough gh]: https://github.com/nattog/passthrough
[lib midi gh]: https://github.com/synthetiv/euclidigons/blob/main/lib/midi.lua
[lib middy lines]: https://llllllll.co/t/middy/39656
[lib middy gh]: https://github.com/schollz/middy
[lib midigrid gh]: https://github.com/jaggednz/midigrid
[lib shape gh]: https://github.com/synthetiv/euclidigons/blob/main/lib/shape.lua
[lib shnth lines]: https://llllllll.co/t/norns-shnth-library/33238
[lib shnth gh]: https://github.com/cfdrake/shnth
[lib noise gh]: https://github.com/naus3a/NauNorns/blob/master/lib/noise.lua
[lib moreFilters lines]: https://llllllll.co/t/rms-filter/36994
[lib moreFilters gh]: https://github.com/naus3a/NauNorns/blob/master/lib/noise.lua
[lib p8 lines]: https://llllllll.co/t/p8-pico-8-wrapper-lib/37947
[lib p8 gh]: https://github.com/p3r7/p8
[lib 3d lines]: https://llllllll.co/t/3d-pure-lua-3d-lib-for-norns/39622
[lib 3d gh]: https://github.com/p3r7/3d
[lib namesizer lines]: https://llllllll.co/t/namesizer-name-synthesis-library/39612
[lib namesizer gh]: https://github.com/Quixotic7/namesizer
[lib wobblewobble lines]: https://llllllll.co/t/wobblewobble/45215
[lib wobblewobble gh]: https://github.com/schollz/wobblewobble/blob/main/lib/wobblewobble.lua
[lib scala gh]: https://github.com/synthetiv/fretwork/blob/main/lib/scala.lua
[lib gridfader gh]: https://github.com/Quixotic7/groovecats/blob/master/lib/gridfader.lua
[lib \_16n gh]: https://github.com/p3r7/_16n

<!-- supercolier engines -->
[lib ack gh lua]: https://github.com/antonhornquist/ack/blob/master/lib/ack.lua
[lib ack gh sc]: https://github.com/antonhornquist/ack/blob/master/lib/Engine_Ack.sc
[lib thunk gh sc]: https://github.com/chrislo/thunk/blob/main/lib/sample_pool.lua
[lib glut gh sc]: https://github.com/artfwo/glut/blob/master/Engine_Glut.sc
[lib timber gh lua]: https://github.com/markwheeler/timber/blob/master/lib/timber_engine.lua
[lib timber gh sc]: https://github.com/markwheeler/timber/blob/master/lib/Engine_Timber.sc
[lib Thebangs lines]: https://llllllll.co/t/engine-thebangs/38865
[lib Thebangs gh]: https://github.com/catfact/thebangs
<!-- [lib PolyPerc gh sc]: https://github.com/tehn/awake/blob/master/lib/Engine_PolyPerc.sc -->
[lib PolyPerc gh sc]: https://github.com/monome/dust/blob/master/lib/sc/Engine_PolyPerc.sc
[lib PolySub gh sc]: https://github.com/monome/dust/blob/master/lib/sc/Engine_PolySub.sc
[lib Gong gh sc]: https://github.com/monome/dust/blob/master/lib/sc/Engine_Gong.sc
[lib TestSine gh sc]: https://github.com/monome/dust/blob/master/lib/sc/Engine_TestSine.sc
[lib molly_the_poly gh lua]: https://github.com/markwheeler/molly_the_poly/blob/master/lib/molly_the_poly_engine.lua
[lib molly_the_poly gh sc]: https://github.com/markwheeler/molly_the_poly/blob/master/lib/Engine_MollyThePoly.sc
[lib passersby gh lua]: https://github.com/markwheeler/passersby/blob/master/lib/passersby_engine.lua
[lib passersby gh sc]: https://github.com/markwheeler/passersby/blob/master/lib/Engine_Passersby.sc
[lib PrimitiveString gh sc]: https://github.com/synthetiv/euclidigons/blob/main/lib/Engine_PrimitiveString.sc
[lib R lines]: https://llllllll.co/t/norns-r-engine/21071
[lib R gh sc]: https://github.com/antonhornquist/r
[lib mi-engines lines]: https://llllllll.co/t/mi-ugens-for-norns/31781
[lib mi-engines gh sc]: https://github.com/okyeron/mi-eng
[lib Dust2 lines]: https://llllllll.co/t/bgc-dust/32033
[lib Dust2 gh sc]: https://github.com/bgc/bgc_dust/blob/master/engine/Engine_bgcDust.sc
[lib thresher gh sc]: https://github.com/justmat/silos/blob/main/lib/Engine_Thresher.sc
<!-- scripts -->
[app bgc_dust lines]: https://llllllll.co/t/bgc-dust/32033
[app pitfalls src]: https://github.com/robmckinnon/pitfalls
[app glut lines]: https://llllllll.co/t/glut/21175
[app timber lines]: https://llllllll.co/t/timber/21407
[app mi-eng lines]: https://llllllll.co/t/mi-engines/32338
[app molly_the_poly lines]: https://llllllll.co/t/molly-the-poly
[app passersby lines]: https://llllllll.co/t/passersby/21089
[app euclidigons lines]: https://llllllll.co/t/euclidigons/36666

