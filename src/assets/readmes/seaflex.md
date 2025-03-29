# seaflex
companion app for earthsea

https://llllllll.co/t/seaflex

This project started with me wanting to get better at playing chords on the grid layout of earthsea for norns, and struggling to figure them out on the fly. So I built a tool to practice, and thought other folks might find it useful too.

In particular I wanted to build up my muscle memory for common chord shapes in various voicings, which seaflex helps with. Options for scale, scale guides, voicing complexity, as well as two-handed vs one-handed play are available in the params page.

Instructions for navigating the app structure are on the norns display.

Just tapping out chords all day can get a little dull, so there is a game mode where you can go for a high score, which is based on speed and accuracy. Separate high scores are saved based on your combination of initial settings (number of hands, voicing complexity, scale type, light/dark mode).

At any time you can toggle between light and dark modes. Chord shapes are displayed in light mode only. In light mode, to advance chords or finish a round (in game mode), all the lit keys must be pressed (and no other keys). Whereas in dark mode any voicing of the chord or chords displayed on screen will be accepted, meaning if all the keys (and no others) belonging to those chords are pressed, anywhere on the keyboard (any octave), the chord(s) will advance.

The norns encoders don't do anything except modify a few parameters of the PolySub engine.

Some code has been copied over from the earthsea implementation shipped with norns 2.0.
