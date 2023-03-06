#program rulebook_usable.
%% make presence of this rulebook available for others
rulebook("dsa5").
%% this rulebook depends on nothing


#program base.
requires(culture("Auelfen";"Firnelfen";"Steppenelfen";"Waldelfen"),species("Elf")).
requires(
    culture("Andergaster";"Aranier";"Bornländer";"Ferkinas";"Fjarninger";"Gjalsker";"Horasier";"Koboldweltler";"Maraskaner";"Menschlichekultur";"Mhanadistani";"Mittelreicher";"Mohas";"Nivesen";"Norbarden";"Nordaventurier";"Nostrier";"Novadis";"Svellttaler";"Südaventurier";"Thorwaler";"Trollzacker";"Zahori";"Zyklopäer"),
    species("Mensch")
).
requires(culture("Ambosszwerge";"Brillantzwerge";"Erzzwerge";"Hügelzwerge";"Wildzwerge"),species("Zwerg")).
known_profession("Händler").
requires(profession("Söldner"),talent("Körperbeherrschung",3;"Kraftakt",3;"Selbstbeherrschung",4;"Zechen",5;"Menschenkenntnis",3;"Überreden",3;"Orientierung",4;"Wildnisleben",3;"Götter & Kulte",3;"Kriegskunst",6;"Sagen & Legenden",5;"Handel",3;"Heilkunde Wunden",4)).
requires(profession("Söldner"),combat_technique("Armbrüste",10;"Raufen",10)).
requires(profession("Söldner"),any_of(1,combat_technique,("Hiebwaffen","Schwerter","Stangenwaffen","Zweihandschwerter","Zweihandhiebwaffen"),10)).
requires(profession("Zauberweber";"Wildnisläuferin"),species("Elf")).
requires(profession("Zauberweber"),talent("Körperbeherrschung",4;"Schwimmen",4;"Singen",5;"Willenskraft",3;"Fährtensuchen",4;"Orientierung",3;"Pflanzenkunde",5;"Wildnisleben",4;"Geschichtswissen",4;"Götter & Kulte",4;"Magiekunde",5;"Sternkunde",5;"Musizieren",7)).