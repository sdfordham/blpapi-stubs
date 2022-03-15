from collections.abc import Mapping as Mapping_t
from typing import Any, Callable, Union, List, Dict
import datetime as dt

from .name import Name
from .schema import SchemaElementDefinition
from .utils import Iterator

class ElementIterator:
    def __init__(self, element: Element) -> None: ...
    def __next__(self) -> int: ...
    next: Callable

class Element:
    def __init__(self, handle: Any, dataHolder: Any) -> None: ...
    def __getitem__(
        self, nameOrIndex: Union[Name, str, int]
    ) -> Union[Element, bool, str, dt.datetime, int, float, Name]: ...
    def __setitem__(self, name: Union[Name, str], value: Dict[str, Any]) -> None: ...
    def __iter__(self) -> ElementIterator: ...
    def __len__(self) -> int: ...
    def __contains__(self, item) -> bool: ...
    def name(self) -> Name: ...
    def datatype(self) -> int: ...
    def isComplexType(self) -> bool: ...
    def isArray(self) -> bool: ...
    def isValid(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isReadOnly(self) -> bool: ...
    def elementDefinition(self) -> SchemaElementDefinition: ...
    def numValues(self) -> int: ...
    def numElements(self) -> int: ...
    def isNullValue(self, position: int = ...) -> bool: ...
    def toPy(self) -> Union[List[Union[str, int]], Dict[str, Union[str, int]]]: ...
    def toString(self, level: int = ..., spacesPerLevel: int = ...) -> str: ...
    def getElement(self, nameOrIndex: Union[Name, str, int]) -> Element: ...
    def elements(self) -> Iterator: ...
    def hasElement(
        self, name: Union[Name, str], excludeNullElements: bool = ...
    ) -> bool: ...
    def getChoice(self) -> Element: ...
    def getValueAsBool(self, index: int = ...) -> bool: ...
    def getValueAsString(self, index: int = ...) -> str: ...
    def getValueAsDatetime(
        self, index: int = ...
    ) -> Union[dt.time, dt.date, dt.datetime]: ...
    def getValueAsInteger(self, index: int = ...) -> int: ...
    def getValueAsFloat(self, index: int = ...) -> float: ...
    def getValueAsName(self, index: int = ...) -> Name: ...
    def getValueAsElement(self, index: int = ...) -> Element: ...
    def getValue(
        self, index: int = ...
    ) -> Union[Element, bool, str, dt.datetime, int, float, Name]: ...
    def values(self) -> Iterator: ...
    def getElementAsBool(self, name: Union[Name, str]) -> bool: ...
    def getElementAsString(self, name: Union[Name, str]) -> str: ...
    def getElementAsDatetime(
        self, name: Union[Name, str]
    ) -> Union[dt.time, dt.date, dt.datetime]: ...
    def getElementAsInteger(self, name: Union[Name, str]) -> int: ...
    def getElementAsFloat(self, name: Union[Name, str]) -> float: ...
    def getElementAsName(self, name: Union[Name, str]) -> Name: ...
    def getElementValue(
        self, name: Union[Name, str]
    ) -> Union[bool, str, dt.datetime, int, float, Name]: ...
    def setElement(
        self,
        name: Union[Name, str],
        value: Union[bool, str, dt.datetime, int, float, Name],
    ) -> None: ...
    def setValue(
        self, value: Union[bool, str, dt.datetime, int, float, Name], index: int = ...
    ) -> None: ...
    def appendValue(
        self, value: Union[bool, str, dt.datetime, int, float, Name]
    ) -> None: ...
    def appendElement(self) -> Element: ...
    def setChoice(self, selectionName: Union[Name, str]) -> Element: ...
    def fromPy(
        self,
        value: Mapping_t[
            Union[Name, str], Union[Element, bool, str, dt.datetime, int, float, Name]
        ],
    ) -> None: ...
