# DSA ("Das Schwarze Auge") Heldenbogen - Backend

This project represents a new way of formalizing the rules of germans most popular
RPG-PP [Das Schwarze Auge](https://ulisses-spiele.de/game-system/das-schwarze-auge/) (DSA) including its countless expansions and
making the players characters verifiable at runtime in no time.

It uses "answer set programming" (ASP) which is widely used in scientific and industrial usage but with a quite different purpose
hence the modelling is unusual for ASP.

It is a python 3.11 webserver using ASGI web server [uvicorn](https://www.uvicorn.org/)
with [FastApi](https://fastapi.tiangolo.com/) for API dokumentation and ASP made available trough
framework [clingo](https://potassco.org/clingo/) (from Potassco, the Potsdam Answer Set Solving Collection).

---

* RPG - role-playing game
* PP - pen & paper
* DSA - Das Schwarze Auge
* ASP - answer set programming

## Documentations

* See how to contribute at [docs/CONTRIBUTE.md](./docs/CONTRIBUTE.md).
  * Always follow as much [https://clean-code-developer.com/](clean code principles) as you can.
  * See how to add a new rulebook (expansion) at [docs/CREATE_A_RULEBOOK.md](./docs/CREATE_A_RULEBOOK.md).
  * Understand ASP modelling (logic program language by clingo) at [docs/CHEATSHEET.lp](./docs/CHEATSHEET.lp).

* See list of open todos at [docs/TODOs.md](./docs/TODOs.md). (there are even more within the code)
