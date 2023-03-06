#program rulebook_usable.
rulebook("dsa5_aventurisches_götterwirken_2").
rulebook_depends("dsa5_aventurisches_götterwirken_2", "dsa5").


#program base.
profession_requires_culture("Skuldrun","Fjarninger").
profession_requires_culture("Säbeltänzerin",("Aranier";"Mhanadistani")).
profession_requires_talent(
    "Skuldrun","Körperbeherrschung",4;"Skuldrun","Kraftakt",6;"Skuldrun","Selbstbeherrschung",4;"Skuldrun","Sinnesschärfe",4;"Skuldrun","Bekehren & Überzeugen",2;"Skuldrun","Einschüchtern",2;"Skuldrun","Etikette",4;"Skuldrun","Menschenkenntnis",4;"Skuldrun","Willenskraft",4;"Skuldrun","Orientierung",4;"Skuldrun","Pflanzenkunde",2;"Skuldrun","Tierkunde",4;"Skuldrun","Wildnisleben",4;"Skuldrun","Geschichtswissen",4;"Skuldrun","Götter & Kulte",5;"Skuldrun","Rechnen",2;"Skuldrun","Rechtskunde",5;"Skuldrun","Sagen & Legenden",6;"Skuldrun","Heilkunde Krankheiten",4;"Skuldrun","Heilkunde Seele",4;"Skuldrun","Heilkunde Wunden",3;
).
