%% KNOWN species to culture
known_species_culture("Elf","Auelfen").
known_species_culture("Mensch","Andergaster").
known_species_culture("Zwerg","Ambosszwerge").
%% KNOWN species/culture to profession
%known_species_profession("Elf","Zauberweber").
known_species_profession("Zwerg","Zauberweber").
known_culture_profession("Auelfen","Zauberweber").
known_profession("Söldner").
%%
known_species(S) :- known_species_culture(S,_).
known_culture(C) :- known_species_culture(_,C).
known_profession(P) :- known_species_profession(_,P).
known_profession(P) :- known_culture_profession(_,P).
%% facts
species("Elf").
culture("Auelfen").
profession("Zauberweber").
%profession("Söldner").

%profession_unusable(species) : species(SS) :- profession(PP), known_species_profession(_,PP).
profession_unusable(species) :- profession(P), species(S), #true : known_species_profession(_,P); not known_species_profession(S,P).

%profession_has_restriction :- profession(P), 0 < {known_species_profession(_,P);known_culture_profession(_,P)}.
%profession_unusable(species) :- profession_has_restriction, profession(P), species(S), not known_species_profession(S,P).
%profession_unusable(culture) :- profession_has_restriction, profession(P), culture(C), not known_culture_profession(C,P).