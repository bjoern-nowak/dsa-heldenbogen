#program world_facts.
program("world_facts").

known_experience_level("exp_lvl_1",1,1,1,1,1,1).
known_race("race_1";"race_2").
known_culture("culture_1";"culture_2";"culture_3").
known_profession("profession_1").
known_advantage("advantage_1","",(1..2)).
known_advantage("advantage_2",("advantage_2_ref1";"advantage_2_ref2"),1).
known_disadvantage(("disadvantage_1";"disadvantage_3"),"",1).
known_disadvantage("disadvantage_2","disadvantage_2_ref",1).
known_talent("talent_1";"talent_2").
known_combat_technique("combat_technique_1").
