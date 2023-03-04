#program rulebook_usable.
%% make presence of this rulebook available for others
rulebook("dsa5").
%% this rulebook depends on nothing


#program base.
culture_requires_species(
    ("Auelfen";"Firnelfen";"Steppenelfen";"Waldelfen"),
    "Elf"
).
culture_requires_species(
    ("Andergaster";"Aranier";"Bornländer";"Ferkinas";"Fjarninger";"Gjalsker";"Horasier";"Koboldweltler";"Maraskaner";"Menschlichekultur";"Mhanadistani";"Mittelreicher";"Mohas";"Nivesen";"Norbarden";"Nordaventurier";"Nostrier";"Novadis";"Svellttaler";"Südaventurier";"Thorwaler";"Trollzacker";"Zahori";"Zyklopäer"),
    "Mensch"
).
culture_requires_species(
    ("Ambosszwerge";"Brillantzwerge";"Erzzwerge";"Hügelzwerge";"Wildzwerge"),
    "Zwerg"
).
profession_requires_species(("Zauberweber";"Wildnisläuferin"),"Elf").
known_profession(("Söldner";"Händler")).
