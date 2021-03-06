from __future__ import annotations
import datetime as dt
from typing import Any, Union, List

from .name import Name
from .session import Session
from .utils import Iterator

class Constant:
    def __init__(self, handle: Any, sessions: List[Session]) -> None: ...
    def name(self) -> Name: ...
    def description(self) -> str: ...
    def status(self) -> int: ...
    def datatype(self) -> int: ...
    def getValueAsInteger(self) -> int: ...
    def getValueAsFloat(self) -> float: ...
    def getValueAsDatetime(self) -> Union[dt.time, dt.date, dt.datetime]: ...
    def getValueAsString(self) -> str: ...
    def getValue(self) -> Union[str, int, float, dt.time, dt.date, dt.datetime]: ...

class ConstantList:
    def __init__(self, handle: Any, sessions: List[Session]) -> None: ...
    def __iter__(self) -> Iterator: ...
    def name(self) -> Name: ...
    def description(self) -> str: ...
    def status(self) -> int: ...
    def numConstants(self) -> int: ...
    def datatype(self) -> int: ...
    def hasConstant(self, name: Union[Name, str]) -> bool: ...
    def getConstant(self, name: Union[Name, str]) -> Constant: ...
    def getConstantAt(self, position: int) -> Constant: ...
