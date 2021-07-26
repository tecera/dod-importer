.PHONY: pipeline

pipeline: format linting unittest

venv: venv/touchfile

venv/touchfile: dev_requirements.txt
	@test -d .venv || virtualenv .venv
	@. .venv/bin/activate; pip install -Ur dev_requirements.txt
	@touch .venv/touchfile

format:
	@isort .
	@black .

linting:
	@flake8 .
	@pylint dod tests

unittest:
	@python -m pytest

clean:
	@rm -rf .venv
	@find -iname "*.pyc" -delete
