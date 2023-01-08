# Learn Guide

## Answer Set Programming (ASP) with Potassco Clingo

* https://potassco.org/book/
* https://teaching.potassco.org/ (!)

# Setup Guide

## Setup local develop environment

* Install python 3.11 `sudo apt install python3.11-full`
* [Install poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) (python packaging and dependency
  management)
  * `curl -sSL https://install.python-poetry.org | python3 -`
  * (Optional) Test installation: `poetry --version`
  * (Optional) Activate shell auto-completion: `poetry completions bash >> ~/.bash_completion`
* (Only if system python version differs from projects) Tell poetry which python version is to use: ` poetry env use python3.11`
* Install projects python dependencies: `poetry install`

## Run tests

```bash
./scripts/run_tests.sh
```

## Start server

```bash
./scripts/start_server.sh
```

### Rest API documentation

An openAPI documentation is automatically available under `/docs`.

# HowTo...

* ...add a dependency: `poetry add <dependency_name_like_in_pypi.org>`