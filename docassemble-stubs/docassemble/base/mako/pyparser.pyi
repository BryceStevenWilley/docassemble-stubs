from _typeshed import Incomplete as Incomplete
from docassemble.base.mako import _ast_util

reserved: Incomplete
arg_id: Incomplete

def parse(code, mode: str = ..., **exception_kwargs): ...

class FindIdentifiers(_ast_util.NodeVisitor):
    in_function: bool
    in_assign_targets: bool
    local_ident_stack: Incomplete
    listener: Incomplete
    exception_kwargs: Incomplete
    def __init__(self, listener, **exception_kwargs) -> None: ...
    def visit_ClassDef(self, node) -> None: ...
    def visit_Assign(self, node) -> None: ...
    def visit_ExceptHandler(self, node) -> None: ...
    def visit_Lambda(self, node, *args) -> None: ...
    def visit_FunctionDef(self, node) -> None: ...
    def visit_For(self, node) -> None: ...
    def visit_Name(self, node) -> None: ...
    def visit_Import(self, node) -> None: ...
    def visit_ImportFrom(self, node) -> None: ...

class FindTuple(_ast_util.NodeVisitor):
    listener: Incomplete
    exception_kwargs: Incomplete
    code_factory: Incomplete
    def __init__(self, listener, code_factory, **exception_kwargs) -> None: ...
    def visit_Tuple(self, node) -> None: ...

class ParseFunc(_ast_util.NodeVisitor):
    listener: Incomplete
    exception_kwargs: Incomplete
    def __init__(self, listener, **exception_kwargs) -> None: ...
    def visit_FunctionDef(self, node) -> None: ...

class ExpressionGenerator:
    generator: Incomplete
    def __init__(self, astnode) -> None: ...
    def value(self) -> None: ...