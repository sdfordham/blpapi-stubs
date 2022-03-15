from __future__ import annotations
from typing import Any, Optional, Union

from .auth import AuthOptions
from .chandle import CHandle
from .event import EventQueue
from .identity import Identity
from .internals import CorrelationId
from .request import Request
from .service import Service

class AbstractSession(CHandle):
    def __init__(self, handle: Any = ..., dtor: Any = ...) -> None: ...
    def openService(self, serviceName: str) -> bool: ...
    def openServiceAsync(
        self, serviceName: str, correlationId: Optional[CorrelationId] = ...
    ) -> Optional[CorrelationId]: ...
    def sendAuthorizationRequest(
        self,
        request: Request,
        identity: Identity,
        correlationId: Optional[CorrelationId] = ...,
        eventQueue: Optional[EventQueue] = ...,
    ) -> Optional[CorrelationId]: ...
    def cancel(
        self, correlationId: Union[CorrelationId, list[CorrelationId]]
    ) -> None: ...
    def generateToken(
        self,
        correlationId: Optional[CorrelationId] = ...,
        eventQueue: Optional[EventQueue] = ...,
        authId: Optional[str] = ...,
        ipAddress: Optional[str] = ...,
    ) -> CorrelationId: ...
    def getService(self, serviceName: str) -> Service: ...
    def createIdentity(self) -> Identity: ...
    def generateAuthorizedIdentity(
        self, authOptions: AuthOptions, correlationId: Optional[CorrelationId] = ...
    ) -> CorrelationId: ...
    def getAuthorizedIdentity(
        self, correlationId: Optional[CorrelationId] = ...
    ) -> Identity: ...