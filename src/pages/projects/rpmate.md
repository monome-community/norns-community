---
layout: project
title: rpmate
permalink: /rpmate
cover: rpmate.png
raw_name: rpmate
sanitized_name: rpmate
project_url: https://github.com/p3r7/rpmate
description: record a sound an play it back at various RPM ratios
discussion_url: https://llllllll.co/t/38542
documentation_url: https://norns.community/authors/eigen/rpmate
tags:
 - utility
 - sampler
authors:
 - eigen
redirect_from:
 - /en/authors/eigen/rpmate
 - /authors/eigen/rpmate
---
# rpmate

norns as a sampler buddy.

![norns_rpmate](https://www.eigenbahn.com/assets/gif/norns_rpmate.gif)


## About

This script allows to record a sound an play it back at various RPM ratios.

The main use is to replay the sample sped up into a hardware sampler to save memory and add some punch.

The second page gives instructions on how to then speed down the recorded sample to retrieve original speed/tune.

Third page allows dirtying the sample being played by altering sample rate and bit depth.


## Usage

```
-- K1 held is SHIFT
--
-- Anywhere:
--  E1: switch page
--
-- Main screen:
--  E2: record speed
--  E3: playback speed
--  SHIFT + E1: sampler model
--  K2: record start/stop
--  K3: playback start/stop
--
-- HW Sampler Instructions:
--  E2: record speed
--  E3: playback speed
--
-- Dirtying:
--  SHIFT + E1: preset
--  E2: sample rate
--  SHIFT + E2: sample rate (x 1k)
--  E3: bit depth
```
