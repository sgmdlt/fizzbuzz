install:
	poetry install

run:
	poetry run fizzbuzz

lint:
	poetry run flake8 fizzbuzz/

test:
	poetry run pytest

check: test lint