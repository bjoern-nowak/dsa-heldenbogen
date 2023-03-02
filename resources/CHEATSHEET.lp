%%
%% This is a cheatsheet about clingo/gringo/clasp language
%%  it is not complete nor states all restrictions
%%  but it gives a good and quick overview/understanding
%%
%% See 'Potassco: User Guide' (source of some text and examples) for a complete guide.
%%  https://github.com/potassco/guide/releases/tag/v2.2.0
%%



%%-----------------------------------------------------------------------------
%% PART: basic semantic
%%-----------------------------------------------------------------------------

%% --- ATOM
%% is a constant or function (see 'language basics' part below)

%% --- RULE: 'HEAD :- BODY.'
%% within the head are atoms
%% the body contains LITERALs which are atoms or negated atoms
%%
%% umbrella if rain and outdoor
umbrella :- rain, outdoor.

%% --- FACT (bodyless rule): 'HEAD.'
%%
%% it rains
rain.

%% --- INTEGRITY CONSTRAINT
%% filters solution candidates: body shall not be satisfied
%%
%% keep candidate if: no umbrella but outdoor
:- umbrella, not outdoor



%%-----------------------------------------------------------------------------
%% PART: language basics
%%-----------------------------------------------------------------------------

%% line comment start with an %
%% block and inline comments starts with %* and ends with *%

%% --- INTEGERS
1

%% --- CONSTANTS
starts_lowercase
_underscorePreventNameClashes

%% --- SPECIAL CONSTANTS
%% greatest and smallest element among all variable-free terms
#sup
#inf

%% --- BOOLEAN CONSTANTS
#true
#false

%% --- VARIABLE
Starts_uppercase
_UnderscorePreventNameClashes

%% --- ANONYMOUS VARIABLE
_

%% --- STRING
"string"
"\\" %% escapes backslash
"\n" %% escapes newline
"\"" %% escapes double quote

%% --- (UNINTERPRETED) FUNCTIONS
%% can be better understood as a named tuple
%%  since there is no self-defined functionality programmed behind these
%%
%% example with three arguments (elements in a tuple)
functionName(constant,function(123),Variable)

%% --- TUPLES
%% are functions without names
()
(functionName,constant,function(123),Variable)
%% end with a ',' (comma) to declare tuple grade: example is a quadruple
(a,b,c,d,)

%% --- INTERVALS
%%
%% in body: expanded disjunctively
num(1..3).
%% result: num(1). num(2). num(3).
%%
%% in head: expanded conjunctively
grid(1..S,1..S) :- size(S).
%% result: grid(1,1). grid(1,2). grid(2,2). grid(2,1).
%% having: size(2).
%%
%%  which is same as (using unification):
grid(X,Y) :- X = 1..S, Y = 1..S, size(S).
%%  were additional constraints could be used
%%  (remove diagonals: X-Y!=0 and X+Y-1!=S)



%%-----------------------------------------------------------------------------
%% PART: evaluations and controls
%%-----------------------------------------------------------------------------


%% --- DISJUNCTION
%% head is derived if at least one atom (of body) is true
%%  (increases computational complexity: use 'choice construct' were possible)
a;b :- c,d.
%% provides answer sets [a] and [b] if c or d is true
a;-b. %% see below for explanation of '-'
%% provides answer sets [a] and [-b] but not [a,-b]


%% --- NEGATION
%%
%% default negation:
%%  'not b' is true until b is derived true
a :- not b.
%%
%% classical/strong negation:
%%  '-b' is only true if b can be derived (to false)
%%  '-b' is complement of 'b' (implicit integrity constraint ':- b, -b')
a :- -b.
%%
%% double negation:
a :- not not b.
a :- not -b.
%%
%% head negation:
%%  can be used in disjunctions
not a :- b.
not not a :- b.
%%  same as integrity constraints
:- b, not not a.
:- b, not a.


%% --- BUILT-IN ARITHMETIC FUNCTIONS
plus    ( L +  R ) :- left(L), right(R). %%  +   := addition
minus   ( L -  R ) :- left(L), right(R). %%  -   := subtraction
uminus  (   -  R ) :-          right(R). %%  -   := unary minus
times   ( L *  R ) :- left(L), right(R). %%  *   := multiplication
divide  ( L /  R ) :- left(L), right(R). %%  /   := integer division
modulo  ( L \  R ) :- left(L), right(R). %%  \   := modulo
power   ( L ** R ) :- left(L), right(R). %%  **  := exponentiation
absolute(|    -R|) :-          right(R). %%  |.| := absolute value
bitand  ( L &  R ) :- left(L), right(R). %%  &   := bitwise AND
bitor   ( L ?  R ) :- left(L), right(R). %%  ?   := bitwise OR
bitxor  ( L ^  R ) :- left(L), right(R). %%  ^   := bitwise exclusive OR
bitneg  (   ~  R ) :-          right(R). %%  ~   := bitwise complement
%% having: left(7). right(2).


%% --- BUILT-IN COMPARISON PREDICATES
%%
%% integers are compared naturally, which are smaller then constants
%% constants are ordered lexicographically, which are smaller then functions
%% functions both structurally and lexicographically
%%
eq (X,Y) :- X =  Y   , num(X), num(Y). %%  =   := equal
neq(X,Y) :- X != Y   , num(X), num(Y). %%  !=  := not equal
lt (X,Y) :- X <  Y   , num(X), num(Y). %%  <   := less than
leq(X,Y) :- X <= Y   , num(X), num(Y). %%  <=  := less than or equal
gt (X,Y) :- X >  Y   , num(X), num(Y). %%  >   := greater than
geq(X,Y) :- X >= Y   , num(X), num(Y). %%  >=  := greater than or equal
%% having: num(1). num(2).
%% also possible with constants and functions: num(a). num( f(a) ).
%%
%% arithmetic functions are evaluated before comparison literals, see:
all(X,Y) :- X-1 < X+Y, num(X), num(Y).
non(X,Y) :- X/X > Y*Y, num(X), num(Y).


%% --- UNIFICATION or SHORTHANDS for terms.
%% Also possible for functions and tuples.
squares(XX,YY) :- XX  = X*X,   Y*Y = YY,
                  Y’-1 = Y,    Y’*Y’ = XX+YY,
                  X<Y, num(X), num(Y).
%% having: num(1). num(2). num(3). num(4). num(5).


%% --- POOLING
%% a set of atoms, function or tuples as an argument
%% intervall '1..3' is same as pool '(1;2;3)'
%%
%% their behavior in head and body is equal to intervals:
grid((1;2),(1;2)).
%% result: grid(1,1). grid(1,2). grid(2,2). grid(2,1).
%%
%% below is same but uses unification which enables us to add constraints
grid(X,Y) :- X = (1;2), Y = (1;2).


%% --- CONDITIONAL LITERAL
%% b is the literal and c is the condition, which may be more than one
%% a yields whenever either c is false (b does not matter) or b and c holds
a :- b : c.
%%
%% usage in head is possible:
%%  if c then a only if b
a : b :- c
%%  if c then yield a(X) if b(X)
a(X) : b(X) :- c
%%
%% usages in body with other literals: conditions ends with an ';' (semicolon)
%% a :- b1, b2 : c1, c2, c3; b3, b4
next(X,Z) :- set(X), #false : X < Y, Y < Z, set(Y); set(Z), X < Z.
%% having: set(1..4).
%%
%% important:
%%  variable names within conditions must no match global variable names
%%  a global variable is within a atom which is NOT subject of a condition



%%-----------------------------------------------------------------------------
%% PART: aggregates
%%-----------------------------------------------------------------------------
%% see example 3.15 from 'Potassco: user guide' for a complex problem

%% --- BODY AGGREGATES
%% lowerBound <= aggregate-function { elements } <= upperBound
%% '<=' is default and can be omitted or replaced by other comparison predicates
%% 'aggregate-function' default is '#count' and can be omitted or replaced
%% '{ elements }' represent a set, hence duplicate elements are ignored
%%  elements are separated by an ; (semicolon)
%%  an element is: <terms tuple>:<conditional literals tuple>
%%  the 'conditional literals tuple' is optional (colon must be omitted then)
%%
%% aggregate functions are applied to terms (weight) only and are:
#count %% number of elements; used for expressing cardinality constraints
#sum   %% sum of weights; used for expressing weight constraints
#sum+  %% sum of positive weights
#min   %% minimum weight
#max   %% maximum weight
%%
%% weight refers the first element of a term tuple:
%%
%% example: the sum must be below 20
#sum{ 1 ; 2 ; 4 ; 8 } < 20
%%
%% example with conditional literal:
%%  the sum of credits (weight) by passed modules (mod) must be at least 20
20 #sum{ 4 : mod(a) ; 4 : mod(b) ; 6 : mod(c) ; 6 : mod(d),mod(dExtra) }
%%  the 'sum' will be '10', due to duplicate terms and hence does not satisfy the constraint
%%  hence non-single tuples can be used make weights (credits) unique (per mod)
20 #sum{ 4,a : mod(a) ; 4,b : mod(b) ; 6,c : mod(c) ; 6,d : mod(d),mod(dExtra) }
%%
%% usage of unification/shorthands is possible but
%%  discouraged due to potential excessive unwrap of possibilities
%%  (see 'Potassco: user guide' chapter 3.1.12 remark 3.9 for details)
cnt(X) :- X = #count { 2:a ; 3:a }. %% if a hold 'cnt(1)' else 'cnt(0)'
sum(X) :- X = #sum   { 2:a ; 3:a }. %% if a hold 'sum(5)' else 'sum(0)'
pos(X) :- X = #sum+  { 2:a ; 3:a }. %% if a hold 'pos(5)' else 'pos(0)'
min(X) :- X = #min   { 2:a ; 3:a }. %% if a hold 'min(2)' else 'min(#sup)'
max(X) :- X = #max   { 2:a ; 3:a }. %% if a hold 'max(3)' else 'max(#inf)'
%%
%% #min and #max can be also expressed without aggregation:
:- #min { X,Y : condition_a(Y), condition_b(Y,X) } 2.
%% is same as
:- condition_a(Y), condition_b(Y,X), X <= 2.


%% --- HEAD AGGREGATES
%% syntax is same as with body aggregates
%%  but elements have an 'head literal to be derived' when constraint(s) holds.
%%  hence of form: <terms tuple>:<derivable literal>:<conditional literals tuple>
%%  the 'conditional literals tuple' is still optional
%%
%% get edges having a cost which is higher then 10
10 < #sum { C,X,Y : edge(X,Y) : cost(X,Y,C) }.



%%-----------------------------------------------------------------------------
%% PART: optimization problems
%%-----------------------------------------------------------------------------


%% --- WEAK CONSTRAINTS
%% syntax is similar to integrity constraints
%%  but associates a weighted term tuple if the body holds
%%  hence answer sets are comparable and will be weight optimized
%%
%% it has the form: (L literal, w weight, p priority, t term)
%%   :~ L1, ..., Ln. [w@p,t1,...,tn]
%%
%% the priority is optional, hence '@p' can be omitted and defaults to 0 (zero)
%%  the greater the p the more important it is
%% the weight can be a term but must be an integer
%%
%% a abstract example:
:~ funcA(X), cost(X,C). [C,X] %% cost C and priority 0 (zero)
:~ funcA(X), funcB(X,Y). [3@1,X,Y] %% cost 3 and a higher priority of 1


%% --- OPTIMIZATION DIRECTIVES
%% above can also be represented like:
#minimize{  C,X : funcA(X), cost(X,C) ,  3@1,X,Y : funcA(X), funcB(X,Y) }.
%% and
#maximize{ -C,X : funcA(X), cost(X,C) , -3@1,X,Y : funcA(X), funcB(X,Y) }.
%% thus multiple weak constraints can be written within one statement


%% --- example 3.16 of 'Potassco: User Guide'
%% given five hotels, find optimal
{ hotel(1..5) } = 1.
%% with information about their stars, cost per night and possible noisiness:
star(1,5). cost(1,170).
star(2,4). cost(2,140).
star(3,3). cost(3,90).
star(4,3). cost(4,75). main_street(4).
star(5,2). cost(5,60).
noisy :- hotel(X), main_street(X).
%% choose by following prioritization (remember: higher '@p' is more important):
#maximize { Y@1,X : hotel(X), star(X,Y) }. %% (1) the highest stars
#minimize { Y/Z@2,X : hotel(X), cost(X,Y), star(X,Z) }. %% (2) the lowest cost per star
:~ noisy. [ 1@3 ] %% (3) it must not be noisy
%% result: hotel 3 is optimal


%%-----------------------------------------------------------------------------
%% PART: more features
%%-----------------------------------------------------------------------------


%% --- OUTPUT CONTROL
%% control output by suppress irrelevant terms and atoms from answer set
%%
%% ONLY show atom n: #show p/n
#show name/2. %% having name(X, Y) show atoms Y
%% ADDITIONALLY show term t if literals hold: #show t : L1, ..., Ln.
#show correct : finished, not error.
%% (optionally) show nothing (except other #show)
#show.


%% --- PROGRAM PARTS
%% a logic programm can be separated into multiple parts
%% per default everything is under the program 'base'
%%  (if not under a '#program <name>' directive other than 'base')
%%  wich is executed per default
a. %% under 'base' program,
#program check_a.
valid_a :- #true. %% under program 'check_a'; not executed per default
#program base. %% below this: rules would be executed by default again
b.
%% result per default to: {a,b}
%%
%% a program can have parameters
#program check_b(x,y).
valid_b :- check(x,y).
%%
%% calling such sub programs:
%%  use parameter 'parts' of 'clingo.Control().ground()'
%%  a list of '(<program>,<list of parameters>)' tuples
%%  e.g.: 'clingo.Control().ground( [ ("check_a",[]) , ("check_b",[2,5]) ] )'


%% --- INCLUDE other logic programs
%% a logic programm can be split into multiple files
%% using '#include <file_path>'
#include held_fakten.lp
%% looks up 'held_fakten.lp' file path in following order:
%%  1. relative to current working folder
%%  2. relative to the file containing the #include statement
%%
%% it its not affected by #program directive (see above)


%% --- EXTERNAL FUNCTIONS (scripting)
%% (implement and) use simple Python functions out of the logic program
%%  their result MUST BE deterministic
%%
%% on any error the current callee rule is dropped with a warning
%%
%% function parameters are terms of the type 'clingo.Symbol' and are generic
%%  which provide properties for different representations:
%%   number: <parameter>.number
%%   string: <parameter>.string
%%   function: <parameter>.name
%%   function arguments: <parameter>.arguments
%%
%% constants and tuples act like functions here:
%%  constants have an empty argument list
%%  tuples a empty name
%%
%% #sub and #inf are concrete and unique objects: clingo.Sup and clingo.Inf
%%
%% first declare such function
#script(python) %% till #end everything will be interpreted as python code
import clingo
N = clingo.Number
def increase(a):
    return N(a.number + 1)
#end
%% then use it: get highest step and add one
step(1).
step(@increase(S)) :- #maximize{ S : step(S)}.
%% result: step(2).
%%
%% the python function could also return a list
%%  each element will then be successively inserted.
%% function f with 'return [ N(3) , N(4) ]'
%%  would make 'step(@f())' to 'step(3,4)' (so behave like 3..4)
%%
%% also returnable are:
%%  strings with 'clingo.String(<string>)'
%%  functions with 'clingo.Function(<name>,<arguments>)'
%%
%%
%% python code must not be implemented within a '#script'; using the python api
%%  the 'clingo.Control().ground()' method provides a parameter 'context'
%%  which would be a class instance
%%  which methods can be called by '@' (as before)


%% --- SOLVING UNDER ASSUMPTIONS
%% an answer set is only valid if the assumption holds (contains the atom)
%%  the 'clingo.Control().solve()' method provides a parameter 'assumptions'
%%  which is a list of '(atom, boolean)' tuples or literals
%%   e.g.: '[(clingo.Function("valid"), True)]'
%%   hence the function valid(<any elements>) must be derived True



%%-----------------------------------------------------------------------------
%% PART: notes about further features not relevant for our use case
%%-----------------------------------------------------------------------------


%% TODO write something about #defined


%% --- EXTERNAL STATEMENTS
%% prevents atoms to be discarded for simplifications;
%%  if they are in the body (of an rule, condition, ...)
%%  but not in any rule head
%%
%% form: '#external A:L1,...,Ln'
#external q(X) : p(X). %% q is the external atom, p the condition
%%
%% its main usage is in extending plain ASP solving like multi-shot solving
%% hence will not be descripted here, more details in 'Potassco: User Guide'
%% under part 'External Statements' in chapter 3.1.15 'Meta-Statements'


%% --- CONSTANTS WITH PARSABLE DEFAULT VALUES
%% a constant having a default value but can be overridden before grounding
%%
%% form: '#const <constant> = <term without variables, pools or intervals>.'
#const x = 42.
#const y = f(x,z).
p(x,y). %% result in p(42,f(42,z))
%% TODO how do override the const using the python api?


%% --- MULTI-SHOT SOLVING
%% TODO may be more to come


%% --- THEORY SOLVING
%% TODO may be more to come

%% --- HEURISTIC-DRIVEN SOLVING
%% TODO may be more to come
