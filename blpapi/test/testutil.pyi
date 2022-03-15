from typing import Optional, Union

from .messageformatter import MessageFormatter
from .messageproperties import MessageProperties
from ..event import Event
from ..name import Name
from ..schema import SchemaElementDefinition
from ..service import Service
from ..topic import Topic

def createEvent(eventType: int) -> Event: ...
def appendMessage(
    event: Event,
    elementDef: SchemaElementDefinition,
    properties: Optional[MessageProperties] = ...,
) -> MessageFormatter: ...
def deserializeService(serviceXMLStr: str) -> Service: ...
def serializeService(service: Service) -> str: ...
def createTopic(service: Service, isActive: bool = ...) -> Topic: ...
def getAdminMessageDefinition(
    messageName: Union[Name, str]
) -> SchemaElementDefinition: ...
