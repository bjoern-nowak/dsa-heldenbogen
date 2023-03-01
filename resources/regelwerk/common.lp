
#program is_usable.
rulebook_unusable(X,Y) :- rulebook_depends(X,Y), rulebook(X), not rulebook(Y).