import ast
from _typeshed import Incomplete
from enum import Enum
from io import IOBase
from user_agents import UserAgent # type: ignore
import us as us # type: ignore
from typing import Any, Union, Literal, Dict, List, Optional, Tuple, Callable

server: Incomplete
this_thread: Incomplete

FileType = IOBase

__all__: List[str] = ['alpha', 'roman', 'item_label', 'ordinal', 'ordinal_number', 'comma_list', 'word', 'get_language', 'set_language', 'get_dialect', 'set_country', 'get_country', 'get_locale', 'set_locale', 'comma_and_list', 'need', 'nice_number', 'quantity_noun', 'currency_symbol', 'verb_past', 'verb_present', 'noun_plural', 'noun_singular', 'indefinite_article', 'capitalize', 'space_to_underscore', 'force_ask', 'period_list', 'name_suffix', 'currency', 'static_image', 'title_case', 'url_of', 'process_action', 'url_action', 'get_info', 'set_info', 'get_config', 'prevent_going_back', 'qr_code', 'action_menu_item', 'from_b64_json', 'defined', 'value', 'message', 'response', 'json_response', 'command', 'background_response', 'background_response_action', 'single_paragraph', 'quote_paragraphs', 'location_returned', 'location_known', 'user_lat_lon', 'interview_url', 'interview_url_action', 'interview_url_as_qr', 'interview_url_action_as_qr', 'interview_email', 'get_emails', 'action_arguments', 'action_argument', 'get_default_timezone', 'user_logged_in', 'user_privileges', 'user_has_privilege', 'user_info', 'background_action', 'background_response', 'background_response_action', 'us', 'set_live_help_status', 'chat_partners_available', 'phone_number_in_e164', 'phone_number_formatted', 'phone_number_is_valid', 'countries_list', 'country_name', 'write_record', 'read_records', 'delete_record', 'variables_as_json', 'all_variables', 'language_from_browser', 'device', 'plain', 'bold', 'italic', 'subdivision_type', 'indent', 'raw', 'fix_punctuation', 'set_progress', 'get_progress', 'referring_url', 'undefine', 'invalidate', 'dispatch', 'yesno', 'noyes', 'phone_number_part', 'log', 'encode_name', 'decode_name', 'interview_list', 'interview_menu', 'server_capabilities', 'session_tags', 'get_chat_log', 'get_user_list', 'get_user_info', 'set_user_info', 'get_user_secret', 'create_user', 'create_session', 'get_session_variables', 'set_session_variables', 'go_back_in_session', 'manage_privileges', 'redact', 'forget_result_of', 're_run_logic', 'reconsider', 'get_question_data', 'set_save_status', 'single_to_double_newlines', 'verbatim', 'add_separators', 'store_variables_snapshot', 'update_terms', 'set_variables', 'language_name', 'run_action_in_session']

class RawValue:
    value: Incomplete
    def __init__(self, the_value) -> None: ...

def raw(val): ...

class ReturnValue:
    extra: Incomplete
    value: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def __str__(self): ...

def get_chat_log(utc: bool = ..., timezone: Incomplete | None = ...): ...
def user_logged_in() -> bool: ...
def device(ip: bool = ...) -> Optional[UserAgent]: ...
def parse_accept_language(language_header, restrict: bool = ...) -> list: ...
def language_from_browser(*pargs) -> Optional[str]: ...
def country_name(country_code) -> str: ...
def state_name(state_code, country_code: Optional[Any] = ...): ...
def language_name(language_code) -> str: ...
def subdivision_type(country_code) -> Optional[str]: ...
def countries_list() -> list: ...
def states_list(country_code: Optional[str] = ...): ...
def interface() -> Optional[str]: ...
def user_privileges() -> list[str]: ...
def user_has_privilege(*pargs) -> bool: ...

class TheUser:
    def name(self) -> str: ...
    def __str__(self) -> str: ...

def user_info(): ...
def action_arguments() -> dict: ...
def action_argument(item: Incomplete | None = ...) -> Any: ...
def location_returned() -> bool: ...
def location_known() -> bool: ...
def user_lat_lon() -> Tuple[Optional[Any], Optional[Any]]: ...
def chat_partners_available(*pargs, **kwargs): ...
def interview_email(key: str | None = ..., index: int | None = ...) -> str: ...
def get_emails(key: str | None = ..., index: int | None = ...) -> List: ... # is actually AddressEmail, but that's only in server.py
def interview_url(**kwargs) -> str: ...
def set_parts(**kwargs): ...
def set_title(**kwargs): ...

class DATagsSet:
    def add(self, item) -> None: ...
    def copy(self): ...
    def clear(self) -> None: ...
    def remove(self, elem) -> None: ...
    def discard(self, elem) -> None: ...
    def pop(self, *pargs): ...
    def __contains__(self, item) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __reversed__(self): ...
    def __and__(self, operand): ...
    def __or__(self, operand): ...
    def __iand__(self, operand): ...
    def __ior__(self, operand): ...
    def __isub__(self, operand): ...
    def __ixor__(self, operand): ...
    def __rand__(self, operand): ...
    def __ror__(self, operand): ...
    def __hash__(self): ...
    def __str__(self): ...
    def union(self, other_set): ...
    def intersection(self, other_set): ...
    def difference(self, other_set): ...
    def isdisjoint(self, other_set): ...
    def issubset(self, other_set): ...
    def issuperset(self, other_set): ...

def session_tags() -> DATagsSet: ...
def interview_url_action(action: str, **kwargs) -> str: ...
def interview_url_as_qr(**kwargs) -> str: ...
def interview_url_action_as_qr(action: str, **kwargs) -> str: ...
def get_info(att): ...
def get_current_info(): ...
def set_info(**kwargs) -> None: ...
def set_progress(number: float) -> None: ...
def get_progress() -> float: ...
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
    def __str__(self): ...
    def set_section(self, section): ...
    def section_ids(self, language: Incomplete | None = ...): ...
    def get_section(self, display: bool = ..., language: Incomplete | None = ...): ...
    def hide(self) -> None: ...
    def unhide(self) -> None: ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...
    def visible(self, language: Incomplete | None = ...): ...
    def enabled(self): ...
    def set_sections(self, sections, language: Incomplete | None = ...) -> None: ...
    def get_sections(self, language: Incomplete | None = ...): ...
    def show_sections(self, style: str = ..., show_links: Incomplete | None = ...): ...

class WebFunc: ...

def write_record(key, data) -> int: ...
def read_records(key) -> dict[int, Any]: ...
def delete_record(key, the_id): ...
def url_of(file_reference: Union[Literal["temp_url", "login_url"], str], **kwargs): ...
def server_capabilities() -> dict[str, bool]: ...

class GenericObject:
    user: Incomplete
    role: str
    def __init__(self) -> None: ...

def background_response(*pargs, **kwargs) -> None: ...
def background_error_action(*pargs, **kwargs) -> None: ...
def background_response_action(*pargs, **kwargs) -> None: ...
def background_action(*pargs, **kwargs): ...

class BackgroundResult:
    def __init__(self, result) -> None: ...

class MyAsyncResult:
    _cached_result: Incomplete
    def wait(self): ...
    def failed(self): ...
    def ready(self): ...
    def result(self): ...
    def get(self): ...
    def revoke(self, terminate: bool = ...): ...

def fix_punctuation(text, mark: Incomplete | None = ..., other_marks: Incomplete | None = ...) -> str: ...
def item_label(num, level: Incomplete | None = ..., punctuation: bool = ...) -> str: ...
def alpha(num, case: Incomplete | None = ...) -> str: ...
def roman(num, case: Incomplete | None = ...) -> str: ...

class LazyWord:
    original: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __mod__(self, other): ...
    def __str__(self) -> str: ...

class LazyArray:
    original: Incomplete
    def __init__(self, array) -> None: ...
    def compute(self): ...
    def copy(self): ...
    def pop(self, *pargs): ...
    def __add__(self, other): ...
    def index(self, *pargs, **kwargs): ...
    def clear(self) -> None: ...
    def append(self, other) -> None: ...
    def remove(self, other) -> None: ...
    def extend(self, other) -> None: ...
    def __contains__(self, item) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __delitem__(self, index) -> None: ...
    def __reversed__(self): ...
    def __setitem__(self, index, the_value): ...
    def __getitem__(self, index): ...
    def __str__(self) -> str: ...
    def __repr__(self): ...
    def __eq__(self, other) -> bool: ...

def word(the_word, **kwargs) -> str: ...
def get_config(key, none_value: Incomplete | None = ...): ...
def get_default_timezone(): ...
def prevent_going_back() -> None: ...
def set_language(lang, dialect: Incomplete | None = ..., voice: Incomplete | None = ...) -> None: ...
def get_language(): ...
def set_country(country) -> None: ...
def get_country() -> str: ...
def get_dialect(): ...
def get_voice(): ...
def set_locale(*pargs, **kwargs) -> None: ...
def get_locale(*pargs): ...
def get_currency_symbol(): ...
def update_locale() -> None: ...
def need(*pargs): ...
def pickleable_objects(input_dict): ...

def language_function_constructor(term) -> Callable[..., str]: ...

verb_past: Callable[..., str]
verb_present: Callable[..., str]
noun_plural: Callable[..., str]
noun_singular: Callable[..., str]
indefinite_article: Callable[..., str]
period_list: Callable[..., list[str]]
name_suffix: Callable[..., list[str]]
currency: Callable[..., str]
currency_symbol: Callable[..., str]
comma_list: Callable[..., str]
comma_and_list: Callable[..., str]
add_separators: Callable[..., str]
nice_number: Callable[..., str]
quantity_noun: Callable[..., str]
capitalize: Callable[..., str]
capitalize_function: Callable[..., str]
title_case: Callable[..., str]
ordinal_number: Callable[..., str]
ordinal: Callable[..., str]

def space_to_underscore(a) -> str: ...
def message(*pargs, **kwargs) -> None: ...
def response(*pargs, **kwargs) -> None: ...
def json_response(data, response_code: Incomplete | None = ...) -> None: ...
def variables_as_json(include_internal: bool = ...) -> None: ...
def store_variables_snapshot(data: Incomplete | None = ..., include_internal: bool = ..., key: Incomplete | None = ..., persistent: bool = ...) -> None: ...
def all_variables(simplify: bool = ..., include_internal: bool = ..., special: str | bool = ..., make_copy: bool = ...): ...
def command(*pargs, **kwargs) -> None: ...
def force_ask(*pargs, **kwargs) -> None: ...
def force_gather(*pargs, forget_prior: bool = ..., evaluate: bool = ...): ...
def static_image(filereference: str, width: Incomplete | None = ...) -> str: ...
def qr_code(string, width: Incomplete | None = ..., alt_text: Incomplete | None = ...) -> str: ...
def package_template_filename(the_file: Incomplete, **kwargs) -> Optional[str]: ...
def process_action() -> None: ...
def url_action(action, **kwargs): ...
def debug_status(): ...
def action_menu_item(label, action, **kwargs): ...
def from_b64_json(string: str) -> Any: ...

class lister(ast.NodeVisitor):
    stack: Incomplete
    def __init__(self) -> None: ...
    def visit_Name(self, node) -> None: ...
    def visit_Attribute(self, node) -> None: ...
    def visit_Subscript(self, node) -> None: ...

def invalidate(*pargs) -> None: ...
def undefine(*pargs, invalidate: bool = ...) -> None: ...
def dispatch(var: str) -> bool: ...
def set_variables(variables, process_objects: bool = ...) -> None: ...
def define(var, val) -> None: ...

class DefCaller(Enum):
    DEFINED: int
    VALUE: int
    SHOWIFDEF: int
    def is_pure(self) -> bool: ...
    def is_predicate(self) -> bool: ...

def value(var: str, prior: bool = ...): ...
def defined(var: str, prior: bool = ...) -> bool: ...
def showifdef(var: str, alternative: str = ..., prior: bool = ...): ...
def single_paragraph(text) -> str: ...
def quote_paragraphs(text) -> str: ...
def set_live_help_status(availability: Incomplete | None = ..., mode: Incomplete | None = ..., partner_roles: Incomplete | None = ...) -> None: ...
def phone_number_in_e164(number, country: Incomplete | None = ...): ...
def phone_number_is_valid(number, country: Incomplete | None = ...) -> bool: ...
def phone_number_part(number, part, country: Incomplete | None = ...) -> str: ...
def phone_number_formatted(number, country: Incomplete | None = ...) -> str | None: ...
def serializable_dict(user_dict, include_internal: bool = ...) -> dict: ...
def safe_json(the_object, level: int = ..., is_key: bool = ...) -> Any: ...
def referring_url(default: Incomplete | None = ..., current: bool = ...): ...
def plain(text, default: Incomplete | None = ...) -> str: ...
def bold(text, default: Incomplete | None = ...) -> str: ...
def italic(text, default: Incomplete | None = ...) -> str: ...
def indent(text, by: Incomplete | None = ...) -> str: ...
def yesno(the_value, invert: bool = ...) -> str: ...
def noyes(the_value, invert: bool = ...) -> str: ...
def split(text, breaks, index): ...
def showif(var, condition, alternative: str = ...): ...
def log(the_message, priority: str = ...) -> None: ...
def encode_name(var: str) -> str: ...
def decode_name(var: str) -> str: ...
def interview_list(exclude_invalid: bool = ..., action: Incomplete | None = ..., filename: Incomplete | None = ..., session: Incomplete | None = ..., user_id: Incomplete | None = ..., query: Incomplete | None = ..., include_dict: bool = ..., delete_shared: bool = ..., next_id: Incomplete | None = ...): ...
def interview_menu(*pargs, **kwargs): ...
def get_user_list(include_inactive: bool = ..., next_id: Incomplete | None = ...) -> Optional[Any]: ...
def manage_privileges(*pargs) -> Optional[Any]: ...
def get_user_info(user_id: Incomplete | None = ..., email: Incomplete | None = ...) -> Optional[Any]: ...
def set_user_info(**kwargs) -> None: ...
def create_user(email, password, privileges: Incomplete | None = ..., info: Incomplete | None = ...): ...
def get_user_secret(username, password): ...
def create_session(yaml_filename, secret: Incomplete | None = ..., url_args: Incomplete | None = ...): ...
def get_session_variables(yaml_filename, session_id, secret: Incomplete | None = ..., simplify: bool = ...): ...
def set_session_variables(yaml_filename, session_id, variables, secret: Incomplete | None = ..., question_name: Incomplete | None = ..., overwrite: bool = ..., process_objects: bool = ..., delete: Incomplete | None = ...) -> None: ...
def run_action_in_session(yaml_filename, session_id, action, arguments: Incomplete | None = ..., secret: Incomplete | None = ..., persistent: bool = ..., overwrite: bool = ...): ...
def get_question_data(yaml_filename, session_id, secret: Incomplete | None = ...): ...
def go_back_in_session(yaml_filename, session_id, secret: Incomplete | None = ...) -> None: ...
def redact(text) -> str: ...
def verbatim(text): ...

class DALocalFile:
    local_path: Incomplete
    def __init__(self, local_path) -> None: ...
    def path(self): ...
    def get_alt_text(self): ...
    alt_text: Incomplete
    def set_alt_text(self, alt_text) -> None: ...

def forget_result_of(*pargs) -> None: ...
def re_run_logic() -> None: ...
def reconsider(*pargs, evaluate: bool = ...) -> None: ...
def single_to_double_newlines(text) -> str: ...

custom_types: dict

class CustomDataTypeRegister(type):
    def __init__(cls, name, bases, orig_clsdict) -> None: ...

class CustomDataType(metaclass=CustomDataTypeRegister):
    @classmethod
    def validate(cls, item): ...
    @classmethod
    def transform(cls, item): ...
    @classmethod
    def default_for(cls, item): ...
    @classmethod
    def empty(cls) -> None: ...

class ServerContext: ...
