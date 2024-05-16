APP = src/
TESTS = tests/

run:
	python3 ${APP}genpassword.py

install:
	pip install --upgrade pip

test:
	python3 ${TESTS}test.py