%#program validate_hero.
%%% [ermittel Spezies der Kultur]
%culture_species("Elf") :- {
%    culture("Auelfen";"Firnelfen";"Steppenelfen";"Waldelfen")
%} = 1.
%culture_species("Mensch") :- {
%    culture(
%        "Andergaster";"Aranier";"Bornländer";"Ferkinas";"Fjarninger";"Gjalsker";"Horasier";"Koboldweltler";"Maraskaner";
%        "Menschlichekultur";"Mhanadistani";"Mittelreicher";"Mohas";"Nivesen";"Norbarden";"Nordaventurier";"Nostrier";"Novadis";
%        "Svellttaler";"Südaventurier";"Thorwaler";"Trollzacker";"Zahori";"Zyklopäer"
%    )
%} = 1.
%culture_species("Zwerg") :- {
%    culture("Ambosszwerge";"Brillantzwerge";"Erzzwerge";"Hügelzwerge";"Wildzwerge")
%} = 1.
%
%
%%% Regel: Kultur muss bekannt sein (bekannt wenn map'bar).
%:- not culture_species("Elf"), not culture_species("Mensch"), not culture_species("Zwerg").
%
%
%%% Regel: Spezies und culture passen zusammen (prüft indirekt dass Spezies bekannt ist)
%{species(KS) : culture_species(S)} = 1 :- species(S), culture_species(KS).
%
