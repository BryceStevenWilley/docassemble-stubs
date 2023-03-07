from _typeshed import Incomplete as Incomplete
from docassemble.base.util import DAList as DAList

class SQLObject:
    id: Incomplete
    def sql_init(self) -> None: ...
    @classmethod
    def filter(cls, instance_name, **kwargs) -> None: ...
    @classmethod
    def any(cls) -> None: ...
    @classmethod
    def all(cls, instance_name: Union[Incomplete, None] = ...): ...
    @classmethod
    def by_id(cls, the_id, instance_name: Union[Incomplete, None] = ...): ...
    @classmethod
    def by_uid(cls, uid, instance_name: Union[Incomplete, None] = ...): ...
    @classmethod
    def delete_by_id(cls, the_id) -> None: ...
    @classmethod
    def delete_by_uid(cls, uid) -> None: ...
    @classmethod
    def id_exists(cls, the_id) -> None: ...
    @classmethod
    def uid_exists(cls, uid) -> None: ...
    def db_from_cache(self, the_id) -> None: ...
    def db_cache(self) -> None: ...
    def __del__(self) -> None: ...
    def db_delete(self) -> None: ...
    def db_save(self) -> None: ...
    def save_if_nascent(self) -> None: ...
    def ready(self) -> None: ...
    def db_read(self) -> None: ...
    def db_find_existing(self) -> None: ...
    def db_get(self, column) -> None: ...
    def db_set(self, column, value) -> None: ...
    def db_null(self, column) -> None: ...
    def has_child(self, rel_name, rel) -> None: ...
    def add_child(self, rel_name, child) -> None: ...
    def get_child(self, rel_name, instance_name: Union[Incomplete, None] = ...): ...
    def del_child(self, rel_name, child) -> None: ...
    def has_parent(self, rel_name, rel) -> None: ...
    def add_parent(self, rel_name, parent) -> None: ...
    def get_parent(self, rel_name, instance_name: Union[Incomplete, None] = ...): ...
    def del_parent(self, rel_name, parent) -> None: ...

def alchemy_url(db_config) -> None: ...
def connect_args(db_config) -> None: ...
def upgrade_db(url, py_file, engine, name: Union[Incomplete, None] = ..., conn_args: Union[Incomplete, None] = ...) -> None: ...

class SQLObjectRelationship(SQLObject):
    def __init_subclass__(cls, **kwargs) -> None: ...
    @classmethod
    def filter_by_parent(cls, instance_name, parent) -> None: ...
    @classmethod
    def filter_by_child(cls, instance_name, child) -> None: ...
    @classmethod
    def filter_by_parent_child(cls, instance_name, parent, child) -> None: ...
    def rel_init(self, *pargs, **kwargs) -> None: ...
    def db_get(self, column) -> None: ...
    def db_set(self, column, value) -> None: ...
    def db_find_existing(self) -> None: ...

class SQLObjectList(DAList):
    elements: Incomplete
    def init(self, *pargs, **kwargs) -> None: ...

class SQLRelationshipList(DAList):
    elements: Incomplete
    def init(self, *pargs, **kwargs) -> None: ...
    def hook_on_remove(self, item, *pargs, **kwargs) -> None: ...
    def reset_gathered(self, recursive: bool = ..., only_if_empty: bool = ..., mark_incomplete: bool = ...) -> None: ...

class StandardRelationshipList(SQLRelationshipList):
    there_is_another: bool
    gathered: bool
    complete_attribute: str
    def init(self, *pargs, **kwargs) -> None: ...