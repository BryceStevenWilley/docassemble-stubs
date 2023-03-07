from _typeshed import Incomplete as Incomplete

class TGPlugin:
    extra_vars_func: Incomplete
    extension: Incomplete
    lookup: Incomplete
    tmpl_options: Incomplete
    def __init__(self, extra_vars_func: Union[Incomplete, None] = ..., options: Union[Incomplete, None] = ..., extension: str = ...) -> None: ...
    def load_template(self, templatename, template_string: Union[Incomplete, None] = ...): ...
    def render(self, info, format: str = ..., fragment: bool = ..., template: Union[Incomplete, None] = ...): ...
