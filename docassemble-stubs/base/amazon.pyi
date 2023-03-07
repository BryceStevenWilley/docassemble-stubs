from _typeshed import Incomplete

epoch: Incomplete

class s3object:
    upload_args: Incomplete
    download_args: Incomplete
    conn: Incomplete
    client: Incomplete
    bucket: Incomplete
    bucket_name: Incomplete
    def __init__(self, s3_config) -> None: ...
    def get_key(self, key_name): ...
    def search_key(self, key_name): ...
    def list_keys(self, prefix): ...

class s3key:
    s3_object: Incomplete
    key_obj: Incomplete
    name: Incomplete
    size: Incomplete
    last_modified: Incomplete
    does_exist: bool
    def __init__(self, s3_object, key_obj) -> None: ...
    content_type: Incomplete
    def get_contents_as_string(self): ...
    def exists(self): ...
    def delete(self) -> None: ...
    def get_epoch_modtime(self): ...
    def get_contents_to_filename(self, filename) -> None: ...
    def set_contents_from_filename(self, filename) -> None: ...
    def set_contents_from_string(self, text) -> None: ...
    def generate_url(self, expires, content_type: Incomplete | None = ..., display_filename: Incomplete | None = ..., inline: bool = ...): ...
