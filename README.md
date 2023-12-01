# oasdowngrade
This program attempts to downgrade certain OpenAPI 3.1 specification files to version 3.0.3, so that they can be used with common generators that still lack full support for 3.1,
including the popular openapi-generator (https://openapi-generator.tech). It may not work in all cases and was only tested with a number of FastAPI projects. It provides
workarounds for the following incompatibilities:

- const definitions - convert to an enum with single value
- null types - remove and set a nullable property for siblings

## Installation
```
pip install .
```

## Usage
```
oasdowngrade [-h] [-o OUTPUTFILE] [-f FORMAT] filename

positional arguments:
  filename

options:
  -h, --help            show this help message and exit
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        Output file name
  -f FORMAT, --format FORMAT
                        Output format (json, redoc)
```


