from _typeshed import Incomplete as Incomplete
from docassemble.base.util import DAList as DAList, DAObject as DAObject

class SpecialReturnObject: ...

class Court(DAObject):
    jurisdiction: Incomplete
    def init(self, *pargs, **kwargs) -> None: ...
    def in_the_court(self, **kwargs) -> None: ...

class PartyList(DAList):
    PartyClass: Incomplete
    object_type: Incomplete
    def init(self, *pargs, **kwargs) -> None: ...

class Case(DAObject):
    PartyListClass: Incomplete
    CourtClass: Incomplete
    firstParty: Incomplete
    secondParty: Incomplete
    is_solo_action: bool
    state: Incomplete
    action_type: str
    def init(self, *pargs, **kwargs) -> None: ...
    def set_action_type(self, the_value) -> None: ...
    def case_id_in_caption(self, **kwargs) -> None: ...
    def determine_court(self, **kwargs) -> None: ...
    def role_of(self, party) -> None: ...
    def all_known_people(self) -> None: ...
    def parties(self) -> None: ...

class Document(DAObject): ...

class LegalFiling(Document):
    def caption(self) -> None: ...

def us_districts(bankruptcy: bool = ...): ...