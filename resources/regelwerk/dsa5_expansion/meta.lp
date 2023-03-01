#program rulebook_usable.
rulebook("dsa5_expansion").
%% this rulebook depends on another one
rulebook_depends("dsa5_expansion", "dsa5").


#program base.
%% KNOWN species
known_species("Expansion_Example_Species").
%% KNOWN cultures
known_culture("Expansion_Example_Culture").
