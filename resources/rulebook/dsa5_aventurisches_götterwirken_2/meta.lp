#program rulebook_usable.
rulebook("dsa5_aventurisches_götterwirken_2").
rulebook_depends("dsa5_aventurisches_götterwirken_2", "dsa5").


#program base.
profession_requires_culture("Skuldrun","Fjarninger").
profession_requires_culture("Säbeltänzerin",("Aranier";"Mhanadistani")).

