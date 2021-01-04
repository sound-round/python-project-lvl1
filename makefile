install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

force-package-install:
	pip install --force-reinstall --user dist/*.whl

package-install:
	pip install --user dist/*.whl

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games
