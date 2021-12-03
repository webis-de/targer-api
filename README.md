# 🗣️ targer-api

Simple, type-safe access to the TARGER neural argument tagging APIs.

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