from _typeshed import Incomplete as Incomplete

class Template:
    lexer_cls: Incomplete
    names_used: Incomplete
    names_set: Incomplete
    module_id: Incomplete
    uri: Incomplete
    input_encoding: Incomplete
    output_encoding: Incomplete
    encoding_errors: Incomplete
    enable_loop: Incomplete
    strict_undefined: Incomplete
    module_writer: Incomplete
    default_filters: Incomplete
    buffer_filters: Incomplete
    imports: Incomplete
    future_imports: Incomplete
    preprocessor: Incomplete
    module: Incomplete
    filename: Incomplete
    callable_: Incomplete
    format_exceptions: Incomplete
    error_handler: Incomplete
    include_error_handler: Incomplete
    lookup: Incomplete
    module_directory: Incomplete
    def __init__(self, text: Union[Incomplete, None] = ..., filename: Union[Incomplete, None] = ..., uri: Union[Incomplete, None] = ..., format_exceptions: bool = ..., error_handler: Union[Incomplete, None] = ..., lookup: Union[Incomplete, None] = ..., output_encoding: Union[Incomplete, None] = ..., encoding_errors: str = ..., module_directory: Union[Incomplete, None] = ..., cache_args: Union[Incomplete, None] = ..., cache_impl: str = ..., cache_enabled: bool = ..., cache_type: Union[Incomplete, None] = ..., cache_dir: Union[Incomplete, None] = ..., cache_url: Union[Incomplete, None] = ..., module_filename: Union[Incomplete, None] = ..., input_encoding: Union[Incomplete, None] = ..., module_writer: Union[Incomplete, None] = ..., default_filters: Union[Incomplete, None] = ..., buffer_filters=..., strict_undefined: bool = ..., imports: Union[Incomplete, None] = ..., future_imports: Union[Incomplete, None] = ..., enable_loop: bool = ..., preprocessor: Union[Incomplete, None] = ..., lexer_cls: Union[Incomplete, None] = ..., include_error_handler: Union[Incomplete, None] = ...) -> None: ...
    def reserved_names(self) -> None: ...
    @property
    def source(self) -> None: ...
    @property
    def code(self) -> None: ...
    def cache(self) -> None: ...
    @property
    def cache_dir(self) -> None: ...
    @property
    def cache_url(self) -> None: ...
    @property
    def cache_type(self) -> None: ...
    def render(self, *args, **data) -> None: ...
    def render_unicode(self, *args, **data) -> None: ...
    def render_context(self, context, *args, **kwargs) -> None: ...
    def has_def(self, name) -> None: ...
    def get_def(self, name) -> None: ...
    def list_defs(self) -> None: ...
    @property
    def last_modified(self) -> None: ...

class ModuleTemplate(Template):
    module_id: Incomplete
    uri: Incomplete
    input_encoding: Incomplete
    output_encoding: Incomplete
    encoding_errors: Incomplete
    enable_loop: Incomplete
    module: Incomplete
    filename: Incomplete
    callable_: Incomplete
    format_exceptions: Incomplete
    error_handler: Incomplete
    include_error_handler: Incomplete
    lookup: Incomplete
    def __init__(self, module, module_filename: Union[Incomplete, None] = ..., template: Union[Incomplete, None] = ..., template_filename: Union[Incomplete, None] = ..., module_source: Union[Incomplete, None] = ..., template_source: Union[Incomplete, None] = ..., output_encoding: Union[Incomplete, None] = ..., encoding_errors: str = ..., format_exceptions: bool = ..., error_handler: Union[Incomplete, None] = ..., lookup: Union[Incomplete, None] = ..., cache_args: Union[Incomplete, None] = ..., cache_impl: str = ..., cache_enabled: bool = ..., cache_type: Union[Incomplete, None] = ..., cache_dir: Union[Incomplete, None] = ..., cache_url: Union[Incomplete, None] = ..., include_error_handler: Union[Incomplete, None] = ...) -> None: ...

class DefTemplate(Template):
    parent: Incomplete
    callable_: Incomplete
    output_encoding: Incomplete
    module: Incomplete
    encoding_errors: Incomplete
    format_exceptions: Incomplete
    error_handler: Incomplete
    include_error_handler: Incomplete
    enable_loop: Incomplete
    lookup: Incomplete
    def __init__(self, parent, callable_) -> None: ...
    def get_def(self, name) -> None: ...

class ModuleInfo:
    module: Incomplete
    module_filename: Incomplete
    template_filename: Incomplete
    module_source: Incomplete
    template_source: Incomplete
    template_uri: Incomplete
    def __init__(self, module, module_filename, template, template_filename, module_source, template_source, template_uri) -> None: ...
    @classmethod
    def get_module_source_metadata(cls, module_source, full_line_map: bool = ...): ...
    @property
    def code(self) -> None: ...
    @property
    def source(self) -> None: ...
