#program rulebook_usable.
#defined rulebook_depends/2. %% supress info 'atom does not occur in any rule head'
rulebook_unusable(R,D) :- rulebook_depends(R,D), rulebook(R), not rulebook(D).
%
%% TODO move below to base progam when 'TODO [2]' is solved
#show. %% hide everything in output but
#defined rulebook_unusable/2.
#show rulebook_unusable/2.


#program base.
#show. %% hide everything in output but
%% rules
#defined requires/2.
%% hero facts
#defined species/1. #show species/1.
#defined culture/1. #show culture/1.
#defined profession/1. #show profession/1.
#defined talent/2. #show talent/2.
#defined combat_technique/2. #show combat_technique/2.
#defined advantage/3. #show advantage/3.
#defined disadvantage/3. #show disadvantage/3.
%% hero validation errors
#defined unknown/1. #show unknown/1.
#defined unusable_by/2. #show unusable_by/2.
#defined missing_level/2. #show missing_level/2.
%% hero validation warnings
#defined unusual_for/2. #show unusual_for/2.


#program hero_facts.
%% to be used with programs 'validate_hero_step<X>'
%% requires 'hero_wrapper.py' as 'context'
species(@species).
culture(@culture).
profession(@profession).
%
%% TODO these '__<XYZ>_wrapper' are ugly helper facts, try to remove it
__talent_wrapper(@talents).
__combat_technique_wrapper(@combat_techniques).
__advantage_wrapper(@advantages).
__disadvantage_wrapper(@disadvantages).
talent(T,L) :- __talent_wrapper((T,L)).
combat_technique(CT,L) :- __combat_technique_wrapper((CT,L)).
advantage(A,L,U) :- __advantage_wrapper((A,L,U)).
disadvantage(DA,L,U) :- __disadvantage_wrapper((DA,L,U)).


#program validate_hero_step_100. %% check species usable
unknown(species(S)) :- species(S), not known_species(S).


#program validate_hero_step_150. %% check species requirements


#program validate_hero_step_200. %% check culture usable
unknown(culture(C)) :- culture(C), not known_culture(C).
%% only check if there is a restriction ('#false : not' part)
%% TODO extract all restriction conditions ('#false : not' part) as separate fact, so that other rulebooks can reuse it
unusable_by(culture(C),species(S)) :- culture(C), species(S), #false : not requires(culture(C),species(_)); not requires(culture(C),species(S)).
% WARNINGS
unusual_for(species(S),culture(C)) :- species(S), culture(C), #false : not has_usual(species(S),culture(_)); not has_usual(species(S),culture(C)).


#program validate_hero_step_250. %% check culture requirements


#program validate_hero_step_300. %% check profession usable
unknown(profession(P)) :- profession(P), not known_profession(P).
unusable_by(profession(P),species(S)) :- profession(P), species(S), #false : not requires(profession(P),species(_)); not requires(profession(P),species(S)).
unusable_by(profession(P),culture(C)) :- profession(P), culture(C), #false : not requires(profession(P),culture(_)); not requires(profession(P),culture(C)).


#program validate_hero_step_350. %% check profession requirements
missing_level(profession(P),talent(T,MIN)) :- profession(P), #false : not requires(profession(P),talent(_,_)); requires(profession(P),talent(T,MIN)), not talent(T,_).
missing_level(profession(P),talent(T,MIN)) :- profession(P), #false : not requires(profession(P),talent(_,_)); requires(profession(P),talent(T,MIN)), talent(T,L), L < MIN.
missing_level(profession(P),combat_technique(CT,MIN)) :- profession(P), #false : not requires(profession(P),combat_technique(_,_)); requires(profession(P),combat_technique(CT,MIN)), not combat_technique(CT,_).
missing_level(profession(P),combat_technique(CT,MIN)) :- profession(P), #false : not requires(profession(P),combat_technique(_,_)); requires(profession(P),combat_technique(CT,MIN)), combat_technique(CT,L), L < MIN.
missing_level(profession(P),combat_technique(any_of(1,CTs),MIN)) :- profession(P), #false : not requires(profession(P),any_of(_,combat_technique,_,_)); requires(profession(P),any_of(CHOICES,combat_technique,CTs,MIN)), #false : @any_of_has_minimum_level(CHOICES,combat_technique,CTs,MIN) = 1.


#program validate_hero_step_500. %% check skills (talents, combat techniques) usable
unknown(talent(T)) :- talent(T,_), not known_talent(T).
unknown(combat_technique(CT)) :- combat_technique(CT,_), not known_combat_technique(CT).


#program validate_hero_step_550. %% check skills (talents, combat techniques) requirements
