from _typeshed import Incomplete
from docassemble.base.config import daconfig as daconfig
from docassemble.base.error import DAError as DAError
from docassemble.base.functions import word as word
from docassemble.base.logger import logmessage as logmessage
from docassemble.base.pdfa import pdf_to_pdfa as pdf_to_pdfa

PDFTK_PATH: str
QPDF_PATH: str

def set_pdftk_path(path) -> None: ...
def read_fields(pdffile): ...
def fieldsorter(x): ...
def recursively_add_fields(fields, id_to_page, outfields, prefix: str = ..., parent_ft: Incomplete | None = ...) -> None: ...
def fill_template(template, data_strings: Incomplete | None = ..., data_names: Incomplete | None = ..., hidden: Incomplete | None = ..., readonly: Incomplete | None = ..., images: Incomplete | None = ..., pdf_url: Incomplete | None = ..., editable: bool = ..., pdfa: bool = ..., password: Incomplete | None = ..., template_password: Incomplete | None = ..., default_export_value: Incomplete | None = ...): ...
def get_passwords(password): ...
def pdf_encrypt(filename, password) -> None: ...
def remove_nonprintable(text): ...
def remove_nonprintable_bytes(byte_list): ...
def remove_nonprintable_bytes_limited(byte_list): ...
def remove_nonprintable_limited(text): ...
def flatten_pdf(filename) -> None: ...
def overlay_pdf_multi(main_file, logo_file, out_file) -> None: ...
def overlay_pdf(main_file, logo_file, out_file, first_page: Incomplete | None = ..., last_page: Incomplete | None = ..., logo_page: Incomplete | None = ..., only: Incomplete | None = ...) -> None: ...
def apply_qpdf(filename) -> None: ...
def extract_pages(input_path, output_path, first, last) -> None: ...
