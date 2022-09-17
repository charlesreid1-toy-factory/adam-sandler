# adam-sandler

Package demonstrating how to run Python package tests via tox, covering
multiple versions of Python. Demonstrate how to modify library implementations
based on the version of Python.

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
