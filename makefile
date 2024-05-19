APP = src/

run:
	python3 ${APP}genpassword.py

install:
	pip install --upgrade pip

test:
	python3 -m unittest discover tests