install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff  --cov-report xml

selfcheck:
	poetry check

check:
	selfcheck test lint


.PHONY: install gendiff build publish package-install package-reinstall lint 
