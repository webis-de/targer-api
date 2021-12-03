# 🗣️ targer-api

Simple, type-safe access to the [TARGER](https://github.com/webis-de/targer/) neural argument tagging APIs.

## Installation

```shell
pip install git+https://github.com/heinrichreimer/targer-api.git
```

## Usage

```python
from targer.api import fetch_arguments

arguments = fetch_arguments("""
Suicide should be a criminal offence. 
It is suspected that Francis committed suicide having been 
faced with being murdered over his large debt to Johnny Boy.
""")
print(arguments)
```

## Citation

If you use this package, please cite the [paper]((https://webis.de/publications.html#bondarenko_2019b))
from the [TARGER](https://github.com/webis-de/targer/) authors. 
You can use the following BibTeX information for citation:

```bibtex
@inproceedings{chernodub2019targer,
    title = {TARGER: Neural Argument Mining at Your Fingertips},
    author = {Chernodub, Artem and Oliynyk, Oleksiy and Heidenreich, Philipp and Bondarenko, Alexander and
 Hagen, Matthias and Biemann, Chris and Panchenko, Alexander},
    booktitle = {Proceedings of the 57th Annual Meeting of the Association of Computational Linguistics (ACL'2019)},
    year = {2019},
    address = {Florence, Italy}
}
```

## License

This repository is released under the [MIT license](LICENSE).
