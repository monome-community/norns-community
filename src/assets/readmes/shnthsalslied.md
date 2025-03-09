# shnthsalslied
fork of schicksalslied for use with shbobo shnth

<i>note: requires schicksalslied as well as the shnth library for norns; the latter can be found at</i> https://github.com/cfdrake/shnth

“What is a poet? A poet is an unhappy being whose heart is torn by secret sufferings, but whose lips are so strangely formed that when the sighs and the cries escape them, they sound like beautiful music.”<br>
-Søren Kierkegaard, Either/Or

shnthsalslied works in essentially the same way as schicksalslied (for which documentation is available at https://github.com/williamthazard/schicksalslied/blob/main/README.md), with one notable exception: rather than being sequenced according to the entered lines of text, 3 of the LiedMotor engine's voices (trisin, karplu, and resonz) are allocated to the shbobo shnth (bars, major buttons, and minor buttons, respectively). The frequencies at which these voices will play is determined by the entered lines of text. <br>
<br>The first four characters entered will determine the frequencies triggered by the four bars. The next four characters will determine the frequencies triggered by the major buttons. And the next four will determine the frequencies triggered by the minor buttons. If there are 8 characters or fewer in the line, the minor buttons won't do anything. If there are 4 characters or fewer, the major buttons won't do anything either. And if there are fewer than 4 characters, only as many bars as there are characters will trigger notes.<br> 
<br>For example, the word "the" will only imbue three bars with notes. The bars populate from left to right (as do the major and minor buttons), so in this example, the rightmost bar wouldn't do anything. And the word "a" would only imbue the leftmost bar with a note.<br>
<br> <b>A Note on the Bars</b>

Shnth's bars trigger LiedMotor's trisin voice. This is an FM voice. The depth of the bar press determines the voice's FM index. Consequently, unlike in schicksalslied, this parameter cannot be edited in params. Instead, the parameter is performed on each bar press.
