---
layout: project
title: bounds
permalink: /bounds
cover: bounds.png
raw_name: bounds
sanitized_name: bounds
project_url: https://github.com/justmat/bounds
description: stereo delay/looper
discussion_url: https://llllllll.co/t/23336
documentation_url: 
tags:
 - looper
 - delay
authors:
 - justmat
redirect_from:
 - /en/authors/justmat/bounds
 - /authors/justmat/bounds
---
# bounds v0.2
stereo delay/looper with probabilistic kinetic sequencing

a mashup of @enneff's [Rebound](https://github.com/nf/rebound) and my [Otis](https://github.com/notjustmat/otis).
join the conversation on [lines](https://llllllll.co/t/23336)

_nb: bounds requires otis to be installed at dust/code/otis_

## controls

* key1 = shift
* key2 = add ball
* key3 = select ball
* shift + key2 = remove ball
* shift + key3 = hold buffer

* enc2 = rotate ball
* enc3 = ball speed
* shift + enc1 = probability
* shift + enc2/3 = feedback l/r

## balls

depending on your probability settings, when a ball collides with the edge of the screen an event may occur.
the nature of this event is determined by the x, y coordinates of the collision. the bounds are pictured bellow.

![bounds.png](https://raw.githubusercontent.com/justmat/bounds/HEAD/assets/bounds.png)

* speed mod = currently a random choice of either half speed, or full speed. likely to change in the future.
* flip = change tape direction, maintaining speed.
* skip = reset loop
