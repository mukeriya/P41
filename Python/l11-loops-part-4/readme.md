# Venv

# Activate venv

```bash
cd venv\Scripts
```

or

```bash
cd venv\bin
```

```bash
activate
```

## Lib installation

```bash
pip install [lib-name]
```

```bash
pip install colorama
```

## Lib uninstallation

```bash
pip uninstall colorama
```

## Write all dependencies in file

```bash
pip freeze > requirements.txt
```

## Install dependencies from file

```bash
pip install -r requirements.txt
```

```python
from colorama import Back

BLOCK = Back.RED + '  ' + Back.RESET

print(BLOCK)
print(BLOCK)

RED = "\033[0;31m"
END = "\033[0m"
BLOCK = RED + '██' + END

print(BLOCK)
print(BLOCK)
```

