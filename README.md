# SearchAndDoc
Discord app that enhances the search feature and utilizes LLMs to create documentation of anything related to the project info discussed in channels

Requirements:
- Python >= 3.13
- Poetry >= 2.1.0

Installing Poetry via pip:
```shell
pip install poetry
```

## Setup
```shell
poetry config virtualenvs.in-project true
poetry env activate
poetry install
```

## Run Pre-Commit
```shell
poetry run pre-commit run -a
```

## Run tests
```shell
poetry run pytest
```

## Run Server
```shell
poetry run uvicorn main:app --reload
```
