#program world_facts.
requires(species("Elfen"),advantage("Zauberer";"Zweistimmiger Gesang")).
requires(culture("Auelfen";"Firnelfen";"Steppenelfen";"Waldelfen"),species("Elfen")).
requires(culture("Andergaster";"Aranier";"Bornländer";"Ferkinas";"Fjarninger";"Gjalsker";"Horasier";"Koboldweltler";"Maraskaner";"Menschlichekultur";"Mhanadistani";"Mittelreicher";"Mohas";"Nivesen";"Norbarden";"Nordaventurier";"Nostrier";"Novadis";"Svellttaler";"Südaventurier";"Thorwaler";"Trollzacker";"Zahori";"Zyklopäer"),species("Mensch")).
requires(culture("Ambosszwerge";"Brillantzwerge";"Erzzwerge";"Hügelzwerge";"Wildzwerge"),species("Zwerg")).
requires(profession("Söldner"),talent("Körperbeherrschung",3;"Kraftakt",3;"Selbstbeherrschung",4;"Zechen",5;"Menschenkenntnis",3;"Überreden",3;"Orientierung",4;"Wildnisleben",3;"Götter & Kulte",3;"Kriegskunst",6;"Sagen & Legenden",5;"Handel",3;"Heilkunde Wunden",4)).
requires(profession("Söldner"),combat_technique("Armbrüste",10;"Raufen",10)).
requires(profession("Söldner"),any_of(1,combat_technique,("Hiebwaffen","Schwerter","Stangenwaffen","Zweihandschwerter","Zweihandhiebwaffen"),10)).
requires(profession("Zauberweber";"Wildnisläuferin"),species("Elfen")).
requires(profession("Zauberweber"),talent("Körperbeherrschung",4;"Schwimmen",4;"Singen",5;"Willenskraft",3;"Fährtensuchen",4;"Orientierung",3;"Pflanzenkunde",5;"Wildnisleben",4;"Geschichtswissen",4;"Götter & Kulte",4;"Magiekunde",5;"Sternkunde",5;"Musizieren",7)).
has_usual(species("Elfen"),culture("Auelfen";"Firnelfen";"Waldelfen")).
has_usual(species("Zwerg"),culture("Ambosszwerge";"Brillantzwerge";"Erzzwerge";"Hügelzwerge")).
has_typical(species("Elfen"),advantage("Begabung","Singen",1;"Begabung","Musizieren",1;"Beidhändig","",1;"Dunkelsicht","",2)).
has_typical(species("Elfen"),disadvantage("Körpergebundene Kraft","",1;"Lästige Mindergeister","",1;"Wahrer Name","",1)).
has_atypical(species("Elfen"),disadvantage("Blutrausch","",1;"Eingeschränkter Sinn","",1;"Fettleibig","",1;"Nachtblind","",1)).
