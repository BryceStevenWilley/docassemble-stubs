from _typeshed import Incomplete
from flask_wtf.csrf import generate_csrf as generate_csrf # type: ignore
from docassemble.base.config import daconfig as daconfig, hostname as hostname
from docassemble.base.error import DAException as DAException
from docassemble.base.functions import pickleable_objects as pickleable_objects
from docassemble.base.generate_key import random_alphanumeric as random_alphanumeric, random_bytes as random_bytes
from docassemble.base.logger import logmessage as logmessage
from docassemble.webapp.app_object import app as app
from docassemble.webapp.core.models import Email as Email, EmailAttachment as EmailAttachment, GlobalObjectStorage as GlobalObjectStorage, MachineLearning as MachineLearning, ObjectStorage as ObjectStorage, Shortener as Shortener, SpeakList as SpeakList, Uploads as Uploads, UploadsRoleAuth as UploadsRoleAuth, UploadsUserAuth as UploadsUserAuth
from docassemble.webapp.da_flask_mail import FlaskMail as FlaskMail, Message as Message
from docassemble.webapp.db_object import db as db
from docassemble.webapp.file_access import get_info_from_file_number as get_info_from_file_number, get_info_from_file_reference as get_info_from_file_reference, url_if_exists as url_if_exists
from docassemble.webapp.file_number import get_new_file_number as get_new_file_number
from docassemble.webapp.files import SavedFile as SavedFile, get_ext_and_mimetype as get_ext_and_mimetype
from docassemble.webapp.fixpickle import fix_pickle_dict as fix_pickle_dict, fix_pickle_obj as fix_pickle_obj
from docassemble.webapp.packages.models import PackageAuth as PackageAuth
from docassemble.webapp.screenreader import to_text as to_text
from docassemble.webapp.users.models import ChatLog as ChatLog, Role as Role, UserAuthModel as UserAuthModel, UserDict as UserDict, UserDictKeys as UserDictKeys, UserModel as UserModel, UserRoles as UserRoles

TypeType: Incomplete
NoneType: Incomplete
DEBUG: Incomplete

def write_record(key, data): ...
def read_records(key) -> dict: ...
def delete_record(key, the_id) -> None: ...
def save_numbered_file(filename, orig_path, yaml_file_name: Incomplete | None = ..., uid: Incomplete | None = ...): ...
def fix_ml_files(playground_number, current_project) -> None: ...
def is_package_ml(parts) -> bool: ...
def project_name(name) -> str: ...
def add_project(filename, current_project): ...
def directory_for(area, current_project): ...
def write_ml_source(playground, playground_number, current_project, filename, finalize: bool = ...): ...
def user_is_developer(user_id) -> bool: ...
def absolute_filename(the_file) -> SavedFile | None: ...
def get_mail_config() -> dict: ...

mail_configs: Incomplete

def da_send_mail(the_message, config: str = ...) -> None: ...

DEFAULT_LANGUAGE: str
DEFAULT_LOCALE: str
DEFAULT_DIALECT: str
DEFAULT_VOICE: Incomplete
DEFAULT_TIMEZONE: str
COOKIELESS_SESSIONS: bool

def url_for(*pargs, **kwargs): ...
def sql_get(key, secret: Incomplete | None = ...) -> Incomplete | None: ...
def sql_defined(key) -> bool: ...
def sql_set(key, val, encrypted: bool = ..., secret: Incomplete | None = ..., the_user_id: Incomplete | None = ...) -> None: ...
def sql_delete(key) -> None: ...
def sql_keys(prefix) -> list: ...
def get_info_from_file_reference_with_uids(*pargs, **kwargs): ...
def get_info_from_file_number_with_uids(*pargs, **kwargs): ...

classes: Incomplete
DEFAULT_TABLE_CLASS: str
DEFAULT_THEAD_CLASS: str | None
DEFAULT_COUNTRY: Incomplete

def fix_words() -> None: ...

cloud: Incomplete
cloud_cache: dict

def cloud_custom(provider, config): ...

initial_dict: dict

def can_access_file_number(file_number, uids: Incomplete | None = ...) -> bool: ...
def pad(the_string: str) -> str: ...
def unpad(the_string: str) -> str: ...
def encrypt_phrase(phrase, secret): ...
def pack_phrase(phrase): ...
def decrypt_phrase(phrase_string, secret): ...
def unpack_phrase(phrase_string): ...
def encrypt_dictionary(the_dict, secret): ...
def pack_object(the_object): ...
def unpack_object(the_string): ...
def encrypt_object(obj, secret): ...
def decrypt_object(obj_string, secret): ...
def parse_the_user_id(the_user_id) -> tuple[int | None, int | None]: ...
def safe_pickle(the_object): ...
def pack_dictionary(the_dict): ...
def decrypt_dictionary(dict_string, secret): ...
def unpack_dictionary(dict_string): ...
def nice_date_from_utc(timestamp, timezone=...): ...
def nice_utc_date(timestamp): ...
def fetch_user_dict(user_code, filename, secret: Incomplete | None = ...): ...
def user_dict_exists(user_code, filename): ...
def fetch_previous_user_dict(user_code, filename, secret): ...
def advance_progress(user_dict, interview) -> None: ...
def delete_temp_user_data(temp_user_id, r) -> None: ...
def delete_user_data(user_id, r, r_user) -> None: ...
def reset_user_dict(user_code, filename, user_id: Incomplete | None = ..., temp_user_id: Incomplete | None = ..., force: bool = ...) -> None: ...
def get_person(user_id, cache): ...
def get_chat_log(chat_mode, yaml_filename, session_id, user_id, temp_user_id, secret, self_user_id, self_temp_id): ...
def file_set_attributes(file_number, **kwargs) -> None: ...
def file_user_access(file_number, allow_user_id: Incomplete | None = ..., allow_email: Incomplete | None = ..., disallow_user_id: Incomplete | None = ..., disallow_email: Incomplete | None = ..., disallow_all: bool = ...): ...
def file_privilege_access(file_number, allow: Incomplete | None = ..., disallow: Incomplete | None = ..., disallow_all: bool = ...): ...
def clear_session(i) -> None: ...
def clear_specific_session(i, uid) -> None: ...
def guess_yaml_filename() -> Incomplete | None: ...
def delete_obsolete() -> None: ...
def get_session(i) -> Incomplete | None: ...
def unattached_uid() -> str: ...
def get_uid_for_filename(i): ...
def update_session(i, uid: Incomplete | None = ..., encrypted: Incomplete | None = ..., key_logged: Incomplete | None = ..., chatstatus: Incomplete | None = ...): ...
def get_session_uids() -> list: ...
