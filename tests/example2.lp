%#program base.
%% [Fakten des Helden]
species(@_species).
culture(@_culture).

%#program check_culture.
%% [ermittel Spezies der Kultur]
culture_species("Elf") :- {
    culture("Auelfen"); culture("Firnelfen"); culture("Steppenelfen"); culture("Waldelfen")
} = 1.
culture_species("Mensch") :- {
    culture("Andergaster"); culture("Aranier"); culture("Bornländer"); culture("Ferkinas"); culture("Fjarninger");
    culture("Gjalsker"); culture("Horasier"); culture("Koboldweltler"); culture("Maraskaner"); culture("Menschlichekultur");
    culture("Mhanadistani"); culture("Mittelreicher"); culture("Mohas"); culture("Nivesen"); culture("Norbarden");
    culture("Nordaventurier"); culture("Nostrier"); culture("Novadis"); culture("Svellttaler"); culture("Südaventurier");
    culture("Thorwaler"); culture("Trollzacker"); culture("Zahori"); culture("Zyklopäer")
} = 1.
culture_species("Zwerg") :- {
    culture("Ambosszwerge"); culture("Brillantzwerge"); culture("Erzzwerge"); culture("Hügelzwerge"); culture("Wildzwerge")
} = 1.
%% Regel: Kultur muss bekannt sein (bekannt wenn map'bar).
:- not culture_species("Elf"), not culture_species("Mensch"), not culture_species("Zwerg").
%% Regel: Spezies und culture passen zusammen
{species(KS) : culture_species(S)} = 1 :- species(S), culture_species(KS).
