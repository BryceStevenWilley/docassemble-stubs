import ast
from _typeshed import Incomplete as Incomplete
from enum import Enum
from io import IOBase

FileType = IOBase

class RawValue:
    value: Incomplete
    def __init__(self, the_value) -> None: ...

def raw(val) -> None: ...

class ReturnValue:
    extra: Incomplete
    value: Incomplete
    def __init__(self, **kwargs) -> None: ...

def get_chat_log(utc: bool = ..., timezone: Union[Incomplete, None] = ...): ...
def user_logged_in() -> None: ...
def device(ip: bool = ...): ...
def language_from_browser(*pargs) -> None: ...
def country_name(country_code) -> None: ...
def language_name(language_code) -> None: ...
def subdivision_type(country_code) -> None: ...
def countries_list() -> None: ...
def user_privileges() -> None: ...
def user_has_privilege(*pargs) -> None: ...

class TheUser:
    def name(self) -> None: ...

def user_info() -> None: ...
def action_arguments() -> None: ...
def action_argument(item: Union[Incomplete, None] = ...): ...
def location_returned() -> None: ...
def location_known() -> None: ...
def user_lat_lon() -> None: ...
def chat_partners_available(*pargs, **kwargs) -> None: ...
def interview_email(key: Union[Incomplete, None] = ..., index: Union[Incomplete, None] = ...): ...
def get_emails(key: Union[Incomplete, None] = ..., index: Union[Incomplete, None] = ...): ...
def interview_url(**kwargs) -> None: ...

class DATagsSet:
    def add(self, item) -> None: ...
    def copy(self) -> None: ...
    def clear(self) -> None: ...
    def remove(self, elem) -> None: ...
    def discard(self, elem) -> None: ...
    def pop(self, *pargs) -> None: ...
    def __contains__(self, item) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __reversed__(self) -> None: ...
    def __and__(self, operand) -> None: ...
    def __or__(self, operand) -> None: ...
    def __iand__(self, operand) -> None: ...
    def __ior__(self, operand) -> None: ...
    def __isub__(self, operand) -> None: ...
    def __ixor__(self, operand) -> None: ...
    def __rand__(self, operand) -> None: ...
    def __ror__(self, operand) -> None: ...
    def __hash__(self): ...
    def union(self, other_set) -> None: ...
    def intersection(self, other_set) -> None: ...
    def difference(self, other_set) -> None: ...
    def isdisjoint(self, other_set) -> None: ...
    def issubset(self, other_set) -> None: ...
    def issuperset(self, other_set) -> None: ...

def session_tags() -> None: ...
def interview_url_action(action, **kwargs) -> None: ...
def interview_url_as_qr(**kwargs) -> None: ...
def interview_url_action_as_qr(action, **kwargs) -> None: ...
def get_info(att) -> None: ...
def set_info(**kwargs) -> None: ...
def set_progress(number) -> None: ...
def get_progress() -> None: ...
def update_terms(dictionary, auto: bool = ..., language: str = ...) -> None: ...
def set_save_status(status) -> None: ...

class DANav:
    past: Incomplete
    sections: Incomplete
    current: Incomplete
    progressive: bool
    hidden: bool
    disabled: bool
    def __init__(self) -> None: ...
    def set_section(self, section) -> None: ...
    def section_ids(self, language: Union[Incomplete, None] = ...): ...
    def get_section(self, display: bool = ..., language: Union[Incomplete, None] = ...): ...
    def hide(self) -> None: ...
    def unhide(self) -> None: ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...
    def visible(self, language: Union[Incomplete, None] = ...): ...
    def enabled(self) -> None: ...
    def set_sections(self, sections, language: Union[Incomplete, None] = ...) -> None: ...
    def get_sections(self, language: Union[Incomplete, None] = ...): ...
    def show_sections(self, style: str = ..., show_links: Union[Incomplete, None] = ...): ...

class WebFunc: ...

def write_record(key, data) -> None: ...
def read_records(key) -> None: ...
def delete_record(key, the_id) -> None: ...
def url_of(file_reference, **kwargs) -> None: ...
def server_capabilities() -> None: ...

class GenericObject:
    user: Incomplete
    role: str
    def __init__(self) -> None: ...

def background_response(*pargs, **kwargs) -> None: ...
def background_response_action(*pargs, **kwargs) -> None: ...
def background_action(*pargs, **kwargs) -> None: ...

class BackgroundResult:
    def __init__(self, result) -> None: ...

class MyAsyncResult:
    def wait(self) -> None: ...
    def failed(self) -> None: ...
    def ready(self) -> None: ...
    def result(self) -> None: ...
    def get(self) -> None: ...

def fix_punctuation(text, mark: Union[Incomplete, None] = ..., other_marks: Union[Incomplete, None] = ...): ...
def item_label(num, level: Union[Incomplete, None] = ..., punctuation: bool = ...): ...
def alpha(num, case: Union[Incomplete, None] = ...): ...
def roman(num, case: Union[Incomplete, None] = ...): ...

class LazyWord:
    original: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __mod__(self, other) -> None: ...

class LazyArray:
    original: Incomplete
    def __init__(self, array) -> None: ...
    def compute(self) -> None: ...
    def copy(self) -> None: ...
    def pop(self, *pargs) -> None: ...
    def __add__(self, other) -> None: ...
    def index(self, *pargs, **kwargs) -> None: ...
    def clear(self) -> None: ...
    def append(self, other) -> None: ...
    def remove(self, other) -> None: ...
    def extend(self, other) -> None: ...
    def __contains__(self, item) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __delitem__(self, index) -> None: ...
    def __reversed__(self) -> None: ...
    def __setitem__(self, index, the_value) -> None: ...
    def __getitem__(self, index) -> None: ...
    def __eq__(self, other): ...

def word(the_word, **kwargs) -> None: ...
def get_config(key, none_value: Union[Incomplete, None] = ...): ...
def get_default_timezone() -> None: ...
def prevent_going_back() -> None: ...
def set_language(lang, dialect: Union[Incomplete, None] = ..., voice: Union[Incomplete, None] = ...) -> None: ...
def get_language() -> None: ...
def set_country(country) -> None: ...
def get_country() -> None: ...
def get_dialect() -> None: ...
def set_locale(*pargs, **kwargs) -> None: ...
def get_locale(*pargs) -> None: ...
def need(*pargs) -> None: ...

verb_past: Incomplete
verb_present: Incomplete
noun_plural: Incomplete
noun_singular: Incomplete
indefinite_article: Incomplete
period_list: Incomplete
name_suffix: Incomplete
currency: Incomplete
currency_symbol: Incomplete
comma_list: Incomplete
comma_and_list: Incomplete
add_separators: Incomplete
nice_number: Incomplete
quantity_noun: Incomplete
capitalize: Incomplete
capitalize_function = capitalize
title_case: Incomplete
ordinal_number: Incomplete
ordinal: Incomplete

def space_to_underscore(a) -> None: ...
def message(*pargs, **kwargs) -> None: ...
def response(*pargs, **kwargs) -> None: ...
def json_response(data, response_code: Union[Incomplete, None] = ...) -> None: ...
def variables_as_json(include_internal: bool = ...) -> None: ...
def store_variables_snapshot(data: Union[Incomplete, None] = ..., include_internal: bool = ..., key: Union[Incomplete, None] = ..., persistent: bool = ...) -> None: ...
def all_variables(simplify: bool = ..., include_internal: bool = ..., special: bool = ..., make_copy: bool = ...): ...
def command(*pargs, **kwargs) -> None: ...
def force_ask(*pargs, **kwargs) -> None: ...
def static_image(filereference, width: Union[Incomplete, None] = ...): ...
def qr_code(string, width: Union[Incomplete, None] = ..., alt_text: Union[Incomplete, None] = ...): ...
def process_action() -> None: ...
def url_action(action, **kwargs) -> None: ...
def action_menu_item(label, action, **kwargs) -> None: ...
def from_b64_json(string) -> None: ...

class lister(ast.NodeVisitor):
    stack: Incomplete
    def __init__(self) -> None: ...
    def visit_Name(self, node) -> None: ...
    def visit_Attribute(self, node) -> None: ...
    def visit_Subscript(self, node) -> None: ...

def invalidate(*pargs) -> None: ...
def undefine(*pargs, invalidate: bool = ...) -> None: ...
def dispatch(var) -> None: ...
def set_variables(variables, process_objects: bool = ...) -> None: ...

class DefCaller(Enum):
    DEFINED: int
    VALUE: int
    SHOWIFDEF: int
    def is_pure(self) -> bool: ...
    def is_predicate(self) -> bool: ...

def value(var: str): ...
def defined(var: str) -> bool: ...
def single_paragraph(text) -> None: ...
def quote_paragraphs(text) -> None: ...
def set_live_help_status(availability: Union[Incomplete, None] = ..., mode: Union[Incomplete, None] = ..., partner_roles: Union[Incomplete, None] = ...) -> None: ...
def phone_number_in_e164(number, country: Union[Incomplete, None] = ...): ...
def phone_number_is_valid(number, country: Union[Incomplete, None] = ...): ...
def phone_number_part(number, part, country: Union[Incomplete, None] = ...): ...
def phone_number_formatted(number, country: Union[Incomplete, None] = ...): ...
def referring_url(default: Union[Incomplete, None] = ..., current: bool = ...): ...
def plain(text, default: Union[Incomplete, None] = ...): ...
def bold(text, default: Union[Incomplete, None] = ...): ...
def italic(text, default: Union[Incomplete, None] = ...): ...
def indent(text, by: Union[Incomplete, None] = ...): ...
def yesno(the_value, invert: bool = ...): ...
def noyes(the_value, invert: bool = ...): ...
def log(the_message, priority: str = ...) -> None: ...
def encode_name(var) -> None: ...
def decode_name(var) -> None: ...
def interview_list(exclude_invalid: bool = ..., action: Union[Incomplete, None] = ..., filename: Union[Incomplete, None] = ..., session: Union[Incomplete, None] = ..., user_id: Union[Incomplete, None] = ..., query: Union[Incomplete, None] = ..., include_dict: bool = ..., delete_shared: bool = ..., next_id: Union[Incomplete, None] = ...): ...
def interview_menu(*pargs, **kwargs) -> None: ...
def get_user_list(include_inactive: bool = ..., next_id: Union[Incomplete, None] = ...): ...
def manage_privileges(*pargs) -> None: ...
def get_user_info(user_id: Union[Incomplete, None] = ..., email: Union[Incomplete, None] = ...): ...
def set_user_info(**kwargs) -> None: ...
def create_user(email, password, privileges: Union[Incomplete, None] = ..., info: Union[Incomplete, None] = ...): ...
def get_user_secret(username, password) -> None: ...
def create_session(yaml_filename, secret: Union[Incomplete, None] = ..., url_args: Union[Incomplete, None] = ...): ...
def get_session_variables(yaml_filename, session_id, secret: Union[Incomplete, None] = ..., simplify: bool = ...): ...
def set_session_variables(yaml_filename, session_id, variables, secret: Union[Incomplete, None] = ..., question_name: Union[Incomplete, None] = ..., overwrite: bool = ..., process_objects: bool = ...) -> None: ...
def run_action_in_session(yaml_filename, session_id, action, arguments: Union[Incomplete, None] = ..., secret: Union[Incomplete, None] = ..., persistent: bool = ..., overwrite: bool = ...): ...
def get_question_data(yaml_filename, session_id, secret: Union[Incomplete, None] = ...): ...
def go_back_in_session(yaml_filename, session_id, secret: Union[Incomplete, None] = ...) -> None: ...
def redact(text) -> None: ...
def verbatim(text) -> None: ...

class DALocalFile:
    local_path: Incomplete
    def __init__(self, local_path) -> None: ...
    def path(self) -> None: ...
    def get_alt_text(self) -> None: ...
    alt_text: Incomplete
    def set_alt_text(self, alt_text) -> None: ...

def forget_result_of(*pargs) -> None: ...
def re_run_logic() -> None: ...
def reconsider(*pargs) -> None: ...
def single_to_double_newlines(text) -> None: ...

class CustomDataTypeRegister(type):
    def __init__(cls, name, bases, orig_clsdict) -> None: ...

class CustomDataType(metaclass=CustomDataTypeRegister):
    @classmethod
    def validate(cls, item) -> None: ...
    @classmethod
    def transform(cls, item) -> None: ...
    @classmethod
    def default_for(cls, item) -> None: ...
    @classmethod
    def empty(cls) -> None: ...

class ServerContext: ...