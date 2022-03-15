from __future__ import annotations
from typing import Any, ByteString, ClassVar, Optional, List

from .auth import AuthOptions
from .chandle import CHandle
from .internals import CorrelationId
from .utils import Iterator

class SessionOptions(CHandle):
    AUTO: ClassVar[int]
    DAPI: ClassVar[int]
    SAPI: ClassVar[int]
    def __init__(self) -> None: ...
    def setServerHost(self, serverHost: str) -> None: ...
    def setServerPort(self, serverPort: int) -> None: ...
    def setServerAddress(
        self, serverHost: str, serverPort: int, index: int
    ) -> None: ...
    def removeServerAddress(self, index: int) -> None: ...
    def setConnectTimeout(self, timeoutMilliSeconds: int) -> None: ...
    def setDefaultServices(self, defaultServices: List[str]) -> None: ...
    def setDefaultSubscriptionService(
        self, defaultSubscriptionService: str
    ) -> None: ...
    def setDefaultTopicPrefix(self, prefix: str) -> None: ...
    def setAllowMultipleCorrelatorsPerMsg(
        self, allowMultipleCorrelatorsPerMsg: bool
    ) -> None: ...
    def setClientMode(self, clientMode: int) -> None: ...
    def setMaxPendingRequests(self, maxPendingRequests: int) -> None: ...
    def setSessionIdentityOptions(
        self, authOptions: AuthOptions, correlationId: Optional[CorrelationId] = ...
    ) -> CorrelationId: ...
    def setAuthenticationOptions(self, authOptions: str) -> None: ...
    def setNumStartAttempts(self, numStartAttempts: int) -> None: ...
    def setAutoRestartOnDisconnection(self, autoRestart: bool) -> None: ...
    def setSlowConsumerWarningHiWaterMark(self, hiWaterMark: float) -> None: ...
    def setSlowConsumerWarningLoWaterMark(self, loWaterMark: float) -> None: ...
    def setMaxEventQueueSize(self, eventQueueSize: int) -> None: ...
    def setKeepAliveEnabled(self, isEnabled: bool) -> None: ...
    def setDefaultKeepAliveInactivityTime(self, inactivityMsecs: int) -> None: ...
    def setDefaultKeepAliveResponseTimeout(self, timeoutMsecs: int) -> None: ...
    def setFlushPublishedEventsTimeout(self, timeoutMsecs: int) -> None: ...
    def setRecordSubscriptionDataReceiveTimes(self, shouldRecord: bool) -> None: ...
    def setServiceCheckTimeout(self, timeoutMsecs: int) -> None: ...
    def setServiceDownloadTimeout(self, timeoutMsecs: int) -> None: ...
    def setTlsOptions(self, tlsOptions: TlsOptions) -> None: ...
    def setBandwidthSaveModeDisabled(self, isDisabled: bool) -> None: ...
    def serverHost(self) -> str: ...
    def serverPort(self) -> int: ...
    def numServerAddresses(self) -> int: ...
    def getServerAddress(self, index) -> tuple[str, int]: ...
    def serverAddresses(self) -> Iterator: ...
    def connectTimeout(self) -> int: ...
    def defaultServices(self) -> str: ...
    def defaultSubscriptionService(self) -> str: ...
    def defaultTopicPrefix(self) -> str: ...
    def allowMultipleCorrelatorsPerMsg(self) -> bool: ...
    def clientMode(self) -> int: ...
    def maxPendingRequests(self) -> int: ...
    def autoRestartOnDisconnection(self) -> bool: ...
    def authenticationOptions(self) -> str: ...
    def numStartAttempts(self) -> int: ...
    def recordSubscriptionDataReceiveTimes(self) -> bool: ...
    def slowConsumerWarningHiWaterMark(self) -> float: ...
    def slowConsumerWarningLoWaterMark(self) -> float: ...
    def maxEventQueueSize(self) -> int: ...
    def defaultKeepAliveInactivityTime(self) -> int: ...
    def defaultKeepAliveResponseTimeout(self) -> int: ...
    def flushPublishedEventsTimeout(self) -> int: ...
    def keepAliveEnabled(self) -> bool: ...
    def serviceCheckTimeout(self) -> int: ...
    def serviceDownloadTimeout(self) -> int: ...
    def bandwidthSaveModeDisabled(self) -> bool: ...
    def toString(
        self, level: Optional[int] = ..., spacesPerLevel: Optional[int] = ...
    ) -> str: ...

class TlsOptions(CHandle):
    def __init__(self, handle: Any) -> None: ...
    def setTlsHandshakeTimeoutMs(self, timeoutMs: int) -> None: ...
    def setCrlFetchTimeoutMs(self, timeoutMs: int) -> None: ...
    @staticmethod
    def createFromFiles(
        clientCredentialsFilename: str,
        clientCredentialsPassword: str,
        trustedCertificatesFilename: str,
    ) -> "TlsOptions": ...
    @staticmethod
    def createFromBlobs(
        clientCredentials: ByteString,
        clientCredentialsPassword: str,
        trustedCertificates: ByteString,
    ) -> "TlsOptions": ...