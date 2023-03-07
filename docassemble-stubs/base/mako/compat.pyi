from _typeshed import Incomplete as Incomplete
from typing import NamedTuple

win32: Incomplete
pypy: Incomplete
py38: Incomplete

class ArgSpec(NamedTuple):
    args: Incomplete
    varargs: Incomplete
    keywords: Incomplete
    defaults: Incomplete

def inspect_getargspec(func) -> None: ...
def load_module(module_id, path) -> None: ...
def exception_as() -> None: ...
def exception_name(exc) -> None: ...
def importlib_metadata_get(group) -> None: ...
