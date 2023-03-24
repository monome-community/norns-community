---
title: midilooop
description: send notes from one midi device to another, where each pressed note is sent to the next midi channel in a loop
published: true
date: 2021-08-27T06:33:59.319Z
tags: utilities, midi
editor: markdown
dateCreated: 2021-08-26T19:11:32.183Z
---

## screenshots

![midilooop.png](/community/topblogger/midilooop.png)
## description

the script allows you to send notes from one midi device to another, where each pressed note is sent to the next midi channel in a loop. This can be used for a monophonic multi-channel synthesizer to convert to polyphony (for example Elektron model:cycles)

## params

+ midi from - choice midi source device
+ midi to - choice midi destination device
+ from device channel - choice midi channel source device
+ count loop channels - choice count midi loop channels (if 6 means loop will be from 1 to 6 channel)

## requirements
+ norns 
+ midi compatible hardware.

## install

from maiden type
`;install https://github.com/topblogger/midilooop`

## links

- [view on github](https://github.com/topblogger/midilooop)
{.links-list}
