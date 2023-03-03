#program rulebook_usable.
rulebook("dsa5_aventurisches_kompendium_2").
rulebook_depends("dsa5_aventurisches_kompendium_2", "dsa5").



#program base.
%% KNOWN species/culture to profession
known_culture_profession("Novadis","Mawdli").
%% KNOWN professions
known_profession(P) :- known_culture_profession(_,P).
