
.DEFAULT_GOAL := prebuild run

## set goals not targeting real files
.PHONY: typehint test lint prebuild run

## meta vars
ROOT:=./
SRC:=$(ROOT)app/
TESTS:=$(ROOT)tests/
MAIN:=$(SRC)main.py

## goals
## TODO may add 'poetry init' as goal

lint:
	python -m pylint $(SRC) $(TESTS)

typehint:
	python -m mypy $(SRC) $(TESTS)

test:
	python -m unittest discover --start-directory $(TESTS) --top-level-directory $(ROOT)

prebuild: lint typehint test

run:
	poetry run python $(MAIN)



