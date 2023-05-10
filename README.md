# docassemble-stubs

Docassemble has a lot of python functions, but no in-source types.
This package lets you install and use types for docassemble functions. 

Currently only includes docassemble.base. Types are fairly close to what's generated
with `stubgen`, and are still "in progress". Will make an official beta
release when I have gone through and tried to type the two largest files,
`util.py` and `functions.py`.

## Installation

Not currently on pypi, so for now, simply download this git repo and `pip install .`
while inside of the repo. `mypy` should be able to find types installed in your python environment.

## Updating the stubs

Install both these stubs and the corresponding version of docassemble, and run:

```bash
stubtest --allowlist base_allowlist.txt docassemble.base
```

All of the errors will be things that are missing in the stubs, and you will have to fix them.

TODO(brycew): find a way to automatically update the stubs without overwriting the manually
changed types?
