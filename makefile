install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 hexlet_python_package

selfcheck:
	poetry check

package-install:
	python3 -m pip install --user dist/*.whl

publish:
	poetry publish --dry-run

br-games:
	poetry run br-games

check: selfcheck test lint

build:
	poetry build

.PHONY: install test lint selfcheck check build