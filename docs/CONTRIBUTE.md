# Learn Guide

## Answer Set Programming (ASP) with Clingo by Potassco

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
* Install projects python dependencies: `make install`
* Install docker and docker-compose (oder docker cli plugin 'docker compose')

## Run tests

```bash
make prebuild
```

## Start server

```bash
make run
```

### Available URLs

* Backend OpenAPI Documentation: http://localhost:8000/docs

# HowTo...

* ...add a (develop) dependency: `poetry add [-G dev] <dependency_name_like_in_pypi.org>`