---
layout: project
title: scholastic
permalink: /scholastic
cover: scholastic.png
raw_name: scholastic
sanitized_name: scholastic
project_url: https://github.com/adamstaff/scholastic
description: multitrack polyrhythmic sequencer
discussion_url: https://llllllll.co/t/scholastic-multitrack-polyrhythmic-sequencer/64232
documentation_url: 
tags:
 - norns
 - sequencer
 - nb
 - midi
authors:
 - adamstaff
redirect_from:
 - /en/authors/adamstaff/scholastic
 - /authors/adamstaff/scholastic
---
# scholastic
A norns script that borrows ideas from Modalics's Beat Scholar:
https://www.modalics.com/beatscholar

Split the measure into many tuplets. Polyrhythms, trap beats, bolero, and bouncing balls.

Send them to the Polyperc engine, an NB voice, or MIDI output.

Encoders:

E1 - Select track

	Scroll to track 0 to change number of tracks with E3
E2 - Select position

	Scroll to beat 0 to change number of beats with E3
E3 - Adjust tracks/beat/division

Keys:

K1 (long) - Shift

K2 - Play/Stop

K3 - Insert / remove a note

K1 + K3 - Edit velocities mode

Encoders and keys:

K1+E1 - Transpose

	Scroll to track 0 to transpose all tracks
K1+E2 - Engine release

K1+E3 - Engine pulse width
