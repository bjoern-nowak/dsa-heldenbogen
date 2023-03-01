%rulebook("A").
rulebook("B").
rulebook_depends("B","A").

%:- rulebook_depends(X,Y), rulebook(X), not rulebook(Y).
rulebook_unusable(X) :- rulebook_depends(X,Y), rulebook(X), not rulebook(Y).

%:- rulebook_unusable(_).
