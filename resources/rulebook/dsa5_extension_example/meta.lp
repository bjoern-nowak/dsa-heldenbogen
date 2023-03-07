#program rulebook_usable.
rulebook("dsa5_extension_example").
% this rulebook actually does not need the base dsa5


#program meta.
%% this rulebook declares that it has an extra hero validation step to be executed
extra_hero_validation_step(175).


#program validate_hero_step_175.
%% this program/step gets executed in order, so it will be between the defaults 150 and 200