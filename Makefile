unittest:
	python -m unittest discover

install-dev:
	pip install -e .["dev"]

install-prod:
	pip install -e .

run:
	python run.py