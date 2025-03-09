# esper

Esper is a lofi interpretation of the Esper machine from [Blade Runner](https://youtu.be/dswKyUUhKMI?si=asedF6KPODwQ288h) (and a spiritual port of my [Color Theory Max patch](https://github.com/cachilders/color-theory)).

Take an image, ideally something 64x64 pixels, and upload it to the esper data directory (`dust/data/esper/`). I like scp, personally, but do you.

```scp [PATH/TO/YOUR-IMAGE].png we@norns.local:dust/data/esper/[YOUR-IMAGE].png```

Now load the image from the PARAMS > ESPER menu. Ok. That's nuts and bolts, and it tells you there's params. The meat and potatoes is you take a pic like this (it's loaded by default):

![image of a wildcat](/assets/stock/wildcat.png)

And it will be made to look something like this:

![image of sequencer at top level](/assets/docs/power1.png)

Wowzers. OK. So this is the top level view of the image. Each tile is a kind of statistical average of the 64 pixels it comprises (`median` here, but you can go `mean` or `mode` from the params).

Now from this level you've got a 64 step sequencer. Start it by toggling the context menu.

Cripes. I forgot to mention, you can use a mouse with this script.

Toggle the menu with either `K2` or a `right click` on the mouse.

![image of sequencer with context menu opened](/assets/docs/menu.png)

You can scroll this menu with any `ENC` or the mouse. `K3` and `left click` on the mouse are the `ACTION` buttons. Use an `ACTION` button to invoke a menu item. Those icons are really small, so there is some hint text next to the `BEAT INDICATOR` to let you know what you're toggling.

If the context menu is not invoked, the `ACTION` button will toggle your zoom depth. Whichever block is selected with be zoomed into and enhanced. That's where things get more interesting.

![image of the sequencer at the lower level](/assets/docs/power2.png)

You can tell you're at the enhanced level by the little plus sign in the Esper machine.

From this level `ENC2` and `ENC3` will allow you to traverse the image, block by block. It may be hard to believe, but these are the actual pixels of the image down here.

Taken as a whole I think that's like 4,096 steps. Hot crackers!

By default the player will loop over the sequence into which you have zoomed, however, you can choose to `TRACK` in the sequence direction from the context menu.

You can also choose to `REVERSE` the sequence direction from that menu, not to mention `PLAY` and `STOP`. Hint: push `STOP` twice to reset the playhead.

That's it. The voice is provided by Zack Schollz's [mx.synths](https://github.com/schollz/mx.synths/tree/main). You can tune it from PARAMS > mx.synths. If you don't have it installed this script will not function.
