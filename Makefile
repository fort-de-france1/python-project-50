install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=diff --cov-report xml

lint:
	poetry run flake8 diff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
