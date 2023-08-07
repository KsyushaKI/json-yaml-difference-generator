<div align="center">

<h1>Difference Generator</h1>

<p>Calculate the difference between two files (JSON and/or YAML )</p>

[![Actions Status](https://github.com/KsyushaKI/json-yaml-difference-generator/workflows/hexlet-check/badge.svg)](https://github.com/KsyushaKI/json-yaml-difference-generator/actions)
[![Actions Status2](https://github.com/KsyushaKI/json-yaml-difference-generator/workflows/Python%20CI/badge.svg)](https://github.com/KsyushaKI/json-yaml-difference-generator/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/368ed91f4862ed523a7f/maintainability)](https://codeclimate.com/github/KsyushaKI/json-yaml-difference-generator/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/368ed91f4862ed523a7f/test_coverage)](https://codeclimate.com/github/KsyushaKI/json-yaml-difference-generator/test_coverage)

</div>

## About

Difference Generator is a tool that determines the difference between two data structures. This is a popular task, for which there are many online services, such as http://www.jsondiff.com/.

Such a mechanism, for example, is used when outputting tests or when automatically tracking changes in configuration files.

Example:

```bash
gendiff --format plain filepath1.json filepath2.yml

Setting "common.setting4" was added with value: False
Setting "group1.baz" was updated. From 'bas' to 'bars'
Section "group2" was removed
```

### Features:

* [X] Supported file formats: JSON, YAML.
* [X] Output as plain text, structured text or JSON.
* [X] Can be used as CLI tool or external library.

### Built With

* Python
* Poetry
* PyYAML
* JSON
* Pytest
* flake8
* argparse

---

## Installation

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.8 or higher installed:

```bash
>> python --version
Python 3.8.0+
```

#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).

### Package

To use the package, you need to clone the repository to your computer. This is done using the ```git clone``` command. Clone the project:

```bash
>> git clone https://github.com/KsyushaKI/json-yaml-difference-generator.git
```

Then you have to build the package and install it:

```bash
>> cd json-yaml-difference-generator
```

```bash
>> poetry build
>> python3 -m pip install --user dist/*.whl
```

---

## Usage

Difference Generator can be used as CLI tool or as an external library.

### As external library

```python
from gendiff import generate_diff
diff = generate_diff(file_path1, file_path2, file_format)
```

### As CLI tool

The general usage is (both absolute and relative paths to files are supported):

```bash
>> gendiff [-f file_format] file_path1 file_path2
```

Difference Generator provides help command as well:

```bash
>> gendiff --help

usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output (default: "stylish")
```

## Demo

### _Stylish format_

If no format option is provided, output will be provided in _stylish_ format.

The difference is based on how the files have changed relative to each other, the keys are rendered in alphabetical order.

The absence of a plus or minus indicates that the key is in both files, and its values coincide. In all other situations, the value of the key is either different, or the key is only in one file.

```bash
>> gendiff file_path1.json file_path2.json

{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

#### :diamonds: Compare two nested JSON and/or YAML files: _stylish_ format

<a href="https://asciinema.org/a/566040" target="_blank"><img src="https://asciinema.org/a/566040.svg" width="300"/></a>

### _Plain format_

_Plain_ format reflects the situation as if we had combined the second object with the first one.

* If the new value of the property is a complex value, ```[complex value]``` is provided.
* If the property is nested, then the entire path to the root is displayed, not just including the parent.

```bash
>> gendiff --format plain file_path1.json file_path2.json

Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
```

#### :diamonds: Compare two nested JSON and/or YAML files: _plain_ format

<a href="https://asciinema.org/a/566251" target="_blank"><img src="https://asciinema.org/a/566251.svg" width="300"/></a>

### _JSON format_

In addition to an unstructured output (as a text), often an output in a structured format, such as JSON, is needed.

JSON (JavaScript Object Notation) is a standard text format for representing structured data based on JavaScript object syntax. It is usually used to transfer data in web applications (e.g. sending some data from the server to the client so that it can be displayed on a web page or vice versa).

```bash
>> gendiff --format json file_path1.json file_path2.json

{
    "follow": {
        "value": false,
        "type": "removed"
    },
    "host": {
        "value": "hexlet.io",
        "type": "unchanged"
    },
    "proxy": {
        "value": "123.234.53.22",
        "type": "removed"
    },
    "timeout": {
        "value": 50,
        "new value": 20,
        "type": "updated"
    },
    "verbose": {
        "value": true,
        "type": "added"
    }
}
```

#### :diamonds: Compare two nested JSON and/or YAML files: _JSON_ format

<a href="https://asciinema.org/a/566302" target="_blank"><img src="https://asciinema.org/a/566302.svg" width="300"/></a>

### :diamonds: _Full demonstration for flat JSON and/or YAML files_

<a href="https://asciinema.org/a/566309" target="_blank"><img src="https://asciinema.org/a/566309.svg" width="300"/></a>

### :diamonds: _Full demonstration for nested JSON and/or YAML files_

<a href="https://asciinema.org/a/566307" target="_blank"><img src="https://asciinema.org/a/566307.svg" width="300"/></a>

---

## Additionally

### Dependencies

* python = "^3.10"
* PyYAML = "^6.0"

### Dev Dependencies

* flake8 = "^6.0.0"
* pytest = "^7.2.1"
* pytest-cov = "^4.0.0"

---

This is the second training project of the ["Python Developer"](https://ru.hexlet.io/programs/python) course on [Hexlet.io](https://hexlet.io)

> GitHub [@KsyushaKI](https://github.com/KsyushaKI) &nbsp;&middot;&nbsp;
> LinkedIn [@Oksana Karshakevich](https://www.linkedin.com/in/oksana-karshakevich/)
