import ast
from _typeshed import Incomplete

fix_assign: Incomplete
valid_variable_match: Incomplete

class myextract(ast.NodeVisitor):
    stack: Incomplete
    in_subscript: int
    in_params: int
    seen_name: bool
    seen_complexity: bool
    def __init__(self) -> None: ...
    def visit_Name(self, node) -> None: ...
    def visit_Call(self, node) -> None: ...
    def visit_Attribute(self, node) -> None: ...
    def visit_Subscript(self, node) -> None: ...

class myvisitnode(ast.NodeVisitor):
    names: Incomplete
    targets: Incomplete
    depth: int
    calls: Incomplete
    def __init__(self) -> None: ...
    def generic_visit(self, node) -> None: ...
    def visit_Call(self, node) -> None: ...
    def visit_Subscript(self, node) -> None: ...
    def visit_Attribute(self, node) -> None: ...
    def visit_ExceptHandler(self, node) -> None: ...
    def visit_Assign(self, node) -> None: ...
    def visit_AugAssign(self, node) -> None: ...
    def visit_AnnAssign(self, node) -> None: ...
    def visit_FunctionDef(self, node) -> None: ...
    def visit_Import(self, node) -> None: ...
    def visit_ImportFrom(self, node) -> None: ...
    def visit_GeneratorExp(self, node) -> None: ...
    def visit_Lambda(self, node) -> None: ...
    def visit_ListComp(self, node) -> None: ...
    def visit_DictComp(self, node) -> None: ...
    def visit_SetComp(self, node) -> None: ...
    def visit_For(self, node) -> None: ...
    def visit_Name(self, node) -> None: ...

class detectIllegal(ast.NodeVisitor):
    illegal: bool
    def __init__(self) -> None: ...
    def visit_FunctionDef(self, node) -> None: ...
    def visit_ExceptHandler(self, node) -> None: ...
    def visit_ClassDef(self, node) -> None: ...
    def visit_Return(self, node) -> None: ...
    def visit_Delete(self, node) -> None: ...
    def visit_Assign(self, node) -> None: ...
    def visit_AugAssign(self, node) -> None: ...
    def visit_Print(self, node) -> None: ...
    def visit_For(self, node) -> None: ...
    def visit_While(self, node) -> None: ...
    def visit_If(self, node) -> None: ...
    def visit_With(self, node) -> None: ...
    def visit_Raise(self, node) -> None: ...
    def visit_TryExcept(self, node) -> None: ...
    def visit_TryFinally(self, node) -> None: ...
    def visit_Assert(self, node) -> None: ...
    def visit_Import(self, node) -> None: ...
    def visit_ImportFrom(self, node) -> None: ...
    def visit_Exec(self, node) -> None: ...
    def visit_Global(self, node) -> None: ...
    def visit_Pass(self, node) -> None: ...
    def visit_Break(self, node) -> None: ...
    def visit_Continue(self, node) -> None: ...
    def visit_BoolOp(self, node) -> None: ...
    def visit_BinOp(self, node) -> None: ...
    def visit_UnaryOp(self, node) -> None: ...
    def visit_Lambda(self, node) -> None: ...
    def visit_IfExp(self, node) -> None: ...
    def visit_Dict(self, node) -> None: ...
    def visit_Set(self, node) -> None: ...
    def visit_ListComp(self, node) -> None: ...
    def visit_SetComp(self, node) -> None: ...
    def visit_DictComp(self, node) -> None: ...
    def visit_GeneratorExp(self, node) -> None: ...
    def visit_Yield(self, node) -> None: ...
    def visit_Compare(self, node) -> None: ...
    def visit_Call(self, node) -> None: ...
    def visit_Repr(self, node) -> None: ...
    def visit_List(self, node) -> None: ...
    def visit_Tuple(self, node) -> None: ...

class detectIllegalQuery(ast.NodeVisitor):
    illegal: bool
    def __init__(self) -> None: ...
    def visit_FunctionDef(self, node) -> None: ...
    def visit_ExceptHandler(self, node) -> None: ...
    def visit_ClassDef(self, node) -> None: ...
    def visit_Return(self, node) -> None: ...
    def visit_Delete(self, node) -> None: ...
    def visit_Assign(self, node) -> None: ...
    def visit_AugAssign(self, node) -> None: ...
    def visit_Print(self, node) -> None: ...
    def visit_For(self, node) -> None: ...
    def visit_While(self, node) -> None: ...
    def visit_If(self, node) -> None: ...
    def visit_With(self, node) -> None: ...
    def visit_Raise(self, node) -> None: ...
    def visit_TryExcept(self, node) -> None: ...
    def visit_TryFinally(self, node) -> None: ...
    def visit_Assert(self, node) -> None: ...
    def visit_Import(self, node) -> None: ...
    def visit_ImportFrom(self, node) -> None: ...
    def visit_Exec(self, node) -> None: ...
    def visit_Global(self, node) -> None: ...
    def visit_Pass(self, node) -> None: ...
    def visit_Break(self, node) -> None: ...
    def visit_Continue(self, node) -> None: ...
    def visit_Lambda(self, node) -> None: ...
    def visit_IfExp(self, node) -> None: ...
    def visit_Dict(self, node) -> None: ...
    def visit_Set(self, node) -> None: ...
    def visit_ListComp(self, node) -> None: ...
    def visit_SetComp(self, node) -> None: ...
    def visit_DictComp(self, node) -> None: ...
    def visit_GeneratorExp(self, node) -> None: ...
    def visit_Yield(self, node) -> None: ...
    def visit_Call(self, node) -> None: ...
    def visit_Repr(self, node) -> None: ...
