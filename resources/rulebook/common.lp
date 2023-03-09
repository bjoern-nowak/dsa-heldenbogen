#program base.
#show. %% hide everything in output but
%% rulebook_usable
#defined rulebook_depends/2.
#defined rulebook_unusable/2. #show rulebook_unusable/2.
%% world facts
#defined known_species/1.
#defined known_culture/1.
#defined known_profession/1.
#defined known_advantage/3.
#defined known_disadvantage/3.
#defined known_talent/2.
#defined known_combat_technique/2.
#defined requires/2.
#defined has_usual/2.
#defined has_typical/2.
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
#defined missing_typical/2. #show missing_typical/2.


#program rulebook_usable.
rulebook_unusable(R,D) :- rulebook_depends(R,D), rulebook(R), not rulebook(D).
%% TODO add check that rulebook only uses known feature values, hence requires program world_facts


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
talent(T,LVL) :- __talent_wrapper((T,LVL)).
combat_technique(CT,LVL) :- __combat_technique_wrapper((CT,LVL)).
advantage(A,USES,LVL) :- __advantage_wrapper((A,USES,LVL)).
disadvantage(DA,USES,LVL) :- __disadvantage_wrapper((DA,USES,LVL)).


#program validate_hero_step_100. %% check species usable
unknown(species(S)) :- species(S), not known_species(S).


#program validate_hero_step_150. %% check species requirements


#program validate_hero_step_200. %% check culture usable
unknown(culture(C)) :- culture(C), not known_culture(C).
%% only check if there is a restriction ('#false : not' part)
%% TODO extract all restriction conditions ('#false : not' part) as separate fact, so that other rulebooks can reuse it
unusable_by(culture(C),species(S)) :- culture(C), species(S), #false : not requires(culture(C),species(_)); not requires(culture(C),species(S)).
% WARNINGS
missing_usual(species(S),culture(C)) :- species(S), culture(C), #false : not has_usual(species(S),culture(_)); not has_usual(species(S),culture(C)).


#program validate_hero_step_250. %% check culture requirements


#program validate_hero_step_300. %% check profession usable
unknown(profession(P)) :- profession(P), not known_profession(P).
unusable_by(profession(P),species(S)) :- profession(P), species(S), #false : not requires(profession(P),species(_)); not requires(profession(P),species(S)).
unusable_by(profession(P),culture(C)) :- profession(P), culture(C), #false : not requires(profession(P),culture(_)); not requires(profession(P),culture(C)).


#program validate_hero_step_350. %% check profession requirements
missing_level(profession(P),talent(T,MIN_LVL)) :- profession(P), #false : not requires(profession(P),talent(_,_)); requires(profession(P),talent(T,MIN_LVL)), not talent(T,_).
missing_level(profession(P),talent(T,MIN_LVL)) :- profession(P), #false : not requires(profession(P),talent(_,_)); requires(profession(P),talent(T,MIN_LVL)), talent(T,LVL), LVL < MIN_LVL.
missing_level(profession(P),combat_technique(CT,MIN_LVL)) :- profession(P), #false : not requires(profession(P),combat_technique(_,_)); requires(profession(P),combat_technique(CT,MIN_LVL)), not combat_technique(CT,_).
missing_level(profession(P),combat_technique(CT,MIN_LVL)) :- profession(P), #false : not requires(profession(P),combat_technique(_,_)); requires(profession(P),combat_technique(CT,MIN_LVL)), combat_technique(CT,LVL), LVL < MIN_LVL.
missing_level(profession(P),combat_technique(any_of(1,CTs),MIN_LVL)) :- profession(P), #false : not requires(profession(P),any_of(_,combat_technique,_,_)); requires(profession(P),any_of(CHOICES,combat_technique,CTs,MIN_LVL)), #false : @any_of_has_minimum_level(CHOICES,combat_technique,CTs,MIN_LVL) = 1.


#program validate_hero_step_400. %% check (dis)advantage usable
unknown(advantage(A,USES,LVL)) :- advantage(A,USES,LVL), not known_advantage(A,USES,LVL).
unknown(disadvantage(DA,USES,LVL)) :- disadvantage(DA,USES,LVL), not known_disadvantage(DA,USES,LVL).


#program validate_hero_step_450. %% check (dis)advantage requirements
% WARNINGS
missing_typical(species(S),advantage(A,USES,LVL)) :- species(S), #false : not has_typical(species(S),advantage(_,_,_)); has_typical(species(S),advantage(A,USES,LVL)), not advantage(A,USES,LVL).
missing_typical(species(S),disadvantage(DA,USES,LVL)) :- species(S), #false : not has_typical(species(S),disadvantage(_,_,_)); has_typical(species(S),disadvantage(DA,USES,LVL)), not disadvantage(DA,USES,LVL).


#program validate_hero_step_500. %% check skills (talents, combat techniques) usable
unknown(talent(T)) :- talent(T,_), not known_talent(T).
unknown(combat_technique(CT)) :- combat_technique(CT,_), not known_combat_technique(CT).


#program validate_hero_step_550. %% check skills (talents, combat techniques) requirements
