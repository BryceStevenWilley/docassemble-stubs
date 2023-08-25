import oauth2client.client
from _typeshed import Incomplete
from docassemble.base.config import daconfig as daconfig, hostname as hostname
from docassemble.base.error import DAError as DAError
from docassemble.base.logger import logmessage as logmessage
from docassemble.webapp.files import SavedFile as SavedFile
from docassemble.webapp.worker_common import error_object as error_object, process_error as process_error, worker_controller as worker_controller, workerapp as workerapp

USING_SUPERVISOR: Incomplete
WEBAPP_PATH: Incomplete
CONTAINER_ROLE: Incomplete
ONEDRIVE_CHUNK_SIZE: int
SUPERVISORCTL: Incomplete

class RedisCredStorage(oauth2client.client.Storage):
    r: Incomplete
    key: Incomplete
    lockkey: Incomplete
    def __init__(self, r, user_id, oauth_app: str = ...) -> None: ...
    def acquire_lock(self) -> None: ...
    def release_lock(self) -> None: ...
    def locked_get(self): ...
    def locked_put(self, credentials) -> None: ...
    def locked_delete(self) -> None: ...

def ensure_directories(the_path) -> None: ...
def sync_with_google_drive(user_id): ...
def try_request(*pargs, **kwargs): ...
def epoch_from_iso(datestring): ...
def iso_from_epoch(seconds): ...
def sync_with_onedrive(user_id): ...
def onedrive_upload(http, folder_id, folder_name, data, the_path, new_item_id: Incomplete | None = ...): ...
def ocr_dummy(doc, indexno, **kwargs): ...
def ocr_page(indexno, **kwargs): ...
def ocr_finalize(*pargs, **kwargs): ...
def make_png_for_pdf(doc, prefix, resolution, user_code, pdf_to_png, page: Incomplete | None = ...) -> None: ...
def reset_server(result, run_create: Incomplete | None = ...): ...
def update_packages(restart: bool = ...): ...
def email_attachments(user_code, email_address, attachment_info, language, subject: Incomplete | None = ..., body: Incomplete | None = ..., html: Incomplete | None = ..., config: Incomplete | None = ...): ...
def background_action(yaml_filename, user_info, session_code, secret, url, url_root, action, extra: Incomplete | None = ...): ...
def ocr_google(image_file, raw_result, user_code): ...