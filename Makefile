install:
		poetry install

test:
		poetry run pytest


test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml


lint:
		poetry run flake8 gendiff


selfcheck:
		poetry check


check: selfcheck test lint


build: check
		poetry build


publish:
		poetry publish --dry-run


package-install:
		pip install --user --force-reinstall dist/*.whl


.PHONY: install test lint selfcheck check build