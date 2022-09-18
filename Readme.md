# adam-sandler

<img alt="version-0.1.0" src="https://img.shields.io/badge/version-0.1.0-orange" />

<img
alt="tests-unittest" src="https://img.shields.io/badge/tests-unittest-green" /><img
alt="tests-pytest" src="https://img.shields.io/badge/tests-pytest-green" />

<img
alt="codestyle-black" src="https://img.shields.io/badge/codestyle-black-%23222222" /><img
alt="codestyle-flake8" src="https://img.shields.io/badge/codestyle-flake8-blue" />

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

<img alt="python-3.7-3.8-3.9-pypy3.9" src="https://img.shields.io/badge/python-3.7%20|%203.8%20|%203.9%20|%20pypy3.9-blue" />

![Adam Sandler as Happy Gilmore](docs/img/happygilmore.png)

Package demonstrating how to run Python package tests via tox, covering
multiple versions of Python. Demonstrate how to modify library implementations
based on the version of Python.

## Extremely Quick Start

The fastest way to get started is to set up a virtual environment, and install tox into it:

```
python -m virtualenv -p py39 vp && source vp/bin/activate

pip install tox
```

Now list all available tox environments:

```
tox -la
```

Build the package:

```
make build
```

Use this one make command to run all the tox tests:

```
make tox
```

(This will require some additional setup to have multiple correct versions of Python,
see pyenv instructions below.)

## Using tox

To use tox to run tests, start by installing the dev dependencies:

```
pip install -r requirements-dev.txt
```

Now you can list all of the available tox environments:

```
$ tox -l -v

default environments:
py39-sdist-test -> Install as source distribution & test
py39-wheel-test -> Install as binary wheel distribution & test
py38-sdist-test -> Install as source distribution & test
py38-wheel-test -> Install as binary wheel distribution & test
build           -> Create a source and wheel distribution. Creates .tar.gz and .whl artifacts in the dist folder.
```

See the next section for notes on how to use multiple python versions.

To run an environment, use `tox -e <env_name>`, for example:

```
tox -e py39-sdist-test
```

The `sdist-test` environments will:

* create a **source** distribution (.tar.gz file) for the package
* install the package from that .tar.gz source distribution into the
  temporary tox virtual environment
* run tests with pytest

The `wheel-test` environment will:

* create a **binary wheel** distribution (.whl file) for the package
* install the package from that wheel into the temporary tox virtual environment
* run tests with pytest

## Using tox with pyenv

Pyenv is a utility for installing and switching between multiple Python versions.
It can be used to provide different Python versions to tox, so that the package
can be tested against different Python versions.

Start by checking which versions of Python are installed via pyenv:

```
$ pyenv versions

  3.7.13
* 3.8.13
  3.9.13
  pypy3.9-7.3.9
```

In this example, there are multilpe versions of python installed and available
via pyenv, with the global version being set to 3.8.13.

To make multiple versions of Python available to use, use the `pyenv local` command
to activate different versions locally:

```
$ pyenv local 3.7.13 3.8.13 3.9.13 pypy3.9-7.3.9

$ pyenv versions

* 3.7.13 (set by /path/to/adam-sandler/.python-version)
* 3.8.13 (set by /path/to/adam-sandler/.python-version)
* 3.9.13 (set by /path/to/adam-sandler/.python-version)
* pypy3.9-7.3.9 (set by /path/to/adam-sandler/.python-version)
``` 

This will create a `.python-local` file. 

Now when you run `tox` with no arguments, it runs all environments, and should be able
to find each different version of python specified:

```
$ tox

...

___________________________________________ summary ____________________________________________
  py39-sdist-test: commands succeeded
  py39-wheel-test: commands succeeded
  py38-sdist-test: commands succeeded
  py38-wheel-test: commands succeeded
  py37-sdist-test: commands succeeded
  py37-wheel-test: commands succeeded
  pypy39-sdist-test: commands succeeded
  build: commands succeeded
  congratulations :)
```

