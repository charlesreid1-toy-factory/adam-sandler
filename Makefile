include common.mk

tox:
	tox

build:
	tox -e build

clean:
	rm -fr build dist __pycache__ *.egg-info/
