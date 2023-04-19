#program rulebook_usable.
program("rulebook_usable").
%% make presence of this rulebook available for others
rulebook("dsa5").
%% this rulebook depends on nothing


#program world_facts.
program("world_facts").

% CC := MAX_CHARACTERISTIC_LVL (only on character creation)
% S := MAX_SKILL_LVL
% CT := MAX_COMBAT_TECHNIQUE_LVL
% CCP := MAX_CHARACTERISTIC_POINTS
% SL := MAX_SPELLS_AND_LITURGIES
% FS := MAX_FOREIGN_SPELL
%                                          CC  S   CT  CCP  SL  FS
known_experience_level("Unerfahren",       12, 10,  8,  95,  8, 0 ).
known_experience_level("Durchschnittlich", 13, 10, 10,  98, 10, 1 ).
known_experience_level("Erfahren",         14, 10, 12, 100, 12, 2 ).
known_experience_level("Kompetent",        15, 13, 14, 102, 14, 3 ).
known_experience_level("Meisterlich",      16, 16, 16, 105, 16, 4 ).
known_experience_level("Brillant",         17, 19, 18, 109, 18, 5 ).
known_experience_level("Legendär",         18, 20, 20, 114, 20, 6 ).

known_race("Elfen";"Halbelfen";"Mensch";"Zwerg").
known_culture("Auelfen";"Firnelfen";"Steppenelfen";"Waldelfen";"Andergaster";"Aranier";"Bornländer";"Ferkinas";"Fjarninger";"Gjalsker";"Horasier";"Koboldweltler";"Maraskaner";"Menschlichekultur";"Mhanadistani";"Mittelreicher";"Mohas";"Nivesen";"Norbarden";"Nordaventurier";"Nostrier";"Novadis";"Svellttaler";"Südaventurier";"Thorwaler";"Trollzacker";"Zahori";"Zyklopäer";"Ambosszwerge";"Brillantzwerge";"Erzzwerge";"Hügelzwerge";"Wildzwerge").
known_profession("Händler";"Söldner";"Zauberweber";"Wildnisläuferin").
known_advantage("Begabung",("Singen";"Musizieren"),1).
known_advantage(("Beidhändig";"Zauberer";"Zweistimmiger Gesang";"Flink";"Giftresistenz";"Gutaussehend";"Altersresistenz";"Nichtschläfer";"Krankheitsresistenz";"Richtungssinn";"Schlangenmensch";"Wohlklang";"Hitzeresistenz";"Schwer zu verzaubern";"Zwergennase";"Entfernungssinn";"Kälteresistenz";"Hohe Zähigkeit";"Zäher Hund";"Angenehmer Geruch";"Geweihter"),"",1).
known_advantage("Dunkelsicht","",(1..2)).
known_advantage("Verbesserte Regeneration","Astralenergie",1).
known_advantage("Herausragender Sinn",("Gehör";"Sicht"),1).
known_advantage("Immunität",("Tulmadron";"Wurara";"Flinken Difar";"Brabaker Schweiß";"Schwarze Wut";"Tollwut";"Lykanthropie"),1).
known_disadvantage(("Körpergebundene Kraft";"Lästige Mindergeister";"Wahrer Name";"Blutrausch";"Eingeschränkter Sinn";"Fettleibig";"Nachtblind";"Sensibler Geruchssinn";"Krankheitsanfällig";"Hitzeempfindlich";"Niedrige Seelenkraft";"Kälteempfindlich";"Niedrige Zähigkeit";"Zerbrechlich"),"",1).
known_disadvantage("Unfähig",("Zechen";"Schwimmen"),1).
known_disadvantage(("Prinzipientreue";"Verpflichtungen"),"",(1..3)).
known_talent("Körperbeherrschung";"Kraftakt";"Selbstbeherrschung";"Sinnesschärfe";"Bekehren & Überzeugen";"Zechen";"Menschenkenntnis";"Überreden";"Orientierung";"Wildnisleben";"Götter & Kulte";"Kriegskunst";"Sagen & Legenden";"Handel";"Heilkunde Wunden";"Schwimmen";"Singen";"Willenskraft";"Fährtensuchen";"Pflanzenkunde";"Geschichtswissen";"Magiekunde";"Sternkunde";"Musizieren";"Einschüchtern";"Etikette";"Tierkunde";"Rechnen";"Rechtskunde";"Heilkunde Krankheiten";"Heilkunde Seele").
known_combat_technique("Armbrüste";"Raufen";"Hiebwaffen";"Schwerter";"Stangenwaffen";"Zweihandschwerter";"Zweihandhiebwaffen";"Wurfwaffen").

max_count(race,1).
max_count(culture,1).
max_count(profession,1).
