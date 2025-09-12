# acme-package-registry
This project is a package management solution meant to replace dependency on tools like HuggingFace with an internally managed tool with low ramp-up time for engineers and lots of documentation

## Collaborators

* Nathan Allie
* Roshen Cherian
* Lekhya sree Akella

# ACME Package Registry

A CLI tool to evaluate and score Hugging Face models, datasets, and codebases for ACME Corporation.

## Features
- CLI with install, test, and model evaluation commands
- Metrics: size, license, ramp up time, bus factor, dataset/code availability, dataset quality, code quality, performance claims
- Strong typing, style, and coverage enforcement
- NDJSON output for model scores
- Logging to file with configurable verbosity

## Usage
- `./run install` — Install dependencies
- `./run test` — Run tests and print coverage
- `./run URL_FILE` — Evaluate models from a list of URLs

## Development
- Python 3.11+
- Typer, Pydantic, HuggingFace Hub, GitPython, pytest, black, isort, flake8, mypy
- See `Makefile` for common tasks
=======