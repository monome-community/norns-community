---
title: ensemble
description: lead and manage multiple norns in a group performance setting
published: true
date: 2022-06-29T18:56:20.108Z
tags: utilities
editor: markdown
dateCreated: 2022-04-16T06:30:55.263Z
---


## screenshots
![ensemble.png](/community/anthony-t-marasco/ensemble.png)


## description

ensemble is a script designed to eliminate the script selection, clock settings, and preset modification process for indivdiual norns performers, allowing a single user (the ensemble leader) to remotely launch scripts and configure audio engine parameters across a group of Norns and reducing the time spent menu diving during performances and rehearsals. The core functionality of the script was modeled after automation systems such as the Laptop Orchestra of Louisiana’s *GRENDL* and a similar ensemble management process practiced by the Raspberry Pi Orchestra at Virginia Tech.

**important:** Ensemble requires use of the [ch-norns](/authors/anthony-t-marasco/ch-norns) mod. before using the ensemble script, all users in the group must first have ch-norns installed and initialized On their instruments. they will then need to navigate to the ch-norns mod menu to connect to the collab-hub server before returning to the ensemble script. 

## documentation
### how it works
On launch, each user designates their role as either a Performer in the group or as the Conductor before connecting to the Collab-Hub server. The Conductor Norns UI provides two pages of controls for managing ensemble members: Concert Program controls and Concert Clock controls. The Concert Program page allows the Conductor to move through a pre-programmed Concert, a pre-loaded file containing pairs of piece titles and performance data packets to be sent out to each Performer Norns. At the press of a key, the Conductor transmits data from the Concert document as the rehearsal or performance progresses. Performance data packets contain the name of the script to load and the preset collection file name to recall

for security reasons, Only one Norns users can be designated as the Conductor at a time, and Performers are blocked from sending out script-loading calls. Once connected to the network, the role of each ensemble member is fixed until they log off from the collab-hub server. 

## install

**ensemble will soon be available for beta testing by the norns community at the end of july 2022. more information on downloading the package and submitting feedback will be posted here and on the [lines forum](https://llllllll.co/), so please check back then.**



## demos

**coming soon!**

<iframe width="560" height="315" src="" title="youtube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>