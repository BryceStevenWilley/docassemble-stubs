from _typeshed import Incomplete as Incomplete
from collections.abc import Generator

class MessageExtractor:
    use_bytes: bool
    def process_file(self, fileobj) -> None: ...
    def extract_nodes(self, nodes) -> Generator[Incomplete, None, None]: ...
