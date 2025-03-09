---
layout: project
title: foundry
permalink: /foundry
cover: foundry.png
raw_name: foundry
sanitized_name: foundry
project_url: https://github.com/csboling/foundry
description: Font / glyph catalog
discussion_url: https://llllllll.co/t/foundry-font-visualizer/33933
documentation_url: 
tags:
 - utility
authors:
 - csboling
redirect_from:
 - /en/authors/csboling/foundry
 - /authors/csboling/foundry
---
# foundry - font viewer for monome norns

Foundry lets you browse the glyphs for all the different fonts
installed on [norns](http://monome.org/docs/norns/) so you can see
what's available and determine the right font face / character codes
to use. You can view glyphs at different sizes and brightness levels,
generate Lua code for drawing a particular glyph in your own script,
and attach a keyboard to type in example text.

Foundry does not know anything about the contents of the fonts, it is
just using `screen.text` to draw everything. Some fonts have many more
glyphs than others so many fonts will have large blank regions, there
are some button / encoder combos to help with skipping over large
numbers of glyphs.

See the comments at the start of `foundry.lua` for usage instructions.
