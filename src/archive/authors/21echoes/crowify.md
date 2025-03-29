---
title: Crowify
description: A Monome Norns library for easily adding Crow input support to existing scripts
published: true
date: 2021-05-25T04:14:03.087Z
tags: crow, utilities
editor: markdown
dateCreated: 2021-05-25T04:13:15.956Z
---

# Crowify

A [Monome Norns](https://monome.org/norns/) library for easily adding [Crow](https://monome.org/docs/crow/) input support to existing scripts.

## Requirements

* An up-to-date Norns (exact OS support unknown)
* A Monome Crow (or the desire to support one in your Norns script)
* If you want to test this script: We/TestSine Engine

## Usage
1. Download [`lib/crowify`](https://raw.githubusercontent.com/21echoes/crowify/main/lib/crowify.lua)
2. Place the file inside your script's folder, typically in the `lib` directory
3. Import it from the path you've chosen (`lib/crowify` in the code below), then use it as follows:
```lua
-- create Crowify class and crowify object
local Crowify = include("lib/crowify")
local crowify = Crowify.new()

-- by default, Crowify updates every 1/25th of a second
-- if you want a different update speed, pass it in
local slowUpdatesCrowify = Crowify.new(1/2)

function init()
    -- register parameters with crowify
    crowify:register("cutoff")
    crowify:register("resonance")

    -- after registering all your params run add_params()
    -- to make them visible in norns params menu
    crowify:add_params()
end

function key(n, z)
    -- if you want to use a shift key with Crowify
    -- pass key params in
    crowify:handle_shift(n, z)
    redraw()
end
```

## Acknowledgements
@mimetaur for the original [Arcify](https://llllllll.co/t/22133)

## Roadmap
1. Beta release & bugfixing
1. Remove the need to `register()` params, and introspect them from the global `params.params_` table directly

github: https://github.com/21echoes/pedalboard

## discussion
For feature requests and bug reports, discuss [over on lines](https://llllllll.co/t/45328)