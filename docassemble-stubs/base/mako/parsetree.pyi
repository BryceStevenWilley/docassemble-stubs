from _typeshed import Incomplete
from docassemble.base.mako import ast as ast, exceptions as exceptions, filters as filters, util as util

class Node:
    source: Incomplete
    lineno: Incomplete
    pos: Incomplete
    filename: Incomplete
    def __init__(self, source, lineno, pos, filename) -> None: ...
    @property
    def exception_kwargs(self): ...
    def get_children(self): ...
    def accept_visitor(self, visitor) -> None: ...

class TemplateNode(Node):
    nodes: Incomplete
    page_attributes: Incomplete
    def __init__(self, filename) -> None: ...
    def get_children(self): ...
    def __repr__(self): ...

class ControlLine(Node):
    has_loop_context: bool
    text: Incomplete
    keyword: Incomplete
    isend: Incomplete
    is_primary: Incomplete
    nodes: Incomplete
    _declared_identifiers: Incomplete
    _undeclared_identifiers: Incomplete
    names_set: Incomplete
    def __init__(self, keyword, isend, text, **kwargs) -> None: ...
    def get_children(self): ...
    def declared_identifiers(self): ...
    def undeclared_identifiers(self): ...
    def is_ternary(self, keyword): ...
    def __repr__(self): ...

class Text(Node):
    content: Incomplete
    def __init__(self, content, **kwargs) -> None: ...
    def __repr__(self): ...

class Code(Node):
    text: Incomplete
    ismodule: Incomplete
    code: Incomplete
    def __init__(self, text, ismodule, **kwargs) -> None: ...
    def declared_identifiers(self): ...
    def undeclared_identifiers(self): ...
    def __repr__(self): ...

class Comment(Node):
    text: Incomplete
    def __init__(self, text, **kwargs) -> None: ...
    def __repr__(self): ...

class Expression(Node):
    text: Incomplete
    escapes: Incomplete
    escapes_code: Incomplete
    code: Incomplete
    def __init__(self, text, escapes, **kwargs) -> None: ...
    def declared_identifiers(self): ...
    def undeclared_identifiers(self): ...
    def __repr__(self): ...

class _TagMeta(type):
    _classmap: Incomplete
    def __init__(cls, clsname, bases, dict_) -> None: ...
    def __call__(cls, keyword, attributes, **kwargs): ...

class Tag(Node, metaclass=_TagMeta):
    __keyword__: Incomplete
    keyword: Incomplete
    attributes: Incomplete
    parent: Incomplete
    nodes: Incomplete
    def __init__(self, keyword, attributes, expressions, nonexpressions, required, **kwargs) -> None: ...
    def is_root(self): ...
    def get_children(self): ...
    parsed_attributes: Incomplete
    expression_undeclared_identifiers: Incomplete
    def _parse_attributes(self, expressions, nonexpressions) -> None: ...
    def declared_identifiers(self): ...
    def undeclared_identifiers(self): ...
    def __repr__(self): ...

class IncludeTag(Tag):
    __keyword__: str
    page_args: Incomplete
    def __init__(self, keyword, attributes, **kwargs) -> None: ...
    def declared_identifiers(self): ...
    def undeclared_identifiers(self): ...

class NamespaceTag(Tag):
    __keyword__: str
    name: Incomplete
    def __init__(self, keyword, attributes, **kwargs) -> None: ...
    def declared_identifiers(self): ...

class TextTag(Tag):
    __keyword__: str
    filter_args: Incomplete
    def __init__(self, keyword, attributes, **kwargs) -> None: ...
    def undeclared_identifiers(self): ...

class DefTag(Tag):
    __keyword__: str
    function_decl: Incomplete
    name: Incomplete
    decorator: Incomplete
    filter_args: Incomplete
    def __init__(self, keyword, attributes, **kwargs) -> None: ...
    is_anonymous: bool
    is_block: bool
    @property
    def funcname(self): ...
    def get_argument_expressions(self, **kw): ...
    def declared_identifiers(self): ...
    def undeclared_identifiers(self): ...

class BlockTag(Tag):
    __keyword__: str
    body_decl: Incomplete
    name: Incomplete
    decorator: Incomplete
    filter_args: Incomplete
    def __init__(self, keyword, attributes, **kwargs) -> None: ...
    is_block: bool
    @property
    def is_anonymous(self): ...
    @property
    def funcname(self): ...
    def get_argument_expressions(self, **kw): ...
    def declared_identifiers(self): ...
    def undeclared_identifiers(self): ...

class CallTag(Tag):
    __keyword__: str
    expression: Incomplete
    code: Incomplete
    body_decl: Incomplete
    def __init__(self, keyword, attributes, **kwargs) -> None: ...
    def declared_identifiers(self): ...
    def undeclared_identifiers(self): ...

class CallNamespaceTag(Tag):
    expression: Incomplete
    code: Incomplete
    body_decl: Incomplete
    def __init__(self, namespace, defname, attributes, **kwargs) -> None: ...
    def declared_identifiers(self): ...
    def undeclared_identifiers(self): ...

class InheritTag(Tag):
    __keyword__: str
    def __init__(self, keyword, attributes, **kwargs) -> None: ...

class PageTag(Tag):
    __keyword__: str
    body_decl: Incomplete
    filter_args: Incomplete
    def __init__(self, keyword, attributes, **kwargs) -> None: ...
    def declared_identifiers(self): ...
