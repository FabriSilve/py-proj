## Virtual Environment

A virtual environment isolates your project dependencies, preventing version conflicts with system-installed Python packages.
Use venv to generate a virtual environment using the standard library
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

To standardize the packages and their versions, use pip with a requirements.txt file.
The requirements.txt file ensures all team members use the same package versions, avoiding inconsistencies.

Save the package versions in a requirements.txt file:

```bash
pip freeze > requirements.txt
```

Install the packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```

Update the packages in the requirements.txt file:

```bash
pip install -r requirements.txt --upgrade
```
