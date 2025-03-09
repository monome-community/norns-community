---
title: foundry
description: browse fonts, inspect glyphs, and generate lua for using them in a script
published: true
date: 2021-04-07T17:25:40.598Z
tags: utilities
editor: markdown
dateCreated: 2021-03-21T17:21:28.037Z
---

# foundry

## screenshots

![foundry.png](/community/csboling/foundry.png)
![foundry-glyphs.png](/community/csboling/foundry-glyphs.png)

## description

foundry is a typeface viewer that lets you browse the glyphs in each available typeface, view what they look like with different size and brightness parameters, and generate lua snippets for drawing a glyph in your own script.

## install

from maiden type
`;install https://github.com/csboling/foundry`
or find "foundry" in the "community" library in maiden's script manager.

## usage

```lua
-- foundry - view norns fonts
--
-- E1 at any time to change font
--    hold K1 to see font names
--
-- K3 descends down a UI level
-- K2 ascends up a UI level
--
-- first level: glyph selector
--   E2 selects y position
--
--   E3 selects x position
--
--   hold K2: y scrolls 8x
--
-- second level: glyph viewer
--   E2 selects parameter
--
--   E3 selects parameter value
--
--   hold K3: scroll glyphs 100x
--
--   press K3 on 'code':
--   print glyph drawing code to
--   the console (maiden)
--
--   press K3 on 'text':
--   enter text input mode
--
-- third level: text input
--   attach a keyboard to
--   type example text
--   K3 to clear
```

## links

- [view on llllllll](https://llllllll.co/t/foundry/33933)
- [view on github](https://github.com/csboling/foundry)
{.links-list}
