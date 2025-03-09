---
title: flora
description: an L-systems sequencer and bandpass-filtered sawtooth engine
published: true
date: 2022-01-24T09:03:17.739Z
tags: synths, sequencers, generative, crow, jf, midi, w/
editor: markdown
dateCreated: 2021-04-09T16:59:09.263Z
---

## UI and Controls

***Plant***
![flora.png](https://llllllll.co/uploads/default/original/3X/1/6/168f1dd49d979f3df027cb03e78680e4db027834.png)
e1: next page  
k1+e1: select active plant  
k1+e2: replace active plant  
e3: increase/decrease angle  
k2/k3: previous/next generation  
k1+k3: reset plants to their original forms and restart their sequences

***Modify***
![modify_wide|690x172](https://llllllll.co/uploads/default/original/3X/4/d/4d0ee19ed1dbc7c6e845eee5f41cc2f8b2943eaf.png) 
e1: next/previous page  
k1+e1: select active plant  
e2: go to next/previous letter  
e3: change letter  
k2/k3: remove/add a letter  
k1+k3: reset plants to their original forms and restart their sequences

***Observe***
![observe_wide|690x172](https://llllllll.co/uploads/default/original/3X/1/8/18ff7e5a4481e515ad26d09184c5f2218be2edb7.png) 
e1: next/previous page  
k1+e1: select active plant  
e2: move up/down  
e3: move left/right  
k2/k3: zoom out/in  
k1+k3: reset plants to their original forms and restart their sequences

***Plow***
![plow_wide|690x172](https://llllllll.co/uploads/default/original/3X/4/2/428eab1f01da8db3daa89892fbd105456eab4fff.png) 
e1: next/previous page 
k1+e1: select active plant  
e2: select control  
e3: change control value  
k2/k3: remove/add a control point 

****Plow modulation**** 
(available with the v0.2.0-beta release)
k1+k3: show/hide plow modulation menu
k1+e1: select active plant  
k2: select control
k3: change control value

***Water***
![water_wide|690x172](https://llllllll.co/uploads/default/original/3X/5/f/5fafb73adc52ab7c55b2ae169e27bf09a5893322.png) 
e1: previous page  
e2: select control  
e3: change control value 

***PSET sequencing***
As of version `v0.2.0-beta`, a PSET sequencer has been built into Flora. Controls for the PSET sequencer are accessed from the PARAMETERS->EDIT menu.

See the documentation on [GitHub](https://github.com/jaseknighter/flora/blob/main/README.md#pset-sequencer) for details.

## Requirements

Norns (required)
Midi, Just Friends, Crow (optional)
Computer (optional for generating custom L-system algorithms)

## Documentation
Press K1+K2 on each screen for basic key/encoder commands.

Complete documentation on [GitHub (jaseknighter/flora)](https://github.com/jaseknighter/flora/blob/main/README.md)

## install

from maiden, type
`;install https://github.com/jaseknighter/flora`

## links
- [view on llllllll](https://llllllll.co/t/40261)
- [view on github](https://github.com/jaseknighter/flora#readme)
{.links-list}

## Acknowledgements
* Flora's L-system code is based on the code in Chapter 8.6 of Daniel Shiffman's [The Nature of Code](https://natureofcode.com/book/chapter-8-fractals/).
* Many of the specific L-system algorithms are based on code from Paul Bourke's [L-System User Notes](http://paulbourke.net/fractals/lsys/).
* *Bandsaw*, a bandpass-filtered sawtooth engine is based on SuperCollider code for a marimba presented by Eli Fieldsteel in his [SuperCollider Tutorial #15: Composing a Piece, Part I](https://youtu.be/lGs7JOOVjag).
* The code for this project was also deeply inspired by the following members of the lines community: Brian Crabtree (@tehn), Dan Derks (@dan_derks), Mark Wheeler (@markeats), Tom Armitage (@infovore), and Tyler Etters (@tyleretters).