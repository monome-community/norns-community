# noizeop
NoizeOP is a little noise synth for monome norns

NOIZEOP! v1.0
Noise Synth
by deeg

@deeg_deeg_deeg

https://github.com/deeg-deeg-deeg

be aware!: may produce very
loud noises!!!

ENC 2: choose parameter

ENC 3: change selected parameter

ENC 1: change the amount parameters will be changed

KEY 2&3: select which synth will receive incoming midi notes

-----------------------------------------
*please be aware! at the moment "noizeop" only works if both reverb and compressor on the norns are turned off!*

-----------------------------------------

if you feel adventurous you can edit the supercollider engine of this project. just edit one of the six algorithms in there to fit your needs! edit this part of lib/Engine_NoizeOP.sc

                    algo01 = ((osc01*osc02)/(osc03*osc04))/a_mod_01;
			algo02 = ((osc02*osc04)/(osc03-osc01))/a_mod_02; 
			algo03 = ((osc01+osc02)-(osc03+osc04)).trunc(a_mod_03); 
			algo04 = (algo01*algo02*algo03).sqrt/a_mod_04;
			algo05 = (hypot(osc01,osc02) + hypot(osc03,osc04))*a_mod_05;
			algo06 = (osc01**2+osc02**2+osc03**2+osc04**2)*a_mod_06;
      
but don't touch the a_mod_XX variables. Try experimenting!

Cheers!
