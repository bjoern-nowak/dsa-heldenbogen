#program rulebook_usable.
%% make presence of this rulebook available for others
rulebook("dsa5").
%% this rulebook depends on nothing


#program base.
culture_requires_species("Elf",("Auelfen";"Firnelfen";"Steppenelfen";"Waldelfen")).
culture_requires_species("Mensch",("Andergaster";"Aranier";"Bornländer";"Ferkinas";"Fjarninger";"Gjalsker";"Horasier";"Koboldweltler";"Maraskaner";"Menschlichekultur";"Mhanadistani";"Mittelreicher";"Mohas";"Nivesen";"Norbarden";"Nordaventurier";"Nostrier";"Novadis";"Svellttaler";"Südaventurier";"Thorwaler";"Trollzacker";"Zahori";"Zyklopäer")).
culture_requires_species("Zwerg",("Ambosszwerge";"Brillantzwerge";"Erzzwerge";"Hügelzwerge";"Wildzwerge")).
profession_requires_species("Elf",("Zauberweber";"Wildnisläuferin")).
known_profession("Söldner").
