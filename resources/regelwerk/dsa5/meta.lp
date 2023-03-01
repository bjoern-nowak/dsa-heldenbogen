#program rulebook_usable.
%% make presence of this rulebook available for others
rulebook("dsa5").
%% this rulebook depends on nothing


#program base.
%% KNOWN species to culture
known_species_culture("Elf",("Auelfen";"Firnelfen";"Steppenelfen";"Waldelfen")).
known_species_culture("Mensch",("Andergaster";"Aranier";"Bornländer";"Ferkinas";"Fjarninger";"Gjalsker";"Horasier";"Koboldweltler";"Maraskaner";"Menschlichekultur";"Mhanadistani";"Mittelreicher";"Mohas";"Nivesen";"Norbarden";"Nordaventurier";"Nostrier";"Novadis";"Svellttaler";"Südaventurier";"Thorwaler";"Trollzacker";"Zahori";"Zyklopäer")).
known_species_culture("Zwerg",("Ambosszwerge";"Brillantzwerge";"Erzzwerge";"Hügelzwerge";"Wildzwerge")).
%% KNOWN species
known_species(S) :- known_species_culture(S,_).
%% KNOWN cultures
known_culture(C) :- known_species_culture(_,C).
