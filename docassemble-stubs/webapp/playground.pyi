from _typeshed import Incomplete
from docassemble.base.util import DADict, DAList, DAObject

class DADecoration(DAObject): ...

class DADecorationDict(DADict):
    object_type: Incomplete
    auto_gather: bool
    there_are_any: bool
    def init(self, *pargs, **kwargs) -> None: ...

class DAAttachment(DAObject): ...

class DAAttachmentList(DAList):
    object_type: Incomplete
    auto_gather: bool
    def init(self, *pargs, **kwargs) -> None: ...
    def url_list(self, project: str = ...): ...

class DAUploadMultiple(DAObject): ...
class DAUpload(DAObject): ...

class DAInterview(DAObject):
    blocks: Incomplete
    questions: Incomplete
    final_screen: Incomplete
    decorations: Incomplete
    target_variable: Incomplete
    def init(self, *pargs, **kwargs) -> None: ...
    def has_decorations(self) -> bool: ...
    def decoration_list(self) -> list: ...
    def package_info(self) -> dict: ...
    def yaml_file_name(self): ...
    def all_blocks(self): ...
    def demonstrate(self) -> None: ...
    def source(self): ...
    def known_source(self, skip: Incomplete | None = ...): ...

class DAField(DAObject): ...

class DAFieldList(DAList):
    object_type: Incomplete
    auto_gather: bool
    gathered: bool
    def init(self, *pargs, **kwargs) -> None: ...
    def __str__(self): ...

class DAQuestion(DAObject):
    field_list: Incomplete
    templates_used: Incomplete
    static_files_used: Incomplete
    def init(self, *pargs, **kwargs) -> None: ...
    def names_reduced(self): ...
    def other_variables(self): ...
    def source(self, follow_additional_fields: bool = ...): ...

class DAQuestionDict(DADict):
    object_type: Incomplete
    auto_gather: bool
    gathered: bool
    is_mandatory: bool
    def init(self, *pargs, **kwargs) -> None: ...

class PlaygroundSection:
    user_id: Incomplete
    current_info: Incomplete
    section: Incomplete
    project: Incomplete
    def __init__(self, section: str = ..., project: str = ...) -> None: ...
    def get_area(self): ...
    file_list: Incomplete
    def _update_file_list(self) -> None: ...
    def image_file_list(self): ...
    def reduced_file_list(self): ...
    def get_file(self, filename): ...
    def get_mimetype(self, filename): ...
    def file_exists(self, filename): ...
    def delete_file(self, filename) -> None: ...
    def read_file(self, filename): ...
    def write_file(self, filename, content, binary: bool = ...) -> None: ...
    def commit(self) -> None: ...
    def copy_from(self, from_file, filename: Incomplete | None = ...): ...
    def is_fillable_docx(self, filename): ...
    def is_markdown(self, filename): ...
    def is_pdf(self, filename): ...
    def get_fields(self, filename): ...
    def convert_file_to_md(self, filename, convert_variables: bool = ...): ...
    def variables_from_file(self, filename): ...

class Playground(PlaygroundSection):
    def interview_url(self, filename): ...
    def write_package(self, pkgname, info) -> None: ...
    def get_package_as_zip(self, pkgname): ...
    def variables_from(self, content): ...

def indent_by(text: str | None, num: int) -> str: ...
def varname(var_name: str) -> str: ...
def oneline(text: str) -> str: ...
def to_yaml_file(text: str) -> str: ...
def base_name(filename): ...
def to_package_name(text) -> str: ...
