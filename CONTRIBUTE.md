# Learn Guide

## Answer Set Programming (ASP) with Potassco Clingo

* https://potassco.org/book/
* https://teaching.potassco.org/ (!)

# Setup Guide

## Setup local develop environment

* Install python 3.8
* [Install poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) (python packaging and dependency
  management)
  * `curl -sSL https://install.python-poetry.org | python3 -`
  * (Optional) Test installation: `poetry --version`
  * (Optional) Activate shell auto-completion: `poetry completions bash >> ~/.bash_completion`
* Install projects python dependencies: `poetry install`

## Start local server

### by command line

#### with python cli (recommended)

```bash
(cd dsa_heldenbogen && poetry run python main.py)
```

#### with uvicorn cli

Schema is `uvicorn <file_path>:<variable> <options>`.
Options:

* `--reload` will automatically load changed py-files.
* `--log-level debug` values: critical, error, warning, debug, trace.

```bash
(cd dsa_heldenbogen && poetry run uvicorn app:app --reload)
```

### Rest API documentation

An openAPI documentation is automatically available under `/docs`.

# HowTo...

* ...add a dependency: `poetry add <dependency_name_like_in_pypi.org>`