# qfwfq
A sequencing toy for [norns](https://monome.org/docs/norns/) based on the brute force password solvers from movies.

![animated demo](./assets/images/demo.gif)

## What it does
This is a simple sequencer with a gimmicky twist. In its current state, user input is accepted in the form of a random sequence of sixteen ASCII characters via k2, and/or by navigation to individual steps (enc2) and adjustment (enc3). The characters range between the ASCII values 32 and 122, which are passed as Hz to PolyPerc and notes via midi. Start and stop the sequence with k3.

A looping ribbon of sequential guesses runs over the sequence, attempting to lock a solution. Locked notes are played, unquantized. If user input "unsolves" a step it returns that step to its unplayed state until the new value is discovered.

External clock is accepted via params, and internal clock adjustment is available on enc1.

## TK
I'll be adding crow cv support in the near term, but in this early stage it's all PolyPerc, midi, and compromise. I plan to add scale quantization, more sophisticated beat clocking, and enhanced playability via arc, but it's all up in the air, and I'm open to suggestions, advice, and admonishments.

## Acknowledgements
The code draws heavily from the efforts of the norns community. The name comes from the protagonist of t-zero and Cosmicomics by Italo Calvino. It's a name owing to [Oulipo](https://en.wikipedia.org/wiki/Oulipo), which feels appropriate here.
