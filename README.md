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
