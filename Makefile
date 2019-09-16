VENV_NAME?=venv
SYSTEM_PYTHON?=python3
PYTHON=${VENV_NAME}/bin/python

.PHONY: clean venv install run
.DEFAULT: help


help:
	@echo "make install"
	@echo "       install the app in the predefined virtualenv"
	@echo "make clean"
	@echo "       clean venv, caches and eggs"

run:
	. ./venv/bin/activate  ; phyton app.py

install:
	virtualenv ${VENV_NAME}
	${SYSTEM_PYTHON} -m virtualenv ${VENV_NAME}
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -r requirements.txt
	$(PYTHON) -m pip install -e .

clean:
	@rm -rf .Python MANIFEST build dist venv* *.egg-info *.egg .eggs .pytest_cache
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete