[![PyPi](https://img.shields.io/pypi/v/targer-api?style=flat-square)](https://pypi.org/project/targer-api/)
[![CI](https://img.shields.io/github/actions/workflow/status/webis-de/targer-api/ci.yml?branch=main&style=flat-square)](https://github.com/webis-de/targer-api/actions/workflows/ci.yml)
[![Code coverage](https://img.shields.io/codecov/c/github/webis-de/targer-api?style=flat-square)](https://codecov.io/github/webis-de/targer-api/)
[![Python](https://img.shields.io/pypi/pyversions/targer-api?style=flat-square)](https://pypi.org/project/targer-api/)
[![Issues](https://img.shields.io/github/issues/webis-de/targer-api?style=flat-square)](https://github.com/webis-de/targer-api/issues)
[![Commit activity](https://img.shields.io/github/commit-activity/m/webis-de/targer-api?style=flat-square)](https://github.com/webis-de/targer-api/commits)
[![Downloads](https://img.shields.io/pypi/dm/targer-api?style=flat-square)](https://pypi.org/project/targer-api/)
[![License](https://img.shields.io/github/license/webis-de/targer-api?style=flat-square)](LICENSE)

# 🗣️ targer-api

Simple, type-safe access to the [TARGER](https://github.com/webis-de/targer/) neural argument tagging APIs.

With this package you can analyze the argumentative structures 
using one of the pre-trained neural models for argument mining 
found in the [TARGER API](https://demo.webis.de/targer-api/apidocs/).
The API is hosted by the [Webis research group](https://webis.de/) 
and free to use.

## Installation

```shell
pip install targer-api
```

## Usage

```python
from targer_api import analyze_text

arguments = analyze_text(
    "The alternative vote is advantageous. "
    "The President is directly elected by secret ballot "
    "under the system of the Alternative Vote."
)
print(arguments)
```

## Citation

If you use this package, please cite the [paper]((https://webis.de/publications.html#bondarenko_2019b))
from the [TARGER](https://github.com/webis-de/targer/) authors. 
You can use the following BibTeX information for citation:

```bibtex
@InProceedings{chernodub:2019,
  author =                {Artem Chernodub and Oleksiy Oliynyk and Philipp Heidenreich and Alexander Bondarenko and Matthias Hagen and Chris Biemann and Alexander Panchenko},
  booktitle =             {57th Annual Meeting of the Association for Computational Linguistics (ACL 2019)},
  editor =                {{Martha R.} {Costa-juss{\`a}} and Enrique Alfonseca},
  ids =                   {bondarenko:2019b},
  month =                 jul,
  pages =                 {195-200},
  publisher =             {Association for Computational Linguistics},
  site =                  {Florence, Italy},
  title =                 {{TARGER: Neural Argument Mining at Your Fingertips}},
  url =                   {https://www.aclweb.org/anthology/P19-3031},
  year =                  2019
}
```

## Development

To build and develop this package you need to install the `build` package:
```shell
pip install build
```

### Installation

Install package dependencies:
```shell
pip install -e .
```

### Testing

Install test dependencies:
```shell
pip install -e .[test]
```

Verify your changes against the test suite to verify.
```shell
flake8 targer_api tests examples
pylint -E targer_api tests examples
pytest targer_api tests examples
```

Please also add tests for the axioms or integrations you've added.

### Build wheel

A wheel for this package can be built by:
```shell
python -m build
```

## License

This repository is released under the [MIT license](LICENSE).
