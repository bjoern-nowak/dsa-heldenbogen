#program rulebook_usable.
#defined rulebook_depends/2. % supress info 'atom does not occur in any rule head'
rulebook_unusable(R,D) :- rulebook_depends(R,D), rulebook(R), not rulebook(D).
%rulebook_unusable(R,D) : rulebook(R), not rulebook(D) :- not rulebook_depends(R,D).


#program validate_hero.
% step 1: check species
species_unknown(S) :- species(S), not known_species(S).
% step 2: check culture
culture_unknown(C) :- culture(C), not known_culture(C).
culture_unusable :- culture(C), species(S), not known_species_culture(S,C).