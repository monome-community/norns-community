---
title: loud numbers
description: data sonification for norns
published: true
date: 2022-10-20T10:42:19.359Z
tags: synths, art, sequencers, crow, grid, utilities, generative
editor: markdown
dateCreated: 2021-12-28T15:06:29.030Z
---

## screenshots

![loud-numbers.png](/community/duncan-geere/loud-numbers.png)

## description

Loud Numbers is a [data sonification](https://en.wikipedia.org/wiki/Sonification) script for Norns. It turns .csv files into melodies and control voltages.

You can select the root note and scale with encoders 2 and 3. Encoder 1 selects the bpm. Key 2 toggles play/pause, and key 3 toggles whether the melody should loop when you reach the end of the dataset or not.

The script comes with a default set of data - temperature.csv, which contains global temperature anomalies since 1950 for the globe, tropics, and northern and southern hemispheres, via [Our World in Data](https://ourworldindata.org/grapher/temperature-anomaly?time=1950..2019&country=~Global). Swap between data columns by turning encoder 1 while holding down key 1. Selecting a new data column will reset the sequence.

You can also add your own data (in fact, that's kind of the point). Place data files in the /data folder - the same folder as temperatures.csv. Once you've loaded your file, restart the script and select it through the parameters menu. Any non-numbers in your data will be converted to zeros.

## install

Install through Maiden project manager

## links

- [view on llllllll](https://llllllll.co/t/loud-numbers-data-sonification-with-norns/51353)
- [view on github](https://github.com/duncangeere/loudnumbers_norns)
{.links-list}

## demos

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/9N2OP0T_qRc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>