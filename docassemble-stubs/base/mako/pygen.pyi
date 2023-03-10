from _typeshed import Incomplete
from docassemble.base.mako import exceptions as exceptions

class PythonPrinter:
    indent: int
    indent_detail: Incomplete
    indentstring: str
    stream: Incomplete
    lineno: int
    line_buffer: Incomplete
    in_indent_lines: bool
    source_map: Incomplete
    _re_space_comment: Incomplete
    _re_space: Incomplete
    _re_indent: Incomplete
    _re_compound: Incomplete
    _re_indent_keyword: Incomplete
    _re_unindentor: Incomplete
    def __init__(self, stream) -> None: ...
    def _update_lineno(self, num) -> None: ...
    def start_source(self, lineno) -> None: ...
    def write_blanks(self, num) -> None: ...
    def write_indented_block(self, block, starting_lineno: Incomplete | None = ...) -> None: ...
    def writelines(self, *lines) -> None: ...
    def writeline(self, line) -> None: ...
    def close(self) -> None: ...
    def _is_unindentor(self, line): ...
    def _indent_line(self, line, stripspace: str = ...): ...
    def _reset_multi_line_flags(self) -> None: ...
    backslashed: Incomplete
    triplequoted: Incomplete
    def _in_multi_line(self, line): ...
    def _flush_adjusted_lines(self) -> None: ...

def adjust_whitespace(text): ...
