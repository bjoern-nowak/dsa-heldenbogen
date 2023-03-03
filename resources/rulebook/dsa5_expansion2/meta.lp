#program rulebook_usable.
rulebook("dsa5_expansion2").
%% this rulebook depends on others
rulebook_depends("dsa5_expansion2", "dsa5").
rulebook_depends("dsa5_expansion2", "dsa5_expansion").



#program base.
%% KNOWN species
known_species("Expansion2_Example_Species").
%% KNOWN cultures
known_culture("Expansion2_Example_Culture").
