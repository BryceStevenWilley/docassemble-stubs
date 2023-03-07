from _typeshed import Incomplete as Incomplete
from html.parser import HTMLParser

equals_byte: Incomplete
NoneType: Incomplete
STRICT_MODE: Incomplete
DECORATION_SIZE: Incomplete
DECORATION_UNITS: Incomplete
BUTTON_ICON_SIZE: Incomplete
BUTTON_ICON_UNITS: Incomplete
BUTTON_CLASS: str
BUTTON_STYLE: str
BUTTON_COLOR: Incomplete
BUTTON_COLOR_YES: Incomplete
BUTTON_COLOR_NO: Incomplete
BUTTON_COLOR_MAYBE: Incomplete
BUTTON_COLOR_CLEAR: Incomplete
BUTTON_COLOR_BACK: Incomplete
BUTTON_COLOR_REGISTER: Incomplete
BUTTON_COLOR_NEW_SESSION: Incomplete
BUTTON_COLOR_LEAVE: Incomplete
BUTTON_COLOR_URL: Incomplete
BUTTON_COLOR_RESTART: Incomplete
BUTTON_COLOR_REFRESH: Incomplete
BUTTON_COLOR_SIGNIN: Incomplete
BUTTON_COLOR_EXIT: Incomplete
BUTTON_COLOR_LOGOUT: Incomplete
BUTTON_COLOR_SEND: Incomplete
BUTTON_COLOR_DOWNLOAD: Incomplete
BUTTON_COLOR_REVIEW: Incomplete
BUTTON_COLOR_ADD: Incomplete
BUTTON_COLOR_DELETE: Incomplete
BUTTON_COLOR_UNDELETE: Incomplete
BUTTON_COLOR_HELP: Incomplete
BUTTON_COLOR_QUESTION_HELP: Incomplete
BUTTON_COLOR_BACK_TO_QUESTION: Incomplete

def process_help(help_section, status, full_page: bool = ...): ...
def tracker_tag(status) -> None: ...
def datatype_tag(datatypes) -> None: ...
def varname_tag(varnames) -> None: ...
def icon_html(status, name, width_value: float = ..., width_units: str = ...): ...
def get_choices_with_abb(status, field, the_user_dict, terms: Union[Incomplete, None] = ..., links: Union[Incomplete, None] = ...): ...

sms_bad_words: Incomplete

def try_to_abbreviate(label, flabel, data, length) -> None: ...
def as_sms(status, the_user_dict, links: Union[Incomplete, None] = ..., menu_items: Union[Incomplete, None] = ...): ...
def embed_input(status, variable) -> None: ...
def help_wrap(content, helptext, status) -> None: ...
def as_html(status, debug, root, validation_rules, field_error, the_progress_bar, steps) -> None: ...
def add_validation(extra_scripts, validation_rules, field_error) -> None: ...
def locale_format_string(the_value) -> None: ...
def double_to_single_newline(text) -> None: ...
def input_for(status, field, wide: bool = ..., embedded: bool = ..., floating_label: Union[Incomplete, None] = ...): ...
def myb64doublequote(text) -> None: ...
def myb64quote(text) -> None: ...
def repad(text) -> None: ...
def indent_by(text, num) -> None: ...
def safeid(text) -> None: ...
def from_safeid(text) -> None: ...
def escape_id(text) -> None: ...
def do_escape_id(text) -> None: ...
def escape_for_jquery(text) -> None: ...
def myb64unquote(the_string) -> None: ...
def strip_quote(the_string) -> None: ...
def safe_html(the_string) -> None: ...
def the_currency_symbol(status, field) -> None: ...
def fix_double_quote(the_string) -> None: ...
def option_escape(the_string) -> None: ...

class MLStripper(HTMLParser):
    strict: bool
    convert_charrefs: bool
    text: Incomplete
    def __init__(self) -> None: ...
    def handle_data(self, data) -> None: ...
    def get_data(self) -> None: ...
    def error(self, message) -> None: ...

def strip_tags(html) -> None: ...
def clean_whitespace(text) -> None: ...
