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
profession_requires_talent(
    "Söldner","Körperbeherrschung",3;"Söldner","Kraftakt",3;"Söldner","Selbstbeherrschung",4;"Söldner","Zechen",5;"Söldner","Menschenkenntnis",3;"Söldner","Überreden",3;"Söldner","Orientierung",4;"Söldner","Wildnisleben",3;"Söldner","Götter & Kulte",3;"Söldner","Kriegskunst",6;"Söldner","Sagen & Legenden",5;"Söldner","Handel",3;"Söldner","Heilkunde Wunden",4;
    "Zauberweber","Körperbeherrschung",4;"Zauberweber","Schwimmen",4;"Zauberweber","Singen",5;"Zauberweber","Willenskraft",3;"Zauberweber","Fährtensuchen",4;"Zauberweber","Orientierung",3;"Zauberweber","Pflanzenkunde",5;"Zauberweber","Wildnisleben",4;"Zauberweber","Geschichtswissen",4;"Zauberweber","Götter & Kulte",4;"Zauberweber","Magiekunde",5;"Zauberweber","Sternkunde",5;"Zauberweber","Musizieren",7;
).
profession_requires_combat_technique(
    "Söldner","Armbrüste",10;"Söldner","Raufen",10;
).
