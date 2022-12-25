# TimeKeeper

[![CI](https://github.com/PyryL/ot-harjoitustyo/actions/workflows/main.yml/badge.svg)](https://github.com/PyryL/ot-harjoitustyo/actions/workflows/main.yml)
[![coverage](https://codecov.io/gh/PyryL/ot-harjoitustyo/branch/main/graph/badge.svg?token=PC8AAR5TL3)](https://codecov.io/gh/PyryL/ot-harjoitustyo)

TimeKeeper is a desktop application allowing running competition hosts to easily organize their timekeeping. Application manages competitors and their results all in cloud, which enables real-time collaboration of multiple users.

This is a project for a computer sciense [course](https://ohjelmistotekniikka-hy.github.io/) in University of Helsinki in autumn 2022.

## Installation

Make sure that you have Python version 3.8 or higher.
Also make sure that you have [Poetry](https://python-poetry.org/) installed.

You can install TimeKeeper by following these steps:

1. Download the latest source code from [releases page](https://github.com/PyryL/ot-harjoitustyo/releases) and unzip the downloaded archive.
2. Open Terminal, navigate to the unzipped directory and run `poetry install`.
3. Start the application by running `poetry run invoke start`.

## Development

Unit tests can be run with `poetry run invoke test`

Style tests can be run with `poetry run invoke lint`

Branch coverage report can be generated with `poetry run invoke coverage-report` after which the report can be seen by opening `htmlcov/index.html`

## Docs

* [User manual](docs/manual.md)
* [Requirement specification](docs/requirements.md)
* [Architecture](docs/architecture.md)
* [Tests](docs/tests.md)
* [Changelog](docs/changelog.md)
* [Records of working hours](docs/working-hours.md)
