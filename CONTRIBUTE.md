# Learn Guide

## Answer Set Programming (ASP) with Potassco Clingo

* https://potassco.org/book/
* https://teaching.potassco.org/ (!)

# Setup Guide

## Setup local develop environment

* Install python 3.8
* [Install poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) (python packaging and dependency management)
  * `curl -sSL https://install.python-poetry.org | python3 -`
  * (Optional) Test installation: `poetry --version`
  * (Optional) Activate shell auto-completion: `poetry completions bash >> ~/.bash_completion`
* Install projects python dependencies: `poetry install`

## HowTo...

...add a dependency: `poetry add <dependency_name_like_in_pypi.org>`

# History of project setup

* Init project with poetry: `poetry new dsa-heldenbogen`
* Include .venv folder in project root: `poetry config virtualenvs.in-project true --local`
* Add python API for answer set programming: `poetry add clingo`
