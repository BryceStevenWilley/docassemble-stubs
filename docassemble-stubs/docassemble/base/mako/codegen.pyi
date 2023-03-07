from _typeshed import Incomplete as Incomplete

MAGIC_NUMBER: int
TOPLEVEL_DECLARED: Incomplete
RESERVED_NAMES: Incomplete

def compile(node, uri, filename: Union[Incomplete, None] = ..., default_filters: Union[Incomplete, None] = ..., buffer_filters: Union[Incomplete, None] = ..., imports: Union[Incomplete, None] = ..., future_imports: Union[Incomplete, None] = ..., source_encoding: Union[Incomplete, None] = ..., generate_magic_comment: bool = ..., strict_undefined: bool = ..., enable_loop: bool = ..., names_used=..., names_set=..., reserved_names=...): ...

class _CompileContext:
    uri: Incomplete
    filename: Incomplete
    default_filters: Incomplete
    buffer_filters: Incomplete
    imports: Incomplete
    future_imports: Incomplete
    source_encoding: Incomplete
    generate_magic_comment: Incomplete
    strict_undefined: Incomplete
    enable_loop: Incomplete
    names_used: Incomplete
    names_set: Incomplete
    reserved_names: Incomplete
    def __init__(self, uri, filename, default_filters, buffer_filters, imports, future_imports, source_encoding, generate_magic_comment, strict_undefined, enable_loop, names_used, names_set, reserved_names) -> None: ...

class _GenerateRenderMethod:
    printer: Incomplete
    compiler: Incomplete
    node: Incomplete
    identifier_stack: Incomplete
    in_def: Incomplete
    def __init__(self, printer, compiler, node) -> None: ...
    def write_metadata_struct(self) -> None: ...
    @property
    def identifiers(self) -> None: ...
    def write_toplevel(self) -> None: ...
    def write_render_callable(self, node, name, args, buffered, filtered, cached) -> None: ...
    def write_module_code(self, module_code) -> None: ...
    def write_inherit(self, node) -> None: ...
    def write_namespaces(self, namespaces) -> None: ...
    def write_variable_declares(self, identifiers, toplevel: bool = ..., limit: Union[Incomplete, None] = ...) -> None: ...
    def write_def_decl(self, node, identifiers) -> None: ...
    def write_inline_def(self, node, identifiers, nested) -> None: ...
    def write_def_finish(self, node, buffered, filtered, cached, callstack: bool = ...) -> None: ...
    def write_cache_decorator(self, node_or_pagetag, name, args, buffered, identifiers, inline: bool = ..., toplevel: bool = ...) -> None: ...
    def create_filter_callable(self, args, target, is_expression) -> None: ...
    def visitExpression(self, node) -> None: ...
    def visitControlLine(self, node) -> None: ...
    def visitText(self, node) -> None: ...
    def visitTextTag(self, node) -> None: ...
    def visitCode(self, node) -> None: ...
    def visitIncludeTag(self, node) -> None: ...
    def visitNamespaceTag(self, node) -> None: ...
    def visitDefTag(self, node) -> None: ...
    def visitBlockTag(self, node) -> None: ...
    def visitCallNamespaceTag(self, node) -> None: ...
    def visitCallTag(self, node) -> None: ...

class _Identifiers:
    declared: Incomplete
    topleveldefs: Incomplete
    compiler: Incomplete
    undeclared: Incomplete
    locally_declared: Incomplete
    locally_assigned: Incomplete
    argument_declared: Incomplete
    closuredefs: Incomplete
    node: Incomplete
    def __init__(self, compiler, node: Union[Incomplete, None] = ..., parent: Union[Incomplete, None] = ..., nested: bool = ...) -> None: ...
    def branch(self, node, **kwargs) -> None: ...
    @property
    def defs(self) -> None: ...
    def check_declared(self, node) -> None: ...
    def add_declared(self, ident) -> None: ...
    def visitExpression(self, node) -> None: ...
    def visitControlLine(self, node) -> None: ...
    def visitCode(self, node) -> None: ...
    def visitNamespaceTag(self, node) -> None: ...
    def visitDefTag(self, node) -> None: ...
    def visitBlockTag(self, node) -> None: ...
    def visitTextTag(self, node) -> None: ...
    def visitIncludeTag(self, node) -> None: ...
    def visitPageTag(self, node) -> None: ...
    def visitCallNamespaceTag(self, node) -> None: ...
    def visitCallTag(self, node) -> None: ...

def mangle_mako_loop(node, printer) -> None: ...

class LoopVariable:
    detected: bool
    def __init__(self) -> None: ...
    def visitControlLine(self, node) -> None: ...
    def visitCode(self, node) -> None: ...
    def visitExpression(self, node) -> None: ...
