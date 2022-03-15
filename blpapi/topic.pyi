from typing import Any, Optional

from .chandle import CHandle
from .service import Service

class Topic(CHandle):
    def __init__(
        self, handle: Optional[Any] = ..., sessions: Optional[Any] = ...
    ) -> None: ...
    def isValid(self) -> bool: ...
    def isActive(self) -> bool: ...
    def service(self) -> Service: ...
    def __cmp__(self, other: Any) -> int: ...
    def __lt__(self, other: "Topic") -> bool: ...
    def __eq__(self, other: "Topic") -> bool: ...
