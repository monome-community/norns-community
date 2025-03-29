---
title: folio
description: browse scripts available in maiden from the comfort of your norns
published: true
date: 2021-07-24T07:23:11.079Z
tags: utilities
editor: markdown
dateCreated: 2021-07-24T07:07:19.877Z
---

# folio

## description

folio is a tool for browsing which scripts are available to be downloaded from the maiden script catalogs. It makes use of a resource for organizing scripts that is already available on the device if you have ever viewed the script library in maiden: JSON files that maiden downloads to /home/we/dust/catalogs. As such it currently knows names, authors, and tags for all scripts that have been submitted to the norns-community repo as of the time of your last sync – it does not currently know which scripts you have installed on your device, or about any scripts available other places. It does not currently support attaching custom tags to scripts, only viewing how the scripts have been tagged in the maiden catalog.

## install

from maiden type
`;install https://github.com/csboling/folio`
or find "folio" in the "community" library in maiden's script manager.

## usage

```lua
--- folio
--- browse library scripts
---
--- E1 at top level:
---   toggle tags / scripts
--- E2: scroll through menus
--- K3: down a level
---   tags -> scripts -> script
---   on 'tag:' browse tag
--- K2: up a level
```