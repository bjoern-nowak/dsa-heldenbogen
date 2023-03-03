#program rulebook_usable.
#defined rulebook_depends/2. %% supress info 'atom does not occur in any rule head'
rulebook_unusable(R,D) :- rulebook_depends(R,D), rulebook(R), not rulebook(D).
%rulebook_unusable(R,D) : rulebook(R), not rulebook(D) :- not rulebook_depends(R,D).


#program base.
%% there can be more specified directly as 'known_' by rulebooks
%% if a restriction is specified (like culture to species) they (the culture) must not be specified directly
%% since it will be 'unpacked' with below:
%% TODO this is debatable: do we want implicit generation of e.g. species by any restriction
known_species(S) :- culture_requires_species(S,_).
known_species(S) :- profession_requires_species(S,_).
%
known_culture(C) :- culture_requires_species(_,C).
known_culture(C) :- profession_requires_culture(C,_).
%
known_profession(P) :- profession_requires_species(_,P).
known_profession(P) :- profession_requires_culture(_,P).


#program hero_facts.
%% to be used with programs 'validate_hero_step<X>'
%% requires 'hero_wrapper.py' as 'context'
species(@hero_species).
culture(@hero_culture).
profession(@hero_profession).


#program validate_hero_step1. %% check species
species_unknown(S) :- species(S), not known_species(S).

#program validate_hero_step2. %% check culture
culture_unknown(C) :- culture(C), not known_culture(C).
#defined known_species_culture/2. %% cultures may not be restricted to a species
culture_unusable(species) :- culture(C), species(S), #false : not culture_requires_species(_,C); not culture_requires_species(S,C).

#program validate_hero_step3. %% check profession
profession_unknown(P) :- profession(P), not known_profession(P).
#defined profession_requires_species/2. %% professions may not be restricted to a species
#defined profession_requires_culture/2. %% professions may not be restricted to a culture
%% only check if there is a restriction ('#false : not' part)
profession_unusable(species) :- profession(P), species(S), #false : not profession_requires_species(_,P); not profession_requires_species(S,P).
profession_unusable(culture) :- profession(P), culture(C), #false : not profession_requires_culture(_,P); not profession_requires_culture(C,P).
%% HINT: below did not work because 'conditional literal' behaves differently in head
%profession_unusable(species) : species(S), not profession_requires_species(S,P) :- profession(P), profession_requires_species(_,P).
%profession_unusable(culture) : culture(C), not culture_requires_species(C,P) :- profession(P), culture_requires_species(_,P).
