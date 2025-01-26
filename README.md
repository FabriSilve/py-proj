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
