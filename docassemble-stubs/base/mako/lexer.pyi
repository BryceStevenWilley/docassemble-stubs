from _typeshed import Incomplete
from docassemble.base.mako import exceptions as exceptions, parsetree as parsetree
from docassemble.base.mako.pygen import adjust_whitespace as adjust_whitespace

_regexp_cache: Incomplete

class Lexer:
    text: Incomplete
    filename: Incomplete
    template: Incomplete
    matched_lineno: int
    matched_charpos: int
    lineno: int
    match_position: int
    tag: Incomplete
    control_line: Incomplete
    ternary_stack: Incomplete
    encoding: Incomplete
    preprocessor: Incomplete
    def __init__(self, text, filename: Incomplete | None = ..., input_encoding: Incomplete | None = ..., preprocessor: Incomplete | None = ...) -> None: ...
    @property
    def exception_kwargs(self): ...
    def match(self, regexp, flags: Incomplete | None = ...): ...
    def match_reg(self, reg): ...
    def parse_until_text(self, watch_nesting, *text): ...
    def append_node(self, nodecls, *args, **kwargs) -> None: ...
    _coding_re: Incomplete
    def decode_raw_stream(self, text, decode_raw, known_encoding, filename): ...
    textlength: Incomplete
    def parse(self): ...
    keyword: Incomplete
    def match_tag_start(self): ...
    def match_tag_end(self): ...
    def match_end(self): ...
    def match_text(self): ...
    def match_python_block(self): ...
    def match_expression(self): ...
    def match_control_line(self): ...
    def match_comment(self): ...
