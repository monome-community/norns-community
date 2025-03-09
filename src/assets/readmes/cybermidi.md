## C Y B E R M I D I

>*Listen up, kid. I don’t need to know how you ended up acquiring not one but *two* Norns-class cyberdecks. But slingin’ two ‘decks without a proper setup is like waltzing into corpo HQ without a plan.*

>*You've got the hardware, sure. It’s gonna take more than just showin' off your chrome to be a legit Netrunner. Do the math: ya got two decks and one interface plug, yeah? That's like tryin' to ride a bike with one wheel. We need to link those bad boys up, turn 'em into a seamless unit with bidirectional comms. Welcome to the sordid world of M.I.D.I.*

>*Now, I get it. Not everyone's got the eddies for a next-gen 2host setup. Lucky for you, my fixer's got a line on a 'less-than-legitimate' option. It's a black-market mod, and yeah, might induce a touch of brain-burn here and there, but in this biz, risk is the name of the game. It’ll get the job done, it’s nanomachine-proof, and here’s the kicker—it’s free.*

>*I'm talkin' CyberMIDI: wireless transmission of M.I.D.I. between ‘decks. Give me a minute to jack in and upload the mod, and I’ll have your hardware singing in harmony. All I need in return is a little job from you. Consider it a favor among friends in the neon-soaked shadows. So, what's the verdict, choom? You in?"*


### What it is
A mod to send MIDI between Norns over IP.

### Requirements

2 Norns-class cyberdecks running update 201023 or later

### How to use it
1. Install from the Maiden project manager (or `;install https://github.com/dstroud/cybermidi`)
2. Enable the mod *on both the sending and receiving units* in SYSTEM>>MODS>>E3 (+ symbol) and restart.
3. Edit mod settings via SYSTEM>>MODS>>CYBERMIDI>>K3. Use E2 to navigate and E3 to change values. K3 refreshes LAN devices.
4. The `LAN` option shows other Norns on your subnet running CyberMIDI and `Manual` allows entering your own IP. You can loop MIDI back using localhost IP 127.0.1.1.
5. IP settings are applied immediately (watch out for hanging notes if you are sending MIDI) and persist on reboot.
6. Add the "virtual" MIDI port in SYSTEM>>DEVICES>>MIDI. Use this to both send and receive MIDI in your script.

### Misc to-do/roadmap stuff:
- Norns' MIDI clocking and CC PMAP functionality does not seem to work with the virtual MIDI interface. We can send and receive those messages but the system ignores them. I don't know if this is intentional or an oversight but I'd appreciate it if anyone who knows what they are doing (i.e. not me) can take a look at [the issue](https://github.com/monome/norns/issues/1744#issuecomment-1836769194). You can sync with Link clock source, however.
- Other [MIDI functions](https://monome.org/docs/norns/reference/midi) should work but I've really only tested MIDI notes and CC so let me know if you find any issues.
