# Contribute to the {{ cookiecutter.repo_name }} package

This is a guide on how the development process works, and how you can easily contribute to the package.

## Install

Install the package in development mode in your environment using:

``` bash
pip install -e '.[dev]'
```

## Testing

For making sure that the application works as expected, we have several layers of testing. These layers are explained in the [Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) of Martin Fowler.

![alt text](static/testing.png "Modified Test Pyramid")

Above is the modified testing pyramid for Data `{Science,Engineering}`.

## Static analysis

For performing static analysis we use [Pre-Commit](https://calmcode.io/pre-commit/the-problem.html). Pre-commit allows us to easily run a suite of tests, as defined in the [.pre-commit-config.yaml](.pre-commit-config.yaml) in the project. By default, the cookie cutter ships with a couple of plugins:

* Trivial checks:
  * The encoding of the files
  * If it is valid Python in the files
  * If the YAML files are nicely formatted
  * The code is free of debug statements
* [**Flake8**](https://pypi.org/project/flake8/) is a Python library that wraps PyFlakes, pycodestyle and Ned Batchelder's McCabe script. It is a great toolkit for checking your code base against coding style ([PEP 8](https://www.python.org/dev/peps/pep-0008/), programming errors (like “library imported but unused” and “Undefined name”) and to check complexity.
* [**Black**](https://github.com/psf/black) is the Python code formatter and makes sure that we format our Python code in the same way. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.
* [**MyPy**](https://github.com/python/mypy) is an optional static type checker for Python. You can add type hints ([PEP 484](https://www.python.org/dev/peps/pep-0484/)) to your Python programs, and use mypy to type check them statically. Find bugs in your programs without even running them!


If you want to run this automatically before each commit, you can install it as a pre-commit hook:
```bash
pip install pre-commit  # install the package in your environment
pre-commit install  # add the git hook
```

You can easily run it also manually using:
```bash
pre-commit run --all-files
```

## `{Unit,Integration}` testing

For running unit and integration tests we use `pytest`. The project ships with a senseless test, but can be used as a starting point for more tests :)

You can run the tests using:
```bash
pytest tests/
```
