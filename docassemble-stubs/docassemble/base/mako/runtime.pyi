from _typeshed import Incomplete as Incomplete

class Context:
    namespaces: Incomplete
    caller_stack: Incomplete
    def __init__(self, buffer, **data) -> None: ...
    @property
    def lookup(self) -> None: ...
    @property
    def kwargs(self) -> None: ...
    def push_caller(self, caller) -> None: ...
    def pop_caller(self) -> None: ...
    def keys(self) -> None: ...
    def __getitem__(self, key) -> None: ...
    def get(self, key, default: Union[Incomplete, None] = ...): ...
    def write(self, string) -> None: ...
    def writer(self) -> None: ...

class CallerStack(list):
    nextcaller: Incomplete
    def __init__(self) -> None: ...
    def __nonzero__(self) -> None: ...
    def __bool__(self) -> bool: ...
    def __getattr__(self, key) -> None: ...

class Undefined:
    def __nonzero__(self) -> None: ...
    def __bool__(self) -> bool: ...

UNDEFINED: Incomplete
STOP_RENDERING: str

class LoopStack:
    stack: Incomplete
    def __init__(self) -> None: ...
    def __getattr__(self, key) -> None: ...
    def __iter__(self): ...

class LoopContext:
    index: int
    parent: Incomplete
    def __init__(self, iterable) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    @property
    def reverse_index(self) -> None: ...
    @property
    def first(self) -> None: ...
    @property
    def last(self) -> None: ...
    @property
    def even(self) -> None: ...
    @property
    def odd(self) -> None: ...
    def cycle(self, *values) -> None: ...

class _NSAttr:
    def __init__(self, parent) -> None: ...
    def __getattr__(self, key) -> None: ...

class Namespace:
    name: Incomplete
    context: Incomplete
    inherits: Incomplete
    callables: Incomplete
    def __init__(self, name, context, callables: Union[Incomplete, None] = ..., inherits: Union[Incomplete, None] = ..., populate_self: bool = ..., calling_uri: Union[Incomplete, None] = ...) -> None: ...
    module: Incomplete
    template: Incomplete
    filename: Incomplete
    uri: Incomplete
    def attr(self) -> None: ...
    def get_namespace(self, uri) -> None: ...
    def get_template(self, uri) -> None: ...
    def get_cached(self, key, **kwargs) -> None: ...
    @property
    def cache(self) -> None: ...
    def include_file(self, uri, **kwargs) -> None: ...
    def __getattr__(self, key) -> None: ...

class TemplateNamespace(Namespace):
    name: Incomplete
    context: Incomplete
    inherits: Incomplete
    callables: Incomplete
    template: Incomplete
    def __init__(self, name, context, template: Union[Incomplete, None] = ..., templateuri: Union[Incomplete, None] = ..., callables: Union[Incomplete, None] = ..., inherits: Union[Incomplete, None] = ..., populate_self: bool = ..., calling_uri: Union[Incomplete, None] = ...) -> None: ...
    @property
    def module(self) -> None: ...
    @property
    def filename(self) -> None: ...
    @property
    def uri(self) -> None: ...
    def __getattr__(self, key) -> None: ...

class ModuleNamespace(Namespace):
    name: Incomplete
    context: Incomplete
    inherits: Incomplete
    callables: Incomplete
    module: Incomplete
    def __init__(self, name, context, module, callables: Union[Incomplete, None] = ..., inherits: Union[Incomplete, None] = ..., populate_self: bool = ..., calling_uri: Union[Incomplete, None] = ...) -> None: ...
    @property
    def filename(self) -> None: ...
    def __getattr__(self, key) -> None: ...

def supports_caller(func) -> None: ...
def capture(context, callable_, *args, **kwargs) -> None: ...