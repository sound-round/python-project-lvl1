install:
	poetry install

brain-games:
	poetry run brain-games

package-install:
	pip install --user dist/*.whl

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games
