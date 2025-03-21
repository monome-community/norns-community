---
layout: project
title: sway
permalink: /sway
cover: sway.png
raw_name: sway
sanitized_name: sway
project_url: https://github.com/carltesta/sway
description: analysis-driven live audio processing
discussion_url: https://llllllll.co/t/sway/21117
documentation_url: 
tags:
 - generative
 - audio_fx
authors:
 - carltesta
redirect_from:
 - /en/authors/carltesta/sway
 - /authors/carltesta/sway
---
# Norns-Sway
Sway for monome norns (live processing environment for one channel)

http://sway.carltesta.net

Demo/walkthrough video here: https://youtu.be/w9RZHmo4JAs

# Install

To install on norns running 2.0 or above

ssh into norns via command line or terminal (see https://monome.org/docs/norns/ under "other access")

then type:
```
cd dust/code
git clone https://github.com/carltesta/sway
```
After installation reset the audio system by navigating to ```System > RESET```

To update, first ssh in and type:
```
cd dust/code/sway
git pull
```

# Usage
1) Plug an instrument or microphone into input 1 (L) on monome norns
2) Plug in headphones or connect output 1, 2 or both to external speaker(s)
3) Start Sway script 

TODO CALIBRATION

TODO SETTINGS

TODO ADDING PROCESSING TYPES

