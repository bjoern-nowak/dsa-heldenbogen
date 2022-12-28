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

## Troubleshoot

### Instructions for local clingo build ([wiki](https://github.com/potassco/clingo/blob/master/INSTALL.md))

Only required if there is an issue with pre-build clingo on ubuntu, were the python module is missing ([[1]](https://github.com/potassco/clingo/issues/189), [[2]](https://github.com/potassco/clorm/issues/22)).

/-/ **WORK-IN-PROGRESS** \-\

```bash
sudo add-apt-repository ppa:potassco/stable
sudo apt install lua5.3
pip install cffi
## here: download clingo release source to 'library/clingo-<version>.zip'
mkdir -p out && unzip library/clingo-5.6.2.zip  -d out/
cmake -Hout/clingo-5.6.2/ -Bout/clingo-5.6.2-build -DCMAKE_BUILD_TYPE=Release -DCLINGO_BUILD_WITH_PYTHON=ON-DCLINGO_BUILD_WITH_PYTHON=pip -DCMAKE_INSTALL_PREFIX=./.venv
sudo cmake --build out/clingo-5.6.2-build --target install
```

More options:

* see/list options: `-LH`
* use existing clingo to build python module: `-DCLINGO_USE_LIB=ON`

# History of project setup

* Init project with poetry: `poetry new dsa-heldenbogen`
* Include .venv folder in project root: `poetry config virtualenvs.in-project true --local`
* Add python API for answer set programming: `poetry add clingo`
