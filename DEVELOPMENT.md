## Clone the project

```shell
git clone https://github.com/surister/cratedb-django
```

The easiest way to work on the project is using `uv`

## Install dependencies
```shell
uv sync
```

## Run tests
Set `tests.settings.DATABASE` the correct CrateDB credentials. A CrateDB instance is expected to be
running, we do not mock database connections.

```shell
uv run pytest
```

## Build

```shell
uv build
```

## Upload new version to pypi

Create a new release on github.com/surister/django-cratedb/releases and the workflow will
take care of it.


## Before hacking

It is recommended to have some good knowledge of Django, the documentation on how to develop
a django database backend is scarce, the best way is to be familiar with Django internals and
read Django's source code, alternatively Postgres and CockroachDB connectors can be a good
place to have a look.



