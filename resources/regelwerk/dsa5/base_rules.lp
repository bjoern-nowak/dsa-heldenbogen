%% [ermittel Spezies der Kultur]
kultur_spezies("Elf") :- {
    kultur("Auelfen";"Firnelfen";"Steppenelfen";"Waldelfen")
} = 1.
kultur_spezies("Mensch") :- {
    kultur(
        "Andergaster";"Aranier";"Bornländer";"Ferkinas";"Fjarninger";"Gjalsker";"Horasier";"Koboldweltler";"Maraskaner";
        "Menschlichekultur";"Mhanadistani";"Mittelreicher";"Mohas";"Nivesen";"Norbarden";"Nordaventurier";"Nostrier";"Novadis";
        "Svellttaler";"Südaventurier";"Thorwaler";"Trollzacker";"Zahori";"Zyklopäer"
    )
} = 1.
kultur_spezies("Zwerg") :- {
    kultur("Ambosszwerge";"Brillantzwerge";"Erzzwerge";"Hügelzwerge";"Wildzwerge")
} = 1.


%% Regel: Kultur muss bekannt sein (bekannt wenn map'bar).
:- not kultur_spezies("Elf"), not kultur_spezies("Mensch"), not kultur_spezies("Zwerg").
%% TODO return fail reason culture is not known

%% Regel: Spezies und kultur passen zusammen (prüft indirekt dass Spezies bekannt ist)
{spezies(KS) : kultur_spezies(S)} = 1 :- spezies(S), kultur_spezies(KS).
%% TODO return fail reason culture not allowed for species
