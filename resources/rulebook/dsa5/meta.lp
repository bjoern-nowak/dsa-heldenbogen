#program rulebook_usable.
%% make presence of this rulebook available for others
rulebook("dsa5").
%% this rulebook depends on nothing


#program base.
culture_requires_species(("Auelfen";"Firnelfen";"Steppenelfen";"Waldelfen"),"Elf").
culture_requires_species(
    ("Andergaster";"Aranier";"Bornländer";"Ferkinas";"Fjarninger";"Gjalsker";"Horasier";"Koboldweltler";"Maraskaner";"Menschlichekultur";"Mhanadistani";"Mittelreicher";"Mohas";"Nivesen";"Norbarden";"Nordaventurier";"Nostrier";"Novadis";"Svellttaler";"Südaventurier";"Thorwaler";"Trollzacker";"Zahori";"Zyklopäer"),
    "Mensch"
).
culture_requires_species(("Ambosszwerge";"Brillantzwerge";"Erzzwerge";"Hügelzwerge";"Wildzwerge"),"Zwerg").
profession_requires_species(("Zauberweber";"Wildnisläuferin"),"Elf").
known_profession(("Söldner";"Händler")).
%% TODO make below better in modelling, may use tuples with pooling
profession_requires_talent("Söldner", "Körperbeherrschung", 3).
profession_requires_talent("Söldner", "Kraftakt", 3).
profession_requires_talent("Söldner", "Selbstbeherrschung", 4).
profession_requires_talent("Söldner", "Zechen", 5).
profession_requires_talent("Söldner", "Menschenkenntnis", 3).
profession_requires_talent("Söldner", "Überreden", 3).
profession_requires_talent("Söldner", "Orientierung", 4).
profession_requires_talent("Söldner", "Wildnisleben", 3).
profession_requires_talent("Söldner", "Götter & Kulte", 3).
profession_requires_talent("Söldner", "Kriegskunst", 6).
profession_requires_talent("Söldner", "Sagen & Legenden", 5).
profession_requires_talent("Söldner", "Handel", 3).
profession_requires_talent("Söldner", "Heilkunde Wunden", 4).
