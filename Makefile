## FYI: .PHONY declares a goal  that does not target a real file

## meta vars
ROOT=./
SRC=$(ROOT)app/
TESTS=$(ROOT)tests/
MAIN=$(SRC)main.py

## goals
.DEFAULT_GOAL=help

.PHONY: help 
help:
	@echo "Usage 'make <goal>'. Values for <goal> are one of:"
	@echo ""
	@echo "  clean       remove all temporary files"
	@echo "  install     install packages and prepare environment"
	@echo "  lint        run code linters"
	@echo "  typehint    run code typehint checker"
	@echo "  test        run all tests"
	@echo "  prebuild    goals: lint, typehint and test"
	@echo "  format      format code (experimental, check code changes)"
	@echo "  debug       start server for development"
	@echo "  start       start server for production"
	@echo ""

.PHONY: clean 
clean:
	rm -rf .venv
	rm -rf .mypy_cache

.PHONY: install 
install:
	poetry install

.PHONY: lint 
lint: ## TODO may use 'flake8' instead of 'pylint'
	## enforce coding standards
	#poetry run python -m --ignore=W503,E501 $(SRC) $(TESTS)
	## very strict (coding standards, code smells, simple refactors)
	poetry run python -m pylint $(SRC) $(TESTS)
	## find security issues
	poetry run python -m bandit -r $(SRC)

	## [PRE CHECK]
	#poetry run python -m isort --profile=black --lines-after-imports=2 --check-only $(TESTS) $(SRC)
	#poetry run python -m black -check $(TESTS) $(SRC) --diff


.PHONY: typehint 
typehint:
	poetry run python -m mypy $(SRC) $(TESTS)

.PHONY: test 
test:
	poetry run python -m unittest discover --start-directory $(TESTS) --top-level-directory $(ROOT)

.PHONY: format 
format: ## TODO currently experimental
	## sort and group imports
	poetry run python -m isort --profile=black --lines-after-imports=2 $(TESTS) $(SRC)
	## opinionated formatter
	poetry run python -m black $(TESTS) $(SRC)
	## only fixes pep8 violations
	poetry run python -m autopep8
	## eformats entire code to the best style possible
	poetry run python -m yapf

.PHONY: prebuild 
prebuild: lint typehint test

.PHONY: debug
debug:
	poetry run python $(MAIN) --reload --loglevel debug

.PHONY: start
start: test
	poetry run python $(MAIN) --workers 4
