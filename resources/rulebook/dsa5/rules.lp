#program world_facts.
program("world_facts").
requires(race("Elfen"),advantage("Zauberer","",1;"Zweistimmiger Gesang","",1)).
% TODO [3] 'Elfen' does not hard-requires below (dis)advantages but these are strongly recommended, we need some extra result type, maybe: error > warning > note/hint, were warning is for such and note/hint for typical/usual
requires(race("Elfen"),advantage("Altersresistenz","",1;"Dunkelsicht","",1;"Nichtschläfer","",1)).
requires(race("Elfen"),disadvantage("Sensibler Geruchssinn","",1;"Unfähig","Zechen",1;)).
%
has_usual(race("Elfen"),culture("Auelfen";"Firnelfen";"Waldelfen")).
% TODO make "Herausragender Sinn",any_of(1,"Gehör","Sicht"),1;
has_typical(race("Elfen"),advantage("Begabung",("Singen";"Musizieren"),1;"Beidhändig","",1;"Dunkelsicht","",2;"Flink","",1;"Giftresistenz","",1;"Gutaussehend","",1;"Herausragender Sinn",("Gehör";"Sicht"),1;"Immunität",("Schwarze Wut";"Tollwut";"Lykanthropie"),1;"Krankheitsresistenz","",1;"Richtungssinn","",1;"Schlangenmensch","",1;"Verbesserte Regeneration","Astralenergie",1;"Wohlklang","",1)).
has_typical(race("Elfen"),disadvantage("Körpergebundene Kraft","",1;"Lästige Mindergeister","",1;"Wahrer Name","",1)).
has_atypical(race("Elfen"),advantage("Hitzeresistenz","",1;"Schwer zu verzaubern","",1;"Zwergennase","",1)).
has_atypical(race("Elfen"),disadvantage("Blutrausch","",1;"Eingeschränkter Sinn","",1;"Fettleibig","",1;"Nachtblind","",1)).


has_usual(race("Halbelfen"),culture("Andergaster";"Auelfen";"Bornländer";"Firnelfen";"Horasier";"Mittelreicher";"Nivesen";"Nordaventurier";"Nostrier";"Svellttaler";"Thorwaler";"Waldelfen")).
% TODO make "Herausragender Sinn",any_of(1,"Gehör","Sicht"),1;
has_typical(race("Halbelfen"),advantage("Begabung",("Singen";"Musizieren"),1;"Beidhändig","",1;"Dunkelsicht","",1;"Flink","",1;"Gutaussehend","",1;"Herausragender Sinn",("Gehör";"Sicht"),1;"Schlangenmensch","",1;"Wohlklang","",1;"Zauberer","",1;"Zweistimmiger Gesang","",1)).
has_typical(race("Halbelfen"),disadvantage("Sensibler Geruchssinn","",1;"Wahrer Name","",1)).
has_atypical(race("Halbelfen"),advantage("Schwer zu verzaubern","",1;"Zwergennase","",1)).
has_atypical(race("Halbelfen"),disadvantage("Blutrausch","",1;"Fettleibig","",1;"Krankheitsanfällig","",1)).


%% TODO 'Mensch' have a kind of origin: like a 'Thorwalder' which would change the usual/typical cultures and (dis)advantages
has_usual(race("Mensch"),culture("Andergaster";"Aranier";"Bornländer";"Fjarninger";"Horasier";"Maraskaner";"Mhanadistani";"Mittelreicher";"Mohas";"Nivesen";"Norbarden";"Nordaventurier";"Nostrier";"Novadis";"Svellttaler";"Südaventurier";"Thorwaler";"Zyklopäer")).
has_typical(race("Mensch"),advantage("Entfernungssinn","",1;"Kälteresistenz","",1;"Hohe Zähigkeit","",1;"Zäher Hund","",1;"Hitzeresistenz","",1;"Angenehmer Geruch","",1;"Hitzeresistenz","",1;"Immunität",("Wurara";"Flinken Difar";"Brabaker Schweiß"),1)).
has_typical(race("Mensch"),disadvantage("Hitzeempfindlich","",1;"Blutrausch","",1;"Niedrige Seelenkraft","",1;"Kälteempfindlich","",1)).


% TODO [3] 'Zwerg' does not hard-requires below (dis)advantages but these are strongly recommended, we need some extra result type, maybe: error > warning > note/hint, were warning is for such and note/hint for typical/usual
requires(race("Zwerg"),advantage("Dunkelsicht","",1;"Immunität","Tulmadron",1)).
requires(race("Zwerg"),disadvantage("Unfähig","Schwimmen",1)).
%
has_usual(race("Zwerg"),culture("Ambosszwerge";"Brillantzwerge";"Erzzwerge";"Hügelzwerge")).
has_typical(race("Zwerg"),advantage("Dunkelsicht","",2;"Hitzeresistenz","",1;"Hohe Zähigkeit","",1;"Krankheitsresistenz","",1;"Richtungssinn","",1;"Schwer zu verzaubern","",1;"Zäher Hund","",1;"Zwergennase","",1)).
has_typical(race("Zwerg"),disadvantage("Blutrausch","",1)).
has_atypical(race("Zwerg"),advantage("Schlangenmensch","",1;"Wohlklang","",1;"Zauberer","",1)).
has_atypical(race("Zwerg"),disadvantage("Hitzeempfindlich","",1;"Nachtblind","",1;"Niedrige Seelenkraft","",1;"Niedrige Zähigkeit","",1;"Zerbrechlich","",1)).


requires(culture("Auelfen";"Firnelfen";"Steppenelfen";"Waldelfen"),race("Elfen")).
requires(culture("Andergaster";"Aranier";"Bornländer";"Ferkinas";"Fjarninger";"Gjalsker";"Horasier";"Koboldweltler";"Maraskaner";"Menschlichekultur";"Mhanadistani";"Mittelreicher";"Mohas";"Nivesen";"Norbarden";"Nordaventurier";"Nostrier";"Novadis";"Svellttaler";"Südaventurier";"Thorwaler";"Trollzacker";"Zahori";"Zyklopäer"),race("Mensch")).
requires(culture("Ambosszwerge";"Brillantzwerge";"Erzzwerge";"Hügelzwerge";"Wildzwerge"),race("Zwerg")).

has_usual(culture("Auelfen"),profession("Wildnisläufer";"Zauberweber")).
%% TODO culture 'Auelfen' has many (a)typical (dis)advantages for an category of talents: how do we implement this


requires(profession("Söldner"),talent("Körperbeherrschung",3;"Kraftakt",3;"Selbstbeherrschung",4;"Zechen",5;"Menschenkenntnis",3;"Überreden",3;"Orientierung",4;"Wildnisleben",3;"Götter & Kulte",3;"Kriegskunst",6;"Sagen & Legenden",5;"Handel",3;"Heilkunde Wunden",4)).
requires(profession("Söldner"),combat_technique("Armbrüste",10;"Raufen",10)).
requires(profession("Söldner"),any_of(1,combat_technique,("Hiebwaffen","Schwerter","Stangenwaffen","Zweihandschwerter","Zweihandhiebwaffen"),10)).
requires(profession("Zauberweber";"Wildnisläuferin"),race("Elfen")).
requires(profession("Zauberweber"),talent("Körperbeherrschung",4;"Schwimmen",4;"Singen",5;"Willenskraft",3;"Fährtensuchen",4;"Orientierung",3;"Pflanzenkunde",5;"Wildnisleben",4;"Geschichtswissen",4;"Götter & Kulte",4;"Magiekunde",5;"Sternkunde",5;"Musizieren",7)).
