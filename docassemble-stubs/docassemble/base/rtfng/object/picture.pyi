from _typeshed import Incomplete as Incomplete
from docassemble.base.rtfng.document.base import RawCode as RawCode

class Image(RawCode):
    PNG_LIB: str
    JPG_LIB: str
    PICT_TYPES: Incomplete
    def __init__(self, file_name, **kwargs) -> None: ...
    def ToRawCode(self, var_name) -> None: ...
