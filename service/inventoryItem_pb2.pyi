import book_pb2 as _book_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
STATUS_AVAILABLE: Status
STATUS_TAKEN: Status
STATUS_UNDEFINED: Status

class InventoryItem(_message.Message):
    __slots__ = ["book", "inventoryNumber", "status"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    INVENTORYNUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    book: _book_pb2.Book
    inventoryNumber: int
    status: Status
    def __init__(self, inventoryNumber: _Optional[int] = ..., book: _Optional[_Union[_book_pb2.Book, _Mapping]] = ..., status: _Optional[_Union[Status, str]] = ...) -> None: ...

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
