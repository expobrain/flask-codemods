# flask-codemods

[![Unit testing, formatting & linting](https://github.com/expobrain/flask-codemods/actions/workflows/test.yml/badge.svg)](https://github.com/expobrain/flask-codemods/actions/workflows/test.yml)

# Flask codemods

This is a collection of codemods to programmatically upgrade your Flaks codebase to a given major version; based on on [LibCST](https://github.com/Instagram/LibCST/).

- [Installation](#Installation)
- [Run the codemods](#Run_the_codemods)
- [Run the tests](#Run_the_tests)
- [Upgrade to 2.0.x](#2_0)
  - [DotInBlueprintNameCommand](#DotInBlueprintNameCommand)

## Installation

Codemods are based on [LibCST](https://github.com/Instagram/LibCST/), it will be installed by running:

```shell
poetry install
```

## Run the codemods

To run the codemods a small shell script `mod` is provided for convenience:

```shell
./mod upgrade_2_0.DotInBlueprintName [<source_code_path>, ...]
```

## Run the tests

Tests are executed using [Pytest](https://docs.pytest.org/) which will be installed as dev requirements:

```shell
make test
```

## Upgrade to 2.0.x

### DotInBlueprintName
