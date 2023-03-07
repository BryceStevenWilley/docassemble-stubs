# docassemble-stubs

Docassemble has a lot of python functions, but no in-source types.
This package lets you install and use types for docassemble functions. 

Currently only includes docassemble.base, but will eventually expand
to include docassemble.webapp. Types are fairly close to what's generated
with `stubgen`, and are still "in progress".

## Installation

Not currently on pypi, so for now, simply download this git repo and `pip install .`
while inside of the repo. `mypy` should be able to find types installed in your python environment.
