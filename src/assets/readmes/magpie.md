# Magpie
signal routing and modulated note echo for norns and crow

![app screen with chirping bird](./assets/docs/main.png)

Magpie takes incoming messages from midi (norns) and cv (crow) and allows them to be rerouted and echoed. It makes no sounds (right now) and has no in-app controls (as yet).


Configuration is done via norns params menus.

![param menu with toggle sources highlighted](./assets/docs/params-1.png)

Every connected device can have its signal routed to any other connected device. It can also have its signal routed to every other connected device by routing to "Omni." Devices default to themselves and the origin channel from which messages come. If nothing is happening, it's probably because you're routing your keys back to your keys by default.

![primary output routing param](./assets/docs/params-routing.png)

Crow inputs 1/2 are interpreted as v/oct and gate respectively. This pattern persists for the outputs 1/2 & 3/4.

Crow only has two channels. In direct crow routing, this is apparent. In omni routing, any channel above 1 (ie 1/2) is interpreted as 2 (ie 3/4).


What about the note echo, though?

Well, it can be toggled on and off.

![param menu for toggling](./assets/docs/params-toggle.png)

It get its own separate routing.

![param menu echo routing](./assets/docs/params-routing-echo.png)

It is controlled via LFO. Each signal source gets its own.

![param menu with lfo highlighted](./assets/docs/params-2.png)

The delay between an incoming note and its echo is the `lfo rate` of the controlling oscillator.

![param menu for lfo at rate](./assets/docs/lfo-delay.png)

The amplitude of the echo is the product of the incoming note's velocity and controlling oscillator's `scaled value` at the time the incoming note is received.

![param menu for lfo at range](./assets/docs/lfo-velocity.png)

That's it. Route stuff. Echo messages. Report bugs. Tada!

Run `;install https://github.com/cachilders/magpie.git` in maiden to...install.

CAVEAT: Connect input and output devices before firing up Magpie. Devices won't be added or removed dynamically (at the moment).
