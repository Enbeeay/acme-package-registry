install:
	pip install --user -r requirements.txt

lint:
	black src tests
	isort src tests
	flake8 src tests
	mypy src tests

test:
	pytest --cov=src --cov-report=term-missing

run:
	python run
