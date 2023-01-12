%% [ermittel Spezies der Kultur]
kultur_spezies("Elf") :- {
    kultur("Auelfen"); kultur("Firnelfen"); kultur("Steppenelfen"); kultur("Waldelfen")
} = 1.
kultur_spezies("Mensch") :- {
    kultur("Andergaster"); kultur("Aranier"); kultur("Bornländer"); kultur("Ferkinas"); kultur("Fjarninger");
    kultur("Gjalsker"); kultur("Horasier"); kultur("Koboldweltler"); kultur("Maraskaner"); kultur("Menschlichekultur");
    kultur("Mhanadistani"); kultur("Mittelreicher"); kultur("Mohas"); kultur("Nivesen"); kultur("Norbarden");
    kultur("Nordaventurier"); kultur("Nostrier"); kultur("Novadis"); kultur("Svellttaler"); kultur("Südaventurier");
    kultur("Thorwaler"); kultur("Trollzacker"); kultur("Zahori"); kultur("Zyklopäer")
} = 1.
kultur_spezies("Zwerg") :- {
    kultur("Ambosszwerge"); kultur("Brillantzwerge"); kultur("Erzzwerge"); kultur("Hügelzwerge"); kultur("Wildzwerge")
} = 1.
%% Regel: Kultur muss bekannt sein (bekannt wenn map'bar).
:- not kultur_spezies("Elf"), not kultur_spezies("Mensch"), not kultur_spezies("Zwerg").
%% Regel: Spezies und kultur passen zusammen (prüft indirekt dass Spezies bekannt ist)
%% TODO is this correct ?
{spezies(KS) : kultur_spezies(S)} = 1 :- spezies(S), kultur_spezies(KS).
