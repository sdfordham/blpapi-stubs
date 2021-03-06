import datetime as _dt
from typing import Any, Union, Optional

from .internals import blpapi_HighPrecisionDatetime_tag, blpapi_Datetime_tag

class FixedOffset(_dt.tzinfo):
    def __init__(self, offsetInMinutes: int = ...) -> None: ...
    def utcoffset(self, dt: Any) -> _dt.timedelta: ...
    def dst(self, dt: Any) -> _dt.timedelta: ...
    def tzname(self, dt: Any) -> Optional[str]: ...
    def getOffsetInMinutes(self) -> int: ...
    def __hash__(self) -> int: ...
    def __cmp__(self, other) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...

UTC: Any

class _DatetimeUtil:
    @staticmethod
    def convertToNative(
        blpapiDatetimeObj: blpapi_HighPrecisionDatetime_tag,
    ) -> Union[_dt.datetime, _dt.date, _dt.time]: ...
    @staticmethod
    def convertToNativeNotHighPrecision(
        blpapiDatetime: blpapi_Datetime_tag,
    ) -> Union[_dt.datetime, _dt.date, _dt.time]: ...
    @staticmethod
    def isDatetime(dtime: Any) -> bool: ...
    @staticmethod
    def convertToBlpapi(
        dtime: Union[_dt.datetime, _dt.date, _dt.time]
    ) -> blpapi_HighPrecisionDatetime_tag: ...
