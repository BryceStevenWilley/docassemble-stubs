import oauth2client.client # type: ignore
import types
from _typeshed import Incomplete
from flask_login import login_user as login_user # type: ignore
from docassemble.base.config import daconfig as daconfig, hostname as hostname, in_celery as in_celery, in_cron as in_cron
from docassemble.base.error import DAError as DAError, DAErrorCompileError as DAErrorCompileError, DAErrorMissingVariable as DAErrorMissingVariable, DAErrorNoEndpoint as DAErrorNoEndpoint, DAException as DAException, DAValidationError as DAValidationError
from docassemble.base.functions import ReturnValue as ReturnValue, get_default_timezone as get_default_timezone, word as word
from docassemble.base.generate_key import random_alphanumeric as random_alphanumeric, random_digits as random_digits, random_lower_string as random_lower_string, random_string as random_string
from docassemble.base.logger import logmessage as logmessage
from docassemble.base.pandoc import convertible_extensions as convertible_extensions, convertible_mimetypes as convertible_mimetypes, word_to_markdown as word_to_markdown
from docassemble.base.standardformatter import as_html as as_html, as_sms as as_sms, get_choices_with_abb as get_choices_with_abb
from docassemble.base.util import DADict as DADict, DAEmail as DAEmail, DAEmailRecipient as DAEmailRecipient, DAEmailRecipientList as DAEmailRecipientList, DAFile as DAFile, DAFileCollection as DAFileCollection, DAFileList as DAFileList, DAList as DAList, DAObject as DAObject, DAStaticFile as DAStaticFile
from docassemble.webapp.api_key import encrypt_api_key as encrypt_api_key
from docassemble.webapp.app_object import app as app, csrf as csrf
from docassemble.webapp.backend import Message as Message, add_project as add_project, advance_progress as advance_progress, can_access_file_number as can_access_file_number, clear_session as clear_session, clear_specific_session as clear_specific_session, cloud as cloud, da_send_mail as da_send_mail, decrypt_dictionary as decrypt_dictionary, decrypt_object as decrypt_object, decrypt_phrase as decrypt_phrase, delete_temp_user_data as delete_temp_user_data, delete_user_data as delete_user_data, directory_for as directory_for, encrypt_dictionary as encrypt_dictionary, encrypt_object as encrypt_object, encrypt_phrase as encrypt_phrase, fetch_previous_user_dict as fetch_previous_user_dict, fetch_user_dict as fetch_user_dict, file_privilege_access as file_privilege_access, file_set_attributes as file_set_attributes, file_user_access as file_user_access, fix_ml_files as fix_ml_files, generate_csrf as generate_csrf, get_chat_log as get_chat_log, get_info_from_file_number as get_info_from_file_number, get_info_from_file_number_with_uids as get_info_from_file_number_with_uids, get_info_from_file_reference as get_info_from_file_reference, get_new_file_number as get_new_file_number, get_person as get_person, get_session as get_session, get_session_uids as get_session_uids, guess_yaml_filename as guess_yaml_filename, initial_dict as initial_dict, is_package_ml as is_package_ml, nice_date_from_utc as nice_date_from_utc, pack_dictionary as pack_dictionary, pack_phrase as pack_phrase, project_name as project_name, reset_user_dict as reset_user_dict, save_numbered_file as save_numbered_file, unpack_dictionary as unpack_dictionary, unpack_phrase as unpack_phrase, update_session as update_session, url_for as url_for, url_if_exists as url_if_exists, write_ml_source as write_ml_source
from docassemble.webapp.core.models import Email as Email, EmailAttachment as EmailAttachment, GlobalObjectStorage as GlobalObjectStorage, MachineLearning as MachineLearning, Shortener as Shortener, SpeakList as SpeakList, Supervisors as Supervisors, Uploads as Uploads, UploadsUserAuth as UploadsUserAuth
from docassemble.webapp.daredis import r as r, r_store as r_store, r_user as r_user
from docassemble.webapp.db_object import db as db
from docassemble.webapp.develop import APIKey as APIKey, AddinUploadForm as AddinUploadForm, ConfigForm as ConfigForm, CreatePackageForm as CreatePackageForm, CreatePlaygroundPackageForm as CreatePlaygroundPackageForm, DeleteProject as DeleteProject, FunctionFileForm as FunctionFileForm, GitHubForm as GitHubForm, GoogleDriveForm as GoogleDriveForm, LogForm as LogForm, NewProject as NewProject, OneDriveForm as OneDriveForm, PlaygroundFilesEditForm as PlaygroundFilesEditForm, PlaygroundFilesForm as PlaygroundFilesForm, PlaygroundForm as PlaygroundForm, PlaygroundPackagesForm as PlaygroundPackagesForm, PlaygroundUploadForm as PlaygroundUploadForm, PullPlaygroundPackage as PullPlaygroundPackage, RenameProject as RenameProject, TrainingForm as TrainingForm, TrainingUploadForm as TrainingUploadForm, UpdatePackageForm as UpdatePackageForm, Utilities as Utilities
from docassemble.webapp.files import SavedFile as SavedFile, get_ext_and_mimetype as get_ext_and_mimetype
from docassemble.webapp.fixpickle import fix_pickle_obj as fix_pickle_obj
from docassemble.webapp.info import system_packages as system_packages
from docassemble.webapp.jsonstore import delete_answer_json as delete_answer_json, read_answer_json as read_answer_json, variables_snapshot_connection as variables_snapshot_connection, write_answer_json as write_answer_json
from docassemble.webapp.packages.models import Package as Package, PackageAuth as PackageAuth
from docassemble.webapp.playground import PlaygroundSection as PlaygroundSection
from docassemble.webapp.screenreader import to_text as to_text
from docassemble.webapp.setup import da_version as da_version
from docassemble.webapp.translations import setup_translation as setup_translation
from docassemble.webapp.users.forms import InterviewsListForm as InterviewsListForm, MFAChooseForm as MFAChooseForm, MFALoginForm as MFALoginForm, MFAReconfigureForm as MFAReconfigureForm, MFASMSSetupForm as MFASMSSetupForm, MFASetupForm as MFASetupForm, MFAVerifySMSSetupForm as MFAVerifySMSSetupForm, ManageAccountForm as ManageAccountForm, MyRegisterForm as MyRegisterForm, MyResendConfirmEmailForm as MyResendConfirmEmailForm, MySignInForm as MySignInForm, PhoneLoginForm as PhoneLoginForm, PhoneLoginVerifyForm as PhoneLoginVerifyForm, RequestDeveloperForm as RequestDeveloperForm
from docassemble.webapp.users.models import AnonymousUserModel as AnonymousUserModel, ChatLog as ChatLog, MyUserInvitation as MyUserInvitation, Role as Role, TempUser as TempUser, UserAuthModel as UserAuthModel, UserDict as UserDict, UserDictKeys as UserDictKeys, UserModel as UserModel, UserRoles as UserRoles
from docassemble.webapp.users.views import user_profile_page as user_profile_page

START_TIME: Incomplete
min_system_version: str
the_method_type = types.FunctionType
equals_byte: Incomplete
TypeType: Incomplete
NoneType: Incomplete
STATS: Incomplete
DEBUG: Incomplete
ERROR_TYPES_NO_EMAIL: Incomplete
COOKIELESS_SESSIONS: Incomplete
BAN_IP_ADDRESSES: Incomplete
CONCURRENCY_LOCK_TIMEOUT: Incomplete
PREVENT_DEMO: bool
REQUIRE_IDEMPOTENT: Incomplete
STRICT_MODE: Incomplete
PACKAGE_PROTECTION: Incomplete
PERMISSIONS_LIST: Incomplete
HTTP_TO_HTTPS: Incomplete
GITHUB_BRANCH: Incomplete
request_active: bool
global_css: str
global_js: str
default_playground_yaml: str
ok_mimetypes: Incomplete
ok_extensions: Incomplete

def update_editable() -> None: ...

default_yaml_filename: Incomplete
final_default_yaml_filename: Incomplete
keymap: Incomplete
google_config: Incomplete
contains_volatile: Incomplete
is_integer: Incomplete
detect_mobile: Incomplete
alphanumeric_only: Incomplete
phone_pattern: Incomplete
document_match: Incomplete
fix_tabs: Incomplete
fix_initial: Incomplete
noquote_match: Incomplete
lt_match: Incomplete
gt_match: Incomplete
amp_match: Incomplete
extraneous_var: Incomplete
key_requires_preassembly: Incomplete
match_brackets: Incomplete
match_inside_and_outside_brackets: Incomplete
match_inside_brackets: Incomplete
valid_python_var: Incomplete
valid_python_exp: Incomplete
default_title: Incomplete
default_short_title: Incomplete
PNG_RESOLUTION: Incomplete
PNG_SCREEN_RESOLUTION: Incomplete
PDFTOPPM_COMMAND: Incomplete
DEFAULT_LANGUAGE: Incomplete
DEFAULT_LOCALE: Incomplete
DEFAULT_DIALECT: Incomplete
DEFAULT_VOICE: Incomplete
LOGSERVER: Incomplete
CHECKIN_INTERVAL: Incomplete
NOTIFICATION_CONTAINER: Incomplete
NOTIFICATION_MESSAGE: Incomplete
USING_SUPERVISOR: Incomplete
SINGLE_SERVER: Incomplete
audio_mimetype_table: Incomplete
valid_voicerss_dialects: Incomplete
voicerss_config: Incomplete
VOICERSS_ENABLED: Incomplete
ROOT: Incomplete
exit_page: Incomplete
SUPERVISORCTL: Incomplete
WEBAPP_PATH: Incomplete
READY_FILE: Incomplete
UPLOAD_DIRECTORY: Incomplete
PACKAGE_DIRECTORY: Incomplete
FULL_PACKAGE_DIRECTORY: Incomplete
LOG_DIRECTORY: Incomplete
PAGINATION_LIMIT: Incomplete
PAGINATION_LIMIT_PLUS_ONE: Incomplete
init_py_file: str
SHOW_LOGIN: Incomplete
ALLOW_REGISTRATION: Incomplete
LOGFILE: Incomplete
store: Incomplete
kv_session: Incomplete

def _call_or_get(function_or_property): ...
def _get_safe_next_param(param_name, default_endpoint): ...
def custom_resend_confirm_email(): ...
def as_int(val): ...
def custom_register(): ...
def custom_login(): ...
def add_secret_to(response): ...
def logout(): ...
def unauthenticated(): ...
def unauthorized(): ...
def my_default_url(error, endpoint, values): ...
def make_safe_url(url): ...
def password_validator(form, field) -> None: ...

the_db_adapter: Incomplete
the_user_manager: Incomplete
lm: Incomplete

def url_for_interview(**args): ...
def syslog_message(message) -> None: ...
def syslog_message_with_timestamp(message) -> None: ...

sys_logger: Incomplete
LOGFORMAT: Incomplete

def add_log_handler() -> None: ...
def login_as_admin(url, url_root) -> None: ...
def import_necessary(url, url_root) -> None: ...

fax_provider: Incomplete

def get_clicksend_config(): ...

clicksend_config: Incomplete

def get_telnyx_config(): ...

telnyx_config: Incomplete

def get_twilio_config(): ...

twilio_config: Incomplete
BUTTON_COLOR_NAV_LOGIN: Incomplete

def get_page_parts(): ...

page_parts: Incomplete
main_page_parts: Incomplete
ga_configured: Incomplete
analytics_configured: bool
reserved_argnames: Incomplete

def get_sms_session(phone_number, config: str = ...): ...
def initiate_sms_session(phone_number, yaml_filename: Incomplete | None = ..., uid: Incomplete | None = ..., secret: Incomplete | None = ..., encrypted: Incomplete | None = ..., user_id: Incomplete | None = ..., email: Incomplete | None = ..., new: bool = ..., config: str = ...): ...
def terminate_sms_session(phone_number, config: str = ...) -> None: ...
def fix_http(url): ...
def safe_quote_func(string, safe: str = ..., encoding: Incomplete | None = ..., errors: Incomplete | None = ...): ...
def remove_question_package(args) -> None: ...
def encrypt_next(args) -> None: ...
def get_url_from_file_reference(file_reference, **kwargs): ...
def user_id_dict(): ...
def get_base_words(): ...
def get_pg_code_cache(): ...
def get_documentation_dict(): ...
def get_name_info(): ...
def get_title_documentation(): ...
def pad_to_16(the_string): ...
def decrypt_session(secret, user_code: Incomplete | None = ..., filename: Incomplete | None = ...) -> None: ...
def encrypt_session(secret, user_code: Incomplete | None = ..., filename: Incomplete | None = ...) -> None: ...
def substitute_secret(oldsecret, newsecret, user: Incomplete | None = ..., to_convert: Incomplete | None = ...): ...
def MD5Hash(data: Incomplete | None = ...): ...
def set_request_active(value) -> None: ...
def copy_playground_modules() -> None: ...
def proc_example_list(example_list, package, directory, examples): ...
def get_examples(): ...
def add_timestamps(the_dict, manual_user_id: Incomplete | None = ...) -> None: ...
def fresh_dictionary(): ...
def manual_checkout(manual_session_id: Incomplete | None = ..., manual_filename: Incomplete | None = ..., user_id: Incomplete | None = ..., delete_session: bool = ..., temp_user_id: Incomplete | None = ...) -> None: ...
def chat_partners_available(session_id, yaml_filename, the_user_id, mode, partner_roles): ...
def do_redirect(url, is_ajax, is_json, js_target): ...
def do_refresh(is_ajax, yaml_filename): ...
def standard_scripts(interview_language=..., external: bool = ...): ...
def additional_scripts(interview_status, yaml_filename, as_javascript: bool = ...): ...
def additional_css(interview_status, js_only: bool = ...): ...
def standard_html_start(interview_language=..., debug: bool = ..., bootstrap_theme: Incomplete | None = ..., external: bool = ..., page_title: Incomplete | None = ..., social: Incomplete | None = ..., yaml_filename: Incomplete | None = ...): ...
def process_file(saved_file, orig_file, mimetype, extension, initial: bool = ...) -> None: ...
def sub_temp_user_dict_key(temp_user_id, user_id): ...
def sub_temp_other(user) -> None: ...
def save_user_dict_key(session_id, filename, priors: bool = ..., user: Incomplete | None = ...) -> None: ...
def save_user_dict(user_code, user_dict, filename, secret: Incomplete | None = ..., changed: bool = ..., encrypt: bool = ..., manual_user_id: Incomplete | None = ..., steps: Incomplete | None = ..., max_indexno: Incomplete | None = ...) -> None: ...
def process_bracket_expression(match): ...
def myb64unquote(the_string): ...
def safeid(text): ...
def from_safeid(text): ...
def repad(text): ...
def test_for_valid_var(varname) -> None: ...
def navigation_bar(nav, interview, wrapper: bool = ..., inner_div_class: Incomplete | None = ..., inner_div_extra: Incomplete | None = ..., show_links: Incomplete | None = ..., hide_inactive_subs: bool = ..., a_class: Incomplete | None = ..., show_nesting: bool = ..., include_arrows: bool = ..., always_open: bool = ..., return_dict: Incomplete | None = ...): ...
def progress_bar(progress, interview): ...
def get_unique_name(filename, secret): ...
def obtain_lock(user_code, filename) -> None: ...
def obtain_lock_patiently(user_code, filename) -> None: ...
def release_lock(user_code, filename) -> None: ...
def make_navbar(status, steps, show_login, chat_info, debug_mode, index_params, extra_class: Incomplete | None = ...): ...
def exit_href(data: bool = ...): ...
def delete_session_for_interview(i: Incomplete | None = ...) -> None: ...
def delete_session_sessions() -> None: ...
def delete_session_info() -> None: ...
def backup_session(): ...
def restore_session(backup) -> None: ...
def get_existing_session(yaml_filename, secret): ...
def reset_session(yaml_filename, secret): ...
def _endpoint_url(endpoint, **kwargs): ...
def user_can_edit_package(pkgname: Incomplete | None = ..., giturl: Incomplete | None = ...): ...
def uninstall_package(packagename) -> None: ...
def summarize_results(results, logmessages, html: bool = ...): ...
def install_zip_package(packagename, file_number) -> None: ...
def install_git_package(packagename, giturl, branch) -> None: ...
def install_pip_package(packagename, limitation) -> None: ...
def get_package_info(): ...
def name_of_user(user, include_email: bool = ...): ...
def flash_as_html(message, message_type: str = ..., is_ajax: bool = ...): ...
def make_example_html(examples, first_id, example_html, data_dict) -> None: ...
def public_method(method, the_class): ...
def noquotetrunc(string): ...
def noquote(string): ...
def infobutton(title): ...
def search_button(var, field_origins, name_origins, interview_source, all_sources): ...

search_key: Incomplete

def find_needed_names(interview, needed_names, the_name: Incomplete | None = ..., the_question: Incomplete | None = ...) -> None: ...
def get_ml_info(varname, default_package, default_file): ...

pg_code_cache: Incomplete

def source_code_url(the_name, datatype: Incomplete | None = ...): ...
def get_vars_in_use(interview, interview_status, debug_mode: bool = ..., return_json: bool = ..., show_messages: bool = ..., show_jinja_help: bool = ..., current_project: str = ..., use_playground: bool = ...): ...
def ocr_google_in_background(image_file, raw_result, user_code): ...
def make_png_for_pdf(doc, prefix, page: Incomplete | None = ...): ...
def fg_make_png_for_pdf(doc, prefix, page: Incomplete | None = ...) -> None: ...
def fg_make_png_for_pdf_path(path, prefix, page: Incomplete | None = ...) -> None: ...
def fg_make_pdf_for_word_path(path, extension) -> None: ...
def task_ready(task_id): ...
def wait_for_task(task_id, timeout: Incomplete | None = ...): ...
def trigger_update(except_for: Incomplete | None = ...) -> None: ...
def restart_on(host): ...
def restart_all() -> None: ...
def restart_this() -> None: ...
def restart_others() -> None: ...
def get_requester_ip(req): ...
def current_info(yaml: Incomplete | None = ..., req: Incomplete | None = ..., action: Incomplete | None = ..., location: Incomplete | None = ..., interface: str = ..., session_info: Incomplete | None = ..., secret: Incomplete | None = ..., device_id: Incomplete | None = ..., session_uid: Incomplete | None = ...): ...
def html_escape(text): ...
def indent_by(text, num): ...
def call_sync() -> None: ...
def formatted_current_time(): ...
def formatted_current_date(): ...

class Object:
    def __init__(self, **kwargs) -> None: ...

class FakeUser: ...
class FakeRole: ...

def verify_email(email): ...

class OAuthSignIn:
    providers: Incomplete
    providers_obtained: bool
    provider_name: Incomplete
    consumer_id: Incomplete
    consumer_secret: Incomplete
    consumer_domain: Incomplete
    def __init__(self, provider_name) -> None: ...
    def authorize(self) -> None: ...
    def callback(self) -> None: ...
    def get_callback_url(self): ...
    @classmethod
    def get_provider(cls, provider_name): ...

class GoogleSignIn(OAuthSignIn):
    service: Incomplete
    def __init__(self) -> None: ...
    def authorize(self) -> None: ...
    def callback(self): ...

class FacebookSignIn(OAuthSignIn):
    service: Incomplete
    def __init__(self) -> None: ...
    def authorize(self): ...
    def callback(self): ...

class AzureSignIn(OAuthSignIn):
    service: Incomplete
    def __init__(self) -> None: ...
    def authorize(self): ...
    def callback(self): ...

def safe_json_loads(data): ...

class Auth0SignIn(OAuthSignIn):
    service: Incomplete
    def __init__(self) -> None: ...
    def authorize(self): ...
    def callback(self): ...

class KeycloakSignIn(OAuthSignIn):
    service: Incomplete
    def __init__(self) -> None: ...
    def authorize(self): ...
    def callback(self): ...

class TwitterSignIn(OAuthSignIn):
    service: Incomplete
    def __init__(self) -> None: ...
    def authorize(self): ...
    def callback(self): ...

def get_user_object(user_id): ...
def load_user(the_id): ...
def run_temp(): ...
def auto_login(): ...
def show_headers(): ...
def oauth_authorize(provider): ...
def oauth_callback(provider): ...
def phone_login(): ...
def phone_login_verify(): ...
def mfa_setup(): ...
def mfa_reconfigure(): ...
def mfa_choose(): ...
def mfa_sms_setup(): ...
def mfa_verify_sms_setup(): ...
def mfa_login(): ...
def manage_account(): ...
def get_github_flow(): ...
def delete_ssh_keys() -> None: ...
def get_ssh_keys(email): ...
def get_next_link(resp): ...
def github_menu(): ...
def github_configure(): ...
def github_unconfigure(): ...
def github_oauth_callback(): ...
def google_page(): ...
def post_sign_in(): ...
def leave(): ...
def restart_session(): ...
def new_session_endpoint(): ...
def exit_endpoint(): ...
def exit_logout(): ...
def cleanup_sessions(): ...
def health_status(): ...
def health_check(): ...
def checkout(): ...
def restart_ajax(): ...

class ChatPartners: ...

def get_current_chat_log(yaml_filename, session_id, secret, utc: bool = ..., timezone: Incomplete | None = ...): ...
def jsonify_with_cache(*pargs, **kwargs): ...
def checkin(): ...
def setup_variables() -> None: ...
def apply_security_headers(response): ...
def get_variables(): ...
def rootindex(): ...
def title_converter(content, part, status): ...
def test_embed(): ...
def launch(): ...
def resume(): ...
def json64unquote(text): ...
def tidy_action(action): ...
def make_response_wrapper(set_cookie, secret, set_device_id, device_id, expire_visitor_secret): ...
def populate_social(social, metadata) -> None: ...

index_path: str
html_index_path: str

def refresh_or_continue(interview, post_data): ...
def update_current_info_with_session_info(the_current_info, session_info) -> None: ...
def index(action_argument: Incomplete | None = ..., refer: Incomplete | None = ...): ...
def process_set_variable(field_name, user_dict, vars_set, old_values) -> None: ...
def add_permissions_for_field(the_field, interview_status, files_to_process) -> None: ...
def fake_up(response, interview_language) -> None: ...
def add_action_to_stack(interview_status, user_dict, action, arguments) -> None: ...
def sub_indices(the_var, the_user_dict): ...
def fixstr(data): ...
def get_history(interview, interview_status): ...
def is_mobile_or_tablet(): ...
def get_referer(): ...
def add_referer(user_dict, referer: Incomplete | None = ...) -> None: ...
def word_filter(text): ...
def get_part(part, default: Incomplete | None = ...): ...
def utility_processor(): ...
def speak_file(): ...
def interview_menu(absolute_urls: bool = ..., start_new: bool = ..., tag: Incomplete | None = ...): ...
def interview_start(): ...
def redirect_to_interview_in_package_directory(package, directory, filename): ...
def redirect_to_interview_in_package(package, filename): ...
def redirect_to_interview(dispatch): ...
def run_interview_in_package_directory(package, directory, filename): ...
def run_interview_in_package(package, filename): ...
def run_interview(dispatch): ...
def serve_stored_file(uid, number, filename, extension): ...
def serve_stored_file_download(uid, number, filename, extension): ...
def do_serve_stored_file(uid, number, filename, extension, download: bool = ...): ...
def serve_temporary_file(code, filename, extension): ...
def serve_temporary_file_download(code, filename, extension): ...
def do_serve_temporary_file(code, filename, extension, download: bool = ...): ...
def download_zip_package(): ...
def serve_uploaded_file_with_filename_and_extension(number, filename, extension): ...
def serve_uploaded_file_with_filename_and_extension_download(number, filename, extension): ...
def do_serve_uploaded_file_with_filename_and_extension(number, filename, extension, download: bool = ...): ...
def serve_uploaded_file_with_extension(number, extension): ...
def serve_uploaded_file_with_extension_download(number, extension): ...
def do_serve_uploaded_file_with_extension(number, extension, download: bool = ...): ...
def serve_uploaded_file(number): ...
def do_serve_uploaded_file(number, download: bool = ...): ...
def serve_uploaded_page(number, page): ...
def serve_uploaded_page_download(number, page): ...
def serve_uploaded_pagescreen(number, page): ...
def serve_uploaded_pagescreen_download(number, page): ...
def do_serve_uploaded_page(number, page, download: bool = ..., size: str = ...): ...
def visit_interview(): ...
def observer(): ...
def decode_dict(the_dict): ...
def monitor(): ...
def update_package_wait(): ...
def update_package_ajax(): ...
def get_package_name_from_zip(zippath): ...
def update_package(): ...
def get_master_branch(giturl): ...
def create_playground_package(): ...
def create_package(): ...
def restart_page(): ...
def playground_poll(): ...
def get_gd_flow(): ...
def get_playground_user(): ...
def set_playground_user(user_id) -> None: ...
def get_gd_folder(): ...
def set_gd_folder(folder) -> None: ...
def get_od_flow(): ...
def get_od_folder(): ...
def set_od_folder(folder) -> None: ...

class RedisCredStorage(oauth2client.client.Storage):
    key: Incomplete
    lockkey: Incomplete
    def __init__(self, oauth_app: str = ...) -> None: ...
    def acquire_lock(self) -> None: ...
    def release_lock(self) -> None: ...
    def locked_get(self): ...
    def locked_put(self, credentials) -> None: ...
    def locked_delete(self) -> None: ...

def google_drive_callback(): ...
def rename_gd_project(old_project, new_project): ...
def trash_gd_project(old_project): ...
def trash_gd_file(section, filename, current_project): ...
def sync_with_google_drive(): ...
def gd_sync_wait(): ...
def onedrive_callback(): ...
def rename_od_project(old_project, new_project): ...
def trash_od_project(old_project): ...
def trash_od_file(section, filename, current_project): ...
def sync_with_onedrive(): ...
def od_sync_wait(): ...
def add_br(text): ...
def checkin_sync_with_google_drive(): ...
def checkin_sync_with_onedrive(): ...
def google_drive_page(): ...
def gd_fix_subdirs(service, the_folder) -> None: ...
def onedrive_page(): ...
def od_fix_subdirs(http, the_folder) -> None: ...
def config_page(): ...
def view_source(): ...
def playground_static(current_project, userid, filename): ...
def playground_modules(current_project, userid, filename): ...
def playground_sources(current_project, userid, filename): ...
def playground_template(current_project, userid, filename): ...
def playground_download(current_project, userid, filename): ...
def playground_office_functionfile(): ...
def playground_office_taskpane(): ...
def playground_office_addin(): ...
def cloud_trash(use_gd, use_od, section, the_file, current_project) -> None: ...
def playground_files(): ...
def pull_playground_package(): ...
def get_branches_of_repo(giturl): ...
def get_repo_info(giturl): ...
def get_git_branches(): ...
def get_user_repositories(http): ...
def get_orgs_info(http): ...
def get_branch_info(http, full_name): ...
def fix_package_folder() -> None: ...
def secure_git_branchname(branch): ...
def do_playground_pull(area, current_project, github_url: Incomplete | None = ..., branch: Incomplete | None = ..., pypi_package: Incomplete | None = ..., can_publish_to_github: bool = ..., github_email: Incomplete | None = ..., pull_only: bool = ...): ...
def get_github_username_and_email(): ...
def playground_packages(): ...
def github_as_http(url): ...
def copy_if_different(source, destination) -> None: ...
def splitall(path): ...
def playground_redirect_poll(): ...
def playground_redirect(): ...
def upload_js(): ...
def search_js(form: Incomplete | None = ...): ...
def variables_js(form: Incomplete | None = ..., office_mode: bool = ...): ...
def variables_report(): ...
def playground_variables(): ...
def ensure_ml_file_exists(interview, yaml_file, current_project) -> None: ...
def assign_opacity(files): ...
def playground_page_run(): ...
def get_list_of_projects(user_id): ...
def rename_project(user_id, old_name, new_name) -> None: ...
def create_project(user_id, new_name) -> None: ...
def delete_project(user_id, the_project_name) -> None: ...
def playground_project(): ...
def set_current_project(new_name): ...
def get_current_project(): ...
def set_current_file(current_project, section, new_name): ...
def get_current_file(current_project, section): ...
def delete_current_file(current_project, section) -> None: ...
def clear_current_playground_info() -> None: ...
def set_variable_file(current_project, variable_file): ...
def get_variable_file(current_project): ...
def delete_variable_file(current_project) -> None: ...
def get_list_of_playgrounds(): ...
def playground_select(): ...
def get_pg_var_cache(): ...
def playground_page(): ...
def page_not_found_error(the_error): ...
def server_error(the_error): ...
def css_bundle(): ...
def playground_css_bundle(): ...
def js_bundle(): ...
def playground_js_bundle(): ...
def js_admin_bundle(): ...
def js_bundle_wrap(): ...
def js_bundle_no_query(): ...
def package_static(package, filename): ...
def logfile(filename): ...
def logs(): ...
def request_developer(): ...
def docx_variable_fix(variable): ...
def sanitize(default): ...
def read_fields(filename, orig_file_name, input_format, output_format): ...
def utilities(): ...
def after_reset(): ...
def needs_to_change_password(): ...
def fix_group_id(the_package, the_file, the_group_id): ...
def ensure_training_loaded(interview) -> None: ...
def get_corresponding_interview(the_package, the_file): ...
def ml_prefix(the_package, the_file): ...
def train(): ...
def user_interviews_filter(obj): ...
def user_interviews(user_id: Incomplete | None = ..., secret: Incomplete | None = ..., exclude_invalid: bool = ..., action: Incomplete | None = ..., filename: Incomplete | None = ..., session: Incomplete | None = ..., tag: Incomplete | None = ..., include_dict: bool = ..., delete_shared: bool = ..., admin: bool = ..., start_id: Incomplete | None = ..., temp_user_id: Incomplete | None = ..., query: Incomplete | None = ..., minimal: bool = ...): ...
def interview_list(): ...
def valid_date_key(x): ...
def fix_secret(user: Incomplete | None = ..., to_convert: Incomplete | None = ...) -> None: ...
def login_or_register(sender, user, source, **extra) -> None: ...
def update_last_login(user) -> None: ...
def _on_user_login(sender, user, **extra) -> None: ...
def _on_password_change(sender, user, **extra) -> None: ...
def on_register_hook(sender, user, **extra) -> None: ...
def fax_callback(): ...
def clicksend_fax_callback(): ...
def telnyx_fax_callback(): ...
def voice(): ...
def digits_endpoint(): ...
def sms_body(phone_number, body: str = ..., config: str = ...): ...
def favicon_file(filename, alt: Incomplete | None = ...): ...
def test_favicon_file(filename, alt: Incomplete | None = ...): ...
def favicon(): ...
def apple_touch_icon(): ...
def favicon_md(): ...
def favicon_sm(): ...
def favicon_site_webmanifest(): ...
def favicon_manifest_json(): ...
def favicon_safari_pinned_tab(): ...
def favicon_android_md(): ...
def favicon_android_lg(): ...
def favicon_mstile(): ...
def favicon_browserconfig(): ...
def robots(): ...
def sms(): ...
def do_sms(form, base_url, url_root, config: str = ..., save: bool = ...): ...
def get_api_key(): ...
def api_verify(roles: Incomplete | None = ..., permissions: Incomplete | None = ...): ...
def jsonify_with_status(data, code): ...
def true_or_false(text): ...
def get_user_list(include_inactive: bool = ..., start_id: Incomplete | None = ...): ...
def translation_file(): ...
def api_user_list(): ...
def get_user_info(user_id: Incomplete | None = ..., email: Incomplete | None = ..., case_sensitive: bool = ..., admin: bool = ...): ...
def make_user_inactive(user_id: Incomplete | None = ..., email: Incomplete | None = ...) -> None: ...
def api_user(): ...
def api_user_privileges(): ...
def api_create_user(): ...
def api_invite_user(): ...
def api_user_info(): ...
def api_user_by_id(user_id): ...
def api_fields(): ...
def api_privileges(): ...
def get_privileges_list(admin: bool = ...): ...
def get_permissions_of_privilege(privilege): ...
def add_privilege(privilege) -> None: ...
def remove_privilege(privilege) -> None: ...
def api_user_by_id_privileges(user_id): ...
def add_user_privilege(user_id, privilege) -> None: ...
def remove_user_privilege(user_id, privilege) -> None: ...
def create_user(email, password, privileges: Incomplete | None = ..., info: Incomplete | None = ...): ...
def set_user_info(**kwargs) -> None: ...
def api_get_secret(): ...
def get_secret(username, password, case_sensitive: bool = ...): ...
def parse_api_sessions_query(query): ...
def api_users_interviews(): ...
def api_user_user_id_interviews(user_id): ...
def api_session_back(): ...
def transform_json_variables(obj): ...
def api_session(): ...
def api_file(file_number): ...
def get_session_variables(yaml_filename, session_id, secret: Incomplete | None = ..., simplify: bool = ..., use_lock: bool = ...): ...
def go_back_in_session(yaml_filename, session_id, secret: Incomplete | None = ..., return_question: bool = ..., use_lock: bool = ..., encode: bool = ...): ...
def set_session_variables(yaml_filename, session_id, variables, secret: Incomplete | None = ..., return_question: bool = ..., literal_variables: Incomplete | None = ..., del_variables: Incomplete | None = ..., question_name: Incomplete | None = ..., event_list: Incomplete | None = ..., advance_progress_meter: bool = ..., post_setting: bool = ..., use_lock: bool = ..., encode: bool = ..., process_objects: bool = ...): ...
def api_session_new(): ...
def create_new_interview(yaml_filename, secret, url_args: Incomplete | None = ..., referer: Incomplete | None = ..., req: Incomplete | None = ...): ...
def api_session_question(): ...
def get_question_data(yaml_filename, session_id, secret, use_lock: bool = ..., user_dict: Incomplete | None = ..., steps: Incomplete | None = ..., is_encrypted: Incomplete | None = ..., old_user_dict: Incomplete | None = ..., save: bool = ..., post_setting: bool = ..., advance_progress_meter: bool = ..., action: Incomplete | None = ..., encode: bool = ...): ...
def api_session_action(): ...
def run_action_in_session(**kwargs): ...
def api_login_url(): ...
def get_login_url(**kwargs): ...
def api_list(): ...
def api_user_interviews(): ...
def api_interviews(): ...
def jsonify_task(result): ...
def jsonify_restart_task(): ...
def should_run_create(package_name): ...
def api_package(): ...
def api_package_update_status(): ...
def api_temporary_redirect(): ...
def api_resume_url(): ...
def api_clear_cache(): ...
def api_config(): ...
def api_playground_pull(): ...
def api_restart(): ...
def api_restart_status(): ...
def api_playground_install(): ...
def api_playground_projects(): ...
def api_playground(): ...
def api_convert_file(): ...
def add_api_key(user_id, name, method, allowed): ...
def api_key_exists(user_id, api_key): ...
def existing_api_names(user_id, except_for: Incomplete | None = ...): ...
def get_api_info(user_id, name: Incomplete | None = ..., api_key: Incomplete | None = ...): ...
def delete_api_key(user_id, api_key) -> None: ...
def update_api_key(user_id, api_key, name, method, allowed, add_to_allowed, remove_from_allowed, permissions, add_to_permissions, remove_from_permissions): ...
def do_api_user_api(user_id): ...
def api_user_api(): ...
def api_user_userid_api(user_id): ...
def api_interview_data(): ...
def api_stash_data(): ...
def api_retrieve_stashed_data(): ...
def manage_api(): ...
def html_index(): ...
def api_interview(): ...
def whoami(): ...
def retrieve_email(email_id): ...

class AddressEmail:
    def __str__(self): ...

def retrieve_emails(**pargs): ...
def get_email_obj(email, short_record, user): ...
def da_send_fax(fax_number, the_file, config, country: Incomplete | None = ...): ...
def write_pypirc() -> None: ...
def url_sanitize(url): ...
def pypi_status(packagename): ...
def page_after_login(): ...
def path_from_reference(file_reference): ...
def secure_filename_spaces_ok(filename): ...
def secure_filename(filename): ...
def sanitize_arguments(*pargs) -> None: ...
def get_short_code(**pargs): ...
def illegal_variable_name(var): ...
def illegal_sessions_query(expr): ...

emoji_match: Incomplete
html_match: Incomplete

def mako_parts(expression): ...
def start_of_line(expression, i): ...
def applock(action, application, maxtime: int = ...) -> None: ...
def handle_csrf_error(the_error): ...
def error_notification(err, message: Incomplete | None = ..., history: Incomplete | None = ..., trace: Incomplete | None = ..., referer: Incomplete | None = ..., the_request: Incomplete | None = ..., the_vars: Incomplete | None = ...) -> None: ...
def stash_data(data, expire): ...
def retrieve_stashed_data(key, secret, delete: bool = ..., refresh: bool = ...): ...
def make_necessary_dirs() -> None: ...

base_words: Incomplete
title_documentation: Incomplete
DOCUMENTATION_BASE: Incomplete
documentation_dict: Incomplete
base_name_info: Incomplete
password_secret_key: Incomplete

def get_base_url(): ...
def null_func(*pargs, **kwargs) -> None: ...
def illegal_worker_convert(*pargs, **kwargs) -> None: ...

pg_ex: Incomplete

def define_examples() -> None: ...

version_warning: Incomplete

class AdminInterview:
    def is_not(self, interview): ...
    def can_use(self): ...
    def get_title(self, language): ...
    def get_url(self): ...

class MenuItem:
    def is_not(self, interview): ...
    def can_use(self): ...
    def get_title(self, language): ...
    def get_url(self): ...

def set_admin_interviews(): ...
def fix_api_key(match): ...
def fix_api_keys() -> None: ...

class TestContext:
    package: Incomplete
    def __init__(self, package) -> None: ...
    app_context: Incomplete
    test_context: Incomplete
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, exc_traceback) -> None: ...

def initialize() -> None: ...
