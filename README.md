# CrateDB django connector.
![PyPI - Version](https://img.shields.io/pypi/v/cratedb-django)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cratedb-django)
![PyPI - License](https://img.shields.io/pypi/l/cratedb-django)
![PyPI - Status](https://img.shields.io/pypi/status/cratedb-django)

Connector to use CrateDB as a database in Django ORM.

# Documentation

## How to install
uv
```shell
uv add cratedb-django
```
pipx
```shell
pipx install cratedb-django
```

### Environment variables
SUPPRESS_UNIQUE_CONSTRAINT_WARNING [true/false] Suppresses warning when a model is created with unique=True constraint.

# License
This project is open-source under a MIT license.