
#program usable.
rulebook("dsa5_expansion").
%% this rulebook depends on another one
rulebook_unusable("dsa5_expansion") :- not rulebook("dsa5").


#program list_spezies.
spezies("Erweiterung_Beispiel_Spezies";).


#program list_kulturen.
kultur("Erweiterung_Beispiel_Kultur").
