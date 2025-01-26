<!--toc:start-->

- [Virtual Environment](#virtual-environment)
- [Dependency management](#dependency-management)
- [Setup linter](#setup-linter)
- [Setup unit testing](#setup-unit-testing)
- [Tests coverage](#tests-coverage)
- [Pre commit](#pre-commit)
<!--toc:end-->

## Virtual Environment

A virtual environment isolates your project dependencies, preventing version conflicts with system-installed Python packages.
Use `venv` to generate a virtual environment using the standard library
The virtual environment ensures all dependencies are local to the project, preventing global changes to your system's Python environment.

```bash
python3 -m venv venv
```

Activate the virtual environment

```bash
# Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

Deactivate the virtual environment

```bash
deactivate
```

## Dependency management

To standardize the packages and their versions, use pip with a `requirements.txt` file.
The requirements.txt file ensures all team members use the same package versions, avoiding inconsistencies.

Save the package versions in a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

Install the packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Update the packages in the `requirements.txt` file:

```bash
pip install -r requirements.txt --upgrade
```

## Setup linter

Linting ensures code align to Python's coding standards (PEP 8).
`pylint` checks for errors, enforces consistency, and improves code readability. The configuration file `.pylintrc` can be customized to suit your team's needs.

Run the linter:

```bash
pylint .
```

Failing rules can be checked from the official [Pylint documentation](https://pylint.pycqa.org/en/latest/user_guide/message-control.html).
Search for the code connected to the failing rule and you will fine the reason of the failure and how to fix it.

## Setup unit testing

Testing ensures your code is reliable and prevents bugs. By creating tests for every new function, you can catch errors early.
The tests are included in the `tests/` folder where the file name matches the module name and path in the project.

Write a test (eg: `tests/test_sample.py`):

```python
def test_example():
    assert 1 + 1 == 2
```

Run the tests:

```bash
pytest tests
# For more details in the output use the --verbose flag
pytest tests --verbose
```

For more information about the tests and dedicated assertions, check the [official documentation](https://docs.pytest.org/en/stable/).

## Tests coverage

Ensure your tests cover a high percentage of your code with `pytest-cov`.
Code coverage ensures you’re testing all parts of your application. An report provides a visual overview of covered and uncovered lines.

Run tests with coverage:

```bash
pytest --cov=source tests
```

Run tests with minimum coverage:

```bash
pytest --cov=source --cov-fail-under=80 tests
```

## Pre commit

Use pre-commit hooks to enforce linting and tests before each commit.
Pre-commit hooks prevent bad code from entering your repository by automatically running linting and testing checks before each commit.

Install the pre-commit hooks:

```bash
pre-commit install
```

Test the hooks:

```bash
pre-commit run --all-files
```
