#program base.
#show. %% hide everything in output but
%% rulebook_usable
#defined rulebook_depends/2.
#defined rulebook_missing/2. #show rulebook_missing/2.
%% world facts
#defined known_experience_level/1.
#defined known_race/1.
#defined known_culture/1.
#defined known_profession/1.
#defined known_advantage/3.
#defined known_disadvantage/3.
#defined known_talent/2.
#defined known_combat_technique/2.
#defined requires/2.
#defined has_usual/2.
#defined has_typical/2.
#defined has_atypical/2.
%% hero facts
#defined race/1. #show race/1.
#defined culture/1. #show culture/1.
#defined profession/1. #show profession/1.
#defined talent/2. #show talent/2.
#defined combat_technique/2. #show combat_technique/2.
#defined advantage/3. #show advantage/3.
#defined disadvantage/3. #show disadvantage/3.
%% hero validation errors
#defined unknown/1. #show unknown/1.
#defined unusable_by/2. #show unusable_by/2.
#defined missing/2. #show missing/2.
#defined missing_level/2. #show missing_level/2.
#defined missing_min_lvl/2. #show missing_min_lvl/2.
#defined max_lvl_exceeded/2. #show max_lvl_exceeded/2.
#defined max_count_exceeded/2. #show max_count_exceeded/2.
%% hero validation warnings
#defined unusual_for/2. #show unusual_for/2.
#defined missing_usual/2. #show missing_usual/2.
#defined missing_typical/2. #show missing_typical/2.
#defined atypical/2. #show atypical/2.


#program rulebook_usable.
rulebook_missing(RB,D) :- rulebook(RB), rulebook_depends(RB,D), not rulebook(D).


#program rulebook_requirements.
%% TODO add check that rulebook only uses known feature values, to be executed by testcases


#program world_facts.
% CC := MAX_CHARACTERISTIC_LVL (only on character creation)
% S := MAX_SKILL_LVL
% CT := MAX_COMBAT_TECHNIQUE_LVL
% CCP := MAX_CHARACTERISTIC_POINTS
% SL := MAX_SPELLS_AND_LITURGIES
% FS := MAX_FOREIGN_SPELL
%                                       CC  S   CT  CCP  SL  FS
known_experience_level("Inexperienced", 12, 10,  8,  95,  8, 0 ).
known_experience_level("Average",       13, 10, 10,  98, 10, 1 ).
known_experience_level("Experienced",   14, 10, 12, 100, 12, 2 ).
known_experience_level("Competent",     15, 13, 14, 102, 14, 3 ).
known_experience_level("Masterful",     16, 16, 16, 105, 16, 4 ).
known_experience_level("Brilliant",     17, 19, 18, 109, 18, 5 ).
known_experience_level("Legendary",     18, 20, 20, 114, 20, 6 ).


#program hero_facts.
%% to be used with programs 'validate_hero_step<X>'
%% requires 'hero_wrapper.py' as 'context'
%% TODO these '__<XYZ>_wrapper' are ugly helper facts, try to remove it
__talent_wrapper(@talents).
__combat_technique_wrapper(@combat_techniques).
__advantage_wrapper(@advantages).
__disadvantage_wrapper(@disadvantages).
%
experience_level(@experience_level).
race(@race).
culture(@culture).
profession(@profession).
talent(T,LVL) :- __talent_wrapper((T,LVL)).
combat_technique(CT,LVL) :- __combat_technique_wrapper((CT,LVL)).
advantage(A,USES,LVL) :- __advantage_wrapper((A,USES,LVL)).
disadvantage(DA,USES,LVL) :- __disadvantage_wrapper((DA,USES,LVL)).


#program validate_hero_step_50. %% pre check - values known
unknown(experience_level(EL)) :- experience_level(EL), not known_experience_level(EL,_,_,_,_,_,_).
unknown(race(R)) :- race(R), not known_race(R).
unknown(culture(C)) :- culture(C), not known_culture(C).
unknown(profession(P)) :- profession(P), not known_profession(P).
unknown(advantage(A,USES,LVL)) :- advantage(A,USES,LVL), not known_advantage(A,USES,LVL).
unknown(disadvantage(DA,USES,LVL)) :- disadvantage(DA,USES,LVL), not known_disadvantage(DA,USES,LVL).
unknown(talent(T)) :- talent(T,_), not known_talent(T).
unknown(combat_technique(CT)) :- combat_technique(CT,_), not known_combat_technique(CT).


#program validate_hero_step_100. %% check race usable
max_count_exceeded(race,MAX) :- COUNT=#count{ R:race(R) }, MAX=#max{ MC:max_count(race,MC) }, COUNT > MAX.


#program validate_hero_step_150. %% check race requirements
% WARNINGS
missing_usual(race(R),culture(C)) :- race(R), has_usual(race(R),culture(_)), culture(C), not has_usual(race(R),culture(C)).


#program validate_hero_step_200. %% check culture usable
max_count_exceeded(culture,MAX) :- COUNT=#count{ C:culture(C) }, MAX=#max{ MC:max_count(culture,MC) }, COUNT > MAX.
unusable_by(culture(C),race(R)) :- culture(C), requires(culture(C),race(_)), race(R), not requires(culture(C),race(R)).


#program validate_hero_step_250. %% check culture requirements


#program validate_hero_step_300. %% check profession usable
max_count_exceeded(profession,MAX) :- COUNT=#count{ P:profession(P) }, MAX=#max{ MC:max_count(profession,MC) }, COUNT > MAX.
unusable_by(profession(P),race(R)) :- profession(P), requires(profession(P),race(_)), race(R), not requires(profession(P),race(R)).
unusable_by(profession(P),culture(C)) :- profession(P), requires(profession(P),culture(_)), culture(C), not requires(profession(P),culture(C)).


#program validate_hero_step_350. %% check profession requirements
missing_level(profession(P),talent(T,MIN_LVL)) :- profession(P), requires(profession(P),talent(T,MIN_LVL)), 1 = #count{ 1: not talent(T,_) ; 1: talent(T,LVL), LVL < MIN_LVL }.
missing_level(profession(P),combat_technique(CT,MIN_LVL)) :- profession(P), requires(profession(P),combat_technique(CT,MIN_LVL)), 1 = #count{ 1: not combat_technique(CT,_) ; 1: combat_technique(CT,LVL), LVL < MIN_LVL }.
missing_level(profession(P),combat_technique(any_of(CHOICES,CTs),MIN_LVL)) :- profession(P), requires(profession(P),any_of(CHOICES,combat_technique,CTs,MIN_LVL)), CHOICES > @count_by("combat_techniques",CTs,MIN_LVL).


#program validate_hero_step_400. %% check (dis)advantage usable


#program validate_hero_step_450. %% check (dis)advantage requirements
missing(race(R),advantage(A,USES,LVL)) :- race(R), requires(race(R),advantage(A,USES,LVL)), not advantage(A,USES,LVL).
missing(race(R),disadvantage(DA,USES,LVL)) :- race(R), requires(race(R),disadvantage(DA,USES,LVL)), not disadvantage(DA,USES,LVL).
% WARNINGS
missing_typical(race(R),advantage(A,USES,LVL)) :- race(R), has_typical(race(R),advantage(A,USES,LVL)), not advantage(A,USES,LVL).
missing_typical(race(R),disadvantage(DA,USES,LVL)) :- race(R), has_typical(race(R),disadvantage(DA,USES,LVL)), not disadvantage(DA,USES,LVL).
atypical(race(R),advantage(A,USES)) :- race(R), has_atypical(race(R),advantage(A,USES,_)), advantage(A,USES,_).
atypical(race(R),disadvantage(DA,USES)) :- race(R), has_atypical(race(R),disadvantage(DA,USES,_)), disadvantage(DA,USES,_).


#program validate_hero_step_500. %% check skills (talents, combat techniques) usable
missing_min_lvl(talent(T,LVL),MIN) :- talent(T,LVL), MIN=0, LVL < MIN.
missing_min_lvl(combat_technique(CT,LVL),MIN) :- combat_technique(CT,LVL), MIN=0, LVL < MIN.
max_lvl_exceeded(talent(T,LVL),MAX_LVL) :- experience_level(EL), known_experience_level(EL,_,MAX_LVL,_,_,_,_), talent(T,LVL), LVL > MAX_LVL.
max_lvl_exceeded(combat_technique(CT,LVL),MAX_LVL) :- experience_level(EL), known_experience_level(EL,_,_,MAX_LVL,_,_,_), combat_technique(CT,LVL), LVL > MAX_LVL.


#program validate_hero_step_550. %% check skills (talents, combat techniques) requirements

