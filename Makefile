PYTHON := python3
PYPY := pypy
PYTHON3 := python3
PYFLAKES := pyflakes
PYLINT := pylint

default: test

test:
	$(PYTHON) setup.py test

test-viewer:
	PYTHONPATH=. $(PYTHON3) tests/test_viewer.py

check: test

run:
	PYTHONPATH=. $(PYTHON) gazerbeam

profile:
	PYTHONPATH=. $(PYTHON) -m cProfile -o stats gazerbeam/__main__.py
	python -c 'import pstats; p = pstats.Stats("stats"); p.sort_stats("cumulative").print_stats(10)'

help:
	PYTHONPATH=. $(PYTHON) gazerbeam --help

dump:
	PYTHONPATH=. $(PYTHON) tools/dumpdiffs.py

run3:
	PYTHONPATH=. $(PYTHON3) gazerbeam

runpypy:
	PYTHONPATH=. $(PYPY) gazerbeam

dist:
	rm -rf dist/*
	WHEEL_TOOL=$(shell which wheel) $(PYTHON) setup.py bdist_wheel

publish: dist
	find dist -type f -exec gpg2 --detach-sign -a {} \;
	twine upload dist/*

setup-pypi-test:
	$(PYTHON) setup.py register -r pypitest
	$(PYTHON) setup.py bdist_wheel upload -r pypitest

setup-pypi-publish:
	$(PYTHON) setup.py register -r pypi
	$(PYTHON) setup.py bdist_wheel upload --sign -r pypi

lint:
	@$(PYFLAKES) `find . -name '*.py' -print`

pylint:
	@$(PYLINT) gazerbeam/*.py

clean:
	find . -name '*.pyc' -exec rm -f {} \;
	rm -rf gazerbeam.egg-info .eggs build dist
