
.DEFAULT_GOAL=clean install prebuild run

## set goals not targeting real files
.PHONY: clean install lint typehint test prebuild run

## meta vars
ROOT=./
SRC=$(ROOT)app/
TESTS=$(ROOT)tests/
MAIN=$(SRC)main.py
VENV=.venv/

## goals

clean:
	rm -rf $(VENV)

install:
	poetry install

lint:
	python -m pylint $(SRC) $(TESTS)

typehint:
	python -m mypy $(SRC) $(TESTS)

test:
	python -m unittest discover --start-directory $(TESTS) --top-level-directory $(ROOT)

prebuild: lint typehint test

run:
	poetry run python $(MAIN)
