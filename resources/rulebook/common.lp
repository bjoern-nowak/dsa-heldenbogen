#program rulebook_usable.
#defined rulebook_depends/2. %% supress info 'atom does not occur in any rule head'
rulebook_unusable(R,D) :- rulebook_depends(R,D), rulebook(R), not rulebook(D).
%rulebook_unusable(R,D) : rulebook(R), not rulebook(D) :- not rulebook_depends(R,D).


#program base.
%% there can be more specified directly as 'known_' by rulebooks
%% if a restriction is specified (like culture to species) they (the culture) must not be specified directly
%% since it will be 'unpacked' with below:
%% TODO this is debatable: do we want implicit generation of e.g. species by any restriction
#defined requires/2. %% may there is no restriction
known_species(S) :- requires(species(S),_).
known_species(S) :- requires(_,species(S)).
known_culture(C) :- requires(culture(C),_).
known_culture(C) :- requires(_,culture(C)).
known_profession(P) :- requires(profession(P),_).
known_profession(P) :- requires(_,profession(P)).


#program hero_facts.
%% to be used with programs 'validate_hero_step<X>'
%% requires 'hero_wrapper.py' as 'context'
species(@species).
culture(@culture).
profession(@profession).
%% TODO this '__talent_wrapper' is a ugly helper construct, try to remove it
__talent_wrapper(@talents).
talent(T,L) :- __talent_wrapper((T, L)).
#defined talent/2. %% hero may does not have any talents
%% TODO this '__combat_technique_wrapper' is a ugly helper construct, try to remove it
__combat_technique_wrapper(@combat_techniques).
combat_technique(C,L) :- __combat_technique_wrapper((C, L)).
#defined combat_technique/2. %% hero may does not have any combat techniques


% TODO make unknown checks an separate step
#program validate_hero_step_100. %% check species
unknown(species(S)) :- species(S), not known_species(S).

#program validate_hero_step_200. %% check culture
unknown(culture(C)) :- culture(C), not known_culture(C).
%% only check if there is a restriction ('#false : not' part)
%% TODO extract all restriction conditions ('#false : not' part) as separate fact, so that other rulebooks can reuse it
unusable_by(culture,species) :- culture(C), species(S), #false : not requires(culture(C),species(_)); not requires(culture(C),species(S)).

#program validate_hero_step_300. %% check profession
unknown(profession(P)) :- profession(P), not known_profession(P).
unusable_by(profession,species) :- profession(P), species(S), #false : not requires(profession(P),species(_)); not requires(profession(P),species(S)).
unusable_by(profession,culture) :- profession(P), culture(C), #false : not requires(profession(P),culture(_)); not requires(profession(P),culture(C)).
missing_level(profession,talent(T,MIN)) :- profession(P), #false : not requires(profession(P),talent(_,_)); requires(profession(P),talent(T,MIN)), not talent(T,_).
missing_level(profession,talent(T,MIN)) :- profession(P), #false : not requires(profession(P),talent(_,_)); requires(profession(P),talent(T,MIN)), talent(T,L), L < MIN.
missing_level(profession,combat_technique(CT,MIN)) :- profession(P), #false : not requires(profession(P),combat_technique(_,_)); requires(profession(P),combat_technique(CT,MIN)), not combat_technique(CT,_).
missing_level(profession,combat_technique(CT,MIN)) :- profession(P), #false : not requires(profession(P),combat_technique(_,_)); requires(profession(P),combat_technique(CT,MIN)), combat_technique(CT,L), L < MIN.
missing_level(profession,combat_technique(any_of(1,CTs),MIN)) :- profession(P), #false : not requires(profession(P),any_of(_,combat_technique,_,_)); requires(profession(P),any_of(CHOICES,combat_technique,CTs,MIN)), #false : @any_of_has_minimum_level(CHOICES,combat_technique,CTs,MIN) = 1.
