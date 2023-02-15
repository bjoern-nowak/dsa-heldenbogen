%%
%% This is a quick cheatsheet about clingo/gringo language
%%  it is not complete nor states all restrictions
%% See 'Potassco: User Guide' (source of some examples) for a complete guide.
%%  https://github.com/potassco/guide/releases/tag/v2.2.0
%%


%%-----------------------------------------------------------------------------
%% basic semantic
%%-----------------------------------------------------------------------------
%% HEAD :- ATOM.
%% TODO improve this part


%% a FACT: it rains
rain.

%% a RULE: umbrella if rain and outdoor
umbrella :- rain, outdoor.

%%% INTEGRITY CONSTRAINT filters solution candidates: body shall not be satisfied
%% keep candidate if: no umbrella but outdoor
:- umbrella, not outdoor


%%-----------------------------------------------------------------------------
%% language basics
%%-----------------------------------------------------------------------------

%% line comment start with an %
%% block and inline comments starts with %* and ends with *%


%%
%% --- INTEGERS
%%
1


%%
%% --- CONSTANTS
%%
starts_lowercase
_underscorePreventNameClashes
%%
%% --- SPECIAL CONSTANTS
%% greatest and smallest element among all variable-free terms
%%
#sup
#inf
%%
%% --- BOOLEAN CONSTANTS
%%
#true
#false


%%
%% --- VARIABLE
%%
Starts_uppercase
_UnderscorePreventNameClashes
%%
%% --- ANONYMOUS VARIABLE
%%
_


%%
%% --- STRING
%%
"string"
%% escapes for backslash, newline and double quote
"\\"
"\n"
"\""


%% --- (UNINTERPRETED) FUNCTIONS
%%
%% example with three arguments
functionName(constant,function(123),Variable)
%%
%% --- TUPLES
%% are functions without names
%%
()
(functionName,constant,function(123),Variable)
%% declares grade of tuple by ending with an ',' (comma): example is a quadruple
(a,b,c,d,)


%%
%% --- INTERVALS
%%
%% in body: expanded disjunctively
num(1..3).
%% result: num(1). num(2). num(3).
%%
%% in head: expanded conjunctively
%% having: size(2).
grid(1..S,1..S) :- size(S).
%% result: grid(1,1). grid(1,2). grid(2,2). grid(2,1).
%% which is same as (using unification):
grid(X,Y) :- X = 1..S, Y = 1..S, size(S).
%% were additional constraints could be used (remove diagonals: X-Y!=0 and X+Y-1!=S)


%%-----------------------------------------------------------------------------
%% evaluations and controls
%%-----------------------------------------------------------------------------


%%
%% --- DISJUNCTION
%% head is derived if at least one atom (of body) is true
%% (increases computational complexity: use 'choice construct' were possible)
%%
%% provides answer sets [a] and [b] if c or d is true
a;b :- c,d.
%% provides answer sets [a] and [b] but not [a,b]
a;b.


%%
%% --- (DEFAULT) NEGATION:
%%
%% 'not b' is true until b is derived true
a :- not b.
%%
%% --- CLASSICAL/STRONG NEGATION:
%% '-b' is only true if b can be derived (to false)
%% '-b' is complement of 'b' (implicit integrity constraint ':- b, -b')
%%
a :- -b.
%% --- DOUBLE NEGATION
a :- not not b.
a :- not -b.
%% --- HEAD NEGATIONS
%% can be used in disjunctions
not a :- b.
not not a :- b.
%% same as integrity constraints
:- b, not not a.
:- b, not a.


%%
%% --- BUILT-IN ARITHMETIC FUNCTIONS
%%
%% + (addition), - (subtraction, unary minus), * (multiplication), / (integer division),
%% \ (modulo), ** (exponentiation), |.| (absolute value),
%% & (bitwise AND), ? (bitwise OR), ^ (bitwise exclusive OR) and ~ (bitwise complement)
%%
plus    ( L +  R ) :- left(L), right(R).
minus   ( L -  R ) :- left(L), right(R).
uminus  (   -  R ) :-          right(R).
times   ( L *  R ) :- left(L), right(R).
divide  ( L /  R ) :- left(L), right(R).
modulo  ( L \  R ) :- left(L), right(R).
power   ( L ** R ) :- left(L), right(R).
absolute(|    -R|) :-          right(R).
bitand  ( L &  R ) :- left(L), right(R).
bitor   ( L ?  R ) :- left(L), right(R).
bitxor  ( L ^  R ) :- left(L), right(R).
bitneg  (   ~  R ) :-          right(R).
%%
%% having: left(7). right(2).


%%
%% --- BUILT-IN COMPARISON PREDICATES
%%
%% integers are compared naturally, which are smaller then constants
%% constants are ordered lexicographically, which are smaller then functions
%% functions both structurally and lexicographically
%%
%% = (equal), != (not equal),
%% < (less than), <= (less than or equal),
%% > (greater than) and >= (greater than or equal)
%%
eq (X,Y) :- X =  Y   , num(X), num(Y).
neq(X,Y) :- X != Y   , num(X), num(Y).
lt (X,Y) :- X <  Y   , num(X), num(Y).
leq(X,Y) :- X <= Y   , num(X), num(Y).
gt (X,Y) :- X >  Y   , num(X), num(Y).
geq(X,Y) :- X >= Y   , num(X), num(Y).
%%
%% having: num(1). num(2).
%% also possible with constants and functions: num(a). num( f(a) ).
%%
%% arithmetic functions are evaluated before comparison literals
all(X,Y) :- X-1 < X+Y, num(X), num(Y).
non(X,Y) :- X/X > Y*Y, num(X), num(Y).


%%
%% --- UNIFICATION or SHORTHANDS for terms.
%% Also possible for functions and tuples.
%%
squares(XX,YY) :- XX  = X*X,   Y*Y = YY,
                  Y’-1 = Y,    Y’*Y’ = XX+YY,
                  X<Y, num(X), num(Y).
%%
%% having: num(1). num(2). num(3). num(4). num(5).


%%
%% --- POOLING
%% a set of atoms, function or tuples as an argument
%% intervall '1..3' is same as pool '(1;2;3)'
%%
%% their behavior in head and body is equal to intervals, same examples:
grid((1;2),(1;2)).
%% result: grid(1,1). grid(1,2). grid(2,2). grid(2,1).
%%
%% below is same but can add constraints
grid(X,Y) :- X = (1;2), Y = (1;2).


%%
%% --- CONDITIONAL LITERAL
%% b is the literal and c is the condition
%%
%% a yields whenever either c is false (and thus no matter whether b holds or not) or both b and c are true
a :- b : c.
%% c can be a list: c, d, e, f
%%
%% usage in head is possible: if c then a only if b
a : b :- c
%% if c then yield a(X) if b(X)
a(X) : b(X) :- c
%%
%% usages in body including other literals: conditions ends with an ';' (semicolon)
%% a :- b1, b2 : c1, c2, c3; b3, b4
next(X,Z) :- set(X), #false : X < Y, Y < Z, set(Y); set(Z), X < Z.
%% having: set(1..4).
%%
%% important: variable names within conditions must no match global variable names
%%            a global variable is within a atom which is NOT subject of a condition


%%-----------------------------------------------------------------------------
%% aggregates
%%-----------------------------------------------------------------------------


%&
%% --- BODY AGGREGATES
%% lowerBound <= aggregate-function { terms } <= upperBound
%% '<=' is default and can be omitted or replaced by other comparison predicates
%% 'aggregate-function' default is '#count' and can be omitted or replaced
%%
%% aggregate functions are:
#count %% (the number of elements; used for expressing cardinality constraints)
#sum   %% (the sum of weights; used for expressing weight constraints)
#sum+  %% (the sum of positive weights)
#min   %% (the minimum weight)
#max   %% (the maximum weight)
%%
%% weight refers the first element of a term tuple:
%%
%% example: the sum must be below 20
#sum{ 4 ; 6 ; 8 ; 3 } < 20
%% example with conditional literal: the sum of passed courses must be at least 20
20 #sum{ 4 : course(db) ; 6 : course(ai) ; 8 : course(project) ; 3 : course(xml) }
%%
%% above example only works as long as weights are different per course
%% terms (due to curly braces) are treated as within a set: duplicates are not counted twice
%% as with below: edge 1 to 2 and edge 2 to 3 have the same cost, but does not counted twice
#sum { 3 : cost(1,2,3); 3 : cost(2,3,3) } = 3
%% hence a ternary tuple with '(cost,from,to)' is used to make the cost unique
#sum { 3,1,2 : cost(1,2,3); 3,2,3 : cost(2,3,3) } = 6
%%
%% usage of unification/shorthands is possible but discouraged due to potential excessive unwrap of possibilities
%% (see potassco user guide, chapter 3.1.12, remark 3.9)
cnt(X) :- X = #count { 2:a ; 3:a }. %% if a hold 'cnt(1)' else 'cnt(0)'
sum(X) :- X = #sum   { 2:a ; 3:a }. %% if a hold 'sum(5)' else 'sum(0)'
pos(X) :- X = #sum+  { 2:a ; 3:a }. %% if a hold 'pos(5)' else 'pos(0)'
min(X) :- X = #min   { 2:a ; 3:a }. %% if a hold 'min(2)' else 'min(#sup)'
max(X) :- X = #max   { 2:a ; 3:a }. %% if a hold 'max(3)' else 'max(#inf)'


%%
%% --- HEAD AGGREGATES
%%
%% TODO coming soon


%%
%% --- NON-GROUNDED AGGREGATES
%%
%% TODO coming soon


%%-----------------------------------------------------------------------------
%% optimization problems
%%-----------------------------------------------------------------------------


%%
%% weak constraints
%%
:~ %% TODO coming soon


%%
%% optimization directives
%%
%% TODO coming soon
#minimize
#maximize


%%-----------------------------------------------------------------------------
%% meta
%%-----------------------------------------------------------------------------


%%
%% #show directive
%%
%% ONLY show atom: #show p/n
#show name/2. %% having name(X, Y) show atoms Y
%% ADDITIONALLY show terms: #show t : L1, , Ln.
#show correct : finished, not error.
%% (optionally) show nothing (except other #show)
#show.


%%
%% #const directive
%%
%% TODO coming soon


%%
%% #external directive
%%
%% TODO coming soon


%%
%% #program directive
%%
%% TODO coming soon


%%
%% #script and #end directive
%%
%% TODO coming soon

