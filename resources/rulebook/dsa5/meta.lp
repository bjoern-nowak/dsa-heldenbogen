#program rulebook_usable.
%% make presence of this rulebook available for others
rulebook("dsa5").
%% this rulebook depends on nothing


#program world_facts.
known_species("Elfen";"Mensch";"Zwerg").
known_culture("Auelfen";"Firnelfen";"Steppenelfen";"Waldelfen";"Andergaster";"Aranier";"Bornländer";"Ferkinas";"Fjarninger";"Gjalsker";"Horasier";"Koboldweltler";"Maraskaner";"Menschlichekultur";"Mhanadistani";"Mittelreicher";"Mohas";"Nivesen";"Norbarden";"Nordaventurier";"Nostrier";"Novadis";"Svellttaler";"Südaventurier";"Thorwaler";"Trollzacker";"Zahori";"Zyklopäer";"Ambosszwerge";"Brillantzwerge";"Erzzwerge";"Hügelzwerge";"Wildzwerge").
known_profession("Händler";"Söldner";"Zauberweber";"Wildnisläuferin").
known_advantage("Begabung",("Singen";"Musizieren"),1).
known_advantage("Beidhändig","",1).
known_advantage("Dunkelsicht","",(1..2)).
known_disadvantage(("Körpergebundene Kraft";"Lästige Mindergeister";"Wahrer Name"),"",1).
known_talent("Körperbeherrschung";"Kraftakt";"Selbstbeherrschung";"Sinnesschärfe";"Bekehren & Überzeugen";"Zechen";"Menschenkenntnis";"Überreden";"Orientierung";"Wildnisleben";"Götter & Kulte";"Kriegskunst";"Sagen & Legenden";"Handel";"Heilkunde Wunden";"Körperbeherrschung";"Schwimmen";"Singen";"Willenskraft";"Fährtensuchen";"Pflanzenkunde";"Geschichtswissen";"Magiekunde";"Sternkunde";"Musizieren";"Einschüchtern";"Etikette";"Tierkunde";"Rechnen";"Rechtskunde";"Heilkunde Krankheiten";"Heilkunde Seele").
known_combat_technique("Armbrüste";"Raufen";"Hiebwaffen";"Schwerter";"Stangenwaffen";"Zweihandschwerter";"Zweihandhiebwaffen").
